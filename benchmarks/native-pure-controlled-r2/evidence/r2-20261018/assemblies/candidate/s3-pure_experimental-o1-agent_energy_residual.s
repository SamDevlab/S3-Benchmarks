.intel_syntax noprefix
# Generated deterministically by the S3 Linux x86-64 backend.
.section .text
.globl agent_energy_residual
.type agent_energy_residual, @function
agent_energy_residual:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_0
    push rbp
    mov rbp, rsp
    sub rsp, 2752
    mov qword ptr [rbp - 2680], rbx
    mov qword ptr [rbp - 2688], r12
    mov qword ptr [rbp - 2696], r13
    mov qword ptr [rbp - 8], rdi
    mov qword ptr [rbp - 16], rsi
    mov qword ptr [rbp - 24], rdx
    mov qword ptr [rbp - 32], rcx
    mov qword ptr [rbp - 40], r8
    mov qword ptr [rbp - 48], r9
    mov rax, qword ptr [rbp + 16]
    mov qword ptr [rbp - 56], rax
    mov rcx, qword ptr [rbp - 8]
    mov r8, qword ptr [rbp - 16]
    mov r9, qword ptr [rbp - 24]
    mov rbx, qword ptr [rbp - 32]
    mov rdx, qword ptr [rbp - 40]
    mov rdi, qword ptr [rbp - 48]
    mov rsi, qword ptr [rbp - 56]
    mov r10, rdi
    mov r11, rcx
    mov byte ptr [rbp - 2265], 0
    mov byte ptr [rbp - 2266], 0
    mov byte ptr [rbp - 2267], 0
    mov byte ptr [rbp - 2268], 0
    mov byte ptr [rbp - 2269], 0
    mov byte ptr [rbp - 2270], 0
    mov byte ptr [rbp - 2271], 0
    mov byte ptr [rbp - 2272], 0
    mov byte ptr [rbp - 2273], 0
    mov byte ptr [rbp - 2274], 0
    mov byte ptr [rbp - 2275], 0
    mov byte ptr [rbp - 2276], 0
    mov byte ptr [rbp - 2277], 0
    mov byte ptr [rbp - 2278], 0
    mov byte ptr [rbp - 2279], 0
    mov byte ptr [rbp - 2280], 0
    mov byte ptr [rbp - 2281], 0
    mov byte ptr [rbp - 2282], 0
    mov byte ptr [rbp - 2283], 0
    mov byte ptr [rbp - 2284], 0
    mov byte ptr [rbp - 2285], 0
    mov byte ptr [rbp - 2286], 0
    mov byte ptr [rbp - 2287], 0
    mov byte ptr [rbp - 2288], 0
    mov byte ptr [rbp - 2289], 0
    mov byte ptr [rbp - 2290], 0
    mov byte ptr [rbp - 2291], 0
    mov byte ptr [rbp - 2292], 0
    mov byte ptr [rbp - 2293], 0
    mov byte ptr [rbp - 2294], 0
    mov byte ptr [rbp - 2295], 0
    mov byte ptr [rbp - 2296], 0
    mov byte ptr [rbp - 2297], 0
    mov byte ptr [rbp - 2298], 0
    mov byte ptr [rbp - 2299], 0
    mov byte ptr [rbp - 2300], 0
    mov byte ptr [rbp - 2301], 0
    mov byte ptr [rbp - 2302], 0
    mov byte ptr [rbp - 2303], 0
    mov byte ptr [rbp - 2304], 0
    mov byte ptr [rbp - 2305], 0
    mov byte ptr [rbp - 2306], 0
    mov byte ptr [rbp - 2307], 0
    mov byte ptr [rbp - 2308], 0
    mov byte ptr [rbp - 2309], 0
    mov byte ptr [rbp - 2310], 0
    mov byte ptr [rbp - 2311], 0
    mov byte ptr [rbp - 2312], 0
    mov byte ptr [rbp - 2313], 0
    mov byte ptr [rbp - 2314], 0
    mov byte ptr [rbp - 2315], 0
    mov byte ptr [rbp - 2316], 0
    mov byte ptr [rbp - 2317], 0
    mov byte ptr [rbp - 2318], 0
    mov byte ptr [rbp - 2319], 0
    mov byte ptr [rbp - 2320], 0
    mov byte ptr [rbp - 2321], 0
    mov byte ptr [rbp - 2322], 0
    mov byte ptr [rbp - 2323], 0
    mov byte ptr [rbp - 2324], 0
    mov byte ptr [rbp - 2325], 0
    mov byte ptr [rbp - 2326], 0
    mov byte ptr [rbp - 2327], 0
    mov byte ptr [rbp - 2328], 0
    mov byte ptr [rbp - 2329], 0
    mov byte ptr [rbp - 2330], 0
    mov byte ptr [rbp - 2331], 0
    mov byte ptr [rbp - 2332], 0
    mov byte ptr [rbp - 2333], 0
    mov byte ptr [rbp - 2334], 0
    mov byte ptr [rbp - 2335], 0
    mov byte ptr [rbp - 2336], 0
    mov byte ptr [rbp - 2337], 0
    mov byte ptr [rbp - 2338], 0
    mov byte ptr [rbp - 2339], 0
    mov byte ptr [rbp - 2340], 0
    mov byte ptr [rbp - 2341], 0
    mov byte ptr [rbp - 2342], 0
    mov byte ptr [rbp - 2343], 0
    mov byte ptr [rbp - 2344], 0
    mov byte ptr [rbp - 2345], 0
    mov byte ptr [rbp - 2346], 0
    mov byte ptr [rbp - 2347], 0
    mov byte ptr [rbp - 2348], 0
    mov byte ptr [rbp - 2349], 0
    mov byte ptr [rbp - 2350], 0
    mov byte ptr [rbp - 2351], 0
    mov byte ptr [rbp - 2352], 0
    mov byte ptr [rbp - 2353], 0
    mov byte ptr [rbp - 2354], 0
    mov byte ptr [rbp - 2355], 0
    mov byte ptr [rbp - 2356], 0
    mov byte ptr [rbp - 2357], 0
    mov byte ptr [rbp - 2358], 0
    mov byte ptr [rbp - 2359], 0
    mov byte ptr [rbp - 2360], 0
    mov byte ptr [rbp - 2361], 0
    mov byte ptr [rbp - 2362], 0
    mov byte ptr [rbp - 2363], 0
    mov byte ptr [rbp - 2364], 0
    mov byte ptr [rbp - 2365], 0
    mov byte ptr [rbp - 2366], 0
    mov byte ptr [rbp - 2367], 0
    mov byte ptr [rbp - 2368], 0
    mov byte ptr [rbp - 2369], 0
    mov byte ptr [rbp - 2370], 0
    mov byte ptr [rbp - 2371], 0
    mov byte ptr [rbp - 2372], 0
    mov byte ptr [rbp - 2373], 0
    mov byte ptr [rbp - 2374], 0
    mov byte ptr [rbp - 2375], 0
    mov byte ptr [rbp - 2376], 0
    mov byte ptr [rbp - 2377], 0
    mov byte ptr [rbp - 2378], 0
    mov byte ptr [rbp - 2379], 0
    mov byte ptr [rbp - 2380], 0
    mov byte ptr [rbp - 2381], 0
    mov byte ptr [rbp - 2382], 0
    mov byte ptr [rbp - 2383], 0
    mov byte ptr [rbp - 2384], 0
    mov byte ptr [rbp - 2385], 0
    mov byte ptr [rbp - 2386], 0
    mov byte ptr [rbp - 2387], 0
    mov byte ptr [rbp - 2388], 0
    mov byte ptr [rbp - 2389], 0
    mov byte ptr [rbp - 2390], 0
    mov byte ptr [rbp - 2391], 0
    mov byte ptr [rbp - 2392], 0
    mov byte ptr [rbp - 2393], 0
    mov byte ptr [rbp - 2394], 0
    mov byte ptr [rbp - 2395], 0
    mov byte ptr [rbp - 2396], 0
    mov byte ptr [rbp - 2397], 0
    mov byte ptr [rbp - 2398], 0
    mov byte ptr [rbp - 2399], 0
    mov byte ptr [rbp - 2400], 0
    mov byte ptr [rbp - 2401], 0
    mov byte ptr [rbp - 2402], 0
    mov byte ptr [rbp - 2403], 0
    mov byte ptr [rbp - 2404], 0
    mov byte ptr [rbp - 2405], 0
    mov byte ptr [rbp - 2406], 0
    mov byte ptr [rbp - 2407], 0
    mov byte ptr [rbp - 2408], 0
    mov byte ptr [rbp - 2409], 0
    mov byte ptr [rbp - 2410], 0
    mov byte ptr [rbp - 2411], 0
    mov byte ptr [rbp - 2412], 0
    mov byte ptr [rbp - 2413], 0
    mov byte ptr [rbp - 2414], 0
    mov byte ptr [rbp - 2415], 0
    mov byte ptr [rbp - 2416], 0
    mov byte ptr [rbp - 2417], 0
    mov byte ptr [rbp - 2418], 0
    mov byte ptr [rbp - 2419], 0
    mov byte ptr [rbp - 2420], 0
    mov byte ptr [rbp - 2421], 0
    mov byte ptr [rbp - 2422], 0
    mov byte ptr [rbp - 2423], 0
    mov byte ptr [rbp - 2424], 0
    mov byte ptr [rbp - 2425], 0
    mov byte ptr [rbp - 2426], 0
    mov byte ptr [rbp - 2427], 0
    mov byte ptr [rbp - 2428], 0
    mov byte ptr [rbp - 2429], 0
    mov byte ptr [rbp - 2430], 0
    mov byte ptr [rbp - 2431], 0
    mov byte ptr [rbp - 2432], 0
    mov byte ptr [rbp - 2433], 0
    mov byte ptr [rbp - 2434], 0
    mov byte ptr [rbp - 2435], 0
    mov byte ptr [rbp - 2436], 0
    mov byte ptr [rbp - 2437], 0
    mov byte ptr [rbp - 2438], 0
    mov byte ptr [rbp - 2439], 0
    mov byte ptr [rbp - 2440], 0
    mov byte ptr [rbp - 2441], 0
    mov byte ptr [rbp - 2442], 0
    mov byte ptr [rbp - 2443], 0
    mov byte ptr [rbp - 2444], 0
    mov byte ptr [rbp - 2445], 0
    mov byte ptr [rbp - 2446], 0
    mov byte ptr [rbp - 2447], 0
    mov byte ptr [rbp - 2448], 0
    mov byte ptr [rbp - 2449], 0
    mov byte ptr [rbp - 2450], 0
    mov byte ptr [rbp - 2451], 0
    mov byte ptr [rbp - 2452], 0
    mov byte ptr [rbp - 2453], 0
    mov byte ptr [rbp - 2454], 0
    mov byte ptr [rbp - 2455], 0
    mov byte ptr [rbp - 2456], 0
    mov byte ptr [rbp - 2457], 0
    mov byte ptr [rbp - 2458], 0
    mov byte ptr [rbp - 2459], 0
    mov byte ptr [rbp - 2460], 0
    mov byte ptr [rbp - 2461], 0
    mov byte ptr [rbp - 2462], 0
    mov byte ptr [rbp - 2463], 0
    mov byte ptr [rbp - 2464], 0
    mov byte ptr [rbp - 2465], 0
    mov byte ptr [rbp - 2466], 0
    mov byte ptr [rbp - 2467], 0
    mov byte ptr [rbp - 2468], 0
    mov byte ptr [rbp - 2469], 0
    mov byte ptr [rbp - 2470], 0
    mov byte ptr [rbp - 2471], 0
    mov byte ptr [rbp - 2472], 0
    mov byte ptr [rbp - 2473], 0
    mov byte ptr [rbp - 2474], 0
    mov byte ptr [rbp - 2475], 0
    mov byte ptr [rbp - 2476], 0
    mov byte ptr [rbp - 2477], 0
    mov byte ptr [rbp - 2478], 0
    mov byte ptr [rbp - 2479], 0
    mov byte ptr [rbp - 2480], 0
    mov byte ptr [rbp - 2481], 0
    mov byte ptr [rbp - 2482], 0
    mov byte ptr [rbp - 2483], 0
    mov byte ptr [rbp - 2484], 0
    mov byte ptr [rbp - 2485], 0
    mov byte ptr [rbp - 2486], 0
    mov byte ptr [rbp - 2487], 0
    mov byte ptr [rbp - 2488], 0
    mov byte ptr [rbp - 2489], 0
    mov byte ptr [rbp - 2490], 0
    mov byte ptr [rbp - 2491], 0
    mov byte ptr [rbp - 2492], 0
    mov byte ptr [rbp - 2493], 0
    mov byte ptr [rbp - 2494], 0
    mov byte ptr [rbp - 2495], 0
    mov byte ptr [rbp - 2496], 0
    mov byte ptr [rbp - 2497], 0
    mov byte ptr [rbp - 2498], 0
    mov byte ptr [rbp - 2499], 0
    mov byte ptr [rbp - 2500], 0
    mov byte ptr [rbp - 2501], 0
    mov byte ptr [rbp - 2502], 0
    mov byte ptr [rbp - 2503], 0
    mov byte ptr [rbp - 2504], 0
    mov byte ptr [rbp - 2505], 0
    mov byte ptr [rbp - 2506], 0
    mov byte ptr [rbp - 2507], 0
    mov byte ptr [rbp - 2508], 0
    mov byte ptr [rbp - 2509], 0
    mov byte ptr [rbp - 2510], 0
    mov byte ptr [rbp - 2511], 0
    mov byte ptr [rbp - 2512], 0
    mov byte ptr [rbp - 2513], 0
    mov byte ptr [rbp - 2514], 0
    mov byte ptr [rbp - 2515], 0
    mov byte ptr [rbp - 2516], 0
    mov byte ptr [rbp - 2517], 0
    mov byte ptr [rbp - 2518], 0
    mov byte ptr [rbp - 2519], 0
    mov byte ptr [rbp - 2520], 0
    mov byte ptr [rbp - 2521], 0
    mov byte ptr [rbp - 2522], 0
    mov byte ptr [rbp - 2523], 0
    mov byte ptr [rbp - 2524], 0
    mov byte ptr [rbp - 2525], 0
    mov byte ptr [rbp - 2526], 0
    mov byte ptr [rbp - 2527], 0
    mov byte ptr [rbp - 2528], 0
    mov byte ptr [rbp - 2529], 0
    mov byte ptr [rbp - 2530], 0
    mov byte ptr [rbp - 2531], 0
    mov byte ptr [rbp - 2532], 0
    mov byte ptr [rbp - 2533], 0
    mov byte ptr [rbp - 2534], 0
    mov byte ptr [rbp - 2535], 0
    mov byte ptr [rbp - 2536], 0
    mov byte ptr [rbp - 2537], 0
    mov byte ptr [rbp - 2538], 0
    mov byte ptr [rbp - 2539], 0
    mov byte ptr [rbp - 2540], 0
    mov byte ptr [rbp - 2541], 0
    mov byte ptr [rbp - 2542], 0
    mov byte ptr [rbp - 2543], 0
    mov byte ptr [rbp - 2544], 0
    mov byte ptr [rbp - 2545], 0
    mov byte ptr [rbp - 2546], 0
    mov byte ptr [rbp - 2547], 0
    lea rdi, [rbp - 2650]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2651]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2652]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2653]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2654]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2655]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2656]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2657]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2658]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2659]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2660]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2661]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2662]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2663]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2664]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2665]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2666]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2667]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2668]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2669]
    mov ecx, 1
    xor eax, eax
    rep stosb
    mov rdi, r10
    mov rcx, r11
    mov byte ptr [rbp - 2265], 1
    mov byte ptr [rbp - 2266], 1
    mov byte ptr [rbp - 2267], 1
    mov byte ptr [rbp - 2268], 1
    mov byte ptr [rbp - 2269], 1
    mov byte ptr [rbp - 2270], 1
    mov byte ptr [rbp - 2271], 1
    jmp .L_s3_f21_agent_energy_residual_b5_entry
.L_s3_f21_agent_energy_residual_b5_entry:
    mov r12, 0
    mov byte ptr [rbp - 2272], 1
    mov r13, 0
    mov byte ptr [rbp - 2273], 1
    cmp byte ptr [rbp - 2273], 0
    je .L__s3_failure_site_1
    mov rax, r13
    cmp byte ptr [rbp - 2272], 0
    je .L__s3_failure_site_2
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_3
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    mov r12, 0
    mov byte ptr [rbp - 2274], 1
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_4
    mov rax, rdx
    cmp byte ptr [rbp - 2274], 0
    je .L__s3_failure_site_5
    mov r10, r12
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b9_rel_neg_0
    jg .L_s3_f21_agent_energy_residual_b9_rel_pos_2
    jmp .L_s3_f21_agent_energy_residual_b10_rel_zero_1
.L_s3_f21_agent_energy_residual_b9_rel_neg_0:
    mov r12, 0
    mov byte ptr [rbp - 2276], 1
    mov r13, -1
    mov byte ptr [rbp - 2277], 1
    cmp byte ptr [rbp - 2276], 0
    je .L__s3_failure_site_6
    mov rax, r12
    cmp byte ptr [rbp - 2277], 0
    je .L__s3_failure_site_7
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_8
    cmp r10, -1
    jl .L__s3_failure_site_9
    cmp r10, 1
    jg .L__s3_failure_site_9
    mov byte ptr [rbp + rax - 2561], r10b
    mov byte ptr [rbp + rax - 2651], 1
    jmp .L_s3_f21_agent_energy_residual_b10_rel_cont_3
.L_s3_f21_agent_energy_residual_b10_rel_zero_1:
    mov r12, 0
    mov byte ptr [rbp - 2278], 1
    mov r13, -1
    mov byte ptr [rbp - 2279], 1
    cmp byte ptr [rbp - 2278], 0
    je .L__s3_failure_site_10
    mov rax, r12
    cmp byte ptr [rbp - 2279], 0
    je .L__s3_failure_site_11
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_12
    cmp r10, -1
    jl .L__s3_failure_site_13
    cmp r10, 1
    jg .L__s3_failure_site_13
    mov byte ptr [rbp + rax - 2561], r10b
    mov byte ptr [rbp + rax - 2651], 1
    jmp .L_s3_f21_agent_energy_residual_b10_rel_cont_3
.L_s3_f21_agent_energy_residual_b9_rel_pos_2:
    mov r12, 0
    mov byte ptr [rbp - 2280], 1
    mov r13, 0
    mov byte ptr [rbp - 2281], 1
    cmp byte ptr [rbp - 2280], 0
    je .L__s3_failure_site_14
    mov rax, r12
    cmp byte ptr [rbp - 2281], 0
    je .L__s3_failure_site_15
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_16
    cmp r10, -1
    jl .L__s3_failure_site_17
    cmp r10, 1
    jg .L__s3_failure_site_17
    mov byte ptr [rbp + rax - 2561], r10b
    mov byte ptr [rbp + rax - 2651], 1
    jmp .L_s3_f21_agent_energy_residual_b10_rel_cont_3
.L_s3_f21_agent_energy_residual_b10_rel_cont_3:
    mov r12, 0
    mov byte ptr [rbp - 2282], 1
    cmp byte ptr [rbp - 2282], 0
    je .L__s3_failure_site_19
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_20
    cmp byte ptr [rbp + r10 - 2651], 0
    je .L__s3_failure_site_18
    movsx rax, byte ptr [rbp + r10 - 2561]
    mov r12, rax
    mov byte ptr [rbp - 2283], 1
    cmp byte ptr [rbp - 2283], 0
    je .L__s3_failure_site_22
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b17_switch_negative_4
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b16_switch_neutral_5
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b17_switch_positive_6
    jmp .L__s3_failure_site_21
.L_s3_f21_agent_energy_residual_b17_switch_negative_4:
    mov r12, 1
    mov byte ptr [rbp - 2284], 1
    mov r13, 0
    mov byte ptr [rbp - 2285], 1
    cmp byte ptr [rbp - 2285], 0
    je .L__s3_failure_site_23
    mov rax, r13
    cmp byte ptr [rbp - 2284], 0
    je .L__s3_failure_site_24
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_25
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b17_switch_continue_7
.L_s3_f21_agent_energy_residual_b16_switch_neutral_5:
    mov r12, 0
    mov byte ptr [rbp - 2286], 1
    cmp byte ptr [rbp - 2286], 0
    je .L__s3_failure_site_27
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_28
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_26
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2287], 1
    mov r13, 0
    mov byte ptr [rbp - 2288], 1
    cmp byte ptr [rbp - 2288], 0
    je .L__s3_failure_site_29
    mov rax, r13
    cmp byte ptr [rbp - 2287], 0
    je .L__s3_failure_site_30
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_31
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b17_switch_continue_7
.L_s3_f21_agent_energy_residual_b17_switch_positive_6:
    mov r12, 0
    mov byte ptr [rbp - 2289], 1
    cmp byte ptr [rbp - 2289], 0
    je .L__s3_failure_site_33
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_34
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_32
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2290], 1
    mov r13, 0
    mov byte ptr [rbp - 2291], 1
    cmp byte ptr [rbp - 2291], 0
    je .L__s3_failure_site_35
    mov rax, r13
    cmp byte ptr [rbp - 2290], 0
    je .L__s3_failure_site_36
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_37
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b17_switch_continue_7
.L_s3_f21_agent_energy_residual_b17_switch_continue_7:
    mov r12, 364
    mov byte ptr [rbp - 2292], 1
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_38
    mov rax, rdx
    cmp byte ptr [rbp - 2292], 0
    je .L__s3_failure_site_39
    mov r10, r12
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b9_rel_neg_8
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_10
    jmp .L_s3_f21_agent_energy_residual_b10_rel_zero_9
.L_s3_f21_agent_energy_residual_b9_rel_neg_8:
    mov r12, 0
    mov byte ptr [rbp - 2294], 1
    mov r13, 0
    mov byte ptr [rbp - 2295], 1
    cmp byte ptr [rbp - 2294], 0
    je .L__s3_failure_site_40
    mov rax, r12
    cmp byte ptr [rbp - 2295], 0
    je .L__s3_failure_site_41
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_42
    cmp r10, -1
    jl .L__s3_failure_site_43
    cmp r10, 1
    jg .L__s3_failure_site_43
    mov byte ptr [rbp + rax - 2562], r10b
    mov byte ptr [rbp + rax - 2652], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_11
.L_s3_f21_agent_energy_residual_b10_rel_zero_9:
    mov r12, 0
    mov byte ptr [rbp - 2296], 1
    mov r13, 0
    mov byte ptr [rbp - 2297], 1
    cmp byte ptr [rbp - 2296], 0
    je .L__s3_failure_site_44
    mov rax, r12
    cmp byte ptr [rbp - 2297], 0
    je .L__s3_failure_site_45
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_46
    cmp r10, -1
    jl .L__s3_failure_site_47
    cmp r10, 1
    jg .L__s3_failure_site_47
    mov byte ptr [rbp + rax - 2562], r10b
    mov byte ptr [rbp + rax - 2652], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_11
.L_s3_f21_agent_energy_residual_b10_rel_pos_10:
    mov r12, 0
    mov byte ptr [rbp - 2298], 1
    mov r13, -1
    mov byte ptr [rbp - 2299], 1
    cmp byte ptr [rbp - 2298], 0
    je .L__s3_failure_site_48
    mov rax, r12
    cmp byte ptr [rbp - 2299], 0
    je .L__s3_failure_site_49
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_50
    cmp r10, -1
    jl .L__s3_failure_site_51
    cmp r10, 1
    jg .L__s3_failure_site_51
    mov byte ptr [rbp + rax - 2562], r10b
    mov byte ptr [rbp + rax - 2652], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_11
.L_s3_f21_agent_energy_residual_b11_rel_cont_11:
    mov r12, 0
    mov byte ptr [rbp - 2300], 1
    cmp byte ptr [rbp - 2300], 0
    je .L__s3_failure_site_53
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_54
    cmp byte ptr [rbp + r10 - 2652], 0
    je .L__s3_failure_site_52
    movsx rax, byte ptr [rbp + r10 - 2562]
    mov r12, rax
    mov byte ptr [rbp - 2301], 1
    cmp byte ptr [rbp - 2301], 0
    je .L__s3_failure_site_56
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_12
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_13
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_14
    jmp .L__s3_failure_site_55
.L_s3_f21_agent_energy_residual_b18_switch_negative_12:
    mov r12, 1
    mov byte ptr [rbp - 2302], 1
    mov r13, 0
    mov byte ptr [rbp - 2303], 1
    cmp byte ptr [rbp - 2303], 0
    je .L__s3_failure_site_57
    mov rax, r13
    cmp byte ptr [rbp - 2302], 0
    je .L__s3_failure_site_58
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_59
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_15
.L_s3_f21_agent_energy_residual_b17_switch_neutral_13:
    mov r12, 0
    mov byte ptr [rbp - 2304], 1
    cmp byte ptr [rbp - 2304], 0
    je .L__s3_failure_site_61
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_62
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_60
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2305], 1
    mov r13, 0
    mov byte ptr [rbp - 2306], 1
    cmp byte ptr [rbp - 2306], 0
    je .L__s3_failure_site_63
    mov rax, r13
    cmp byte ptr [rbp - 2305], 0
    je .L__s3_failure_site_64
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_65
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_15
.L_s3_f21_agent_energy_residual_b18_switch_positive_14:
    mov r12, 0
    mov byte ptr [rbp - 2307], 1
    cmp byte ptr [rbp - 2307], 0
    je .L__s3_failure_site_67
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_68
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_66
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2308], 1
    mov r13, 0
    mov byte ptr [rbp - 2309], 1
    cmp byte ptr [rbp - 2309], 0
    je .L__s3_failure_site_69
    mov rax, r13
    cmp byte ptr [rbp - 2308], 0
    je .L__s3_failure_site_70
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_71
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_15
.L_s3_f21_agent_energy_residual_b18_switch_continue_15:
    mov r12, 0
    mov byte ptr [rbp - 2310], 1
    cmp byte ptr [rbp - 2310], 0
    je .L__s3_failure_site_73
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_74
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_72
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2311], 1
    mov r13, 0
    mov byte ptr [rbp - 2312], 1
    cmp byte ptr [rbp - 2311], 0
    je .L__s3_failure_site_75
    mov rax, r12
    cmp byte ptr [rbp - 2312], 0
    je .L__s3_failure_site_76
    mov r10, r13
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_16
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_18
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_17
.L_s3_f21_agent_energy_residual_b10_rel_neg_16:
    mov r12, 0
    mov byte ptr [rbp - 2314], 1
    mov r13, 0
    mov byte ptr [rbp - 2315], 1
    cmp byte ptr [rbp - 2314], 0
    je .L__s3_failure_site_77
    mov rax, r12
    cmp byte ptr [rbp - 2315], 0
    je .L__s3_failure_site_78
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_79
    cmp r10, -1
    jl .L__s3_failure_site_80
    cmp r10, 1
    jg .L__s3_failure_site_80
    mov byte ptr [rbp + rax - 2563], r10b
    mov byte ptr [rbp + rax - 2653], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_19
