#[no_mangle]
pub extern "C" fn agent_energy_residual(actual: *const f64, actual_n: i64,
    load: *const f64, load_n: i64, count: i64, output: *mut f64, output_n: i64) -> i64 {
    if count <= 0 || count > 364 || actual_n != count || load_n != count || output_n != 3 { return 1; }
    let mut signed_sum = 0.0; let mut absolute_sum = 0.0; let mut maximum_absolute = 0.0;
    for i in 0..count as usize {
        let difference = unsafe { *actual.add(i) - *load.add(i) };
        let magnitude = if difference < 0.0 { 0.0 - difference } else { difference };
        signed_sum += difference; absolute_sum += magnitude;
        if magnitude > maximum_absolute { maximum_absolute = magnitude; }
    }
    let mut divisor = 0.0; for _ in 0..count { divisor += 1.0; }
    unsafe { *output.add(0) = signed_sum; *output.add(1) = maximum_absolute; *output.add(2) = absolute_sum / divisor; }
    0
}

#[no_mangle]
pub extern "C" fn agent_point_bounds(coordinates: *const f64, coordinate_n: i64,
    point_count: i64, output: *mut f64, output_n: i64) -> i64 {
    if point_count <= 0 || point_count > 121 || coordinate_n != point_count * 3 || output_n != 6 { return 1; }
    let (mut min_x, mut min_y, mut min_z) = unsafe { (*coordinates, *coordinates.add(1), *coordinates.add(2)) };
    let (mut max_x, mut max_y, mut max_z) = (min_x, min_y, min_z);
    for base in (3..point_count as usize * 3).step_by(3) {
        let (x, y, z) = unsafe { (*coordinates.add(base), *coordinates.add(base + 1), *coordinates.add(base + 2)) };
        if x < min_x { min_x = x; } if x > max_x { max_x = x; }
        if y < min_y { min_y = y; } if y > max_y { max_y = y; }
        if z < min_z { min_z = z; } if z > max_z { max_z = z; }
    }
    unsafe { *output.add(0)=min_x; *output.add(1)=min_y; *output.add(2)=min_z; *output.add(3)=max_x; *output.add(4)=max_y; *output.add(5)=max_z; }
    0
}

#[no_mangle]
pub extern "C" fn agent_raster_threshold_count(values: *const f64, value_n: i64,
    valid_mask: *const i64, mask_n: i64, cell_count: i64, threshold: f64,
    output: *mut i64, output_n: i64) -> i64 {
    if cell_count <= 0 || cell_count > 364 || value_n != cell_count || mask_n != cell_count || output_n != 1 { return 1; }
    let mut count = 0; for i in 0..cell_count as usize { if unsafe { *valid_mask.add(i) } == 1 && unsafe { *values.add(i) } > threshold { count += 1; } }
    unsafe { *output = count; } 0
}

#[no_mangle]
pub extern "C" fn agent_raster_valid_mean(values: *const f64, value_n: i64,
    valid_mask: *const i64, mask_n: i64, cell_count: i64, output: *mut f64, output_n: i64) -> i64 {
    if cell_count <= 0 || cell_count > 364 || value_n != cell_count || mask_n != cell_count || output_n != 1 { return 1; }
    let mut sum = 0.0; let mut valid_count = 0i64;
    for i in 0..cell_count as usize { if unsafe { *valid_mask.add(i) } == 1 { sum += unsafe { *values.add(i) }; valid_count += 1; } }
    if valid_count == 0 { return 1; }
    let mut divisor = 0.0; for _ in 0..valid_count { divisor += 1.0; }
    unsafe { *output = sum / divisor; } 0
}

#[no_mangle]
pub extern "C" fn energy_series_aggregation(ac_power: *const f64, ac_count: i64,
    load: *const f64, load_count: i64, capacity_w: f64, output: *mut f64, output_count: i64) -> i64 {
    if ac_count <= 0 || ac_count > 364 || capacity_w <= 0.0 { return 1; }
    if load_count != ac_count || output_count != 5 { return 2; }
    let mut ac_energy = 0.0; let mut net_energy = 0.0; let mut peak = unsafe { *ac_power }; let mut absolute_balance = 0.0;
    for i in 0..ac_count as usize {
        let (a, demand) = unsafe { (*ac_power.add(i), *load.add(i)) }; ac_energy += a; net_energy = net_energy + a - demand;
        let balance = a - demand; absolute_balance += if balance < 0.0 { 0.0 - balance } else { balance };
        if a > peak { peak = a; }
    }
    unsafe { *output.add(0)=ac_energy; *output.add(1)=peak; *output.add(2)=net_energy; *output.add(3)=ac_energy/(capacity_w*ac_count as f64); *output.add(4)=absolute_balance/ac_count as f64; }
    0
}

#[no_mangle]
pub extern "C" fn point_cloud_summary(coordinates: *const f64, coordinate_n: i64,
    point_count: i64, output: *mut f64, output_n: i64) -> i64 {
    if point_count <= 0 || point_count > 121 { return 1; }
    if coordinate_n != point_count * 3 || output_n != 10 { return 2; }
    let (mut min_x, mut min_y, mut min_z) = unsafe { (*coordinates, *coordinates.add(1), *coordinates.add(2)) };
    let (mut max_x, mut max_y, mut max_z) = (min_x, min_y, min_z);
    let (mut total_x, mut total_y, mut total_z) = (0.0, 0.0, 0.0);
    for point in 0..point_count as usize {
        let base = point * 3; let (x,y,z) = unsafe { (*coordinates.add(base),*coordinates.add(base+1),*coordinates.add(base+2)) };
        total_x += x; total_y += y; total_z += z;
        if x < min_x {min_x=x;} if y < min_y {min_y=y;} if z < min_z {min_z=z;}
        if x > max_x {max_x=x;} if y > max_y {max_y=y;} if z > max_z {max_z=z;}
    }
    let (cx, cy, cz) = (total_x / point_count as f64, total_y / point_count as f64, total_z / point_count as f64);
    let mut radius_sum = 0.0;
    for point in 0..point_count as usize {
        let base=point*3; let (dx,dy,dz)=unsafe { (*coordinates.add(base)-cx,*coordinates.add(base+1)-cy,*coordinates.add(base+2)-cz) };
        radius_sum += dx*dx + dy*dy + dz*dz;
    }
    unsafe { *output.add(0)=cx; *output.add(1)=cy; *output.add(2)=cz; *output.add(3)=min_x; *output.add(4)=min_y; *output.add(5)=min_z; *output.add(6)=max_x; *output.add(7)=max_y; *output.add(8)=max_z; *output.add(9)=(radius_sum/point_count as f64).sqrt(); }
    0
}
