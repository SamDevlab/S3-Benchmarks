export fn agent_energy_residual(actual: [*]const f64, actual_n: i64, load: [*]const f64,
    load_n: i64, count: i64, output: [*]f64, output_n: i64) i64 {
    if (count <= 0 or count > 364 or actual_n != count or load_n != count or output_n != 3) return 1;
    var signed_sum: f64 = 0; var absolute_sum: f64 = 0; var maximum_absolute: f64 = 0;
    var i: i64 = 0;
    while (i < count) : (i += 1) {
        const index: usize = @intCast(i);
        const difference = actual[index] - load[index];
        const magnitude = if (difference < 0) 0 - difference else difference;
        signed_sum += difference; absolute_sum += magnitude;
        if (magnitude > maximum_absolute) maximum_absolute = magnitude;
    }
    var divisor: f64 = 0; i = 0; while (i < count) : (i += 1) { divisor += 1; }
    output[0]=signed_sum; output[1]=maximum_absolute; output[2]=absolute_sum/divisor;
    return 0;
}

export fn agent_point_bounds(coordinates: [*]const f64, coordinate_n: i64,
    point_count: i64, output: [*]f64, output_n: i64) i64 {
    if (point_count <= 0 or point_count > 121 or coordinate_n != point_count * 3 or output_n != 6) return 1;
    var min_x=coordinates[0]; var min_y=coordinates[1]; var min_z=coordinates[2];
    var max_x=min_x; var max_y=min_y; var max_z=min_z;
    var base: i64=3;
    while (base < point_count * 3) : (base += 3) {
        const b: usize=@intCast(base); const x=coordinates[b]; const y=coordinates[b+1]; const z=coordinates[b+2];
        if (x < min_x) min_x=x; if (x > max_x) max_x=x;
        if (y < min_y) min_y=y; if (y > max_y) max_y=y;
        if (z < min_z) min_z=z; if (z > max_z) max_z=z;
    }
    output[0]=min_x; output[1]=min_y; output[2]=min_z; output[3]=max_x; output[4]=max_y; output[5]=max_z;
    return 0;
}

export fn agent_raster_threshold_count(values: [*]const f64, value_n: i64, valid_mask: [*]const i64,
    mask_n: i64, cell_count: i64, threshold: f64, output: [*]i64, output_n: i64) i64 {
    if (cell_count <= 0 or cell_count > 364 or value_n != cell_count or mask_n != cell_count or output_n != 1) return 1;
    var count: i64=0; var i: i64=0;
    while (i < cell_count) : (i += 1) { const k: usize=@intCast(i); if (valid_mask[k] == 1 and values[k] > threshold) count += 1; }
    output[0]=count; return 0;
}

export fn agent_raster_valid_mean(values: [*]const f64, value_n: i64, valid_mask: [*]const i64,
    mask_n: i64, cell_count: i64, output: [*]f64, output_n: i64) i64 {
    if (cell_count <= 0 or cell_count > 364 or value_n != cell_count or mask_n != cell_count or output_n != 1) return 1;
    var sum: f64=0; var valid_count: i64=0; var i: i64=0;
    while (i < cell_count) : (i += 1) { const k: usize=@intCast(i); if (valid_mask[k] == 1) { sum += values[k]; valid_count += 1; } }
    if (valid_count == 0) return 1;
    var divisor: f64=0; i=0; while (i < valid_count) : (i += 1) { divisor += 1; }
    output[0]=sum/divisor; return 0;
}

export fn energy_series_aggregation(ac_power: [*]const f64, ac_count: i64, load: [*]const f64,
    load_count: i64, capacity_w: f64, output: [*]f64, output_count: i64) i64 {
    if (ac_count <= 0 or ac_count > 364 or capacity_w <= 0) return 1;
    if (load_count != ac_count or output_count != 5) return 2;
    var ac_energy: f64=0; var net_energy: f64=0; var peak=ac_power[0]; var absolute_balance: f64=0;
    var i: i64=0;
    while (i < ac_count) : (i += 1) {
        const k: usize=@intCast(i); const ac=ac_power[k]; const demand=load[k];
        ac_energy += ac; net_energy = net_energy + ac - demand;
        const balance=ac-demand; absolute_balance += if (balance < 0) 0-balance else balance;
        if (ac > peak) peak=ac;
    }
    const count_f: f64=@floatFromInt(ac_count);
    output[0]=ac_energy; output[1]=peak; output[2]=net_energy;
    output[3]=ac_energy/(capacity_w*count_f); output[4]=absolute_balance/count_f;
    return 0;
}

export fn point_cloud_summary(coordinates: [*]const f64, coordinate_n: i64,
    point_count: i64, output: [*]f64, output_n: i64) i64 {
    if (point_count <= 0 or point_count > 121) return 1;
    if (coordinate_n != point_count * 3 or output_n != 10) return 2;
    var min_x=coordinates[0]; var min_y=coordinates[1]; var min_z=coordinates[2];
    var max_x=min_x; var max_y=min_y; var max_z=min_z;
    var total_x: f64=0; var total_y: f64=0; var total_z: f64=0;
    var point: i64=0;
    while (point < point_count) : (point += 1) {
        const base: usize=@intCast(point*3); const x=coordinates[base]; const y=coordinates[base+1]; const z=coordinates[base+2];
        total_x += x; total_y += y; total_z += z;
        if (x < min_x) min_x=x; if (y < min_y) min_y=y; if (z < min_z) min_z=z;
        if (x > max_x) max_x=x; if (y > max_y) max_y=y; if (z > max_z) max_z=z;
    }
    const count_f: f64=@floatFromInt(point_count);
    const center_x=total_x/count_f; const center_y=total_y/count_f; const center_z=total_z/count_f;
    var squared_radius_sum: f64=0; point=0;
    while (point < point_count) : (point += 1) {
        const base: usize=@intCast(point*3); const dx=coordinates[base]-center_x;
        const dy=coordinates[base+1]-center_y; const dz=coordinates[base+2]-center_z;
        squared_radius_sum += dx*dx + dy*dy + dz*dz;
    }
    output[0]=center_x; output[1]=center_y; output[2]=center_z;
    output[3]=min_x; output[4]=min_y; output[5]=min_z;
    output[6]=max_x; output[7]=max_y; output[8]=max_z;
    output[9]=@sqrt(squared_radius_sum/count_f);
    return 0;
}