.L_s3_f21_agent_energy_residual_b11_rel_zero_17:
    mov r12, 0
    mov byte ptr [rbp - 2316], 1
    mov r13, -1
    mov byte ptr [rbp - 2317], 1
    cmp byte ptr [rbp - 2316], 0
    je .L__s3_failure_site_81
    mov rax, r12
    cmp byte ptr [rbp - 2317], 0
    je .L__s3_failure_site_82
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_83
    cmp r10, -1
    jl .L__s3_failure_site_84
    cmp r10, 1
    jg .L__s3_failure_site_84
    mov byte ptr [rbp + rax - 2563], r10b
    mov byte ptr [rbp + rax - 2653], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_19
.L_s3_f21_agent_energy_residual_b10_rel_pos_18:
    mov r12, 0
    mov byte ptr [rbp - 2318], 1
    mov r13, 0
    mov byte ptr [rbp - 2319], 1
    cmp byte ptr [rbp - 2318], 0
    je .L__s3_failure_site_85
    mov rax, r12
    cmp byte ptr [rbp - 2319], 0
    je .L__s3_failure_site_86
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_87
    cmp r10, -1
    jl .L__s3_failure_site_88
    cmp r10, 1
    jg .L__s3_failure_site_88
    mov byte ptr [rbp + rax - 2563], r10b
    mov byte ptr [rbp + rax - 2653], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_19
.L_s3_f21_agent_energy_residual_b11_rel_cont_19:
    mov r12, 0
    mov byte ptr [rbp - 2320], 1
    cmp byte ptr [rbp - 2320], 0
    je .L__s3_failure_site_90
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_91
    cmp byte ptr [rbp + r10 - 2653], 0
    je .L__s3_failure_site_89
    movsx rax, byte ptr [rbp + r10 - 2563]
    mov r12, rax
    mov byte ptr [rbp - 2321], 1
    cmp byte ptr [rbp - 2321], 0
    je .L__s3_failure_site_93
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_20
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_21
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_22
    jmp .L__s3_failure_site_92
.L_s3_f21_agent_energy_residual_b18_switch_negative_20:
    cmp byte ptr [rbp - 2266], 0
    je .L__s3_failure_site_94
    mov rax, r8
    mov r12, rax
    mov byte ptr [rbp - 2322], 1
    cmp byte ptr [rbp - 2322], 0
    je .L__s3_failure_site_95
    mov rax, r12
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_96
    mov r10, rdx
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_23
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_25
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_24
.L_s3_f21_agent_energy_residual_b17_switch_neutral_21:
    mov r12, 0
    mov byte ptr [rbp - 2356], 1
    cmp byte ptr [rbp - 2356], 0
    je .L__s3_failure_site_98
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_99
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_97
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2357], 1
    mov r13, 0
    mov byte ptr [rbp - 2358], 1
    cmp byte ptr [rbp - 2358], 0
    je .L__s3_failure_site_100
    mov rax, r13
    cmp byte ptr [rbp - 2357], 0
    je .L__s3_failure_site_101
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_102
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b18_switch_positive_22:
    mov r12, 0
    mov byte ptr [rbp - 2359], 1
    cmp byte ptr [rbp - 2359], 0
    je .L__s3_failure_site_104
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_105
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_103
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2360], 1
    mov r13, 0
    mov byte ptr [rbp - 2361], 1
    cmp byte ptr [rbp - 2361], 0
    je .L__s3_failure_site_106
    mov rax, r13
    cmp byte ptr [rbp - 2360], 0
    je .L__s3_failure_site_107
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_108
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b10_rel_neg_23:
    mov r12, 0
    mov byte ptr [rbp - 2324], 1
    mov r13, 0
    mov byte ptr [rbp - 2325], 1
    cmp byte ptr [rbp - 2324], 0
    je .L__s3_failure_site_109
    mov rax, r12
    cmp byte ptr [rbp - 2325], 0
    je .L__s3_failure_site_110
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_111
    cmp r10, -1
    jl .L__s3_failure_site_112
    cmp r10, 1
    jg .L__s3_failure_site_112
    mov byte ptr [rbp + rax - 2564], r10b
    mov byte ptr [rbp + rax - 2654], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_26
.L_s3_f21_agent_energy_residual_b11_rel_zero_24:
    mov r12, 0
    mov byte ptr [rbp - 2326], 1
    mov r13, -1
    mov byte ptr [rbp - 2327], 1
    cmp byte ptr [rbp - 2326], 0
    je .L__s3_failure_site_113
    mov rax, r12
    cmp byte ptr [rbp - 2327], 0
    je .L__s3_failure_site_114
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_115
    cmp r10, -1
    jl .L__s3_failure_site_116
    cmp r10, 1
    jg .L__s3_failure_site_116
    mov byte ptr [rbp + rax - 2564], r10b
    mov byte ptr [rbp + rax - 2654], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_26
.L_s3_f21_agent_energy_residual_b10_rel_pos_25:
    mov r12, 0
    mov byte ptr [rbp - 2328], 1
    mov r13, 0
    mov byte ptr [rbp - 2329], 1
    cmp byte ptr [rbp - 2328], 0
    je .L__s3_failure_site_117
    mov rax, r12
    cmp byte ptr [rbp - 2329], 0
    je .L__s3_failure_site_118
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_119
    cmp r10, -1
    jl .L__s3_failure_site_120
    cmp r10, 1
    jg .L__s3_failure_site_120
    mov byte ptr [rbp + rax - 2564], r10b
    mov byte ptr [rbp + rax - 2654], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_26
.L_s3_f21_agent_energy_residual_b11_rel_cont_26:
    mov r12, 0
    mov byte ptr [rbp - 2330], 1
    cmp byte ptr [rbp - 2330], 0
    je .L__s3_failure_site_122
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_123
    cmp byte ptr [rbp + r10 - 2654], 0
    je .L__s3_failure_site_121
    movsx rax, byte ptr [rbp + r10 - 2564]
    mov r12, rax
    mov byte ptr [rbp - 2331], 1
    cmp byte ptr [rbp - 2331], 0
    je .L__s3_failure_site_125
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_27
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_28
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_29
    jmp .L__s3_failure_site_124
.L_s3_f21_agent_energy_residual_b18_switch_negative_27:
    mov r12, 0
    mov byte ptr [rbp - 2332], 1
    cmp byte ptr [rbp - 2332], 0
    je .L__s3_failure_site_127
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_128
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_126
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2333], 1
    mov r13, 0
    mov byte ptr [rbp - 2334], 1
    cmp byte ptr [rbp - 2334], 0
    je .L__s3_failure_site_129
    mov rax, r13
    cmp byte ptr [rbp - 2333], 0
    je .L__s3_failure_site_130
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_131
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_30
.L_s3_f21_agent_energy_residual_b17_switch_neutral_28:
    mov r12, 1
    mov byte ptr [rbp - 2335], 1
    mov r13, 0
    mov byte ptr [rbp - 2336], 1
    cmp byte ptr [rbp - 2336], 0
    je .L__s3_failure_site_132
    mov rax, r13
    cmp byte ptr [rbp - 2335], 0
    je .L__s3_failure_site_133
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_134
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_30
.L_s3_f21_agent_energy_residual_b18_switch_positive_29:
    mov r12, 1
    mov byte ptr [rbp - 2337], 1
    mov r13, 0
    mov byte ptr [rbp - 2338], 1
    cmp byte ptr [rbp - 2338], 0
    je .L__s3_failure_site_135
    mov rax, r13
    cmp byte ptr [rbp - 2337], 0
    je .L__s3_failure_site_136
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_137
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_30
.L_s3_f21_agent_energy_residual_b18_switch_continue_30:
    cmp byte ptr [rbp - 2268], 0
    je .L__s3_failure_site_138
    mov rax, rbx
    mov r12, rax
    mov byte ptr [rbp - 2339], 1
    cmp byte ptr [rbp - 2339], 0
    je .L__s3_failure_site_139
    mov rax, r12
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_140
    mov r10, rdx
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_31
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_33
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_32
.L_s3_f21_agent_energy_residual_b10_rel_neg_31:
    mov r12, 0
    mov byte ptr [rbp - 2341], 1
    mov r13, 0
    mov byte ptr [rbp - 2342], 1
    cmp byte ptr [rbp - 2341], 0
    je .L__s3_failure_site_141
    mov rax, r12
    cmp byte ptr [rbp - 2342], 0
    je .L__s3_failure_site_142
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_143
    cmp r10, -1
    jl .L__s3_failure_site_144
    cmp r10, 1
    jg .L__s3_failure_site_144
    mov byte ptr [rbp + rax - 2565], r10b
    mov byte ptr [rbp + rax - 2655], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_34
.L_s3_f21_agent_energy_residual_b11_rel_zero_32:
    mov r12, 0
    mov byte ptr [rbp - 2343], 1
    mov r13, -1
    mov byte ptr [rbp - 2344], 1
    cmp byte ptr [rbp - 2343], 0
    je .L__s3_failure_site_145
    mov rax, r12
    cmp byte ptr [rbp - 2344], 0
    je .L__s3_failure_site_146
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_147
    cmp r10, -1
    jl .L__s3_failure_site_148
    cmp r10, 1
    jg .L__s3_failure_site_148
    mov byte ptr [rbp + rax - 2565], r10b
    mov byte ptr [rbp + rax - 2655], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_34
.L_s3_f21_agent_energy_residual_b10_rel_pos_33:
    mov r12, 0
    mov byte ptr [rbp - 2345], 1
    mov r13, 0
    mov byte ptr [rbp - 2346], 1
    cmp byte ptr [rbp - 2345], 0
    je .L__s3_failure_site_149
    mov rax, r12
    cmp byte ptr [rbp - 2346], 0
    je .L__s3_failure_site_150
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_151
    cmp r10, -1
    jl .L__s3_failure_site_152
    cmp r10, 1
    jg .L__s3_failure_site_152
    mov byte ptr [rbp + rax - 2565], r10b
    mov byte ptr [rbp + rax - 2655], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_34
.L_s3_f21_agent_energy_residual_b11_rel_cont_34:
    mov r12, 0
    mov byte ptr [rbp - 2347], 1
    cmp byte ptr [rbp - 2347], 0
    je .L__s3_failure_site_154
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_155
    cmp byte ptr [rbp + r10 - 2655], 0
    je .L__s3_failure_site_153
    movsx rax, byte ptr [rbp + r10 - 2565]
    mov r12, rax
    mov byte ptr [rbp - 2348], 1
    cmp byte ptr [rbp - 2348], 0
    je .L__s3_failure_site_157
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_35
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_36
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_37
    jmp .L__s3_failure_site_156
.L_s3_f21_agent_energy_residual_b18_switch_negative_35:
    mov r12, 0
    mov byte ptr [rbp - 2349], 1
    cmp byte ptr [rbp - 2349], 0
    je .L__s3_failure_site_159
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_160
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_158
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2350], 1
    mov r13, 0
    mov byte ptr [rbp - 2351], 1
    cmp byte ptr [rbp - 2351], 0
    je .L__s3_failure_site_161
    mov rax, r13
    cmp byte ptr [rbp - 2350], 0
    je .L__s3_failure_site_162
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_163
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b17_switch_neutral_36:
    mov r12, 1
    mov byte ptr [rbp - 2352], 1
    mov r13, 0
    mov byte ptr [rbp - 2353], 1
    cmp byte ptr [rbp - 2353], 0
    je .L__s3_failure_site_164
    mov rax, r13
    cmp byte ptr [rbp - 2352], 0
    je .L__s3_failure_site_165
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_166
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b18_switch_positive_37:
    mov r12, 1
    mov byte ptr [rbp - 2354], 1
    mov r13, 0
    mov byte ptr [rbp - 2355], 1
    cmp byte ptr [rbp - 2355], 0
    je .L__s3_failure_site_167
    mov rax, r13
    cmp byte ptr [rbp - 2354], 0
    je .L__s3_failure_site_168
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_169
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b18_switch_continue_39:
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_170
    mov rax, rsi
    mov r12, rax
    mov byte ptr [rbp - 2362], 1
    mov r13, 3
    mov byte ptr [rbp - 2363], 1
    cmp byte ptr [rbp - 2362], 0
    je .L__s3_failure_site_171
    mov rax, r12
    cmp byte ptr [rbp - 2363], 0
    je .L__s3_failure_site_172
    mov r10, r13
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_40
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_42
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_41
.L_s3_f21_agent_energy_residual_b10_rel_neg_40:
    mov r12, 0
    mov byte ptr [rbp - 2365], 1
    mov r13, -1
    mov byte ptr [rbp - 2366], 1
    cmp byte ptr [rbp - 2365], 0
    je .L__s3_failure_site_173
    mov rax, r12
    cmp byte ptr [rbp - 2366], 0
    je .L__s3_failure_site_174
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_175
    cmp r10, -1
    jl .L__s3_failure_site_176
    cmp r10, 1
    jg .L__s3_failure_site_176
    mov byte ptr [rbp + rax - 2566], r10b
    mov byte ptr [rbp + rax - 2656], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_43
.L_s3_f21_agent_energy_residual_b11_rel_zero_41:
    mov r12, 0
    mov byte ptr [rbp - 2367], 1
    mov r13, 0
    mov byte ptr [rbp - 2368], 1
    cmp byte ptr [rbp - 2367], 0
    je .L__s3_failure_site_177
    mov rax, r12
    cmp byte ptr [rbp - 2368], 0
    je .L__s3_failure_site_178
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_179
    cmp r10, -1
    jl .L__s3_failure_site_180
    cmp r10, 1
    jg .L__s3_failure_site_180
    mov byte ptr [rbp + rax - 2566], r10b
    mov byte ptr [rbp + rax - 2656], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_43
.L_s3_f21_agent_energy_residual_b10_rel_pos_42:
    mov r12, 0
    mov byte ptr [rbp - 2369], 1
    mov r13, 0
    mov byte ptr [rbp - 2370], 1
    cmp byte ptr [rbp - 2369], 0
    je .L__s3_failure_site_181
    mov rax, r12
    cmp byte ptr [rbp - 2370], 0
    je .L__s3_failure_site_182
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_183
    cmp r10, -1
    jl .L__s3_failure_site_184
    cmp r10, 1
    jg .L__s3_failure_site_184
    mov byte ptr [rbp + rax - 2566], r10b
    mov byte ptr [rbp + rax - 2656], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_43
.L_s3_f21_agent_energy_residual_b11_rel_cont_43:
    mov r12, 0
    mov byte ptr [rbp - 2371], 1
    cmp byte ptr [rbp - 2371], 0
    je .L__s3_failure_site_186
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_187
    cmp byte ptr [rbp + r10 - 2656], 0
    je .L__s3_failure_site_185
    movsx rax, byte ptr [rbp + r10 - 2566]
    mov r12, rax
    mov byte ptr [rbp - 2372], 1
    cmp byte ptr [rbp - 2372], 0
    je .L__s3_failure_site_189
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_44
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_45
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_46
    jmp .L__s3_failure_site_188
.L_s3_f21_agent_energy_residual_b18_switch_negative_44:
    mov r12, 0
    mov byte ptr [rbp - 2373], 1
    cmp byte ptr [rbp - 2373], 0
    je .L__s3_failure_site_191
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_192
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_190
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2374], 1
    mov r13, 0
    mov byte ptr [rbp - 2375], 1
    cmp byte ptr [rbp - 2374], 0
    je .L__s3_failure_site_193
    mov rax, r12
    cmp byte ptr [rbp - 2375], 0
    je .L__s3_failure_site_194
    mov r10, r13
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_47
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_49
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_48
.L_s3_f21_agent_energy_residual_b17_switch_neutral_45:
    mov r12, 0
    mov byte ptr [rbp - 2393], 1
    cmp byte ptr [rbp - 2393], 0
    je .L__s3_failure_site_196
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_197
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_195
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2394], 1
    mov r13, 0
    mov byte ptr [rbp - 2395], 1
    cmp byte ptr [rbp - 2395], 0
    je .L__s3_failure_site_198
    mov rax, r13
    cmp byte ptr [rbp - 2394], 0
    je .L__s3_failure_site_199
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_200
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b18_switch_positive_46:
    mov r12, 0
    mov byte ptr [rbp - 2396], 1
    cmp byte ptr [rbp - 2396], 0
    je .L__s3_failure_site_202
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_203
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_201
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2397], 1
    mov r13, 0
    mov byte ptr [rbp - 2398], 1
    cmp byte ptr [rbp - 2398], 0
    je .L__s3_failure_site_204
    mov rax, r13
    cmp byte ptr [rbp - 2397], 0
    je .L__s3_failure_site_205
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_206
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b10_rel_neg_47:
    mov r12, 0
    mov byte ptr [rbp - 2377], 1
    mov r13, 0
    mov byte ptr [rbp - 2378], 1
    cmp byte ptr [rbp - 2377], 0
    je .L__s3_failure_site_207
    mov rax, r12
    cmp byte ptr [rbp - 2378], 0
    je .L__s3_failure_site_208
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_209
    cmp r10, -1
    jl .L__s3_failure_site_210
    cmp r10, 1
    jg .L__s3_failure_site_210
    mov byte ptr [rbp + rax - 2567], r10b
    mov byte ptr [rbp + rax - 2657], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_50
.L_s3_f21_agent_energy_residual_b11_rel_zero_48:
    mov r12, 0
    mov byte ptr [rbp - 2379], 1
    mov r13, -1
    mov byte ptr [rbp - 2380], 1
    cmp byte ptr [rbp - 2379], 0
    je .L__s3_failure_site_211
    mov rax, r12
    cmp byte ptr [rbp - 2380], 0
    je .L__s3_failure_site_212
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_213
    cmp r10, -1
    jl .L__s3_failure_site_214
    cmp r10, 1
    jg .L__s3_failure_site_214
    mov byte ptr [rbp + rax - 2567], r10b
    mov byte ptr [rbp + rax - 2657], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_50
.L_s3_f21_agent_energy_residual_b10_rel_pos_49:
    mov r12, 0
    mov byte ptr [rbp - 2381], 1
    mov r13, 0
    mov byte ptr [rbp - 2382], 1
    cmp byte ptr [rbp - 2381], 0
    je .L__s3_failure_site_215
    mov rax, r12
    cmp byte ptr [rbp - 2382], 0
    je .L__s3_failure_site_216
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_217
    cmp r10, -1
    jl .L__s3_failure_site_218
    cmp r10, 1
    jg .L__s3_failure_site_218
    mov byte ptr [rbp + rax - 2567], r10b
    mov byte ptr [rbp + rax - 2657], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_50
.L_s3_f21_agent_energy_residual_b11_rel_cont_50:
    mov r12, 0
    mov byte ptr [rbp - 2383], 1
    cmp byte ptr [rbp - 2383], 0
    je .L__s3_failure_site_220
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_221
    cmp byte ptr [rbp + r10 - 2657], 0
    je .L__s3_failure_site_219
    movsx rax, byte ptr [rbp + r10 - 2567]
    mov r12, rax
    mov byte ptr [rbp - 2384], 1
    cmp byte ptr [rbp - 2384], 0
    je .L__s3_failure_site_223
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_51
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_52
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_53
    jmp .L__s3_failure_site_222
.L_s3_f21_agent_energy_residual_b18_switch_negative_51:
    mov r12, 2
    mov byte ptr [rbp - 2385], 1
    mov r13, 0
    mov byte ptr [rbp - 2386], 1
    cmp byte ptr [rbp - 2386], 0
    je .L__s3_failure_site_224
    mov rax, r13
    cmp byte ptr [rbp - 2385], 0
    je .L__s3_failure_site_225
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_226
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b17_switch_neutral_52:
    mov r12, 0
    mov byte ptr [rbp - 2387], 1
    cmp byte ptr [rbp - 2387], 0
    je .L__s3_failure_site_228
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_229
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_227
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2388], 1
    mov r13, 0
    mov byte ptr [rbp - 2389], 1
    cmp byte ptr [rbp - 2389], 0
    je .L__s3_failure_site_230
    mov rax, r13
    cmp byte ptr [rbp - 2388], 0
    je .L__s3_failure_site_231
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_232
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b18_switch_positive_53:
    mov r12, 0
    mov byte ptr [rbp - 2390], 1
    cmp byte ptr [rbp - 2390], 0
    je .L__s3_failure_site_234
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_235
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_233
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2391], 1
    mov r13, 0
    mov byte ptr [rbp - 2392], 1
    cmp byte ptr [rbp - 2392], 0
    je .L__s3_failure_site_236
    mov rax, r13
    cmp byte ptr [rbp - 2391], 0
    je .L__s3_failure_site_237
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_238
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b18_switch_continue_55:
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_239
    mov rax, rsi
    mov r12, rax
    mov byte ptr [rbp - 2399], 1
    mov r13, 3
    mov byte ptr [rbp - 2400], 1
    cmp byte ptr [rbp - 2399], 0
    je .L__s3_failure_site_240
    mov rax, r12
    cmp byte ptr [rbp - 2400], 0
    je .L__s3_failure_site_241
    mov r10, r13
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_56
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_58
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_57
.L_s3_f21_agent_energy_residual_b10_rel_neg_56:
    mov r12, 0
    mov byte ptr [rbp - 2402], 1
    mov r13, 0
    mov byte ptr [rbp - 2403], 1
    cmp byte ptr [rbp - 2402], 0
    je .L__s3_failure_site_242
    mov rax, r12
    cmp byte ptr [rbp - 2403], 0
    je .L__s3_failure_site_243
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_244
    cmp r10, -1
    jl .L__s3_failure_site_245
    cmp r10, 1
    jg .L__s3_failure_site_245
    mov byte ptr [rbp + rax - 2568], r10b
    mov byte ptr [rbp + rax - 2658], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_59
.L_s3_f21_agent_energy_residual_b11_rel_zero_57:
    mov r12, 0
    mov byte ptr [rbp - 2404], 1
    mov r13, 0
    mov byte ptr [rbp - 2405], 1
    cmp byte ptr [rbp - 2404], 0
    je .L__s3_failure_site_246
    mov rax, r12
    cmp byte ptr [rbp - 2405], 0
    je .L__s3_failure_site_247
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_248
    cmp r10, -1
    jl .L__s3_failure_site_249
    cmp r10, 1
    jg .L__s3_failure_site_249
    mov byte ptr [rbp + rax - 2568], r10b
    mov byte ptr [rbp + rax - 2658], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_59
.L_s3_f21_agent_energy_residual_b10_rel_pos_58:
    mov r12, 0
    mov byte ptr [rbp - 2406], 1
    mov r13, -1
    mov byte ptr [rbp - 2407], 1
    cmp byte ptr [rbp - 2406], 0
    je .L__s3_failure_site_250
    mov rax, r12
    cmp byte ptr [rbp - 2407], 0
    je .L__s3_failure_site_251
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_252
    cmp r10, -1
    jl .L__s3_failure_site_253
    cmp r10, 1
    jg .L__s3_failure_site_253
    mov byte ptr [rbp + rax - 2568], r10b
    mov byte ptr [rbp + rax - 2658], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_59
.L_s3_f21_agent_energy_residual_b11_rel_cont_59:
    mov r12, 0
    mov byte ptr [rbp - 2408], 1
    cmp byte ptr [rbp - 2408], 0
    je .L__s3_failure_site_255
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_256
    cmp byte ptr [rbp + r10 - 2658], 0
    je .L__s3_failure_site_254
    movsx rax, byte ptr [rbp + r10 - 2568]
    mov r12, rax
    mov byte ptr [rbp - 2409], 1
    cmp byte ptr [rbp - 2409], 0
    je .L__s3_failure_site_258
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_60
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_61
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_62
    jmp .L__s3_failure_site_257
.L_s3_f21_agent_energy_residual_b18_switch_negative_60:
    mov r12, 1
    mov byte ptr [rbp - 2410], 1
    mov r13, 0
    mov byte ptr [rbp - 2411], 1
    cmp byte ptr [rbp - 2411], 0
    je .L__s3_failure_site_259
    mov rax, r13
    cmp byte ptr [rbp - 2410], 0
    je .L__s3_failure_site_260
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_261
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_63
.L_s3_f21_agent_energy_residual_b17_switch_neutral_61:
    mov r12, 0
    mov byte ptr [rbp - 2412], 1
    cmp byte ptr [rbp - 2412], 0
    je .L__s3_failure_site_263
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_264
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_262
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2413], 1
    mov r13, 0
    mov byte ptr [rbp - 2414], 1
    cmp byte ptr [rbp - 2414], 0
    je .L__s3_failure_site_265
    mov rax, r13
    cmp byte ptr [rbp - 2413], 0
    je .L__s3_failure_site_266
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_267
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_63
.L_s3_f21_agent_energy_residual_b18_switch_positive_62:
    mov r12, 0
    mov byte ptr [rbp - 2415], 1
    cmp byte ptr [rbp - 2415], 0
    je .L__s3_failure_site_269
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_270
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_268
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2416], 1
    mov r13, 0
    mov byte ptr [rbp - 2417], 1
    cmp byte ptr [rbp - 2417], 0
    je .L__s3_failure_site_271
    mov rax, r13
    cmp byte ptr [rbp - 2416], 0
    je .L__s3_failure_site_272
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_273
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_63
.L_s3_f21_agent_energy_residual_b18_switch_continue_63:
    mov r12, 0
    mov byte ptr [rbp - 2418], 1
    cmp byte ptr [rbp - 2418], 0
    je .L__s3_failure_site_275
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_276
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_274
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2419], 1
    mov r13, 0
    mov byte ptr [rbp - 2420], 1
    cmp byte ptr [rbp - 2419], 0
    je .L__s3_failure_site_277
    mov rax, r12
    cmp byte ptr [rbp - 2420], 0
    je .L__s3_failure_site_278
    mov r10, r13
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_64
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_66
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_65
.L_s3_f21_agent_energy_residual_b10_rel_neg_64:
    mov r12, 0
    mov byte ptr [rbp - 2422], 1
    mov r13, 0
    mov byte ptr [rbp - 2423], 1
    cmp byte ptr [rbp - 2422], 0
    je .L__s3_failure_site_279
    mov rax, r12
    cmp byte ptr [rbp - 2423], 0
    je .L__s3_failure_site_280
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_281
    cmp r10, -1
    jl .L__s3_failure_site_282
    cmp r10, 1
    jg .L__s3_failure_site_282
    mov byte ptr [rbp + rax - 2569], r10b
    mov byte ptr [rbp + rax - 2659], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_67
.L_s3_f21_agent_energy_residual_b11_rel_zero_65:
    mov r12, 0
    mov byte ptr [rbp - 2424], 1
    mov r13, -1
    mov byte ptr [rbp - 2425], 1
    cmp byte ptr [rbp - 2424], 0
    je .L__s3_failure_site_283
    mov rax, r12
    cmp byte ptr [rbp - 2425], 0
    je .L__s3_failure_site_284
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_285
    cmp r10, -1
    jl .L__s3_failure_site_286
    cmp r10, 1
    jg .L__s3_failure_site_286
    mov byte ptr [rbp + rax - 2569], r10b
    mov byte ptr [rbp + rax - 2659], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_67
.L_s3_f21_agent_energy_residual_b10_rel_pos_66:
    mov r12, 0
    mov byte ptr [rbp - 2426], 1
    mov r13, 0
    mov byte ptr [rbp - 2427], 1
    cmp byte ptr [rbp - 2426], 0
    je .L__s3_failure_site_287
    mov rax, r12
    cmp byte ptr [rbp - 2427], 0
    je .L__s3_failure_site_288
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_289
    cmp r10, -1
    jl .L__s3_failure_site_290
    cmp r10, 1
    jg .L__s3_failure_site_290
    mov byte ptr [rbp + rax - 2569], r10b
    mov byte ptr [rbp + rax - 2659], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_67
.L_s3_f21_agent_energy_residual_b11_rel_cont_67:
    mov r12, 0
    mov byte ptr [rbp - 2428], 1
    cmp byte ptr [rbp - 2428], 0
    je .L__s3_failure_site_292
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_293
    cmp byte ptr [rbp + r10 - 2659], 0
    je .L__s3_failure_site_291
    movsx rax, byte ptr [rbp + r10 - 2569]
    mov r12, rax
    mov byte ptr [rbp - 2429], 1
    cmp byte ptr [rbp - 2429], 0
    je .L__s3_failure_site_295
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_68
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_69
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_70
    jmp .L__s3_failure_site_294
.L_s3_f21_agent_energy_residual_b18_switch_negative_68:
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2430], 1
    mov r13, 0
    mov byte ptr [rbp - 2431], 1
    cmp byte ptr [rbp - 2431], 0
    je .L__s3_failure_site_296
    mov rax, r13
    cmp byte ptr [rbp - 2430], 0
    je .L__s3_failure_site_297
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_298
    mov qword ptr [rbp + rax*8 - 2584], r10
    mov byte ptr [rbp + rax - 2660], 1
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2432], 1
    mov r13, 0
    mov byte ptr [rbp - 2433], 1
    cmp byte ptr [rbp - 2433], 0
    je .L__s3_failure_site_299
    mov rax, r13
    cmp byte ptr [rbp - 2432], 0
    je .L__s3_failure_site_300
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_301
    mov qword ptr [rbp + rax*8 - 2592], r10
    mov byte ptr [rbp + rax - 2661], 1
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2434], 1
    mov r13, 0
    mov byte ptr [rbp - 2435], 1
    cmp byte ptr [rbp - 2435], 0
    je .L__s3_failure_site_302
    mov rax, r13
    cmp byte ptr [rbp - 2434], 0
    je .L__s3_failure_site_303
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_304
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    mov r12, 0
    mov byte ptr [rbp - 2436], 1
    mov r13, 0
    mov byte ptr [rbp - 2437], 1
    cmp byte ptr [rbp - 2437], 0
    je .L__s3_failure_site_305
    mov rax, r13
    cmp byte ptr [rbp - 2436], 0
    je .L__s3_failure_site_306
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_307
    mov qword ptr [rbp + rax*8 - 2608], r10
    mov byte ptr [rbp + rax - 2663], 1
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_71
.L_s3_f21_agent_energy_residual_b17_switch_neutral_69:
    mov rdi, 0
    mov byte ptr [rbp - 2544], 1
    cmp byte ptr [rbp - 2544], 0
    je .L__s3_failure_site_309
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_310
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_308
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov rdi, rax
    mov byte ptr [rbp - 2545], 1
    cmp byte ptr [rbp - 2545], 0
    je .L__s3_failure_site_311
    mov rax, rdi
    mov rbx, qword ptr [rbp - 2680]
    mov r12, qword ptr [rbp - 2688]
    mov r13, qword ptr [rbp - 2696]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f21_agent_energy_residual_b18_switch_positive_70:
    mov rdi, 0
    mov byte ptr [rbp - 2546], 1
    cmp byte ptr [rbp - 2546], 0
    je .L__s3_failure_site_313
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_314
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_312
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov rdi, rax
    mov byte ptr [rbp - 2547], 1
    cmp byte ptr [rbp - 2547], 0
    je .L__s3_failure_site_315
    mov rax, rdi
    mov rbx, qword ptr [rbp - 2680]
    mov r12, qword ptr [rbp - 2688]
    mov r13, qword ptr [rbp - 2696]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f21_agent_energy_residual_b18_while_condition_71:
    mov r12, 0
    mov byte ptr [rbp - 2438], 1
    cmp byte ptr [rbp - 2438], 0
    je .L__s3_failure_site_317
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_318
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_316
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r12, rax
    mov byte ptr [rbp - 2439], 1
    cmp byte ptr [rbp - 2439], 0
    je .L__s3_failure_site_319
    mov rax, r12
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_320
    mov r10, rdx
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_76
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_78
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_77
.L_s3_f21_agent_energy_residual_b13_while_body_72:
    mov r12, 0
    mov byte ptr [rbp - 2449], 1
    cmp byte ptr [rbp - 2449], 0
    je .L__s3_failure_site_322
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_323
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_321
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r12, rax
    mov byte ptr [rbp - 2450], 1
    cmp byte ptr [rbp - 2265], 0
    je .L__s3_failure_site_325
    cmp byte ptr [rbp - 2266], 0
    je .L__s3_failure_site_326
    cmp byte ptr [rbp - 2450], 0
    je .L__s3_failure_site_327
    cmp r12, r8
    jae .L__s3_failure_site_324
    mov r12, qword ptr [rcx + r12 * 8]
    mov byte ptr [rbp - 2451], 1
    mov r13, 0
    mov byte ptr [rbp - 2452], 1
    cmp byte ptr [rbp - 2452], 0
    je .L__s3_failure_site_329
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_330
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_328
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r13, rax
    mov byte ptr [rbp - 2453], 1
    cmp byte ptr [rbp - 2267], 0
    je .L__s3_failure_site_332
    cmp byte ptr [rbp - 2268], 0
    je .L__s3_failure_site_333
    cmp byte ptr [rbp - 2453], 0
    je .L__s3_failure_site_334
    cmp r13, rbx
    jae .L__s3_failure_site_331
    mov r13, qword ptr [r9 + r13 * 8]
    mov byte ptr [rbp - 2454], 1
    cmp byte ptr [rbp - 2451], 0
    je .L__s3_failure_site_335
    mov rax, r12
    cmp byte ptr [rbp - 2454], 0
    je .L__s3_failure_site_336
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2455], 1
    mov r13, 0
    mov byte ptr [rbp - 2456], 1
    cmp byte ptr [rbp - 2456], 0
    je .L__s3_failure_site_337
    mov rax, r13
    cmp byte ptr [rbp - 2455], 0
    je .L__s3_failure_site_338
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_339
    mov qword ptr [rbp + rax*8 - 2624], r10
    mov byte ptr [rbp + rax - 2665], 1
    mov r12, 0
    mov byte ptr [rbp - 2457], 1
    cmp byte ptr [rbp - 2457], 0
    je .L__s3_failure_site_341
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_342
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_340
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2458], 1
    mov r13, 0
    mov byte ptr [rbp - 2459], 1
    cmp byte ptr [rbp - 2459], 0
    je .L__s3_failure_site_343
    mov rax, r13
    cmp byte ptr [rbp - 2458], 0
    je .L__s3_failure_site_344
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_345
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    mov r12, 0
    mov byte ptr [rbp - 2460], 1
    cmp byte ptr [rbp - 2460], 0
    je .L__s3_failure_site_347
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_348
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_346
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2461], 1
    movabs rax, 0
    mov r13, rax
    mov byte ptr [rbp - 2462], 1
    cmp byte ptr [rbp - 2461], 0
    je .L__s3_failure_site_349
    mov rax, r12
    cmp byte ptr [rbp - 2462], 0
    je .L__s3_failure_site_350
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    ucomisd xmm0, xmm1
    setb al
    setnp r11b
    and al, r11b
    movzx r11, al
    neg r11
    mov r12, r11
    mov byte ptr [rbp - 2463], 1
    cmp byte ptr [rbp - 2463], 0
    je .L__s3_failure_site_352
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_80
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_81
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_82
    jmp .L__s3_failure_site_351
.L_s3_f21_agent_energy_residual_b15_while_exit_0_73:
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_75
.L_s3_f21_agent_energy_residual_b15_while_exit_1_74:
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_75
.L_s3_f21_agent_energy_residual_b13_while_exit_75:
    movabs rax, 0
    mov rcx, rax
    mov byte ptr [rbp - 2506], 1
    mov r8, 0
    mov byte ptr [rbp - 2507], 1
    cmp byte ptr [rbp - 2507], 0
    je .L__s3_failure_site_353
    mov rax, r8
    cmp byte ptr [rbp - 2506], 0
    je .L__s3_failure_site_354
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_355
    mov qword ptr [rbp + rax*8 - 2640], r10
    mov byte ptr [rbp + rax - 2667], 1
    mov rcx, 0
    mov byte ptr [rbp - 2508], 1
    mov r8, 0
    mov byte ptr [rbp - 2509], 1
    cmp byte ptr [rbp - 2509], 0
    je .L__s3_failure_site_356
    mov rax, r8
    cmp byte ptr [rbp - 2508], 0
    je .L__s3_failure_site_357
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_358
    mov qword ptr [rbp + rax*8 - 2648], r10
    mov byte ptr [rbp + rax - 2668], 1
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_88
.L_s3_f21_agent_energy_residual_b10_rel_neg_76:
    mov r12, 0
    mov byte ptr [rbp - 2441], 1
    mov r13, -1
    mov byte ptr [rbp - 2442], 1
    cmp byte ptr [rbp - 2441], 0
    je .L__s3_failure_site_359
    mov rax, r12
    cmp byte ptr [rbp - 2442], 0
    je .L__s3_failure_site_360
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_361
    cmp r10, -1
    jl .L__s3_failure_site_362
    cmp r10, 1
    jg .L__s3_failure_site_362
    mov byte ptr [rbp + rax - 2609], r10b
    mov byte ptr [rbp + rax - 2664], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_79
.L_s3_f21_agent_energy_residual_b11_rel_zero_77:
    mov r12, 0
    mov byte ptr [rbp - 2443], 1
    mov r13, 0
    mov byte ptr [rbp - 2444], 1
    cmp byte ptr [rbp - 2443], 0
    je .L__s3_failure_site_363
    mov rax, r12
    cmp byte ptr [rbp - 2444], 0
    je .L__s3_failure_site_364
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_365
    cmp r10, -1
    jl .L__s3_failure_site_366
    cmp r10, 1
    jg .L__s3_failure_site_366
    mov byte ptr [rbp + rax - 2609], r10b
    mov byte ptr [rbp + rax - 2664], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_79
.L_s3_f21_agent_energy_residual_b10_rel_pos_78:
    mov r12, 0
    mov byte ptr [rbp - 2445], 1
    mov r13, 0
    mov byte ptr [rbp - 2446], 1
    cmp byte ptr [rbp - 2445], 0
    je .L__s3_failure_site_367
    mov rax, r12
    cmp byte ptr [rbp - 2446], 0
    je .L__s3_failure_site_368
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_369
    cmp r10, -1
    jl .L__s3_failure_site_370
    cmp r10, 1
    jg .L__s3_failure_site_370
    mov byte ptr [rbp + rax - 2609], r10b
    mov byte ptr [rbp + rax - 2664], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_79
.L_s3_f21_agent_energy_residual_b11_rel_cont_79:
    mov r12, 0
    mov byte ptr [rbp - 2447], 1
    cmp byte ptr [rbp - 2447], 0
    je .L__s3_failure_site_372
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_373
    cmp byte ptr [rbp + r10 - 2664], 0
    je .L__s3_failure_site_371
    movsx rax, byte ptr [rbp + r10 - 2609]
    mov r12, rax
    mov byte ptr [rbp - 2448], 1
    cmp byte ptr [rbp - 2448], 0
    je .L__s3_failure_site_375
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b13_while_body_72
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b15_while_exit_0_73
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b15_while_exit_1_74
    jmp .L__s3_failure_site_374
.L_s3_f21_agent_energy_residual_b18_switch_negative_80:
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2464], 1
    mov r13, 0
    mov byte ptr [rbp - 2465], 1
    cmp byte ptr [rbp - 2465], 0
    je .L__s3_failure_site_377
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_378
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_376
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r13, rax
    mov byte ptr [rbp - 2466], 1
    cmp byte ptr [rbp - 2464], 0
    je .L__s3_failure_site_379
    mov rax, r12
    cmp byte ptr [rbp - 2466], 0
    je .L__s3_failure_site_380
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2467], 1
    mov r13, 0
    mov byte ptr [rbp - 2468], 1
    cmp byte ptr [rbp - 2468], 0
    je .L__s3_failure_site_381
    mov rax, r13
    cmp byte ptr [rbp - 2467], 0
    je .L__s3_failure_site_382
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_383
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_83
.L_s3_f21_agent_energy_residual_b17_switch_neutral_81:
    mov r12, 0
    mov byte ptr [rbp - 2469], 1
    cmp byte ptr [rbp - 2469], 0
    je .L__s3_failure_site_385
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_386
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_384
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2470], 1
    mov r13, 0
    mov byte ptr [rbp - 2471], 1
    cmp byte ptr [rbp - 2471], 0
    je .L__s3_failure_site_387
    mov rax, r13
    cmp byte ptr [rbp - 2470], 0
    je .L__s3_failure_site_388
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_389
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_83
.L_s3_f21_agent_energy_residual_b18_switch_positive_82:
    mov r12, 0
    mov byte ptr [rbp - 2472], 1
    cmp byte ptr [rbp - 2472], 0
    je .L__s3_failure_site_391
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_392
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_390
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2473], 1
    mov r13, 0
    mov byte ptr [rbp - 2474], 1
    cmp byte ptr [rbp - 2474], 0
    je .L__s3_failure_site_393
    mov rax, r13
    cmp byte ptr [rbp - 2473], 0
    je .L__s3_failure_site_394
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_395
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_83
.L_s3_f21_agent_energy_residual_b18_switch_continue_83:
    mov r12, 0
    mov byte ptr [rbp - 2475], 1
    cmp byte ptr [rbp - 2475], 0
    je .L__s3_failure_site_397
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_398
    cmp byte ptr [rbp + r10 - 2660], 0
    je .L__s3_failure_site_396
    mov rax, qword ptr [rbp + r10*8 - 2584]
    mov r12, rax
    mov byte ptr [rbp - 2476], 1
    mov r13, 0
    mov byte ptr [rbp - 2477], 1
    cmp byte ptr [rbp - 2477], 0
    je .L__s3_failure_site_400
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_401
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_399
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r13, rax
    mov byte ptr [rbp - 2478], 1
    cmp byte ptr [rbp - 2476], 0
    je .L__s3_failure_site_402
    mov rax, r12
    cmp byte ptr [rbp - 2478], 0
    je .L__s3_failure_site_403
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2479], 1
    mov r13, 0
    mov byte ptr [rbp - 2480], 1
    cmp byte ptr [rbp - 2480], 0
    je .L__s3_failure_site_404
    mov rax, r13
    cmp byte ptr [rbp - 2479], 0
    je .L__s3_failure_site_405
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_406
    mov qword ptr [rbp + rax*8 - 2584], r10
    mov byte ptr [rbp + rax - 2660], 1
    mov r12, 0
    mov byte ptr [rbp - 2481], 1
    cmp byte ptr [rbp - 2481], 0
    je .L__s3_failure_site_408
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_409
    cmp byte ptr [rbp + r10 - 2661], 0
    je .L__s3_failure_site_407
    mov rax, qword ptr [rbp + r10*8 - 2592]
    mov r12, rax
    mov byte ptr [rbp - 2482], 1
    mov r13, 0
    mov byte ptr [rbp - 2483], 1
    cmp byte ptr [rbp - 2483], 0
    je .L__s3_failure_site_411
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_412
    cmp byte ptr [rbp + r10 - 2666], 0
    je .L__s3_failure_site_410
    mov rax, qword ptr [rbp + r10*8 - 2632]
    mov r13, rax
    mov byte ptr [rbp - 2484], 1
    cmp byte ptr [rbp - 2482], 0
    je .L__s3_failure_site_413
    mov rax, r12
    cmp byte ptr [rbp - 2484], 0
    je .L__s3_failure_site_414
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2485], 1
    mov r13, 0
    mov byte ptr [rbp - 2486], 1
    cmp byte ptr [rbp - 2486], 0
    je .L__s3_failure_site_415
    mov rax, r13
    cmp byte ptr [rbp - 2485], 0
    je .L__s3_failure_site_416
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_417
    mov qword ptr [rbp + rax*8 - 2592], r10
    mov byte ptr [rbp + rax - 2661], 1
    mov r12, 0
    mov byte ptr [rbp - 2487], 1
    cmp byte ptr [rbp - 2487], 0
    je .L__s3_failure_site_419
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_420
    cmp byte ptr [rbp + r10 - 2666], 0
    je .L__s3_failure_site_418
    mov rax, qword ptr [rbp + r10*8 - 2632]
    mov r12, rax
    mov byte ptr [rbp - 2488], 1
    mov r13, 0
    mov byte ptr [rbp - 2489], 1
    cmp byte ptr [rbp - 2489], 0
    je .L__s3_failure_site_422
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_423
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_421
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov r13, rax
    mov byte ptr [rbp - 2490], 1
    cmp byte ptr [rbp - 2488], 0
    je .L__s3_failure_site_424
    mov rax, r12
    cmp byte ptr [rbp - 2490], 0
    je .L__s3_failure_site_425
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    ucomisd xmm0, xmm1
    seta al
    movzx r11, al
    neg r11
    mov r12, r11
    mov byte ptr [rbp - 2491], 1
    cmp byte ptr [rbp - 2491], 0
    je .L__s3_failure_site_427
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_84
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_85
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_86
    jmp .L__s3_failure_site_426
.L_s3_f21_agent_energy_residual_b18_switch_negative_84:
    mov r12, 0
    mov byte ptr [rbp - 2492], 1
    cmp byte ptr [rbp - 2492], 0
    je .L__s3_failure_site_429
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_430
    cmp byte ptr [rbp + r10 - 2666], 0
    je .L__s3_failure_site_428
    mov rax, qword ptr [rbp + r10*8 - 2632]
    mov r12, rax
    mov byte ptr [rbp - 2493], 1
    mov r13, 0
    mov byte ptr [rbp - 2494], 1
    cmp byte ptr [rbp - 2494], 0
    je .L__s3_failure_site_431
    mov rax, r13
    cmp byte ptr [rbp - 2493], 0
    je .L__s3_failure_site_432
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_433
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_87
.L_s3_f21_agent_energy_residual_b17_switch_neutral_85:
    mov r12, 0
    mov byte ptr [rbp - 2495], 1
    cmp byte ptr [rbp - 2495], 0
    je .L__s3_failure_site_435
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_436
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_434
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov r12, rax
    mov byte ptr [rbp - 2496], 1
    mov r13, 0
    mov byte ptr [rbp - 2497], 1
    cmp byte ptr [rbp - 2497], 0
    je .L__s3_failure_site_437
    mov rax, r13
    cmp byte ptr [rbp - 2496], 0
    je .L__s3_failure_site_438
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_439
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_87
.L_s3_f21_agent_energy_residual_b18_switch_positive_86:
    mov r12, 0
    mov byte ptr [rbp - 2498], 1
    cmp byte ptr [rbp - 2498], 0
    je .L__s3_failure_site_441
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_442
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_440
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov r12, rax
    mov byte ptr [rbp - 2499], 1
    mov r13, 0
    mov byte ptr [rbp - 2500], 1
    cmp byte ptr [rbp - 2500], 0
    je .L__s3_failure_site_443
    mov rax, r13
    cmp byte ptr [rbp - 2499], 0
    je .L__s3_failure_site_444
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_445
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_87
.L_s3_f21_agent_energy_residual_b18_switch_continue_87:
    mov r12, 0
    mov byte ptr [rbp - 2501], 1
    cmp byte ptr [rbp - 2501], 0
    je .L__s3_failure_site_447
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_448
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_446
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r12, rax
    mov byte ptr [rbp - 2502], 1
    mov r13, 1
    mov byte ptr [rbp - 2503], 1
    cmp byte ptr [rbp - 2502], 0
    je .L__s3_failure_site_450
    mov rax, r12
    cmp byte ptr [rbp - 2503], 0
    je .L__s3_failure_site_451
    mov r10, r13
    add rax, r10
    jo .L__s3_failure_site_449
    mov r12, rax
    mov byte ptr [rbp - 2504], 1
    mov r13, 0
    mov byte ptr [rbp - 2505], 1
    cmp byte ptr [rbp - 2505], 0
    je .L__s3_failure_site_452
    mov rax, r13
    cmp byte ptr [rbp - 2504], 0
    je .L__s3_failure_site_453
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_454
    mov qword ptr [rbp + rax*8 - 2608], r10
    mov byte ptr [rbp + rax - 2663], 1
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_71
.L_s3_f21_agent_energy_residual_b18_while_condition_88:
    mov rcx, 0
    mov byte ptr [rbp - 2510], 1
    cmp byte ptr [rbp - 2510], 0
    je .L__s3_failure_site_456
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_457
    cmp byte ptr [rbp + r10 - 2668], 0
    je .L__s3_failure_site_455
    mov rax, qword ptr [rbp + r10*8 - 2648]
    mov rcx, rax
    mov byte ptr [rbp - 2511], 1
    cmp byte ptr [rbp - 2511], 0
    je .L__s3_failure_site_458
    mov rax, rcx
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_459
    mov r10, rdx
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_93
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_95
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_94
.L_s3_f21_agent_energy_residual_b13_while_body_89:
    mov rcx, 0
    mov byte ptr [rbp - 2521], 1
    cmp byte ptr [rbp - 2521], 0
    je .L__s3_failure_site_461
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_462
    cmp byte ptr [rbp + r10 - 2667], 0
    je .L__s3_failure_site_460
    mov rax, qword ptr [rbp + r10*8 - 2640]
    mov rcx, rax
    mov byte ptr [rbp - 2522], 1
    movabs rax, 4607182418800017408
    mov r8, rax
    mov byte ptr [rbp - 2523], 1
    cmp byte ptr [rbp - 2522], 0
    je .L__s3_failure_site_463
    mov rax, rcx
    cmp byte ptr [rbp - 2523], 0
    je .L__s3_failure_site_464
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 2524], 1
    mov r8, 0
    mov byte ptr [rbp - 2525], 1
    cmp byte ptr [rbp - 2525], 0
    je .L__s3_failure_site_465
    mov rax, r8
    cmp byte ptr [rbp - 2524], 0
    je .L__s3_failure_site_466
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_467
    mov qword ptr [rbp + rax*8 - 2640], r10
    mov byte ptr [rbp + rax - 2667], 1
    mov rcx, 0
    mov byte ptr [rbp - 2526], 1
    cmp byte ptr [rbp - 2526], 0
    je .L__s3_failure_site_469
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_470
    cmp byte ptr [rbp + r10 - 2668], 0
    je .L__s3_failure_site_468
    mov rax, qword ptr [rbp + r10*8 - 2648]
    mov rcx, rax
    mov byte ptr [rbp - 2527], 1
    mov r8, 1
    mov byte ptr [rbp - 2528], 1
    cmp byte ptr [rbp - 2527], 0
    je .L__s3_failure_site_472
    mov rax, rcx
    cmp byte ptr [rbp - 2528], 0
    je .L__s3_failure_site_473
    mov r10, r8
    add rax, r10
    jo .L__s3_failure_site_471
    mov rcx, rax
    mov byte ptr [rbp - 2529], 1
    mov r8, 0
    mov byte ptr [rbp - 2530], 1
    cmp byte ptr [rbp - 2530], 0
    je .L__s3_failure_site_474
    mov rax, r8
    cmp byte ptr [rbp - 2529], 0
    je .L__s3_failure_site_475
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_476
    mov qword ptr [rbp + rax*8 - 2648], r10
    mov byte ptr [rbp + rax - 2668], 1
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_88
.L_s3_f21_agent_energy_residual_b15_while_exit_0_90:
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_92
.L_s3_f21_agent_energy_residual_b15_while_exit_1_91:
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_92
.L_s3_f21_agent_energy_residual_b13_while_exit_92:
    mov rdx, 0
    mov byte ptr [rbp - 2531], 1
    mov rcx, 0
    mov byte ptr [rbp - 2532], 1
    cmp byte ptr [rbp - 2532], 0
    je .L__s3_failure_site_478
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_479
    cmp byte ptr [rbp + r10 - 2660], 0
    je .L__s3_failure_site_477
    mov rax, qword ptr [rbp + r10*8 - 2584]
    mov rcx, rax
    mov byte ptr [rbp - 2533], 1
    cmp byte ptr [rbp - 2270], 0
    je .L__s3_failure_site_481
    mov r10, rdi
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_482
    mov r11, rsi
    cmp byte ptr [rbp - 2531], 0
    je .L__s3_failure_site_483
    mov rax, rdx
    cmp byte ptr [rbp - 2533], 0
    je .L__s3_failure_site_484
    cmp rax, r11
    jae .L__s3_failure_site_480
    mov qword ptr [r10 + rax * 8], rcx
    mov rdx, 1
    mov byte ptr [rbp - 2534], 1
    mov rcx, 0
    mov byte ptr [rbp - 2535], 1
    cmp byte ptr [rbp - 2535], 0
    je .L__s3_failure_site_486
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_487
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_485
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov rcx, rax
    mov byte ptr [rbp - 2536], 1
    cmp byte ptr [rbp - 2270], 0
    je .L__s3_failure_site_489
    mov r10, rdi
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_490
    mov r11, rsi
    cmp byte ptr [rbp - 2534], 0
    je .L__s3_failure_site_491
    mov rax, rdx
    cmp byte ptr [rbp - 2536], 0
    je .L__s3_failure_site_492
    cmp rax, r11
    jae .L__s3_failure_site_488
    mov qword ptr [r10 + rax * 8], rcx
    mov rdx, 2
    mov byte ptr [rbp - 2537], 1
    mov rcx, 0
    mov byte ptr [rbp - 2538], 1
    cmp byte ptr [rbp - 2538], 0
    je .L__s3_failure_site_494
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_495
    cmp byte ptr [rbp + r10 - 2661], 0
    je .L__s3_failure_site_493
    mov rax, qword ptr [rbp + r10*8 - 2592]
    mov rcx, rax
    mov byte ptr [rbp - 2539], 1
    mov r8, 0
    mov byte ptr [rbp - 2540], 1
    cmp byte ptr [rbp - 2540], 0
    je .L__s3_failure_site_497
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_498
    cmp byte ptr [rbp + r10 - 2667], 0
    je .L__s3_failure_site_496
    mov rax, qword ptr [rbp + r10*8 - 2640]
    mov r8, rax
    mov byte ptr [rbp - 2541], 1
    cmp byte ptr [rbp - 2539], 0
    je .L__s3_failure_site_499
    mov rax, rcx
    cmp byte ptr [rbp - 2541], 0
    je .L__s3_failure_site_500
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 2542], 1
    cmp byte ptr [rbp - 2270], 0
    je .L__s3_failure_site_502
    mov r10, rdi
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_503
    mov r11, rsi
    cmp byte ptr [rbp - 2537], 0
    je .L__s3_failure_site_504
    mov rax, rdx
    cmp byte ptr [rbp - 2542], 0
    je .L__s3_failure_site_505
    cmp rax, r11
    jae .L__s3_failure_site_501
    mov qword ptr [r10 + rax * 8], rcx
    mov rdi, 0
    mov byte ptr [rbp - 2543], 1
    cmp byte ptr [rbp - 2543], 0
    je .L__s3_failure_site_506
    mov rax, rdi
    mov rbx, qword ptr [rbp - 2680]
    mov r12, qword ptr [rbp - 2688]
    mov r13, qword ptr [rbp - 2696]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f21_agent_energy_residual_b10_rel_neg_93:
    mov rcx, 0
    mov byte ptr [rbp - 2513], 1
    mov r8, -1
    mov byte ptr [rbp - 2514], 1
    cmp byte ptr [rbp - 2513], 0
    je .L__s3_failure_site_507
    mov rax, rcx
    cmp byte ptr [rbp - 2514], 0
    je .L__s3_failure_site_508
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_509
    cmp r10, -1
    jl .L__s3_failure_site_510
    cmp r10, 1
    jg .L__s3_failure_site_510
    mov byte ptr [rbp + rax - 2649], r10b
    mov byte ptr [rbp + rax - 2669], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_96
.L_s3_f21_agent_energy_residual_b11_rel_zero_94:
    mov rcx, 0
    mov byte ptr [rbp - 2515], 1
    mov r8, 0
    mov byte ptr [rbp - 2516], 1
    cmp byte ptr [rbp - 2515], 0
    je .L__s3_failure_site_511
    mov rax, rcx
    cmp byte ptr [rbp - 2516], 0
    je .L__s3_failure_site_512
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_513
    cmp r10, -1
    jl .L__s3_failure_site_514
    cmp r10, 1
    jg .L__s3_failure_site_514
    mov byte ptr [rbp + rax - 2649], r10b
    mov byte ptr [rbp + rax - 2669], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_96
.L_s3_f21_agent_energy_residual_b10_rel_pos_95:
    mov rcx, 0
    mov byte ptr [rbp - 2517], 1
    mov r8, 0
    mov byte ptr [rbp - 2518], 1
    cmp byte ptr [rbp - 2517], 0
    je .L__s3_failure_site_515
    mov rax, rcx
    cmp byte ptr [rbp - 2518], 0
    je .L__s3_failure_site_516
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_517
    cmp r10, -1
    jl .L__s3_failure_site_518
    cmp r10, 1
    jg .L__s3_failure_site_518
    mov byte ptr [rbp + rax - 2649], r10b
    mov byte ptr [rbp + rax - 2669], 1
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_96
.L_s3_f21_agent_energy_residual_b11_rel_cont_96:
    mov rcx, 0
    mov byte ptr [rbp - 2519], 1
    cmp byte ptr [rbp - 2519], 0
    je .L__s3_failure_site_520
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_521
    cmp byte ptr [rbp + r10 - 2669], 0
    je .L__s3_failure_site_519
    movsx rax, byte ptr [rbp + r10 - 2649]
    mov rcx, rax
    mov byte ptr [rbp - 2520], 1
    cmp byte ptr [rbp - 2520], 0
    je .L__s3_failure_site_523
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b13_while_body_89
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b15_while_exit_0_90
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b15_while_exit_1_91
    jmp .L__s3_failure_site_522
.size agent_energy_residual, .-agent_energy_residual

.globl s3_main
.type s3_main, @function
s3_main:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_524
    push rbp
    mov rbp, rsp
    sub rsp, 32
    jmp .L_s3_f4_main_b5_entry
.L_s3_f4_main_b5_entry:
    mov rdi, 0
    mov rax, rdi
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.size s3_main, .-s3_main

.section .text
.L__s3_failure_site_0:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_0]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_0]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_1:
    lea rsi, [rip + .L__s3_failure_prefix_1]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_2:
    lea rsi, [rip + .L__s3_failure_prefix_2]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_3:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_3]
    mov edx, 102
    lea rcx, [rip + .L__s3_failure_suffix_3]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_4:
    lea rsi, [rip + .L__s3_failure_prefix_4]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_5:
    lea rsi, [rip + .L__s3_failure_prefix_5]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_6:
    lea rsi, [rip + .L__s3_failure_prefix_6]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_7:
    lea rsi, [rip + .L__s3_failure_prefix_7]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_8:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_8]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_8]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_9:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_9]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_9]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_10:
    lea rsi, [rip + .L__s3_failure_prefix_10]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_11:
    lea rsi, [rip + .L__s3_failure_prefix_11]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_12:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_12]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_12]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_13:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_13]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_13]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_14:
    lea rsi, [rip + .L__s3_failure_prefix_14]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_15:
    lea rsi, [rip + .L__s3_failure_prefix_15]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_16:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_16]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_16]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_17:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_17]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_17]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_18:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_18]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_18]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_19:
    lea rsi, [rip + .L__s3_failure_prefix_19]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_20:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_20]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_20]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_21:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_21]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_21]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_22:
    lea rsi, [rip + .L__s3_failure_prefix_22]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_23:
    lea rsi, [rip + .L__s3_failure_prefix_23]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_24:
    lea rsi, [rip + .L__s3_failure_prefix_24]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_25:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_25]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_25]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_26:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_26]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_26]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_27:
    lea rsi, [rip + .L__s3_failure_prefix_27]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_28:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_28]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_28]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_29:
    lea rsi, [rip + .L__s3_failure_prefix_29]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_30:
    lea rsi, [rip + .L__s3_failure_prefix_30]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_31:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_31]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_31]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_32:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_32]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_32]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_33:
    lea rsi, [rip + .L__s3_failure_prefix_33]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_34:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_34]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_34]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_35:
    lea rsi, [rip + .L__s3_failure_prefix_35]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_36:
    lea rsi, [rip + .L__s3_failure_prefix_36]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_37:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_37]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_37]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_38:
    lea rsi, [rip + .L__s3_failure_prefix_38]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_39:
    lea rsi, [rip + .L__s3_failure_prefix_39]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_40:
    lea rsi, [rip + .L__s3_failure_prefix_40]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_41:
    lea rsi, [rip + .L__s3_failure_prefix_41]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_42:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_42]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_42]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_43:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_43]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_43]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_44:
    lea rsi, [rip + .L__s3_failure_prefix_44]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_45:
    lea rsi, [rip + .L__s3_failure_prefix_45]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_46:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_46]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_46]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_47:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_47]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_47]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_48:
    lea rsi, [rip + .L__s3_failure_prefix_48]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_49:
    lea rsi, [rip + .L__s3_failure_prefix_49]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_50:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_50]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_50]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_51:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_51]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_51]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_52:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_52]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_52]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_53:
    lea rsi, [rip + .L__s3_failure_prefix_53]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_54:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_54]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_54]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_55:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_55]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_55]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_56:
    lea rsi, [rip + .L__s3_failure_prefix_56]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_57:
    lea rsi, [rip + .L__s3_failure_prefix_57]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_58:
    lea rsi, [rip + .L__s3_failure_prefix_58]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_59:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_59]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_59]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_60:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_60]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_60]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_61:
    lea rsi, [rip + .L__s3_failure_prefix_61]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_62:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_62]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_62]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_63:
    lea rsi, [rip + .L__s3_failure_prefix_63]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_64:
    lea rsi, [rip + .L__s3_failure_prefix_64]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_65:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_65]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_65]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_66:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_66]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_66]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_67:
    lea rsi, [rip + .L__s3_failure_prefix_67]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_68:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_68]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_68]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_69:
    lea rsi, [rip + .L__s3_failure_prefix_69]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_70:
    lea rsi, [rip + .L__s3_failure_prefix_70]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_71:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_71]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_71]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_72:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_72]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_72]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_73:
    lea rsi, [rip + .L__s3_failure_prefix_73]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_74:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_74]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_74]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_75:
    lea rsi, [rip + .L__s3_failure_prefix_75]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_76:
    lea rsi, [rip + .L__s3_failure_prefix_76]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_77:
    lea rsi, [rip + .L__s3_failure_prefix_77]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_78:
    lea rsi, [rip + .L__s3_failure_prefix_78]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_79:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_79]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_79]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_80:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_80]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_80]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_81:
    lea rsi, [rip + .L__s3_failure_prefix_81]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_82:
    lea rsi, [rip + .L__s3_failure_prefix_82]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_83:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_83]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_83]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_84:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_84]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_84]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_85:
    lea rsi, [rip + .L__s3_failure_prefix_85]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_86:
    lea rsi, [rip + .L__s3_failure_prefix_86]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_87:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_87]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_87]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_88:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_88]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_88]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_89:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_89]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_89]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_90:
    lea rsi, [rip + .L__s3_failure_prefix_90]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_91:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_91]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_91]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_92:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_92]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_92]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_93:
    lea rsi, [rip + .L__s3_failure_prefix_93]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_94:
    lea rsi, [rip + .L__s3_failure_prefix_94]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_95:
    lea rsi, [rip + .L__s3_failure_prefix_95]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_96:
    lea rsi, [rip + .L__s3_failure_prefix_96]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_97:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_97]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_97]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_98:
    lea rsi, [rip + .L__s3_failure_prefix_98]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_99:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_99]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_99]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_100:
    lea rsi, [rip + .L__s3_failure_prefix_100]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_101:
    lea rsi, [rip + .L__s3_failure_prefix_101]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_102:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_102]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_102]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_103:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_103]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_103]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_104:
    lea rsi, [rip + .L__s3_failure_prefix_104]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_105:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_105]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_105]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_106:
    lea rsi, [rip + .L__s3_failure_prefix_106]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_107:
    lea rsi, [rip + .L__s3_failure_prefix_107]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_108:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_108]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_108]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_109:
    lea rsi, [rip + .L__s3_failure_prefix_109]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_110:
    lea rsi, [rip + .L__s3_failure_prefix_110]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_111:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_111]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_111]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_112:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_112]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_112]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_113:
    lea rsi, [rip + .L__s3_failure_prefix_113]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_114:
    lea rsi, [rip + .L__s3_failure_prefix_114]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_115:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_115]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_115]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_116:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_116]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_116]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_117:
    lea rsi, [rip + .L__s3_failure_prefix_117]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_118:
    lea rsi, [rip + .L__s3_failure_prefix_118]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_119:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_119]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_119]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_120:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_120]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_120]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_121:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_121]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_121]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_122:
    lea rsi, [rip + .L__s3_failure_prefix_122]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_123:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_123]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_123]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_124:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_124]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_124]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_125:
    lea rsi, [rip + .L__s3_failure_prefix_125]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_126:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_126]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_126]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_127:
    lea rsi, [rip + .L__s3_failure_prefix_127]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_128:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_128]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_128]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_129:
    lea rsi, [rip + .L__s3_failure_prefix_129]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_130:
    lea rsi, [rip + .L__s3_failure_prefix_130]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_131:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_131]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_131]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_132:
    lea rsi, [rip + .L__s3_failure_prefix_132]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_133:
    lea rsi, [rip + .L__s3_failure_prefix_133]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_134:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_134]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_134]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_135:
    lea rsi, [rip + .L__s3_failure_prefix_135]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_136:
    lea rsi, [rip + .L__s3_failure_prefix_136]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_137:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_137]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_137]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_138:
    lea rsi, [rip + .L__s3_failure_prefix_138]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_139:
    lea rsi, [rip + .L__s3_failure_prefix_139]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_140:
    lea rsi, [rip + .L__s3_failure_prefix_140]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_141:
    lea rsi, [rip + .L__s3_failure_prefix_141]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_142:
    lea rsi, [rip + .L__s3_failure_prefix_142]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_143:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_143]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_143]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_144:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_144]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_144]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_145:
    lea rsi, [rip + .L__s3_failure_prefix_145]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_146:
    lea rsi, [rip + .L__s3_failure_prefix_146]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_147:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_147]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_147]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_148:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_148]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_148]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_149:
    lea rsi, [rip + .L__s3_failure_prefix_149]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_150:
    lea rsi, [rip + .L__s3_failure_prefix_150]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_151:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_151]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_151]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_152:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_152]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_152]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_153:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_153]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_153]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_154:
    lea rsi, [rip + .L__s3_failure_prefix_154]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_155:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_155]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_155]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_156:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_156]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_156]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_157:
    lea rsi, [rip + .L__s3_failure_prefix_157]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_158:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_158]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_158]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_159:
    lea rsi, [rip + .L__s3_failure_prefix_159]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_160:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_160]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_160]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_161:
    lea rsi, [rip + .L__s3_failure_prefix_161]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_162:
    lea rsi, [rip + .L__s3_failure_prefix_162]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_163:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_163]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_163]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_164:
    lea rsi, [rip + .L__s3_failure_prefix_164]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_165:
    lea rsi, [rip + .L__s3_failure_prefix_165]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_166:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_166]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_166]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_167:
    lea rsi, [rip + .L__s3_failure_prefix_167]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_168:
    lea rsi, [rip + .L__s3_failure_prefix_168]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_169:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_169]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_169]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_170:
    lea rsi, [rip + .L__s3_failure_prefix_170]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_171:
    lea rsi, [rip + .L__s3_failure_prefix_171]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_172:
    lea rsi, [rip + .L__s3_failure_prefix_172]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_173:
    lea rsi, [rip + .L__s3_failure_prefix_173]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_174:
    lea rsi, [rip + .L__s3_failure_prefix_174]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_175:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_175]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_175]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_176:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_176]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_176]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_177:
    lea rsi, [rip + .L__s3_failure_prefix_177]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_178:
    lea rsi, [rip + .L__s3_failure_prefix_178]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_179:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_179]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_179]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_180:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_180]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_180]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_181:
    lea rsi, [rip + .L__s3_failure_prefix_181]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_182:
    lea rsi, [rip + .L__s3_failure_prefix_182]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_183:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_183]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_183]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_184:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_184]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_184]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_185:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_185]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_185]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_186:
    lea rsi, [rip + .L__s3_failure_prefix_186]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_187:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_187]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_187]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_188:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_188]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_188]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_189:
    lea rsi, [rip + .L__s3_failure_prefix_189]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_190:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_190]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_190]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_191:
    lea rsi, [rip + .L__s3_failure_prefix_191]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_192:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_192]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_192]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_193:
    lea rsi, [rip + .L__s3_failure_prefix_193]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_194:
    lea rsi, [rip + .L__s3_failure_prefix_194]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_195:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_195]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_195]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_196:
    lea rsi, [rip + .L__s3_failure_prefix_196]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_197:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_197]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_197]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_198:
    lea rsi, [rip + .L__s3_failure_prefix_198]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_199:
    lea rsi, [rip + .L__s3_failure_prefix_199]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_200:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_200]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_200]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_201:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_201]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_201]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_202:
    lea rsi, [rip + .L__s3_failure_prefix_202]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_203:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_203]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_203]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_204:
    lea rsi, [rip + .L__s3_failure_prefix_204]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_205:
    lea rsi, [rip + .L__s3_failure_prefix_205]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_206:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_206]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_206]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_207:
    lea rsi, [rip + .L__s3_failure_prefix_207]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_208:
    lea rsi, [rip + .L__s3_failure_prefix_208]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_209:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_209]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_209]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_210:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_210]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_210]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_211:
    lea rsi, [rip + .L__s3_failure_prefix_211]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_212:
    lea rsi, [rip + .L__s3_failure_prefix_212]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_213:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_213]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_213]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_214:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_214]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_214]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_215:
    lea rsi, [rip + .L__s3_failure_prefix_215]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_216:
    lea rsi, [rip + .L__s3_failure_prefix_216]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_217:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_217]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_217]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_218:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_218]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_218]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_219:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_219]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_219]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_220:
    lea rsi, [rip + .L__s3_failure_prefix_220]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_221:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_221]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_221]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_222:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_222]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_222]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_223:
    lea rsi, [rip + .L__s3_failure_prefix_223]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_224:
    lea rsi, [rip + .L__s3_failure_prefix_224]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_225:
    lea rsi, [rip + .L__s3_failure_prefix_225]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_226:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_226]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_226]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_227:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_227]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_227]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_228:
    lea rsi, [rip + .L__s3_failure_prefix_228]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_229:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_229]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_229]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_230:
    lea rsi, [rip + .L__s3_failure_prefix_230]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_231:
    lea rsi, [rip + .L__s3_failure_prefix_231]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_232:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_232]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_232]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_233:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_233]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_233]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_234:
    lea rsi, [rip + .L__s3_failure_prefix_234]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_235:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_235]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_235]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_236:
    lea rsi, [rip + .L__s3_failure_prefix_236]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_237:
    lea rsi, [rip + .L__s3_failure_prefix_237]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_238:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_238]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_238]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_239:
    lea rsi, [rip + .L__s3_failure_prefix_239]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_240:
    lea rsi, [rip + .L__s3_failure_prefix_240]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_241:
    lea rsi, [rip + .L__s3_failure_prefix_241]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_242:
    lea rsi, [rip + .L__s3_failure_prefix_242]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_243:
    lea rsi, [rip + .L__s3_failure_prefix_243]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_244:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_244]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_244]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_245:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_245]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_245]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_246:
    lea rsi, [rip + .L__s3_failure_prefix_246]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_247:
    lea rsi, [rip + .L__s3_failure_prefix_247]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_248:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_248]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_248]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_249:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_249]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_249]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_250:
    lea rsi, [rip + .L__s3_failure_prefix_250]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_251:
    lea rsi, [rip + .L__s3_failure_prefix_251]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_252:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_252]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_252]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_253:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_253]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_253]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_254:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_254]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_254]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_255:
    lea rsi, [rip + .L__s3_failure_prefix_255]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_256:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_256]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_256]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_257:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_257]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_257]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_258:
    lea rsi, [rip + .L__s3_failure_prefix_258]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_259:
    lea rsi, [rip + .L__s3_failure_prefix_259]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_260:
    lea rsi, [rip + .L__s3_failure_prefix_260]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_261:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_261]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_261]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_262:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_262]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_262]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_263:
    lea rsi, [rip + .L__s3_failure_prefix_263]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_264:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_264]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_264]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_265:
    lea rsi, [rip + .L__s3_failure_prefix_265]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_266:
    lea rsi, [rip + .L__s3_failure_prefix_266]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_267:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_267]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_267]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_268:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_268]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_268]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_269:
    lea rsi, [rip + .L__s3_failure_prefix_269]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_270:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_270]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_270]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_271:
    lea rsi, [rip + .L__s3_failure_prefix_271]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_272:
    lea rsi, [rip + .L__s3_failure_prefix_272]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_273:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_273]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_273]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_274:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_274]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_274]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_275:
    lea rsi, [rip + .L__s3_failure_prefix_275]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_276:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_276]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_276]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_277:
    lea rsi, [rip + .L__s3_failure_prefix_277]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_278:
    lea rsi, [rip + .L__s3_failure_prefix_278]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_279:
    lea rsi, [rip + .L__s3_failure_prefix_279]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_280:
    lea rsi, [rip + .L__s3_failure_prefix_280]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_281:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_281]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_281]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_282:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_282]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_282]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_283:
    lea rsi, [rip + .L__s3_failure_prefix_283]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_284:
    lea rsi, [rip + .L__s3_failure_prefix_284]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_285:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_285]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_285]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_286:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_286]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_286]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_287:
    lea rsi, [rip + .L__s3_failure_prefix_287]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_288:
    lea rsi, [rip + .L__s3_failure_prefix_288]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_289:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_289]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_289]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_290:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_290]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_290]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_291:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_291]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_291]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_292:
    lea rsi, [rip + .L__s3_failure_prefix_292]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_293:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_293]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_293]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_294:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_294]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_294]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_295:
    lea rsi, [rip + .L__s3_failure_prefix_295]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_296:
    lea rsi, [rip + .L__s3_failure_prefix_296]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_297:
    lea rsi, [rip + .L__s3_failure_prefix_297]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_298:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_298]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_298]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_299:
    lea rsi, [rip + .L__s3_failure_prefix_299]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_300:
    lea rsi, [rip + .L__s3_failure_prefix_300]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_301:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_301]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_301]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_302:
    lea rsi, [rip + .L__s3_failure_prefix_302]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_303:
    lea rsi, [rip + .L__s3_failure_prefix_303]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_304:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_304]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_304]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_305:
    lea rsi, [rip + .L__s3_failure_prefix_305]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_306:
    lea rsi, [rip + .L__s3_failure_prefix_306]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_307:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_307]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_307]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_308:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_308]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_308]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_309:
    lea rsi, [rip + .L__s3_failure_prefix_309]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_310:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_310]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_310]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_311:
    lea rsi, [rip + .L__s3_failure_prefix_311]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_312:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_312]
    mov edx, 131
    lea rcx, [rip + .L__s3_failure_suffix_312]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_313:
    lea rsi, [rip + .L__s3_failure_prefix_313]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_314:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_314]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_314]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_315:
    lea rsi, [rip + .L__s3_failure_prefix_315]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_316:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_316]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_316]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_317:
    lea rsi, [rip + .L__s3_failure_prefix_317]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_318:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_318]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_318]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_319:
    lea rsi, [rip + .L__s3_failure_prefix_319]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_320:
    lea rsi, [rip + .L__s3_failure_prefix_320]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_321:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_321]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_321]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_322:
    lea rsi, [rip + .L__s3_failure_prefix_322]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_323:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_323]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_323]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_324:
    mov rdi, r12
    lea rsi, [rip + .L__s3_failure_prefix_324]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_324]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_325:
    lea rsi, [rip + .L__s3_failure_prefix_325]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_326:
    lea rsi, [rip + .L__s3_failure_prefix_326]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_327:
    lea rsi, [rip + .L__s3_failure_prefix_327]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_328:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_328]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_328]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_329:
    lea rsi, [rip + .L__s3_failure_prefix_329]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_330:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_330]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_330]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_331:
    mov rdi, r13
    lea rsi, [rip + .L__s3_failure_prefix_331]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_331]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_332:
    lea rsi, [rip + .L__s3_failure_prefix_332]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_333:
    lea rsi, [rip + .L__s3_failure_prefix_333]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_334:
    lea rsi, [rip + .L__s3_failure_prefix_334]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_335:
    lea rsi, [rip + .L__s3_failure_prefix_335]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_336:
    lea rsi, [rip + .L__s3_failure_prefix_336]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_337:
    lea rsi, [rip + .L__s3_failure_prefix_337]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_338:
    lea rsi, [rip + .L__s3_failure_prefix_338]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_339:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_339]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_339]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_340:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_340]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_340]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_341:
    lea rsi, [rip + .L__s3_failure_prefix_341]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_342:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_342]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_342]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_343:
    lea rsi, [rip + .L__s3_failure_prefix_343]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_344:
    lea rsi, [rip + .L__s3_failure_prefix_344]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_345:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_345]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_345]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_346:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_346]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_346]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_347:
    lea rsi, [rip + .L__s3_failure_prefix_347]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_348:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_348]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_348]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_349:
    lea rsi, [rip + .L__s3_failure_prefix_349]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_350:
    lea rsi, [rip + .L__s3_failure_prefix_350]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_351:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_351]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_351]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_352:
    lea rsi, [rip + .L__s3_failure_prefix_352]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_353:
    lea rsi, [rip + .L__s3_failure_prefix_353]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_354:
    lea rsi, [rip + .L__s3_failure_prefix_354]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_355:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_355]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_355]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_356:
    lea rsi, [rip + .L__s3_failure_prefix_356]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_357:
    lea rsi, [rip + .L__s3_failure_prefix_357]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_358:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_358]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_358]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_359:
    lea rsi, [rip + .L__s3_failure_prefix_359]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_360:
    lea rsi, [rip + .L__s3_failure_prefix_360]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_361:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_361]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_361]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_362:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_362]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_362]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_363:
    lea rsi, [rip + .L__s3_failure_prefix_363]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_364:
    lea rsi, [rip + .L__s3_failure_prefix_364]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_365:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_365]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_365]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_366:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_366]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_366]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_367:
    lea rsi, [rip + .L__s3_failure_prefix_367]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_368:
    lea rsi, [rip + .L__s3_failure_prefix_368]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_369:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_369]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_369]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_370:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_370]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_370]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_371:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_371]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_371]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_372:
    lea rsi, [rip + .L__s3_failure_prefix_372]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_373:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_373]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_373]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_374:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_374]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_374]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_375:
    lea rsi, [rip + .L__s3_failure_prefix_375]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_376:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_376]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_376]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_377:
    lea rsi, [rip + .L__s3_failure_prefix_377]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_378:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_378]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_378]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_379:
    lea rsi, [rip + .L__s3_failure_prefix_379]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_380:
    lea rsi, [rip + .L__s3_failure_prefix_380]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_381:
    lea rsi, [rip + .L__s3_failure_prefix_381]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_382:
    lea rsi, [rip + .L__s3_failure_prefix_382]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_383:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_383]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_383]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_384:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_384]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_384]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_385:
    lea rsi, [rip + .L__s3_failure_prefix_385]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_386:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_386]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_386]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_387:
    lea rsi, [rip + .L__s3_failure_prefix_387]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_388:
    lea rsi, [rip + .L__s3_failure_prefix_388]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_389:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_389]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_389]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_390:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_390]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_390]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_391:
    lea rsi, [rip + .L__s3_failure_prefix_391]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_392:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_392]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_392]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_393:
    lea rsi, [rip + .L__s3_failure_prefix_393]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_394:
    lea rsi, [rip + .L__s3_failure_prefix_394]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_395:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_395]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_395]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_396:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_396]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_396]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_397:
    lea rsi, [rip + .L__s3_failure_prefix_397]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_398:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_398]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_398]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_399:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_399]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_399]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_400:
    lea rsi, [rip + .L__s3_failure_prefix_400]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_401:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_401]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_401]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_402:
    lea rsi, [rip + .L__s3_failure_prefix_402]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_403:
    lea rsi, [rip + .L__s3_failure_prefix_403]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_404:
    lea rsi, [rip + .L__s3_failure_prefix_404]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_405:
    lea rsi, [rip + .L__s3_failure_prefix_405]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_406:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_406]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_406]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_407:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_407]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_407]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_408:
    lea rsi, [rip + .L__s3_failure_prefix_408]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_409:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_409]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_409]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_410:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_410]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_410]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_411:
    lea rsi, [rip + .L__s3_failure_prefix_411]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_412:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_412]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_412]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_413:
    lea rsi, [rip + .L__s3_failure_prefix_413]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_414:
    lea rsi, [rip + .L__s3_failure_prefix_414]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_415:
    lea rsi, [rip + .L__s3_failure_prefix_415]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_416:
    lea rsi, [rip + .L__s3_failure_prefix_416]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_417:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_417]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_417]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_418:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_418]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_418]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_419:
    lea rsi, [rip + .L__s3_failure_prefix_419]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_420:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_420]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_420]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_421:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_421]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_421]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_422:
    lea rsi, [rip + .L__s3_failure_prefix_422]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_423:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_423]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_423]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_424:
    lea rsi, [rip + .L__s3_failure_prefix_424]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_425:
    lea rsi, [rip + .L__s3_failure_prefix_425]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_426:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_426]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_426]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_427:
    lea rsi, [rip + .L__s3_failure_prefix_427]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_428:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_428]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_428]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_429:
    lea rsi, [rip + .L__s3_failure_prefix_429]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_430:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_430]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_430]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_431:
    lea rsi, [rip + .L__s3_failure_prefix_431]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_432:
    lea rsi, [rip + .L__s3_failure_prefix_432]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_433:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_433]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_433]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_434:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_434]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_434]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_435:
    lea rsi, [rip + .L__s3_failure_prefix_435]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_436:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_436]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_436]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_437:
    lea rsi, [rip + .L__s3_failure_prefix_437]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_438:
    lea rsi, [rip + .L__s3_failure_prefix_438]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_439:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_439]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_439]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_440:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_440]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_440]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_441:
    lea rsi, [rip + .L__s3_failure_prefix_441]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_442:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_442]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_442]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_443:
    lea rsi, [rip + .L__s3_failure_prefix_443]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_444:
    lea rsi, [rip + .L__s3_failure_prefix_444]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_445:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_445]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_445]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_446:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_446]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_446]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_447:
    lea rsi, [rip + .L__s3_failure_prefix_447]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_448:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_448]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_448]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_449:
    lea rsi, [rip + .L__s3_failure_prefix_449]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_450:
    lea rsi, [rip + .L__s3_failure_prefix_450]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_451:
    lea rsi, [rip + .L__s3_failure_prefix_451]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_452:
    lea rsi, [rip + .L__s3_failure_prefix_452]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_453:
    lea rsi, [rip + .L__s3_failure_prefix_453]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_454:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_454]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_454]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_455:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_455]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_455]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_456:
    lea rsi, [rip + .L__s3_failure_prefix_456]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_457:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_457]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_457]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_458:
    lea rsi, [rip + .L__s3_failure_prefix_458]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_459:
    lea rsi, [rip + .L__s3_failure_prefix_459]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_460:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_460]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_460]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_461:
    lea rsi, [rip + .L__s3_failure_prefix_461]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_462:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_462]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_462]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_463:
    lea rsi, [rip + .L__s3_failure_prefix_463]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_464:
    lea rsi, [rip + .L__s3_failure_prefix_464]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_465:
    lea rsi, [rip + .L__s3_failure_prefix_465]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_466:
    lea rsi, [rip + .L__s3_failure_prefix_466]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_467:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_467]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_467]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_468:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_468]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_468]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_469:
    lea rsi, [rip + .L__s3_failure_prefix_469]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_470:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_470]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_470]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_471:
    lea rsi, [rip + .L__s3_failure_prefix_471]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_472:
    lea rsi, [rip + .L__s3_failure_prefix_472]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_473:
    lea rsi, [rip + .L__s3_failure_prefix_473]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_474:
    lea rsi, [rip + .L__s3_failure_prefix_474]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_475:
    lea rsi, [rip + .L__s3_failure_prefix_475]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_476:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_476]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_476]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_477:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_477]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_477]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_478:
    lea rsi, [rip + .L__s3_failure_prefix_478]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_479:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_479]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_479]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_480:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_480]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_480]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_481:
    lea rsi, [rip + .L__s3_failure_prefix_481]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_482:
    lea rsi, [rip + .L__s3_failure_prefix_482]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_483:
    lea rsi, [rip + .L__s3_failure_prefix_483]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_484:
    lea rsi, [rip + .L__s3_failure_prefix_484]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_485:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_485]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_485]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_486:
    lea rsi, [rip + .L__s3_failure_prefix_486]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_487:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_487]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_487]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_488:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_488]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_488]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_489:
    lea rsi, [rip + .L__s3_failure_prefix_489]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_490:
    lea rsi, [rip + .L__s3_failure_prefix_490]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_491:
    lea rsi, [rip + .L__s3_failure_prefix_491]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_492:
    lea rsi, [rip + .L__s3_failure_prefix_492]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_493:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_493]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_493]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_494:
    lea rsi, [rip + .L__s3_failure_prefix_494]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_495:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_495]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_495]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_496:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_496]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_496]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_497:
    lea rsi, [rip + .L__s3_failure_prefix_497]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_498:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_498]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_498]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_499:
    lea rsi, [rip + .L__s3_failure_prefix_499]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_500:
    lea rsi, [rip + .L__s3_failure_prefix_500]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_501:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_501]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_501]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_502:
    lea rsi, [rip + .L__s3_failure_prefix_502]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_503:
    lea rsi, [rip + .L__s3_failure_prefix_503]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_504:
    lea rsi, [rip + .L__s3_failure_prefix_504]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_505:
    lea rsi, [rip + .L__s3_failure_prefix_505]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_506:
    lea rsi, [rip + .L__s3_failure_prefix_506]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_507:
    lea rsi, [rip + .L__s3_failure_prefix_507]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_508:
    lea rsi, [rip + .L__s3_failure_prefix_508]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_509:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_509]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_509]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_510:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_510]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_510]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_511:
    lea rsi, [rip + .L__s3_failure_prefix_511]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_512:
    lea rsi, [rip + .L__s3_failure_prefix_512]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_513:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_513]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_513]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_514:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_514]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_514]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_515:
    lea rsi, [rip + .L__s3_failure_prefix_515]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_516:
    lea rsi, [rip + .L__s3_failure_prefix_516]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_517:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_517]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_517]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_518:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_518]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_518]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_519:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_519]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_519]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_520:
    lea rsi, [rip + .L__s3_failure_prefix_520]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_521:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_521]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_521]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_522:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_522]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_522]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_523:
    lea rsi, [rip + .L__s3_failure_prefix_523]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_524:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_524]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_524]
    mov r8d, 20
    jmp __s3_fail_value

.section .rodata
.L__s3_failure_prefix_0:
    .ascii "runtime error [frame limit] in function 'agent_energy_residual'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_0:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_1:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 4:5 (block entry, TSTORE): register r8 is uninitialized\n"
.L__s3_failure_prefix_2:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 4:5 (block entry, TSTORE): register r7 is uninitialized\n"
.L__s3_failure_prefix_3:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 4:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_3:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_4:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block entry, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_5:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block entry, TCMP): register r9 is uninitialized\n"
.L__s3_failure_prefix_6:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): register r11 is uninitialized\n"
.L__s3_failure_prefix_7:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): register r12 is uninitialized\n"
.L__s3_failure_prefix_8:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): index "
.L__s3_failure_suffix_8:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_9:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): trit result "
.L__s3_failure_suffix_9:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_10:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): register r13 is uninitialized\n"
.L__s3_failure_prefix_11:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): register r14 is uninitialized\n"
.L__s3_failure_prefix_12:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): index "
.L__s3_failure_suffix_12:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_13:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): trit result "
.L__s3_failure_suffix_13:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_14:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): register r15 is uninitialized\n"
.L__s3_failure_prefix_15:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): register r16 is uninitialized\n"
.L__s3_failure_prefix_16:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): index "
.L__s3_failure_suffix_16:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_17:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): trit result "
.L__s3_failure_suffix_17:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_18:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TLOAD): index "
.L__s3_failure_suffix_18:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_19:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TLOAD): register r17 is uninitialized\n"
.L__s3_failure_prefix_20:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TLOAD): index "
.L__s3_failure_suffix_20:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_21:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 5:5 (block rel_cont_3, TBR3): value "
.L__s3_failure_suffix_21:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_22:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:5 (block rel_cont_3, TBR3): register r18 is uninitialized\n"
.L__s3_failure_prefix_23:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TSTORE): register r20 is uninitialized\n"
.L__s3_failure_prefix_24:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TSTORE): register r19 is uninitialized\n"
.L__s3_failure_prefix_25:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TSTORE): index "
.L__s3_failure_suffix_25:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_26:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TLOAD): index "
.L__s3_failure_suffix_26:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_27:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TLOAD): register r21 is uninitialized\n"
.L__s3_failure_prefix_28:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TLOAD): index "
.L__s3_failure_suffix_28:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_29:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TSTORE): register r23 is uninitialized\n"
.L__s3_failure_prefix_30:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TSTORE): register r22 is uninitialized\n"
.L__s3_failure_prefix_31:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TSTORE): index "
.L__s3_failure_suffix_31:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_32:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TLOAD): index "
.L__s3_failure_suffix_32:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_33:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TLOAD): register r24 is uninitialized\n"
.L__s3_failure_prefix_34:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TLOAD): index "
.L__s3_failure_suffix_34:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_35:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TSTORE): register r26 is uninitialized\n"
.L__s3_failure_prefix_36:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TSTORE): register r25 is uninitialized\n"
.L__s3_failure_prefix_37:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TSTORE): index "
.L__s3_failure_suffix_37:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_38:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block switch_continue_7, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_39:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block switch_continue_7, TCMP): register r27 is uninitialized\n"
.L__s3_failure_prefix_40:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): register r29 is uninitialized\n"
.L__s3_failure_prefix_41:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): register r30 is uninitialized\n"
.L__s3_failure_prefix_42:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): index "
.L__s3_failure_suffix_42:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_43:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): trit result "
.L__s3_failure_suffix_43:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_44:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): register r31 is uninitialized\n"
.L__s3_failure_prefix_45:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): register r32 is uninitialized\n"
.L__s3_failure_prefix_46:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): index "
.L__s3_failure_suffix_46:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_47:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): trit result "
.L__s3_failure_suffix_47:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_48:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): register r33 is uninitialized\n"
.L__s3_failure_prefix_49:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): register r34 is uninitialized\n"
.L__s3_failure_prefix_50:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): index "
.L__s3_failure_suffix_50:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_51:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): trit result "
.L__s3_failure_suffix_51:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_52:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TLOAD): index "
.L__s3_failure_suffix_52:
    .ascii " is uninitialized in m2\n"
.L__s3_failure_prefix_53:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TLOAD): register r35 is uninitialized\n"
.L__s3_failure_prefix_54:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TLOAD): index "
.L__s3_failure_suffix_54:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_55:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 12:5 (block rel_cont_11, TBR3): value "
.L__s3_failure_suffix_55:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_56:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:5 (block rel_cont_11, TBR3): register r36 is uninitialized\n"
.L__s3_failure_prefix_57:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TSTORE): register r38 is uninitialized\n"
.L__s3_failure_prefix_58:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TSTORE): register r37 is uninitialized\n"
.L__s3_failure_prefix_59:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TSTORE): index "
.L__s3_failure_suffix_59:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_60:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_60:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_61:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TLOAD): register r39 is uninitialized\n"
.L__s3_failure_prefix_62:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_62:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_63:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TSTORE): register r41 is uninitialized\n"
.L__s3_failure_prefix_64:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TSTORE): register r40 is uninitialized\n"
.L__s3_failure_prefix_65:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TSTORE): index "
.L__s3_failure_suffix_65:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_66:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TLOAD): index "
.L__s3_failure_suffix_66:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_67:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TLOAD): register r42 is uninitialized\n"
.L__s3_failure_prefix_68:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TLOAD): index "
.L__s3_failure_suffix_68:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_69:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TSTORE): register r44 is uninitialized\n"
.L__s3_failure_prefix_70:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TSTORE): register r43 is uninitialized\n"
.L__s3_failure_prefix_71:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TSTORE): index "
.L__s3_failure_suffix_71:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_72:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TLOAD): index "
.L__s3_failure_suffix_72:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_73:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TLOAD): register r45 is uninitialized\n"
.L__s3_failure_prefix_74:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TLOAD): index "
.L__s3_failure_suffix_74:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_75:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block switch_continue_15, TCMP): register r46 is uninitialized\n"
.L__s3_failure_prefix_76:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block switch_continue_15, TCMP): register r47 is uninitialized\n"
.L__s3_failure_prefix_77:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): register r49 is uninitialized\n"
.L__s3_failure_prefix_78:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): register r50 is uninitialized\n"
.L__s3_failure_prefix_79:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): index "
.L__s3_failure_suffix_79:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_80:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): trit result "
.L__s3_failure_suffix_80:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_81:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): register r51 is uninitialized\n"
.L__s3_failure_prefix_82:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): register r52 is uninitialized\n"
.L__s3_failure_prefix_83:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): index "
.L__s3_failure_suffix_83:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_84:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): trit result "
.L__s3_failure_suffix_84:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_85:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): register r53 is uninitialized\n"
.L__s3_failure_prefix_86:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): register r54 is uninitialized\n"
.L__s3_failure_prefix_87:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): index "
.L__s3_failure_suffix_87:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_88:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): trit result "
.L__s3_failure_suffix_88:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_89:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TLOAD): index "
.L__s3_failure_suffix_89:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_90:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TLOAD): register r55 is uninitialized\n"
.L__s3_failure_prefix_91:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TLOAD): index "
.L__s3_failure_suffix_91:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_92:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 20:5 (block rel_cont_19, TBR3): value "
.L__s3_failure_suffix_92:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_93:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:5 (block rel_cont_19, TBR3): register r56 is uninitialized\n"
.L__s3_failure_prefix_94:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:19 (block switch_negative_20, TSLEN): register r1 is uninitialized\n"
.L__s3_failure_prefix_95:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block switch_negative_20, TCMP): register r57 is uninitialized\n"
.L__s3_failure_prefix_96:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block switch_negative_20, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_97:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TLOAD): index "
.L__s3_failure_suffix_97:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_98:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TLOAD): register r91 is uninitialized\n"
.L__s3_failure_prefix_99:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TLOAD): index "
.L__s3_failure_suffix_99:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_100:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TSTORE): register r93 is uninitialized\n"
.L__s3_failure_prefix_101:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TSTORE): register r92 is uninitialized\n"
.L__s3_failure_prefix_102:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TSTORE): index "
.L__s3_failure_suffix_102:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_103:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TLOAD): index "
.L__s3_failure_suffix_103:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_104:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TLOAD): register r94 is uninitialized\n"
.L__s3_failure_prefix_105:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TLOAD): index "
.L__s3_failure_suffix_105:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_106:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TSTORE): register r96 is uninitialized\n"
.L__s3_failure_prefix_107:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TSTORE): register r95 is uninitialized\n"
.L__s3_failure_prefix_108:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TSTORE): index "
.L__s3_failure_suffix_108:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_109:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): register r59 is uninitialized\n"
.L__s3_failure_prefix_110:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): register r60 is uninitialized\n"
.L__s3_failure_prefix_111:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): index "
.L__s3_failure_suffix_111:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_112:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): trit result "
.L__s3_failure_suffix_112:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_113:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): register r61 is uninitialized\n"
.L__s3_failure_prefix_114:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): register r62 is uninitialized\n"
.L__s3_failure_prefix_115:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): index "
.L__s3_failure_suffix_115:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_116:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): trit result "
.L__s3_failure_suffix_116:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_117:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): register r63 is uninitialized\n"
.L__s3_failure_prefix_118:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): register r64 is uninitialized\n"
.L__s3_failure_prefix_119:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): index "
.L__s3_failure_suffix_119:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_120:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): trit result "
.L__s3_failure_suffix_120:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_121:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TLOAD): index "
.L__s3_failure_suffix_121:
    .ascii " is uninitialized in m4\n"
.L__s3_failure_prefix_122:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TLOAD): register r65 is uninitialized\n"
.L__s3_failure_prefix_123:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TLOAD): index "
.L__s3_failure_suffix_123:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_124:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 22:13 (block rel_cont_26, TBR3): value "
.L__s3_failure_suffix_124:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_125:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:13 (block rel_cont_26, TBR3): register r66 is uninitialized\n"
.L__s3_failure_prefix_126:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TLOAD): index "
.L__s3_failure_suffix_126:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_127:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TLOAD): register r67 is uninitialized\n"
.L__s3_failure_prefix_128:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TLOAD): index "
.L__s3_failure_suffix_128:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_129:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TSTORE): register r69 is uninitialized\n"
.L__s3_failure_prefix_130:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TSTORE): register r68 is uninitialized\n"
.L__s3_failure_prefix_131:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TSTORE): index "
.L__s3_failure_suffix_131:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_132:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TSTORE): register r71 is uninitialized\n"
.L__s3_failure_prefix_133:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TSTORE): register r70 is uninitialized\n"
.L__s3_failure_prefix_134:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TSTORE): index "
.L__s3_failure_suffix_134:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_135:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TSTORE): register r73 is uninitialized\n"
.L__s3_failure_prefix_136:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TSTORE): register r72 is uninitialized\n"
.L__s3_failure_prefix_137:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TSTORE): index "
.L__s3_failure_suffix_137:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_138:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:19 (block switch_continue_30, TSLEN): register r3 is uninitialized\n"
.L__s3_failure_prefix_139:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block switch_continue_30, TCMP): register r74 is uninitialized\n"
.L__s3_failure_prefix_140:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block switch_continue_30, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_141:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): register r76 is uninitialized\n"
.L__s3_failure_prefix_142:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): register r77 is uninitialized\n"
.L__s3_failure_prefix_143:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): index "
.L__s3_failure_suffix_143:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_144:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): trit result "
.L__s3_failure_suffix_144:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_145:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): register r78 is uninitialized\n"
.L__s3_failure_prefix_146:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): register r79 is uninitialized\n"
.L__s3_failure_prefix_147:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): index "
.L__s3_failure_suffix_147:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_148:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): trit result "
.L__s3_failure_suffix_148:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_149:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): register r80 is uninitialized\n"
.L__s3_failure_prefix_150:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): register r81 is uninitialized\n"
.L__s3_failure_prefix_151:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): index "
.L__s3_failure_suffix_151:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_152:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): trit result "
.L__s3_failure_suffix_152:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_153:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TLOAD): index "
.L__s3_failure_suffix_153:
    .ascii " is uninitialized in m5\n"
.L__s3_failure_prefix_154:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TLOAD): register r82 is uninitialized\n"
.L__s3_failure_prefix_155:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TLOAD): index "
.L__s3_failure_suffix_155:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_156:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 29:13 (block rel_cont_34, TBR3): value "
.L__s3_failure_suffix_156:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_157:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:13 (block rel_cont_34, TBR3): register r83 is uninitialized\n"
.L__s3_failure_prefix_158:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TLOAD): index "
.L__s3_failure_suffix_158:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_159:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TLOAD): register r84 is uninitialized\n"
.L__s3_failure_prefix_160:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TLOAD): index "
.L__s3_failure_suffix_160:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_161:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TSTORE): register r86 is uninitialized\n"
.L__s3_failure_prefix_162:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TSTORE): register r85 is uninitialized\n"
.L__s3_failure_prefix_163:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TSTORE): index "
.L__s3_failure_suffix_163:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_164:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TSTORE): register r88 is uninitialized\n"
.L__s3_failure_prefix_165:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TSTORE): register r87 is uninitialized\n"
.L__s3_failure_prefix_166:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TSTORE): index "
.L__s3_failure_suffix_166:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_167:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TSTORE): register r90 is uninitialized\n"
.L__s3_failure_prefix_168:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TSTORE): register r89 is uninitialized\n"
.L__s3_failure_prefix_169:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TSTORE): index "
.L__s3_failure_suffix_169:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_170:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:11 (block switch_continue_39, TSLEN): register r6 is uninitialized\n"
.L__s3_failure_prefix_171:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block switch_continue_39, TCMP): register r97 is uninitialized\n"
.L__s3_failure_prefix_172:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block switch_continue_39, TCMP): register r98 is uninitialized\n"
.L__s3_failure_prefix_173:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): register r100 is uninitialized\n"
.L__s3_failure_prefix_174:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): register r101 is uninitialized\n"
.L__s3_failure_prefix_175:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): index "
.L__s3_failure_suffix_175:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_176:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): trit result "
.L__s3_failure_suffix_176:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_177:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): register r102 is uninitialized\n"
.L__s3_failure_prefix_178:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): register r103 is uninitialized\n"
.L__s3_failure_prefix_179:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): index "
.L__s3_failure_suffix_179:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_180:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): trit result "
.L__s3_failure_suffix_180:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_181:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): register r104 is uninitialized\n"
.L__s3_failure_prefix_182:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): register r105 is uninitialized\n"
.L__s3_failure_prefix_183:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): index "
.L__s3_failure_suffix_183:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_184:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): trit result "
.L__s3_failure_suffix_184:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_185:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TLOAD): index "
.L__s3_failure_suffix_185:
    .ascii " is uninitialized in m6\n"
.L__s3_failure_prefix_186:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TLOAD): register r106 is uninitialized\n"
.L__s3_failure_prefix_187:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TLOAD): index "
.L__s3_failure_suffix_187:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_188:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 41:5 (block rel_cont_43, TBR3): value "
.L__s3_failure_suffix_188:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_189:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:5 (block rel_cont_43, TBR3): register r107 is uninitialized\n"
.L__s3_failure_prefix_190:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TLOAD): index "
.L__s3_failure_suffix_190:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_191:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TLOAD): register r108 is uninitialized\n"
.L__s3_failure_prefix_192:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TLOAD): index "
.L__s3_failure_suffix_192:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_193:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block switch_negative_44, TCMP): register r109 is uninitialized\n"
.L__s3_failure_prefix_194:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block switch_negative_44, TCMP): register r110 is uninitialized\n"
.L__s3_failure_prefix_195:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TLOAD): index "
.L__s3_failure_suffix_195:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_196:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TLOAD): register r128 is uninitialized\n"
.L__s3_failure_prefix_197:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TLOAD): index "
.L__s3_failure_suffix_197:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_198:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TSTORE): register r130 is uninitialized\n"
.L__s3_failure_prefix_199:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TSTORE): register r129 is uninitialized\n"
.L__s3_failure_prefix_200:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TSTORE): index "
.L__s3_failure_suffix_200:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_201:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TLOAD): index "
.L__s3_failure_suffix_201:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_202:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TLOAD): register r131 is uninitialized\n"
.L__s3_failure_prefix_203:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TLOAD): index "
.L__s3_failure_suffix_203:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_204:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TSTORE): register r133 is uninitialized\n"
.L__s3_failure_prefix_205:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TSTORE): register r132 is uninitialized\n"
.L__s3_failure_prefix_206:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TSTORE): index "
.L__s3_failure_suffix_206:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_207:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): register r112 is uninitialized\n"
.L__s3_failure_prefix_208:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): register r113 is uninitialized\n"
.L__s3_failure_prefix_209:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): index "
.L__s3_failure_suffix_209:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_210:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): trit result "
.L__s3_failure_suffix_210:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_211:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): register r114 is uninitialized\n"
.L__s3_failure_prefix_212:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): register r115 is uninitialized\n"
.L__s3_failure_prefix_213:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): index "
.L__s3_failure_suffix_213:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_214:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): trit result "
.L__s3_failure_suffix_214:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_215:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): register r116 is uninitialized\n"
.L__s3_failure_prefix_216:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): register r117 is uninitialized\n"
.L__s3_failure_prefix_217:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): index "
.L__s3_failure_suffix_217:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_218:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): trit result "
.L__s3_failure_suffix_218:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_219:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TLOAD): index "
.L__s3_failure_suffix_219:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_220:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TLOAD): register r118 is uninitialized\n"
.L__s3_failure_prefix_221:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TLOAD): index "
.L__s3_failure_suffix_221:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_222:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 43:13 (block rel_cont_50, TBR3): value "
.L__s3_failure_suffix_222:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_223:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:13 (block rel_cont_50, TBR3): register r119 is uninitialized\n"
.L__s3_failure_prefix_224:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TSTORE): register r121 is uninitialized\n"
.L__s3_failure_prefix_225:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TSTORE): register r120 is uninitialized\n"
.L__s3_failure_prefix_226:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TSTORE): index "
.L__s3_failure_suffix_226:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_227:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TLOAD): index "
.L__s3_failure_suffix_227:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_228:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TLOAD): register r122 is uninitialized\n"
.L__s3_failure_prefix_229:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TLOAD): index "
.L__s3_failure_suffix_229:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_230:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TSTORE): register r124 is uninitialized\n"
.L__s3_failure_prefix_231:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TSTORE): register r123 is uninitialized\n"
.L__s3_failure_prefix_232:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TSTORE): index "
.L__s3_failure_suffix_232:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_233:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TLOAD): index "
.L__s3_failure_suffix_233:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_234:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TLOAD): register r125 is uninitialized\n"
.L__s3_failure_prefix_235:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TLOAD): index "
.L__s3_failure_suffix_235:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_236:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TSTORE): register r127 is uninitialized\n"
.L__s3_failure_prefix_237:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TSTORE): register r126 is uninitialized\n"
.L__s3_failure_prefix_238:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TSTORE): index "
.L__s3_failure_suffix_238:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_239:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:11 (block switch_continue_55, TSLEN): register r6 is uninitialized\n"
.L__s3_failure_prefix_240:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block switch_continue_55, TCMP): register r134 is uninitialized\n"
.L__s3_failure_prefix_241:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block switch_continue_55, TCMP): register r135 is uninitialized\n"
.L__s3_failure_prefix_242:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): register r137 is uninitialized\n"
.L__s3_failure_prefix_243:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): register r138 is uninitialized\n"
.L__s3_failure_prefix_244:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): index "
.L__s3_failure_suffix_244:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_245:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): trit result "
.L__s3_failure_suffix_245:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_246:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): register r139 is uninitialized\n"
.L__s3_failure_prefix_247:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): register r140 is uninitialized\n"
.L__s3_failure_prefix_248:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): index "
.L__s3_failure_suffix_248:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_249:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): trit result "
.L__s3_failure_suffix_249:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_250:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): register r141 is uninitialized\n"
.L__s3_failure_prefix_251:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): register r142 is uninitialized\n"
.L__s3_failure_prefix_252:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): index "
.L__s3_failure_suffix_252:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_253:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): trit result "
.L__s3_failure_suffix_253:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_254:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TLOAD): index "
.L__s3_failure_suffix_254:
    .ascii " is uninitialized in m8\n"
.L__s3_failure_prefix_255:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TLOAD): register r143 is uninitialized\n"
.L__s3_failure_prefix_256:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TLOAD): index "
.L__s3_failure_suffix_256:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_257:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 54:5 (block rel_cont_59, TBR3): value "
.L__s3_failure_suffix_257:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_258:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:5 (block rel_cont_59, TBR3): register r144 is uninitialized\n"
.L__s3_failure_prefix_259:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TSTORE): register r146 is uninitialized\n"
.L__s3_failure_prefix_260:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TSTORE): register r145 is uninitialized\n"
.L__s3_failure_prefix_261:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TSTORE): index "
.L__s3_failure_suffix_261:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_262:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TLOAD): index "
.L__s3_failure_suffix_262:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_263:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TLOAD): register r147 is uninitialized\n"
.L__s3_failure_prefix_264:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TLOAD): index "
.L__s3_failure_suffix_264:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_265:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TSTORE): register r149 is uninitialized\n"
.L__s3_failure_prefix_266:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TSTORE): register r148 is uninitialized\n"
.L__s3_failure_prefix_267:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TSTORE): index "
.L__s3_failure_suffix_267:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_268:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TLOAD): index "
.L__s3_failure_suffix_268:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_269:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TLOAD): register r150 is uninitialized\n"
.L__s3_failure_prefix_270:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TLOAD): index "
.L__s3_failure_suffix_270:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_271:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TSTORE): register r152 is uninitialized\n"
.L__s3_failure_prefix_272:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TSTORE): register r151 is uninitialized\n"
.L__s3_failure_prefix_273:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TSTORE): index "
.L__s3_failure_suffix_273:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_274:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TLOAD): index "
.L__s3_failure_suffix_274:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_275:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TLOAD): register r153 is uninitialized\n"
.L__s3_failure_prefix_276:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TLOAD): index "
.L__s3_failure_suffix_276:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_277:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block switch_continue_63, TCMP): register r154 is uninitialized\n"
.L__s3_failure_prefix_278:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block switch_continue_63, TCMP): register r155 is uninitialized\n"
.L__s3_failure_prefix_279:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): register r157 is uninitialized\n"
.L__s3_failure_prefix_280:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): register r158 is uninitialized\n"
.L__s3_failure_prefix_281:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): index "
.L__s3_failure_suffix_281:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_282:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): trit result "
.L__s3_failure_suffix_282:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_283:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): register r159 is uninitialized\n"
.L__s3_failure_prefix_284:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): register r160 is uninitialized\n"
.L__s3_failure_prefix_285:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): index "
.L__s3_failure_suffix_285:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_286:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): trit result "
.L__s3_failure_suffix_286:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_287:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): register r161 is uninitialized\n"
.L__s3_failure_prefix_288:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): register r162 is uninitialized\n"
.L__s3_failure_prefix_289:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): index "
.L__s3_failure_suffix_289:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_290:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): trit result "
.L__s3_failure_suffix_290:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_291:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TLOAD): index "
.L__s3_failure_suffix_291:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_292:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TLOAD): register r163 is uninitialized\n"
.L__s3_failure_prefix_293:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TLOAD): index "
.L__s3_failure_suffix_293:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_294:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 62:5 (block rel_cont_67, TBR3): value "
.L__s3_failure_suffix_294:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_295:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:5 (block rel_cont_67, TBR3): register r164 is uninitialized\n"
.L__s3_failure_prefix_296:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TSTORE): register r166 is uninitialized\n"
.L__s3_failure_prefix_297:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TSTORE): register r165 is uninitialized\n"
.L__s3_failure_prefix_298:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_298:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_299:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TSTORE): register r168 is uninitialized\n"
.L__s3_failure_prefix_300:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TSTORE): register r167 is uninitialized\n"
.L__s3_failure_prefix_301:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_301:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_302:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TSTORE): register r170 is uninitialized\n"
.L__s3_failure_prefix_303:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TSTORE): register r169 is uninitialized\n"
.L__s3_failure_prefix_304:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_304:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_305:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TSTORE): register r172 is uninitialized\n"
.L__s3_failure_prefix_306:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TSTORE): register r171 is uninitialized\n"
.L__s3_failure_prefix_307:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_307:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_308:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TLOAD): index "
.L__s3_failure_suffix_308:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_309:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TLOAD): register r279 is uninitialized\n"
.L__s3_failure_prefix_310:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TLOAD): index "
.L__s3_failure_suffix_310:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_311:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 101:13 (block switch_neutral_69, TRET): register r280 is uninitialized\n"
.L__s3_failure_prefix_312:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TLOAD): index "
.L__s3_failure_suffix_312:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_313:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TLOAD): register r281 is uninitialized\n"
.L__s3_failure_prefix_314:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TLOAD): index "
.L__s3_failure_suffix_314:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_315:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 103:13 (block switch_positive_70, TRET): register r282 is uninitialized\n"
.L__s3_failure_prefix_316:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TLOAD): index "
.L__s3_failure_suffix_316:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_317:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TLOAD): register r173 is uninitialized\n"
.L__s3_failure_prefix_318:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TLOAD): index "
.L__s3_failure_suffix_318:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_319:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block while_condition_71, TCMP): register r174 is uninitialized\n"
.L__s3_failure_prefix_320:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block while_condition_71, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_321:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_321:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_322:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TLOAD): register r184 is uninitialized\n"
.L__s3_failure_prefix_323:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_323:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_324:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): slice index "
.L__s3_failure_suffix_324:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_325:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_326:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_327:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): register r185 is uninitialized\n"
.L__s3_failure_prefix_328:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_328:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_329:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TLOAD): register r187 is uninitialized\n"
.L__s3_failure_prefix_330:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_330:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_331:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): slice index "
.L__s3_failure_suffix_331:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_332:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_333:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_334:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): register r188 is uninitialized\n"
.L__s3_failure_prefix_335:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:53 (block while_body_72, TNDIFF): register r186 is uninitialized\n"
.L__s3_failure_prefix_336:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:53 (block while_body_72, TNDIFF): register r189 is uninitialized\n"
.L__s3_failure_prefix_337:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TSTORE): register r191 is uninitialized\n"
.L__s3_failure_prefix_338:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TSTORE): register r190 is uninitialized\n"
.L__s3_failure_prefix_339:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TSTORE): index "
.L__s3_failure_suffix_339:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_340:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_340:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_341:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TLOAD): register r192 is uninitialized\n"
.L__s3_failure_prefix_342:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_342:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_343:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TSTORE): register r194 is uninitialized\n"
.L__s3_failure_prefix_344:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TSTORE): register r193 is uninitialized\n"
.L__s3_failure_prefix_345:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TSTORE): index "
.L__s3_failure_suffix_345:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_346:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_346:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_347:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TLOAD): register r195 is uninitialized\n"
.L__s3_failure_prefix_348:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_348:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_349:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:34 (block while_body_72, TREL): register r196 is uninitialized\n"
.L__s3_failure_prefix_350:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:34 (block while_body_72, TREL): register r197 is uninitialized\n"
.L__s3_failure_prefix_351:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 71:17 (block while_body_72, TBR3): value "
.L__s3_failure_suffix_351:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_352:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:17 (block while_body_72, TBR3): register r198 is uninitialized\n"
.L__s3_failure_prefix_353:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TSTORE): register r242 is uninitialized\n"
.L__s3_failure_prefix_354:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TSTORE): register r241 is uninitialized\n"
.L__s3_failure_prefix_355:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TSTORE): index "
.L__s3_failure_suffix_355:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_356:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TSTORE): register r244 is uninitialized\n"
.L__s3_failure_prefix_357:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TSTORE): register r243 is uninitialized\n"
.L__s3_failure_prefix_358:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TSTORE): index "
.L__s3_failure_suffix_358:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_359:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): register r176 is uninitialized\n"
.L__s3_failure_prefix_360:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): register r177 is uninitialized\n"
.L__s3_failure_prefix_361:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): index "
.L__s3_failure_suffix_361:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_362:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): trit result "
.L__s3_failure_suffix_362:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_363:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): register r178 is uninitialized\n"
.L__s3_failure_prefix_364:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): register r179 is uninitialized\n"
.L__s3_failure_prefix_365:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): index "
.L__s3_failure_suffix_365:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_366:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): trit result "
.L__s3_failure_suffix_366:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_367:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): register r180 is uninitialized\n"
.L__s3_failure_prefix_368:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): register r181 is uninitialized\n"
.L__s3_failure_prefix_369:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): index "
.L__s3_failure_suffix_369:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_370:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): trit result "
.L__s3_failure_suffix_370:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_371:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TLOAD): index "
.L__s3_failure_suffix_371:
    .ascii " is uninitialized in m14\n"
.L__s3_failure_prefix_372:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TLOAD): register r182 is uninitialized\n"
.L__s3_failure_prefix_373:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TLOAD): index "
.L__s3_failure_suffix_373:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_374:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 68:13 (block rel_cont_79, TBR3): value "
.L__s3_failure_suffix_374:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_375:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:13 (block rel_cont_79, TBR3): register r183 is uninitialized\n"
.L__s3_failure_prefix_376:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TLOAD): index "
.L__s3_failure_suffix_376:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_377:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TLOAD): register r200 is uninitialized\n"
.L__s3_failure_prefix_378:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TLOAD): index "
.L__s3_failure_suffix_378:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_379:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:41 (block switch_negative_80, TNDIFF): register r199 is uninitialized\n"
.L__s3_failure_prefix_380:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:41 (block switch_negative_80, TNDIFF): register r201 is uninitialized\n"
.L__s3_failure_prefix_381:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TSTORE): register r203 is uninitialized\n"
.L__s3_failure_prefix_382:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TSTORE): register r202 is uninitialized\n"
.L__s3_failure_prefix_383:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TSTORE): index "
.L__s3_failure_suffix_383:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_384:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TLOAD): index "
.L__s3_failure_suffix_384:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_385:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TLOAD): register r204 is uninitialized\n"
.L__s3_failure_prefix_386:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TLOAD): index "
.L__s3_failure_suffix_386:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_387:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TSTORE): register r206 is uninitialized\n"
.L__s3_failure_prefix_388:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TSTORE): register r205 is uninitialized\n"
.L__s3_failure_prefix_389:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TSTORE): index "
.L__s3_failure_suffix_389:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_390:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TLOAD): index "
.L__s3_failure_suffix_390:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_391:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TLOAD): register r207 is uninitialized\n"
.L__s3_failure_prefix_392:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TLOAD): index "
.L__s3_failure_suffix_392:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_393:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TSTORE): register r209 is uninitialized\n"
.L__s3_failure_prefix_394:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TSTORE): register r208 is uninitialized\n"
.L__s3_failure_prefix_395:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TSTORE): index "
.L__s3_failure_suffix_395:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_396:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_396:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_397:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TLOAD): register r210 is uninitialized\n"
.L__s3_failure_prefix_398:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_398:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_399:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_399:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_400:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TLOAD): register r212 is uninitialized\n"
.L__s3_failure_prefix_401:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_401:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_402:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:41 (block switch_continue_83, TADD): register r211 is uninitialized\n"
.L__s3_failure_prefix_403:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:41 (block switch_continue_83, TADD): register r213 is uninitialized\n"
.L__s3_failure_prefix_404:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TSTORE): register r215 is uninitialized\n"
.L__s3_failure_prefix_405:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TSTORE): register r214 is uninitialized\n"
.L__s3_failure_prefix_406:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TSTORE): index "
.L__s3_failure_suffix_406:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_407:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_407:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_408:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TLOAD): register r216 is uninitialized\n"
.L__s3_failure_prefix_409:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_409:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_410:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_410:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_411:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TLOAD): register r218 is uninitialized\n"
.L__s3_failure_prefix_412:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_412:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_413:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:45 (block switch_continue_83, TADD): register r217 is uninitialized\n"
.L__s3_failure_prefix_414:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:45 (block switch_continue_83, TADD): register r219 is uninitialized\n"
.L__s3_failure_prefix_415:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TSTORE): register r221 is uninitialized\n"
.L__s3_failure_prefix_416:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TSTORE): register r220 is uninitialized\n"
.L__s3_failure_prefix_417:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TSTORE): index "
.L__s3_failure_suffix_417:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_418:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_418:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_419:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TLOAD): register r222 is uninitialized\n"
.L__s3_failure_prefix_420:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_420:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_421:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_421:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_422:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TLOAD): register r224 is uninitialized\n"
.L__s3_failure_prefix_423:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_423:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_424:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:33 (block switch_continue_83, TREL): register r223 is uninitialized\n"
.L__s3_failure_prefix_425:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:33 (block switch_continue_83, TREL): register r225 is uninitialized\n"
.L__s3_failure_prefix_426:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 81:17 (block switch_continue_83, TBR3): value "
.L__s3_failure_suffix_426:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_427:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:17 (block switch_continue_83, TBR3): register r226 is uninitialized\n"
.L__s3_failure_prefix_428:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TLOAD): index "
.L__s3_failure_suffix_428:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_429:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TLOAD): register r227 is uninitialized\n"
.L__s3_failure_prefix_430:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TLOAD): index "
.L__s3_failure_suffix_430:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_431:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TSTORE): register r229 is uninitialized\n"
.L__s3_failure_prefix_432:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TSTORE): register r228 is uninitialized\n"
.L__s3_failure_prefix_433:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TSTORE): index "
.L__s3_failure_suffix_433:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_434:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TLOAD): index "
.L__s3_failure_suffix_434:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_435:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TLOAD): register r230 is uninitialized\n"
.L__s3_failure_prefix_436:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TLOAD): index "
.L__s3_failure_suffix_436:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_437:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TSTORE): register r232 is uninitialized\n"
.L__s3_failure_prefix_438:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TSTORE): register r231 is uninitialized\n"
.L__s3_failure_prefix_439:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TSTORE): index "
.L__s3_failure_suffix_439:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_440:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TLOAD): index "
.L__s3_failure_suffix_440:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_441:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TLOAD): register r233 is uninitialized\n"
.L__s3_failure_prefix_442:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TLOAD): index "
.L__s3_failure_suffix_442:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_443:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TSTORE): register r235 is uninitialized\n"
.L__s3_failure_prefix_444:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TSTORE): register r234 is uninitialized\n"
.L__s3_failure_prefix_445:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TSTORE): index "
.L__s3_failure_suffix_445:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_446:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TLOAD): index "
.L__s3_failure_suffix_446:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_447:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TLOAD): register r236 is uninitialized\n"
.L__s3_failure_prefix_448:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TLOAD): index "
.L__s3_failure_suffix_448:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_449:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 88:31 (block switch_continue_87, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_450:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:31 (block switch_continue_87, TADD): register r237 is uninitialized\n"
.L__s3_failure_prefix_451:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:31 (block switch_continue_87, TADD): register r238 is uninitialized\n"
.L__s3_failure_prefix_452:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TSTORE): register r240 is uninitialized\n"
.L__s3_failure_prefix_453:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TSTORE): register r239 is uninitialized\n"
.L__s3_failure_prefix_454:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TSTORE): index "
.L__s3_failure_suffix_454:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_455:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TLOAD): index "
.L__s3_failure_suffix_455:
    .ascii " is uninitialized in m18\n"
.L__s3_failure_prefix_456:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TLOAD): register r245 is uninitialized\n"
.L__s3_failure_prefix_457:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TLOAD): index "
.L__s3_failure_suffix_457:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_458:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block while_condition_88, TCMP): register r246 is uninitialized\n"
.L__s3_failure_prefix_459:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block while_condition_88, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_460:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_460:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_461:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TLOAD): register r256 is uninitialized\n"
.L__s3_failure_prefix_462:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_462:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_463:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:35 (block while_body_89, TADD): register r257 is uninitialized\n"
.L__s3_failure_prefix_464:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:35 (block while_body_89, TADD): register r258 is uninitialized\n"
.L__s3_failure_prefix_465:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TSTORE): register r260 is uninitialized\n"
.L__s3_failure_prefix_466:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TSTORE): register r259 is uninitialized\n"
.L__s3_failure_prefix_467:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TSTORE): index "
.L__s3_failure_suffix_467:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_468:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_468:
    .ascii " is uninitialized in m18\n"
.L__s3_failure_prefix_469:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TLOAD): register r261 is uninitialized\n"
.L__s3_failure_prefix_470:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_470:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_471:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 94:47 (block while_body_89, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_472:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:47 (block while_body_89, TADD): register r262 is uninitialized\n"
.L__s3_failure_prefix_473:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:47 (block while_body_89, TADD): register r263 is uninitialized\n"
.L__s3_failure_prefix_474:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TSTORE): register r265 is uninitialized\n"
.L__s3_failure_prefix_475:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TSTORE): register r264 is uninitialized\n"
.L__s3_failure_prefix_476:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TSTORE): index "
.L__s3_failure_suffix_476:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_477:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_477:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_478:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TLOAD): register r267 is uninitialized\n"
.L__s3_failure_prefix_479:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_479:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_480:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): slice index "
.L__s3_failure_suffix_480:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_481:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_482:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_483:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r266 is uninitialized\n"
.L__s3_failure_prefix_484:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r268 is uninitialized\n"
.L__s3_failure_prefix_485:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_485:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_486:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TLOAD): register r270 is uninitialized\n"
.L__s3_failure_prefix_487:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_487:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_488:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): slice index "
.L__s3_failure_suffix_488:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_489:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_490:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_491:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r269 is uninitialized\n"
.L__s3_failure_prefix_492:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r271 is uninitialized\n"
.L__s3_failure_prefix_493:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_493:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_494:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TLOAD): register r273 is uninitialized\n"
.L__s3_failure_prefix_495:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_495:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_496:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_496:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_497:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TLOAD): register r275 is uninitialized\n"
.L__s3_failure_prefix_498:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_498:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_499:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:38 (block while_exit_92, TDIV): register r274 is uninitialized\n"
.L__s3_failure_prefix_500:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:38 (block while_exit_92, TDIV): register r276 is uninitialized\n"
.L__s3_failure_prefix_501:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): slice index "
.L__s3_failure_suffix_501:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_502:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_503:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_504:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r272 is uninitialized\n"
.L__s3_failure_prefix_505:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r277 is uninitialized\n"
.L__s3_failure_prefix_506:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 99:13 (block while_exit_92, TRET): register r278 is uninitialized\n"
.L__s3_failure_prefix_507:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): register r248 is uninitialized\n"
.L__s3_failure_prefix_508:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): register r249 is uninitialized\n"
.L__s3_failure_prefix_509:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): index "
.L__s3_failure_suffix_509:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_510:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): trit result "
.L__s3_failure_suffix_510:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_511:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): register r250 is uninitialized\n"
.L__s3_failure_prefix_512:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): register r251 is uninitialized\n"
.L__s3_failure_prefix_513:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): index "
.L__s3_failure_suffix_513:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_514:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): trit result "
.L__s3_failure_suffix_514:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_515:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): register r252 is uninitialized\n"
.L__s3_failure_prefix_516:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): register r253 is uninitialized\n"
.L__s3_failure_prefix_517:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): index "
.L__s3_failure_suffix_517:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_518:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): trit result "
.L__s3_failure_suffix_518:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_519:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TLOAD): index "
.L__s3_failure_suffix_519:
    .ascii " is uninitialized in m19\n"
.L__s3_failure_prefix_520:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TLOAD): register r254 is uninitialized\n"
.L__s3_failure_prefix_521:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TLOAD): index "
.L__s3_failure_suffix_521:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_522:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 92:13 (block rel_cont_96, TBR3): value "
.L__s3_failure_suffix_522:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_523:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:13 (block rel_cont_96, TBR3): register r255 is uninitialized\n"
.L__s3_failure_prefix_524:
    .ascii "runtime error [frame limit] in function 'main'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_524:
    .ascii " exceeds limit 1024\n"

.section .text

.type __s3_print_i64, @function
__s3_print_i64:
    push rbp
    mov rbp, rsp
    sub rsp, 64
    lea rsi, [rbp - 1]
    mov byte ptr [rsi], 10
    mov r8, 1
    mov rax, rdi
    test rax, rax
    jne .L__s3_print_nonzero
    dec rsi
    mov byte ptr [rsi], 48
    inc r8
    jmp .L__s3_print_write
.L__s3_print_nonzero:
    xor r9d, r9d
    test rax, rax
    jns .L__s3_print_digits
    mov r9d, 1
    neg rax
.L__s3_print_digits:
    xor edx, edx
    mov r10, 10
    div r10
    add dl, 48
    dec rsi
    mov byte ptr [rsi], dl
    inc r8
    test rax, rax
    jne .L__s3_print_digits
    test r9d, r9d
    je .L__s3_print_write
    dec rsi
    mov byte ptr [rsi], 45
    inc r8
.L__s3_print_write:
    mov eax, 1
    mov edi, 1
    mov rdx, r8
    syscall
    leave
    ret
.size __s3_print_i64, .-__s3_print_i64

.type __s3_tryte_min, @function
__s3_tryte_min:
    xor r11d, r11d
    jmp .L__s3_tryte_extreme
.size __s3_tryte_min, .-__s3_tryte_min

.type __s3_tryte_max, @function
__s3_tryte_max:
    mov r11d, 1
.L__s3_tryte_extreme:
    push r12
    push r13
    push r14
    push r15
    mov r12, rdi
    mov r13, rsi
    xor r14d, r14d
    mov r15, 1
    mov ecx, 6
    mov r10, 3
.L__s3_tryte_digit_loop:
    mov rax, r12
    cqo
    idiv r10
    cmp rdx, 2
    jne .L__s3_tryte_left_negative_two
    mov rdx, -1
    inc rax
    jmp .L__s3_tryte_left_ready
.L__s3_tryte_left_negative_two:
    cmp rdx, -2
    jne .L__s3_tryte_left_ready
    mov rdx, 1
    dec rax
.L__s3_tryte_left_ready:
    mov r12, rax
    mov r8, rdx
    mov rax, r13
    cqo
    idiv r10
    cmp rdx, 2
    jne .L__s3_tryte_right_negative_two
    mov rdx, -1
    inc rax
    jmp .L__s3_tryte_right_ready
.L__s3_tryte_right_negative_two:
    cmp rdx, -2
    jne .L__s3_tryte_right_ready
    mov rdx, 1
    dec rax
.L__s3_tryte_right_ready:
    mov r13, rax
    mov r9, rdx
    test r11d, r11d
    jne .L__s3_tryte_select_max
    cmp r8, r9
    cmovg r8, r9
    jmp .L__s3_tryte_selected
.L__s3_tryte_select_max:
    cmp r8, r9
    cmovl r8, r9
.L__s3_tryte_selected:
    imul r8, r15
    add r14, r8
    imul r15, r15, 3
    dec ecx
    jne .L__s3_tryte_digit_loop
    mov rax, r14
    pop r15
    pop r14
    pop r13
    pop r12
    ret
.size __s3_tryte_max, .-__s3_tryte_max

.type __s3_dyn_copy,@function
__s3_dyn_copy:
    test rcx,rcx
    jz .L__s3_dyn_copy_done
.L__s3_dyn_copy_loop:
    mov al,byte ptr [rsi]
    mov byte ptr [rdi],al
    inc rsi
    inc rdi
    dec rcx
    jnz .L__s3_dyn_copy_loop
.L__s3_dyn_copy_done:
    ret

.type __s3_dyn_new,@function
__s3_dyn_new:
    push r12
    mov r12,rdi
    test rdi,rdi
    js __s3_fail_capacity
    cmp rdi,67108864
    ja __s3_fail_allocation
    add rdi,24
    jc __s3_fail_capacity
    mov rsi,rdi
    xor edi,edi
    mov eax,9
    mov edx,3
    mov r10d,34
    mov r8,-1
    xor r9d,r9d
    syscall
    test rax,rax
    js __s3_fail_allocation
    lea rdx,[rax+24]
    mov qword ptr [rax],rdx
    mov qword ptr [rax+8],0
    mov qword ptr [rax+16],r12
    pop r12
    ret

.type __s3_builtin_bytes_new,@function
__s3_builtin_bytes_new:
    jmp __s3_dyn_new
.type __s3_builtin_text_new,@function
__s3_builtin_text_new:
    jmp __s3_dyn_new

.type __s3_builtin_sqrt,@function
__s3_builtin_sqrt:
    movq xmm0,rdi
    sqrtsd xmm0,xmm0
    movq rax,xmm0
    ret

.type __s3_builtin_bytes_len,@function
__s3_builtin_bytes_len:
    mov rax,[rdi]
    mov rax,[rax+8]
    ret
.type __s3_builtin_text_len,@function
__s3_builtin_text_len:
    jmp __s3_builtin_bytes_len
.type __s3_builtin_bytes_capacity,@function
__s3_builtin_bytes_capacity:
    mov rax,[rdi]
    mov rax,[rax+16]
    ret
.type __s3_builtin_text_capacity,@function
__s3_builtin_text_capacity:
    jmp __s3_builtin_bytes_capacity

.type __s3_builtin_bytes_get,@function
__s3_builtin_bytes_get:
    mov r10,[rdi]
    cmp rsi,0
    jl __s3_fail_bounds
    cmp rsi,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    movzx eax,byte ptr [r11+rsi]
    ret
.type __s3_builtin_bytes_set,@function
__s3_builtin_bytes_set:
    cmp rdx,0
    jl __s3_fail_capacity
    cmp rdx,255
    jg __s3_fail_capacity
    mov r10,[rdi]
    cmp rsi,0
    jl __s3_fail_bounds
    cmp rsi,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov byte ptr [r11+rsi],dl
    xor eax,eax
    ret
.type __s3_builtin_bytes_push,@function
__s3_builtin_bytes_push:
    cmp rsi,0
    jl __s3_fail_capacity
    cmp rsi,255
    jg __s3_fail_capacity
    mov r10,[rdi]
    mov rax,[r10+8]
    cmp rax,[r10+16]
    jae __s3_fail_capacity
    mov r11,[r10]
    mov byte ptr [r11+rax],sil
    inc rax
    mov [r10+8],rax
    xor eax,eax
    ret

.type __s3_dyn_reserve,@function
__s3_dyn_reserve:
    push r12
    push r13
    push r14
    push r15
    mov r12,rdi
    mov r13,[rdi]
    mov r15,[r13+8]
    cmp rsi,r15
    jb __s3_fail_capacity
    cmp rsi,[r13+16]
    jbe .L__s3_dyn_reserve_done
    mov rdi,rsi
    call __s3_dyn_new
    mov r14,rax
    mov rcx,r15
    mov rsi,[r13]
    mov rdi,[r14]
    call __s3_dyn_copy
    mov [r14+8],r15
    mov [r12],r14
    mov rdi,r13
    mov rsi,[r13+16]
    add rsi,24
    mov eax,11
    syscall
.L__s3_dyn_reserve_done:
    xor eax,eax
    pop r15
    pop r14
    pop r13
    pop r12
    ret
.type __s3_builtin_bytes_reserve,@function
__s3_builtin_bytes_reserve:
    jmp __s3_dyn_reserve
.type __s3_builtin_text_reserve,@function
__s3_builtin_text_reserve:
    jmp __s3_dyn_reserve

.type __s3_dyn_clone_exact_length,@function
__s3_dyn_clone_exact_length:
    push r12
    push r13
    mov r12,[rdi]
    mov rdi,[r12+8]
    call __s3_dyn_new
    mov r13,rax
    mov rcx,[r12+8]
    mov rsi,[r12]
    mov rdi,[r13]
    call __s3_dyn_copy
    mov rax,[r12+8]
    mov [r13+8],rax
    mov rax,r13
    pop r13
    pop r12
    ret
.type __s3_dyn_clone_preserve_capacity,@function
__s3_dyn_clone_preserve_capacity:
    push r12
    push r13
    mov r12,[rdi]
    mov rdi,[r12+16]
    call __s3_dyn_new
    mov r13,rax
    mov rcx,[r12+8]
    mov rsi,[r12]
    mov rdi,[r13]
    call __s3_dyn_copy
    mov rax,[r12+8]
    mov [r13+8],rax
    mov rax,r13
    pop r13
    pop r12
    ret
.type __s3_builtin_bytes_clone,@function
__s3_builtin_bytes_clone:
    jmp __s3_dyn_clone_exact_length
.type __s3_builtin_text_clone,@function
__s3_builtin_text_clone:
    jmp __s3_dyn_clone_exact_length
.type __s3_builtin_bytes_from_text,@function
__s3_builtin_bytes_from_text:
    jmp __s3_dyn_clone_exact_length

.type __s3_dyn_concat,@function
__s3_dyn_concat:
    push r12
    push r13
    push r14
    push r15
    mov r12,[rdi]
    mov r13,[rsi]
    mov r15,[r12+8]
    mov rdi,r15
    add rdi,[r13+8]
    jc __s3_fail_capacity
    call __s3_dyn_new
    mov r14,rax
    mov rcx,r15
    mov rsi,[r12]
    mov rdi,[r14]
    call __s3_dyn_copy
    mov rcx,[r13+8]
    mov rsi,[r13]
    mov rdi,[r14]
    add rdi,r15
    call __s3_dyn_copy
    mov rax,r15
    add rax,[r13+8]
    mov [r14+8],rax
    mov rax,r14
    pop r15
    pop r14
    pop r13
    pop r12
    ret
.type __s3_builtin_bytes_concat,@function
__s3_builtin_bytes_concat:
    jmp __s3_dyn_concat
.type __s3_builtin_text_concat,@function
__s3_builtin_text_concat:
    jmp __s3_dyn_concat

.type __s3_dyn_slice,@function
__s3_dyn_slice:
    push r12
    push r13
    push r14
    push r15
    mov r12,[rdi]
    mov r14,rsi
    mov r15,rdx
    cmp r14,0
    jl __s3_fail_bounds
    cmp r15,r14
    jl __s3_fail_bounds
    cmp r15,[r12+8]
    jg __s3_fail_bounds
    mov rdi,r15
    sub rdi,r14
    call __s3_dyn_new
    mov r13,rax
    mov rcx,r15
    sub rcx,r14
    mov rsi,[r12]
    add rsi,r14
    mov rdi,[r13]
    call __s3_dyn_copy
    mov rax,r15
    sub rax,r14
    mov [r13+8],rax
    mov rax,r13
    pop r15
    pop r14
    pop r13
    pop r12
    ret
.type __s3_builtin_bytes_slice,@function
__s3_builtin_bytes_slice:
    jmp __s3_dyn_slice
.type __s3_dyn_is_boundary,@function
__s3_dyn_is_boundary:
    cmp rsi,0
    je .L__s3_boundary_yes
    cmp rsi,[rdi+8]
    je .L__s3_boundary_yes
    mov rdx,[rdi]
    movzx eax,byte ptr [rdx+rsi]
    and eax,192
    cmp eax,128
    sete al
    movzx eax,al
    xor eax,1
    ret
.L__s3_boundary_yes:
    mov eax,1
    ret
.type __s3_builtin_text_slice,@function
__s3_builtin_text_slice:
    push r12
    push r13
    push r14
    mov r12,rdi
    mov r13,rsi
    mov r14,rdx
    mov r10,[rdi]
    cmp r13,0
    jl __s3_fail_bounds
    cmp r14,r13
    jl __s3_fail_bounds
    cmp r14,[r10+8]
    jg __s3_fail_bounds
    mov rdi,r10
    mov rsi,r13
    call __s3_dyn_is_boundary
    test eax,eax
    jz __s3_fail_boundary
    mov rdi,r10
    mov rsi,r14
    call __s3_dyn_is_boundary
    test eax,eax
    jz __s3_fail_boundary
    mov rdi,r12
    mov rsi,r13
    mov rdx,r14
    pop r14
    pop r13
    pop r12
    jmp __s3_dyn_slice

.type __s3_builtin_text_from_static,@function
__s3_builtin_text_from_static:
    push r12
    push r13
    push r14
    mov r12,rdi
    xor r13d,r13d
.L__s3_dyn_strlen:
    cmp byte ptr [r12+r13],0
    je .L__s3_dyn_strlen_done
    inc r13
    jmp .L__s3_dyn_strlen
.L__s3_dyn_strlen_done:
    mov rdi,r13
    call __s3_dyn_new
    mov r14,rax
    mov rdx,[r14]
    mov rcx,r13
    mov rsi,r12
    mov rdi,rdx
    call __s3_dyn_copy
    mov [r14+8],r13
    mov rax,r14
    pop r14
    pop r13
    pop r12
    ret

.type __s3_builtin_text_append,@function
__s3_builtin_text_append:
    push r12
    push r13
    push r14
    push r15
    mov r12,[rdi]
    mov r13,[rsi]
    mov r14,[r12+8]
    mov r15,[r13+8]
    mov rax,r14
    add rax,r15
    jc __s3_fail_capacity
    cmp rax,[r12+16]
    ja __s3_fail_capacity
    mov rcx,r15
    mov rsi,[r13]
    mov rdi,[r12]
    add rdi,r14
    call __s3_dyn_copy
    add r14,r15
    mov [r12+8],r14
    xor eax,eax
    pop r15
    pop r14
    pop r13
    pop r12
    ret
.type __s3_builtin_text_append_static,@function
__s3_builtin_text_append_static:
    push r12
    push r13
    push r14
    push r15
    mov r12,[rdi]
    mov r13,rsi
    mov r14,[r12+8]
    xor rsi,rsi
.L__s3_dyn_append_strlen:
    cmp byte ptr [r13+rsi],0
    je .L__s3_dyn_append_strlen_done
    inc rsi
    jmp .L__s3_dyn_append_strlen
.L__s3_dyn_append_strlen_done:
    mov rax,r14
    add rax,rsi
    jc __s3_fail_capacity
    cmp rax,[r12+16]
    ja __s3_fail_capacity
    mov r15,rax
    mov rcx,rsi
    mov rsi,r13
    mov rdi,[r12]
    add rdi,r14
    call __s3_dyn_copy
    mov [r12+8],r15
    xor eax,eax
    pop r15
    pop r14
    pop r13
    pop r12
    ret

.type __s3_dyn_utf8_valid,@function
__s3_dyn_utf8_valid:
    mov r10,rdi
    lea r11,[rdi+rsi]
.L__s3_utf8_loop:
    cmp r10,r11
    jae .L__s3_utf8_yes
    movzx eax,byte ptr [r10]
    mov r9d,eax
    cmp eax,128
    jb .L__s3_utf8_one
    cmp eax,194
    jb .L__s3_utf8_no
    cmp eax,223
    jbe .L__s3_utf8_two
    cmp eax,239
    jbe .L__s3_utf8_three
    cmp eax,244
    jbe .L__s3_utf8_four
    jmp .L__s3_utf8_no
.L__s3_utf8_one:
    inc r10
    jmp .L__s3_utf8_loop
.L__s3_utf8_two:
    add r10,2
    cmp r10,r11
    ja .L__s3_utf8_no
    movzx eax,byte ptr [r10-1]
    and eax,192
    cmp eax,128
    jne .L__s3_utf8_no
    jmp .L__s3_utf8_loop
.L__s3_utf8_three:
    add r10,3
    cmp r10,r11
    ja .L__s3_utf8_no
    movzx eax,byte ptr [r10-2]
    mov r8d,eax
    and eax,192
    cmp eax,128
    jne .L__s3_utf8_no
    movzx eax,byte ptr [r10-1]
    and eax,192
    cmp eax,128
    jne .L__s3_utf8_no
    cmp r9d,224
    jne .L__s3_utf8_three_not_e0
    cmp r8d,160
    jb .L__s3_utf8_no
.L__s3_utf8_three_not_e0:
    cmp r9d,237
    jne .L__s3_utf8_three_done
    cmp r8d,159
    ja .L__s3_utf8_no
.L__s3_utf8_three_done:
    jmp .L__s3_utf8_loop
.L__s3_utf8_four:
    add r10,4
    cmp r10,r11
    ja .L__s3_utf8_no
    movzx eax,byte ptr [r10-3]
    mov r8d,eax
    and eax,192
    cmp eax,128
    jne .L__s3_utf8_no
    movzx eax,byte ptr [r10-2]
    and eax,192
    cmp eax,128
    jne .L__s3_utf8_no
    movzx eax,byte ptr [r10-1]
    and eax,192
    cmp eax,128
    jne .L__s3_utf8_no
    cmp r9d,240
    jne .L__s3_utf8_four_not_f0
    cmp r8d,144
    jb .L__s3_utf8_no
.L__s3_utf8_four_not_f0:
    cmp r9d,244
    jne .L__s3_utf8_four_done
    cmp r8d,143
    ja .L__s3_utf8_no
.L__s3_utf8_four_done:
    jmp .L__s3_utf8_loop
.L__s3_utf8_yes:
    mov eax,1
    ret
.L__s3_utf8_no:
    xor eax,eax
    ret
.type __s3_builtin_text_from_bytes,@function
__s3_builtin_text_from_bytes:
    push r12
    push r14
    mov r12,[rdi]
    mov rdi,[r12]
    mov rsi,[r12+8]
    call __s3_dyn_utf8_valid
    test eax,eax
    jz __s3_fail_encoding
    mov rdi,[r12+8]
    call __s3_dyn_new
    mov r14,rax
    mov rcx,[r12+8]
    mov rsi,[r12]
    mov rdx,rcx
    mov rdi,[r14]
    call __s3_dyn_copy
    mov [r14+8],rdx
    mov rax,r14
    pop r14
    pop r12
    ret

.type __s3_builtin_text_find,@function
__s3_builtin_text_find:
    push r12
    push r13
    push r14
    push r15
    mov r12,[rdi]
    mov r13,[r12+8]
    mov r14,[rsi]
    mov r15,[r14+8]
    test r15,r15
    jz .L__s3_find_zero
    cmp r15,r13
    ja .L__s3_find_no
    xor r8d,r8d
.L__s3_find_outer:
    mov rax,r13
    sub rax,r15
    cmp r8,rax
    ja .L__s3_find_no
    mov rdi,[r12]
    add rdi,r8
    mov rsi,[r14]
    mov rcx,r15
    repe cmpsb
    je .L__s3_find_yes
    inc r8
    jmp .L__s3_find_outer
.L__s3_find_zero:
    xor eax,eax
    jmp .L__s3_find_done
.L__s3_find_yes:
    mov rax,r8
    jmp .L__s3_find_done
.L__s3_find_no:
    mov rax,-1
.L__s3_find_done:
    pop r15
    pop r14
    pop r13
    pop r12
    ret

.type __s3_vec_new,@function
__s3_vec_new:
    test rdi,rdi
    js __s3_fail_capacity
    imul rdi,rsi
    jo __s3_fail_capacity
    jmp __s3_dyn_new
.type __s3_vec_reserve,@function
__s3_vec_reserve:
    test rsi,rsi
    js __s3_fail_capacity
    imul rsi,rdx
    jo __s3_fail_capacity
    jmp __s3_dyn_reserve

.type __s3_builtin_tryte_vector_new,@function
__s3_builtin_tryte_vector_new:
    mov esi,2
    jmp __s3_vec_new
.type __s3_builtin_i64_vector_new,@function
__s3_builtin_i64_vector_new:
    mov esi,8
    jmp __s3_vec_new
.type __s3_builtin_f64_vector_new,@function
__s3_builtin_f64_vector_new:
    mov esi,8
    jmp __s3_vec_new

.type __s3_vec_len_2,@function
__s3_vec_len_2:
    mov r10,[rdi]
    mov rax,[r10+8]
    sar rax,1
    ret
.type __s3_vec_len_8,@function
__s3_vec_len_8:
    mov r10,[rdi]
    mov rax,[r10+8]
    sar rax,3
    ret
.type __s3_vec_cap_2,@function
__s3_vec_cap_2:
    mov r10,[rdi]
    mov rax,[r10+16]
    sar rax,1
    ret
.type __s3_vec_cap_8,@function
__s3_vec_cap_8:
    mov r10,[rdi]
    mov rax,[r10+16]
    sar rax,3
    ret
.type __s3_builtin_tryte_vector_len,@function
__s3_builtin_tryte_vector_len:
    jmp __s3_vec_len_2
.type __s3_builtin_tryte_vector_capacity,@function
__s3_builtin_tryte_vector_capacity:
    jmp __s3_vec_cap_2
.type __s3_builtin_i64_vector_len,@function
__s3_builtin_i64_vector_len:
    jmp __s3_vec_len_8
.type __s3_builtin_i64_vector_capacity,@function
__s3_builtin_i64_vector_capacity:
    jmp __s3_vec_cap_8
.type __s3_builtin_f64_vector_len,@function
__s3_builtin_f64_vector_len:
    jmp __s3_vec_len_8
.type __s3_builtin_f64_vector_capacity,@function
__s3_builtin_f64_vector_capacity:
    jmp __s3_vec_cap_8

.type __s3_builtin_tryte_vector_reserve,@function
__s3_builtin_tryte_vector_reserve:
    mov edx,2
    jmp __s3_vec_reserve
.type __s3_builtin_i64_vector_reserve,@function
__s3_builtin_i64_vector_reserve:
    mov edx,8
    jmp __s3_vec_reserve
.type __s3_builtin_f64_vector_reserve,@function
__s3_builtin_f64_vector_reserve:
    mov edx,8
    jmp __s3_vec_reserve

.type __s3_vec_push_2,@function
__s3_vec_push_2:
    cmp rsi,-364
    jl __s3_fail_capacity
    cmp rsi,364
    jg __s3_fail_capacity
    mov r10,[rdi]
    mov rax,[r10+8]
    mov r8,rax
    add r8,2
    jc __s3_fail_capacity
    cmp r8,[r10+16]
    ja __s3_fail_capacity
    mov r11,[r10]
    mov word ptr [r11+rax],si
    mov [r10+8],r8
    xor eax,eax
    ret
.type __s3_vec_push_8,@function
__s3_vec_push_8:
    mov r10,[rdi]
    mov rax,[r10+8]
    mov r8,rax
    add r8,8
    jc __s3_fail_capacity
    cmp r8,[r10+16]
    ja __s3_fail_capacity
    mov r11,[r10]
    mov qword ptr [r11+rax],rsi
    mov [r10+8],r8
    xor eax,eax
    ret
.type __s3_builtin_tryte_vector_push,@function
__s3_builtin_tryte_vector_push:
    jmp __s3_vec_push_2
.type __s3_builtin_i64_vector_push,@function
__s3_builtin_i64_vector_push:
    jmp __s3_vec_push_8
.type __s3_builtin_f64_vector_push,@function
__s3_builtin_f64_vector_push:
    jmp __s3_vec_push_8

.type __s3_vec_get_2,@function
__s3_vec_get_2:
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,1
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    movsx eax,word ptr [r11+rax]
    ret
.type __s3_vec_get_8,@function
__s3_vec_get_8:
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,3
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov rax,[r11+rax]
    ret
.type __s3_builtin_tryte_vector_get,@function
__s3_builtin_tryte_vector_get:
    jmp __s3_vec_get_2
.type __s3_builtin_i64_vector_get,@function
__s3_builtin_i64_vector_get:
    jmp __s3_vec_get_8
.type __s3_builtin_f64_vector_get,@function
__s3_builtin_f64_vector_get:
    jmp __s3_vec_get_8

.type __s3_vec_set_2,@function
__s3_vec_set_2:
    cmp rdx,-364
    jl __s3_fail_capacity
    cmp rdx,364
    jg __s3_fail_capacity
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,1
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov word ptr [r11+rax],dx
    xor eax,eax
    ret
.type __s3_vec_set_8,@function
__s3_vec_set_8:
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,3
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov qword ptr [r11+rax],rdx
    xor eax,eax
    ret
.type __s3_builtin_tryte_vector_set,@function
__s3_builtin_tryte_vector_set:
    jmp __s3_vec_set_2
.type __s3_builtin_i64_vector_set,@function
__s3_builtin_i64_vector_set:
    jmp __s3_vec_set_8
.type __s3_builtin_f64_vector_set,@function
__s3_builtin_f64_vector_set:
    jmp __s3_vec_set_8

.type __s3_vec_pop_2,@function
__s3_vec_pop_2:
    mov r10,[rdi]
    mov rax,[r10+8]
    cmp rax,2
    jb __s3_fail_bounds
    sub rax,2
    mov [r10+8],rax
    mov r11,[r10]
    movsx eax,word ptr [r11+rax]
    ret
.type __s3_vec_pop_8,@function
__s3_vec_pop_8:
    mov r10,[rdi]
    mov rax,[r10+8]
    cmp rax,8
    jb __s3_fail_bounds
    sub rax,8
    mov [r10+8],rax
    mov r11,[r10]
    mov rax,[r11+rax]
    ret
.type __s3_builtin_tryte_vector_pop,@function
__s3_builtin_tryte_vector_pop:
    jmp __s3_vec_pop_2
.type __s3_builtin_i64_vector_pop,@function
__s3_builtin_i64_vector_pop:
    jmp __s3_vec_pop_8
.type __s3_builtin_f64_vector_pop,@function
__s3_builtin_f64_vector_pop:
    jmp __s3_vec_pop_8

.type __s3_builtin_tryte_vector_clone,@function
__s3_builtin_tryte_vector_clone:
    jmp __s3_dyn_clone_preserve_capacity
.type __s3_builtin_i64_vector_clone,@function
__s3_builtin_i64_vector_clone:
    jmp __s3_dyn_clone_preserve_capacity
.type __s3_builtin_f64_vector_clone,@function
__s3_builtin_f64_vector_clone:
    jmp __s3_dyn_clone_preserve_capacity

.type __s3_vec_slice_2,@function
__s3_vec_slice_2:
    shl rsi,1
    jo __s3_fail_bounds
    shl rdx,1
    jo __s3_fail_bounds
    jmp __s3_dyn_slice
.type __s3_vec_slice_8,@function
__s3_vec_slice_8:
    shl rsi,3
    jo __s3_fail_bounds
    shl rdx,3
    jo __s3_fail_bounds
    jmp __s3_dyn_slice
.type __s3_builtin_tryte_vector_slice,@function
__s3_builtin_tryte_vector_slice:
    jmp __s3_vec_slice_2
.type __s3_builtin_i64_vector_slice,@function
__s3_builtin_i64_vector_slice:
    jmp __s3_vec_slice_8
.type __s3_builtin_f64_vector_slice,@function
__s3_builtin_f64_vector_slice:
    jmp __s3_vec_slice_8

.type __s3_vec_len_stride,@function
__s3_vec_len_stride:
    test rsi,rsi
    jz __s3_fail_invalid_runtime_state
    mov r10,[rdi]
    mov rax,[r10+8]
    xor edx,edx
    div rsi
    ret
.type __s3_vec_capacity_stride,@function
__s3_vec_capacity_stride:
    test rsi,rsi
    jz __s3_fail_invalid_runtime_state
    mov r10,[rdi]
    mov rax,[r10+16]
    xor edx,edx
    div rsi
    ret

.type __s3_dyn_clone_descriptor,@function
__s3_dyn_clone_descriptor:
    test rdi,rdi
    jz __s3_fail_invalid_runtime_state
    push r12
    mov r12,rdi
    mov rdi,[r12+8]
    call __s3_dyn_new
    mov r10,rax
    mov rdx,[r12+8]
    mov rcx,rdx
    mov rsi,[r12]
    mov rdi,[r10]
    call __s3_dyn_copy
    mov [r10+8],rdx
    mov rax,r10
    pop r12
    ret

.type __s3_dyn_drop_descriptor,@function
__s3_dyn_drop_descriptor:
    test rdi,rdi
    jz __s3_fail_invalid_runtime_state
    mov rsi,[rdi+16]
    add rsi,24
    jc __s3_fail_capacity
    mov eax,11
    syscall
    test rax,rax
    js __s3_fail_allocation
    xor eax,eax
    ret

.type __s3_composite_vector_push,@function
__s3_composite_vector_push:
    push rbx
    push r12
    push r13
    push r14
    push r15
    mov r12,rdi
    mov r13,rsi
    mov r14,rdx
    mov r15,rcx
    mov rbx,r8
    mov r10,[r12]
    mov rax,[r10+8]
    mov r11,rax
    add r11,rbx
    jc __s3_fail_capacity
    cmp r11,[r10+16]
    ja __s3_fail_capacity
    xor ecx,ecx
.L__s3_composite_push_validate:
    cmp rcx,r15
    jae .L__s3_composite_push_store
    movzx eax,byte ptr [r14+rcx]
    mov r9,qword ptr [r13+rcx*8]
    cmp eax,0
    je .L__s3_composite_push_validate_ternary
    cmp eax,1
    je .L__s3_composite_push_validate_tryte
    cmp eax,2
    je .L__s3_composite_push_validate_next
    cmp eax,4
    ja .L__s3_composite_push_invalid
    test r9,r9
    jz .L__s3_composite_push_invalid
    jmp .L__s3_composite_push_validate_next
.L__s3_composite_push_validate_ternary:
    cmp r9,-1
    jl .L__s3_composite_push_invalid
    cmp r9,1
    jg .L__s3_composite_push_invalid
    jmp .L__s3_composite_push_validate_next
.L__s3_composite_push_validate_tryte:
    cmp r9,-364
    jl .L__s3_composite_push_invalid
    cmp r9,364
    jg .L__s3_composite_push_invalid
.L__s3_composite_push_validate_next:
    inc rcx
    jmp .L__s3_composite_push_validate
.L__s3_composite_push_invalid:
    jmp __s3_fail_invalid_runtime_state
.L__s3_composite_push_store:
    mov r10,[r12]
    mov rdi,[r10]
    xor ecx,ecx
    mov r8,[r10+8]
.L__s3_composite_push_store_loop:
    cmp rcx,r15
    jae .L__s3_composite_push_done
    movzx eax,byte ptr [r14+rcx]
    mov r9,qword ptr [r13+rcx*8]
    cmp eax,2
    jae .L__s3_composite_push_store_qword
    mov word ptr [rdi+r8],r9w
    add r8,2
    jmp .L__s3_composite_push_store_next
.L__s3_composite_push_store_qword:
    mov qword ptr [rdi+r8],r9
    add r8,8
.L__s3_composite_push_store_next:
    inc rcx
    jmp .L__s3_composite_push_store_loop
.L__s3_composite_push_done:
    mov rax,[r10+8]
    add rax,rbx
    mov [r10+8],rax
    xor eax,eax
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    ret

.type __s3_composite_vector_set,@function
__s3_composite_vector_set:
    push rbx
    push r12
    push r13
    push r14
    push r15
    mov r12,rdi
    mov r13,rdx
    mov r14,rcx
    mov r15,r8
    mov r10,[r12]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    imul rax,r9
    jo __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov rbx,rax
    xor ecx,ecx
.L__s3_composite_set_validate:
    cmp rcx,r15
    jae .L__s3_composite_set_drop
    movzx eax,byte ptr [r14+rcx]
    mov r9,qword ptr [r13+rcx*8]
    cmp eax,0
    je .L__s3_composite_set_validate_ternary
    cmp eax,1
    je .L__s3_composite_set_validate_tryte
    cmp eax,2
    je .L__s3_composite_set_validate_next
    cmp eax,4
    ja .L__s3_composite_set_invalid
    test r9,r9
    jz .L__s3_composite_set_invalid
    jmp .L__s3_composite_set_validate_next
.L__s3_composite_set_validate_ternary:
    cmp r9,-1
    jl .L__s3_composite_set_invalid
    cmp r9,1
    jg .L__s3_composite_set_invalid
    jmp .L__s3_composite_set_validate_next
.L__s3_composite_set_validate_tryte:
    cmp r9,-364
    jl .L__s3_composite_set_invalid
    cmp r9,364
    jg .L__s3_composite_set_invalid
.L__s3_composite_set_validate_next:
    inc rcx
    jmp .L__s3_composite_set_validate
.L__s3_composite_set_invalid:
    jmp __s3_fail_invalid_runtime_state
.L__s3_composite_set_drop:
    xor ecx,ecx
    xor r8d,r8d
.L__s3_composite_set_drop_loop:
    cmp rcx,r15
    jae .L__s3_composite_set_store
    movzx eax,byte ptr [r14+rcx]
    cmp eax,3
    je .L__s3_composite_set_drop_owned
    cmp eax,4
    jne .L__s3_composite_set_drop_next
.L__s3_composite_set_drop_owned:
    mov r10,[r12]
    mov rdi,[r10]
    lea r9,[rdi+rbx]
    mov rdx,[r9+r8]
    test rdx,rdx
    jz __s3_fail_invalid_runtime_state
    push rcx
    sub rsp,8
    mov rdi,rdx
    call __s3_dyn_drop_descriptor
    add rsp,8
    pop rcx
.L__s3_composite_set_drop_next:
    movzx eax,byte ptr [r14+rcx]
    cmp eax,2
    jae .L__s3_composite_set_drop_wide
    add r8,2
    jmp .L__s3_composite_set_drop_advance
.L__s3_composite_set_drop_wide:
    add r8,8
.L__s3_composite_set_drop_advance:
    inc rcx
    jmp .L__s3_composite_set_drop_loop
.L__s3_composite_set_store:
    mov r10,[r12]
    mov rdi,[r10]
    lea r11,[rdi+rbx]
    xor ecx,ecx
    xor r8d,r8d
.L__s3_composite_set_store_loop:
    cmp rcx,r15
    jae .L__s3_composite_set_done
    movzx eax,byte ptr [r14+rcx]
    mov r9,qword ptr [r13+rcx*8]
    cmp eax,2
    jae .L__s3_composite_set_store_qword
    mov word ptr [r11+r8],r9w
    add r8,2
    jmp .L__s3_composite_set_store_next
.L__s3_composite_set_store_qword:
    mov qword ptr [r11+r8],r9
    add r8,8
.L__s3_composite_set_store_next:
    inc rcx
    jmp .L__s3_composite_set_store_loop
.L__s3_composite_set_done:
    xor eax,eax
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    ret

.type __s3_composite_vector_get,@function
__s3_composite_vector_get:
    push rbx
    push r12
    push r13
    push r14
    push r15
    mov r12,rdi
    mov r13,rsi
    mov r14,rcx
    mov r15,r8
    mov rbx,r9
    mov r10,[r13]
    test rdx,rdx
    js __s3_fail_bounds
    mov rax,rdx
    imul rax,rbx
    jo __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,rax
    mov r10,[r10]
    lea r9,[r10+r11]
    xor ecx,ecx
    xor r8d,r8d
.L__s3_composite_get_loop:
    cmp rcx,r15
    jae .L__s3_composite_get_done
    movzx eax,byte ptr [r14+rcx]
    cmp eax,2
    jae .L__s3_composite_get_wide
    movsx rdx,word ptr [r9+r8]
    mov qword ptr [r12+rcx*8],rdx
    add r8,2
    jmp .L__s3_composite_get_next
.L__s3_composite_get_wide:
    mov rdx,qword ptr [r9+r8]
    mov qword ptr [r12+rcx*8],rdx
    add r8,8
.L__s3_composite_get_next:
    inc rcx
    jmp .L__s3_composite_get_loop
.L__s3_composite_get_done:
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    ret

.type __s3_composite_vector_pop,@function
__s3_composite_vector_pop:
    push rbx
    push r12
    push r13
    push r14
    push r15
    mov r12,rdi
    mov r13,rsi
    mov r14,rdx
    mov r15,rcx
    mov rbx,r8
    mov r10,[r13]
    mov rax,[r10+8]
    cmp rax,rbx
    jb __s3_fail_bounds
    sub rax,rbx
    mov [r10+8],rax
    mov r11,rax
    mov r10,[r10]
    lea r9,[r10+r11]
    xor ecx,ecx
    xor r8d,r8d
.L__s3_composite_pop_loop:
    cmp rcx,r15
    jae .L__s3_composite_pop_done
    movzx eax,byte ptr [r14+rcx]
    cmp eax,2
    jae .L__s3_composite_pop_wide
    movsx rdx,word ptr [r9+r8]
    mov qword ptr [r12+rcx*8],rdx
    add r8,2
    jmp .L__s3_composite_pop_next
.L__s3_composite_pop_wide:
    mov rdx,qword ptr [r9+r8]
    mov qword ptr [r12+rcx*8],rdx
    add r8,8
.L__s3_composite_pop_next:
    inc rcx
    jmp .L__s3_composite_pop_loop
.L__s3_composite_pop_done:
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    ret

.type __s3_composite_vector_clone,@function
__s3_composite_vector_clone:
    push rbx
    push r12
    push r13
    push r14
    push r15
    mov r13,rdi
    mov r14,rsi
    mov r15,rdx
    mov rbx,rcx
    mov r10,[r13]
    mov rdi,[r10+16]
    call __s3_dyn_new
    mov r12,rax
    mov r10,[r13]
    mov rax,[r10+8]
    mov [r12+8],rax
    mov rcx,rax
    mov rsi,[r10]
    mov rdi,[r12]
    call __s3_dyn_copy
    xor r11d,r11d
.L__s3_composite_clone_element:
    mov r10,[r13]
    cmp r11,[r10+8]
    jae .L__s3_composite_clone_done
    xor ecx,ecx
    xor edx,edx
.L__s3_composite_clone_cell:
    cmp rcx,r15
    jae .L__s3_composite_clone_next_element
    movzx eax,byte ptr [r14+rcx]
    cmp eax,3
    je .L__s3_composite_clone_owned
    cmp eax,4
    jne .L__s3_composite_clone_advance
.L__s3_composite_clone_owned:
    mov r10,[r13]
    mov rdi,[r10]
    add rdi,r11
    mov rdi,[rdi+rdx]
    test rdi,rdi
    jz __s3_fail_invalid_runtime_state
    push r11
    push rdx
    push rcx
    sub rsp,8
    call __s3_dyn_clone_descriptor
    add rsp,8
    pop rcx
    pop rdx
    pop r11
    mov r10,[r12]
    add r10,r11
    mov [r10+rdx],rax
.L__s3_composite_clone_advance:
    movzx eax,byte ptr [r14+rcx]
    cmp eax,2
    jae .L__s3_composite_clone_advance_wide
    add rdx,2
    jmp .L__s3_composite_clone_advance_next
.L__s3_composite_clone_advance_wide:
    add rdx,8
.L__s3_composite_clone_advance_next:
    inc rcx
    jmp .L__s3_composite_clone_cell
.L__s3_composite_clone_next_element:
    add r11,rbx
    jmp .L__s3_composite_clone_element
.L__s3_composite_clone_done:
    mov rax,r12
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    ret

.type __s3_composite_vector_slice,@function
__s3_composite_vector_slice:
    push rbx
    push r12
    push r13
    push r14
    push r15
    mov r13,rdi
    mov r14,rcx
    mov r15,r8
    mov rbx,r9
    test rsi,rsi
    js __s3_fail_bounds
    test rdx,rdx
    js __s3_fail_bounds
    cmp rdx,rsi
    jl __s3_fail_bounds
    mov rax,rsi
    imul rax,rbx
    jo __s3_fail_bounds
    mov r12,rax
    mov rax,rdx
    imul rax,rbx
    jo __s3_fail_bounds
    mov r11,rax
    mov r10,[r13]
    cmp r11,[r10+8]
    ja __s3_fail_bounds
    sub r11,r12
    sub rsp,16
    mov [rsp],r12
    mov [rsp+8],r11
    mov rdi,r11
    call __s3_dyn_new
    mov r12,rax
    mov r11,[rsp+8]
    mov rcx,r11
    mov r10,[r13]
    mov rsi,[r10]
    add rsi,[rsp]
    mov rdi,[r12]
    call __s3_dyn_copy
    mov [r12+8],r11
    add rsp,16
    xor r10d,r10d
.L__s3_composite_slice_element:
    mov r11,[r12+8]
    cmp r10,r11
    jae .L__s3_composite_slice_done
    xor ecx,ecx
    xor edx,edx
.L__s3_composite_slice_cell:
    cmp rcx,r15
    jae .L__s3_composite_slice_next_element
    movzx eax,byte ptr [r14+rcx]
    cmp eax,3
    je .L__s3_composite_slice_owned
    cmp eax,4
    jne .L__s3_composite_slice_advance
.L__s3_composite_slice_owned:
    mov rdi,[r12]
    add rdi,r10
    mov rdi,[rdi+rdx]
    test rdi,rdi
    jz __s3_fail_invalid_runtime_state
    push r10
    push rdx
    push rcx
    sub rsp,8
    call __s3_dyn_clone_descriptor
    add rsp,8
    pop rcx
    pop rdx
    pop r10
    mov r11,[r12]
    add r11,r10
    mov [r11+rdx],rax
.L__s3_composite_slice_advance:
    movzx eax,byte ptr [r14+rcx]
    cmp eax,2
    jae .L__s3_composite_slice_advance_wide
    add rdx,2
    jmp .L__s3_composite_slice_advance_next
.L__s3_composite_slice_advance_wide:
    add rdx,8
.L__s3_composite_slice_advance_next:
    inc rcx
    jmp .L__s3_composite_slice_cell
.L__s3_composite_slice_next_element:
    add r10,rbx
    jmp .L__s3_composite_slice_element
.L__s3_composite_slice_done:
    mov rax,r12
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    ret

.type __s3_i64_map_find,@function
__s3_i64_map_find:
    mov r10,[rdi]
    mov r11,[r10+8]
    mov r9,[r10]
    xor eax,eax
.L__s3_i64_map_find_loop:
    cmp rax,r11
    jae .L__s3_i64_map_find_no
    mov r8,[r9+rax]
    cmp r8,rsi
    je .L__s3_i64_map_find_done
    add rax,16
    jmp .L__s3_i64_map_find_loop
.L__s3_i64_map_find_no:
    mov rax,-1
.L__s3_i64_map_find_done:
    ret

.type __s3_builtin_i64_map_new,@function
__s3_builtin_i64_map_new:
    mov esi,16
    jmp __s3_vec_new
.type __s3_builtin_i64_map_len,@function
__s3_builtin_i64_map_len:
    mov r10,[rdi]
    mov rax,[r10+8]
    sar rax,4
    ret
.type __s3_builtin_i64_map_capacity,@function
__s3_builtin_i64_map_capacity:
    mov r10,[rdi]
    mov rax,[r10+16]
    sar rax,4
    ret
.type __s3_builtin_i64_map_reserve,@function
__s3_builtin_i64_map_reserve:
    mov edx,16
    jmp __s3_vec_reserve

.type __s3_builtin_i64_map_put,@function
__s3_builtin_i64_map_put:
    push r12
    push r13
    push r14
    mov r12,rdi
    mov r13,rsi
    mov r14,rdx
    call __s3_i64_map_find
    cmp rax,-1
    je .L__s3_i64_map_put_new
    mov r10,[r12]
    mov r11,[r10]
    mov [r11+rax+8],r14
    xor eax,eax
    pop r14
    pop r13
    pop r12
    ret
.L__s3_i64_map_put_new:
    mov r10,[r12]
    mov rax,[r10+8]
    mov r8,rax
    add r8,16
    jc __s3_fail_capacity
    cmp r8,[r10+16]
    ja __s3_fail_capacity
    mov r11,[r10]
    mov [r11+rax],r13
    mov [r11+rax+8],r14
    mov [r10+8],r8
    xor eax,eax
    pop r14
    pop r13
    pop r12
    ret

.type __s3_builtin_i64_map_contains,@function
__s3_builtin_i64_map_contains:
    call __s3_i64_map_find
    cmp rax,-1
    je .L__s3_i64_map_contains_no
    mov rax,-1
    ret
.L__s3_i64_map_contains_no:
    xor eax,eax
    ret
.type __s3_builtin_i64_map_get,@function
__s3_builtin_i64_map_get:
    call __s3_i64_map_find
    cmp rax,-1
    je __s3_fail_bounds
    mov r10,[rdi]
    mov r11,[r10]
    mov rax,[r11+rax+8]
    ret
.type __s3_builtin_i64_map_key_at,@function
__s3_builtin_i64_map_key_at:
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,4
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov rax,[r11+rax]
    ret
.type __s3_builtin_i64_map_value_at,@function
__s3_builtin_i64_map_value_at:
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,4
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov rax,[r11+rax+8]
    ret
.type __s3_builtin_i64_map_remove,@function
__s3_builtin_i64_map_remove:
    push r12
    push r13
    push r14
    mov r12,rdi
    call __s3_i64_map_find
    cmp rax,-1
    je .L__s3_i64_map_remove_done
    mov r13,rax
    mov r10,[r12]
    mov r14,[r10+8]
    mov r8,r14
    sub r8,r13
    sub r8,16
    jz .L__s3_i64_map_remove_length
    mov rdi,[r10]
    add rdi,r13
    mov rsi,rdi
    add rsi,16
    mov rcx,r8
    call __s3_dyn_copy
.L__s3_i64_map_remove_length:
    sub r14,16
    mov [r10+8],r14
.L__s3_i64_map_remove_done:
    xor eax,eax
    pop r14
    pop r13
    pop r12
    ret
.type __s3_builtin_i64_map_clone,@function
__s3_builtin_i64_map_clone:
    jmp __s3_dyn_clone_preserve_capacity

.type __s3_text_i64_map_find,@function
__s3_text_i64_map_find:
    push r12
    push r13
    push r14
    push r15
    mov r12,rdi
    mov r13,[rsi]
    test r13,r13
    jz __s3_fail_invalid_runtime_state
    mov r10,[r12]
    mov r15,[r10+8]
    mov r9,[r10]
    xor r14d,r14d
.L__s3_text_i64_map_find_loop:
    cmp r14,r15
    jae .L__s3_text_i64_map_find_no
    mov r8,[r9+r14]
    test r8,r8
    jz __s3_fail_invalid_runtime_state
    mov r12,[r13+8]
    mov rax,[r8+8]
    cmp rax,r12
    jne .L__s3_text_i64_map_find_next
    mov rdx,[r8]
    mov rcx,[r13]
    xor eax,eax
.L__s3_text_i64_map_find_bytes:
    cmp rax,r12
    jae .L__s3_text_i64_map_find_done
    movzx r10d,byte ptr [rdx+rax]
    movzx r11d,byte ptr [rcx+rax]
    cmp r10d,r11d
    jne .L__s3_text_i64_map_find_next
    inc rax
    jmp .L__s3_text_i64_map_find_bytes
.L__s3_text_i64_map_find_next:
    add r14,16
    jmp .L__s3_text_i64_map_find_loop
.L__s3_text_i64_map_find_no:
    mov rax,-1
    jmp .L__s3_text_i64_map_find_return
.L__s3_text_i64_map_find_done:
    mov rax,r14
.L__s3_text_i64_map_find_return:
    pop r15
    pop r14
    pop r13
    pop r12
    ret

.type __s3_builtin_text_i64_map_new,@function
__s3_builtin_text_i64_map_new:
    mov esi,16
    jmp __s3_vec_new
.type __s3_builtin_text_i64_map_len,@function
__s3_builtin_text_i64_map_len:
    mov r10,[rdi]
    mov rax,[r10+8]
    sar rax,4
    ret
.type __s3_builtin_text_i64_map_capacity,@function
__s3_builtin_text_i64_map_capacity:
    mov r10,[rdi]
    mov rax,[r10+16]
    sar rax,4
    ret
.type __s3_builtin_text_i64_map_reserve,@function
__s3_builtin_text_i64_map_reserve:
    mov edx,16
    jmp __s3_vec_reserve

.type __s3_builtin_text_i64_map_put,@function
__s3_builtin_text_i64_map_put:
    push r12
    push r13
    push r14
    push r15
    mov r12,rdi
    mov r13,rsi
    mov r14,rdx
    call __s3_text_i64_map_find
    cmp rax,-1
    je .L__s3_text_i64_map_put_new
    mov r10,[r12]
    mov r11,[r10]
    mov [r11+rax+8],r14
    xor eax,eax
    jmp .L__s3_text_i64_map_put_return
.L__s3_text_i64_map_put_new:
    mov r10,[r12]
    mov rax,[r10+8]
    mov r8,rax
    add rax,16
    jc __s3_fail_capacity
    cmp rax,[r10+16]
    ja __s3_fail_capacity
    push r14
    mov r15,r8
    mov r14,rax
    mov rdi,[r13]
    call __s3_dyn_clone_descriptor
    mov r8,rax
    pop r13
    mov r10,[r12]
    mov r11,[r10]
    mov [r11+r15],r8
    mov [r11+r15+8],r13
    mov [r10+8],r14
    xor eax,eax
.L__s3_text_i64_map_put_return:
    pop r15
    pop r14
    pop r13
    pop r12
    ret

.type __s3_builtin_text_i64_map_contains,@function
__s3_builtin_text_i64_map_contains:
    call __s3_text_i64_map_find
    cmp rax,-1
    je .L__s3_text_i64_map_contains_no
    mov rax,-1
    ret
.L__s3_text_i64_map_contains_no:
    xor eax,eax
    ret
.type __s3_builtin_text_i64_map_get,@function
__s3_builtin_text_i64_map_get:
    call __s3_text_i64_map_find
    cmp rax,-1
    je __s3_fail_bounds
    mov r10,[rdi]
    mov r11,[r10]
    mov rax,[r11+rax+8]
    ret
.type __s3_builtin_text_i64_map_key_at,@function
__s3_builtin_text_i64_map_key_at:
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,4
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov rdi,[r11+rax]
    jmp __s3_dyn_clone_descriptor
.type __s3_builtin_text_i64_map_value_at,@function
__s3_builtin_text_i64_map_value_at:
    mov r10,[rdi]
    test rsi,rsi
    js __s3_fail_bounds
    mov rax,rsi
    shl rax,4
    jc __s3_fail_bounds
    cmp rax,[r10+8]
    jae __s3_fail_bounds
    mov r11,[r10]
    mov rax,[r11+rax+8]
    ret
.type __s3_builtin_text_i64_map_remove,@function
__s3_builtin_text_i64_map_remove:
    push r12
    push r13
    push r14
    mov r12,rdi
    call __s3_text_i64_map_find
    cmp rax,-1
    je .L__s3_text_i64_map_remove_done
    mov r13,rax
    mov r10,[r12]
    mov rdi,[r10]
    mov rdi,[rdi+r13]
    call __s3_dyn_drop_descriptor
    mov r10,[r12]
    mov r14,[r10+8]
    mov r8,r14
    sub r8,r13
    sub r8,16
    jz .L__s3_text_i64_map_remove_length
    mov rdi,[r10]
    add rdi,r13
    mov rsi,rdi
    add rsi,16
    mov rcx,r8
    call __s3_dyn_copy
.L__s3_text_i64_map_remove_length:
    sub r14,16
    mov [r10+8],r14
.L__s3_text_i64_map_remove_done:
    xor eax,eax
    pop r14
    pop r13
    pop r12
    ret
.type __s3_builtin_text_i64_map_clone,@function
__s3_builtin_text_i64_map_clone:
    push r12
    push r13
    push r14
    push r15
    mov r15,[rdi]
    mov rdi,[r15+16]
    call __s3_dyn_new
    mov r12,rax
    mov r13,[r15+8]
    mov [r12+8],r13
    mov rcx,r13
    mov rsi,[r15]
    mov rdi,[r12]
    call __s3_dyn_copy
    xor r14d,r14d
.L__s3_text_i64_map_clone_loop:
    cmp r14,r13
    jae .L__s3_text_i64_map_clone_done
    mov r10,[r15]
    mov rdi,[r10+r14]
    call __s3_dyn_clone_descriptor
    mov r10,[r12]
    mov [r10+r14],rax
    add r14,16
    jmp .L__s3_text_i64_map_clone_loop
.L__s3_text_i64_map_clone_done:
    mov rax,r12
    pop r15
    pop r14
    pop r13
    pop r12
    ret

.type __s3_i64_set_find,@function
__s3_i64_set_find:
    mov r10,[rdi]
    mov r11,[r10+8]
    mov r9,[r10]
    xor eax,eax
.L__s3_i64_set_find_loop:
    cmp rax,r11
    jae .L__s3_i64_set_find_no
    mov r8,[r9+rax]
    cmp r8,rsi
    je .L__s3_i64_set_find_done
    add rax,8
    jmp .L__s3_i64_set_find_loop
.L__s3_i64_set_find_no:
    mov rax,-1
.L__s3_i64_set_find_done:
    ret
.type __s3_builtin_i64_set_new,@function
__s3_builtin_i64_set_new:
    jmp __s3_builtin_i64_vector_new
.type __s3_builtin_i64_set_len,@function
__s3_builtin_i64_set_len:
    jmp __s3_builtin_i64_vector_len
.type __s3_builtin_i64_set_capacity,@function
__s3_builtin_i64_set_capacity:
    jmp __s3_builtin_i64_vector_capacity
.type __s3_builtin_i64_set_reserve,@function
__s3_builtin_i64_set_reserve:
    jmp __s3_builtin_i64_vector_reserve
.type __s3_builtin_i64_set_add,@function
__s3_builtin_i64_set_add:
    push r12
    mov r12,rsi
    call __s3_i64_set_find
    cmp rax,-1
    jne .L__s3_i64_set_add_done
    mov rsi,r12
    call __s3_vec_push_8
.L__s3_i64_set_add_done:
    xor eax,eax
    pop r12
    ret
.type __s3_builtin_i64_set_contains,@function
__s3_builtin_i64_set_contains:
    call __s3_i64_set_find
    cmp rax,-1
    je .L__s3_i64_set_contains_no
    mov rax,-1
    ret
.L__s3_i64_set_contains_no:
    xor eax,eax
    ret
.type __s3_builtin_i64_set_remove,@function
__s3_builtin_i64_set_remove:
    push r12
    push r13
    push r14
    mov r12,rdi
    call __s3_i64_set_find
    cmp rax,-1
    je .L__s3_i64_set_remove_done
    mov r13,rax
    mov r10,[r12]
    mov r14,[r10+8]
    mov r8,r14
    sub r8,r13
    sub r8,8
    jz .L__s3_i64_set_remove_length
    mov rdi,[r10]
    add rdi,r13
    mov rsi,rdi
    add rsi,8
    mov rcx,r8
    call __s3_dyn_copy
.L__s3_i64_set_remove_length:
    sub r14,8
    mov [r10+8],r14
.L__s3_i64_set_remove_done:
    xor eax,eax
    pop r14
    pop r13
    pop r12
    ret
.type __s3_builtin_i64_set_at,@function
__s3_builtin_i64_set_at:
    jmp __s3_vec_get_8
.type __s3_builtin_i64_set_clone,@function
__s3_builtin_i64_set_clone:
    jmp __s3_dyn_clone_preserve_capacity
.type __s3_builtin_host_capability_grant,@function
__s3_builtin_host_capability_grant:
    cmp rdi,1
    jb __s3_fail_bounds
    cmp rdi,3
    ja __s3_fail_bounds
    mov rax,rdi
    ret
.type __s3_resource_find,@function
__s3_resource_find:
    mov rax,[rdi]
    test rax,rax
    jz .L__s3_resource_find_no
    lea r10,[rip+__s3_resource_slots]
    xor ecx,ecx
.L__s3_resource_find_loop:
    cmp qword ptr [r10+rcx*8],rax
    je .L__s3_resource_find_match
    inc ecx
    cmp ecx,3
    jb .L__s3_resource_find_loop
.L__s3_resource_find_no:
    mov rax,-1
    jmp .L__s3_resource_find_done
.L__s3_resource_find_match:
    mov rax,rcx
.L__s3_resource_find_done:
    ret
.type __s3_builtin_resource_open,@function
__s3_builtin_resource_open:
    cmp rdi,1
    jb __s3_fail_bounds
    cmp rdi,3
    ja __s3_fail_bounds
    mov r10,rdi
    lea r11,[rip+__s3_resource_slots]
    xor ecx,ecx
.L__s3_resource_open_loop:
    cmp qword ptr [r11+rcx*8],0
    je .L__s3_resource_open_slot
    inc ecx
    cmp ecx,3
    jb .L__s3_resource_open_loop
    jmp __s3_fail_capacity
.L__s3_resource_open_slot:
    lea rdx,[rip+__s3_resource_generations]
    inc qword ptr [rdx+rcx*8]
    mov rax,[rdx+rcx*8]
    mov r8,r10
    shl r8,56
    mov r9,rcx
    inc r9
    shl r9,48
    or rax,r8
    or rax,r9
    mov [r11+rcx*8],rax
    ret
.type __s3_builtin_resource_is_open,@function
__s3_builtin_resource_is_open:
    call __s3_resource_find
    cmp rax,-1
    je .L__s3_resource_is_open_no
    mov rax,-1
    ret
.L__s3_resource_is_open_no:
    xor eax,eax
    ret
.type __s3_builtin_resource_kind,@function
__s3_builtin_resource_kind:
    call __s3_resource_find
    cmp rax,-1
    je __s3_fail_bounds
    mov r10,[rdi]
    shr r10,56
    mov rax,r10
    ret
.type __s3_builtin_resource_invoke,@function
__s3_builtin_resource_invoke:
    call __s3_resource_find
    cmp rax,-1
    je __s3_fail_bounds
    xor eax,eax
    ret
.type __s3_builtin_resource_close,@function
__s3_builtin_resource_close:
    call __s3_resource_find
    cmp rax,-1
    je __s3_fail_bounds
    lea r11,[rip+__s3_resource_slots]
    mov qword ptr [r11+rax*8],0
    mov qword ptr [rdi],0
    xor eax,eax
    ret

__s3_fail_overflow:
    lea rsi, [rip + .L__s3_error_overflow]
    mov edx, 24
    jmp __s3_fail_message
__s3_fail_bounds:
    lea rsi, [rip + .L__s3_error_bounds]
    mov edx, 22
    jmp __s3_fail_message
__s3_fail_uninitialized_register:
    lea rsi, [rip + .L__s3_error_uninitialized_register]
    mov edx, 38
    jmp __s3_fail_message
__s3_fail_uninitialized_memory:
    lea rsi, [rip + .L__s3_error_uninitialized_memory]
    mov edx, 36
    jmp __s3_fail_message
__s3_fail_immutable_memory:
    lea rsi, [rip + .L__s3_error_immutable_memory]
    mov edx, 32
    jmp __s3_fail_message
__s3_fail_invalid_trit:
    lea rsi, [rip + .L__s3_error_invalid_trit]
    mov edx, 28
    jmp __s3_fail_message
__s3_fail_frame_limit:
    lea rsi, [rip + .L__s3_error_frame_limit]
    mov edx, 27
    jmp __s3_fail_message
__s3_fail_instruction_limit:
    lea rsi, [rip + .L__s3_error_instruction_limit]
    mov edx, 33
    jmp __s3_fail_message
__s3_fail_invalid_runtime_state:
    lea rsi, [rip + .L__s3_error_invalid_runtime_state]
    mov edx, 37
    jmp __s3_fail_message
__s3_fail_capacity:
    lea rsi, [rip + .L__s3_error_capacity]
    mov edx, 39
    jmp __s3_fail_message
__s3_fail_allocation:
    lea rsi, [rip + .L__s3_error_allocation]
    mov edx, 41
    jmp __s3_fail_message
__s3_fail_encoding:
    lea rsi, [rip + .L__s3_error_encoding]
    mov edx, 29
    jmp __s3_fail_message
__s3_fail_boundary:
    lea rsi, [rip + .L__s3_error_boundary]
    mov edx, 38
    jmp __s3_fail_message
__s3_fail:
__s3_fail_message:
    mov eax, 1
    mov edi, 2
    syscall
    mov eax, 60
    mov edi, 1
    syscall
    ud2

__s3_fail_value:
    mov r12, rdi
    mov r13, rcx
    mov r14, r8
    mov eax, 1
    mov edi, 2
    syscall
    sub rsp, 64
    lea rsi, [rsp + 64]
    xor r15d, r15d
    mov rax, r12
    test rax, rax
    jne .L__s3_fail_value_nonzero
    dec rsi
    mov byte ptr [rsi], 48
    inc r15
    jmp .L__s3_fail_value_write
.L__s3_fail_value_nonzero:
    xor r9d, r9d
    test rax, rax
    jns .L__s3_fail_value_digits
    mov r9d, 1
    neg rax
.L__s3_fail_value_digits:
    xor edx, edx
    mov r10, 10
    div r10
    add dl, 48
    dec rsi
    mov byte ptr [rsi], dl
    inc r15
    test rax, rax
    jne .L__s3_fail_value_digits
    test r9d, r9d
    je .L__s3_fail_value_write
    dec rsi
    mov byte ptr [rsi], 45
    inc r15
.L__s3_fail_value_write:
    mov eax, 1
    mov edi, 2
    mov rdx, r15
    syscall
    mov eax, 1
    mov edi, 2
    mov rsi, r13
    mov rdx, r14
    syscall
    mov eax, 60
    mov edi, 1
    syscall
    ud2

.section .rodata
.L__s3_result_prefix:
    .ascii "program returned: "
.L__s3_error_overflow:
    .ascii "runtime error: overflow\n"
.L__s3_error_bounds:
    .ascii "runtime error: bounds\n"
.L__s3_error_uninitialized_register:
    .ascii "runtime error: uninitialized register\n"
.L__s3_error_uninitialized_memory:
    .ascii "runtime error: uninitialized memory\n"
.L__s3_error_immutable_memory:
    .ascii "runtime error: immutable memory\n"
.L__s3_error_invalid_trit:
    .ascii "runtime error: invalid trit\n"
.L__s3_error_frame_limit:
    .ascii "runtime error: frame limit\n"
.L__s3_error_instruction_limit:
    .ascii "runtime error: instruction limit\n"
.L__s3_error_invalid_runtime_state:
    .ascii "runtime error: invalid runtime state\n"
.L__s3_error_capacity:
    .ascii "runtime error: dynamic buffer capacity\n"
.L__s3_error_allocation:
    .ascii "runtime error: dynamic buffer allocation\n"
.L__s3_error_encoding:
    .ascii "runtime error: invalid UTF-8\n"
.L__s3_error_boundary:
    .ascii "runtime error: invalid UTF-8 boundary\n"

.section .bss
    .align 8
__s3_frame_count:
    .zero 8
    .align 8
__s3_instruction_count:
    .zero 8
    .align 8
__s3_resource_slots:
    .zero 24
    .align 8
__s3_resource_generations:
    .zero 24

.section .note.GNU-stack,"",@progbits
