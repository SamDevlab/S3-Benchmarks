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
    mov qword ptr [rbp - 2704], r15
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
    mov r15, qword ptr [rip + __s3_instruction_remaining]
    jmp .L_s3_f21_agent_energy_residual_b5_entry
.L_s3_f21_agent_energy_residual_b5_entry:
    dec r15
    js .L__s3_failure_site_1
    mov r12, 0
    mov byte ptr [rbp - 2272], 1
    dec r15
    js .L__s3_failure_site_2
    mov r13, 0
    mov byte ptr [rbp - 2273], 1
    dec r15
    js .L__s3_failure_site_3
    cmp byte ptr [rbp - 2273], 0
    je .L__s3_failure_site_4
    mov rax, r13
    cmp byte ptr [rbp - 2272], 0
    je .L__s3_failure_site_5
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_6
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_7
    mov r12, 0
    mov byte ptr [rbp - 2274], 1
    dec r15
    js .L__s3_failure_site_8
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_9
    mov rax, rdx
    cmp byte ptr [rbp - 2274], 0
    je .L__s3_failure_site_10
    mov r10, r12
    dec r15
    js .L__s3_failure_site_11
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b9_rel_neg_0
    jg .L_s3_f21_agent_energy_residual_b9_rel_pos_2
    jmp .L_s3_f21_agent_energy_residual_b10_rel_zero_1
.L_s3_f21_agent_energy_residual_b9_rel_neg_0:
    dec r15
    js .L__s3_failure_site_12
    mov r12, 0
    mov byte ptr [rbp - 2276], 1
    dec r15
    js .L__s3_failure_site_13
    mov r13, -1
    mov byte ptr [rbp - 2277], 1
    dec r15
    js .L__s3_failure_site_14
    cmp byte ptr [rbp - 2276], 0
    je .L__s3_failure_site_15
    mov rax, r12
    cmp byte ptr [rbp - 2277], 0
    je .L__s3_failure_site_16
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_17
    cmp r10, -1
    jl .L__s3_failure_site_18
    cmp r10, 1
    jg .L__s3_failure_site_18
    mov byte ptr [rbp + rax - 2561], r10b
    mov byte ptr [rbp + rax - 2651], 1
    dec r15
    js .L__s3_failure_site_19
    jmp .L_s3_f21_agent_energy_residual_b10_rel_cont_3
.L_s3_f21_agent_energy_residual_b10_rel_zero_1:
    dec r15
    js .L__s3_failure_site_20
    mov r12, 0
    mov byte ptr [rbp - 2278], 1
    dec r15
    js .L__s3_failure_site_21
    mov r13, -1
    mov byte ptr [rbp - 2279], 1
    dec r15
    js .L__s3_failure_site_22
    cmp byte ptr [rbp - 2278], 0
    je .L__s3_failure_site_23
    mov rax, r12
    cmp byte ptr [rbp - 2279], 0
    je .L__s3_failure_site_24
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_25
    cmp r10, -1
    jl .L__s3_failure_site_26
    cmp r10, 1
    jg .L__s3_failure_site_26
    mov byte ptr [rbp + rax - 2561], r10b
    mov byte ptr [rbp + rax - 2651], 1
    dec r15
    js .L__s3_failure_site_27
    jmp .L_s3_f21_agent_energy_residual_b10_rel_cont_3
.L_s3_f21_agent_energy_residual_b9_rel_pos_2:
    dec r15
    js .L__s3_failure_site_28
    mov r12, 0
    mov byte ptr [rbp - 2280], 1
    dec r15
    js .L__s3_failure_site_29
    mov r13, 0
    mov byte ptr [rbp - 2281], 1
    dec r15
    js .L__s3_failure_site_30
    cmp byte ptr [rbp - 2280], 0
    je .L__s3_failure_site_31
    mov rax, r12
    cmp byte ptr [rbp - 2281], 0
    je .L__s3_failure_site_32
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_33
    cmp r10, -1
    jl .L__s3_failure_site_34
    cmp r10, 1
    jg .L__s3_failure_site_34
    mov byte ptr [rbp + rax - 2561], r10b
    mov byte ptr [rbp + rax - 2651], 1
    dec r15
    js .L__s3_failure_site_35
    jmp .L_s3_f21_agent_energy_residual_b10_rel_cont_3
.L_s3_f21_agent_energy_residual_b10_rel_cont_3:
    dec r15
    js .L__s3_failure_site_36
    mov r12, 0
    mov byte ptr [rbp - 2282], 1
    dec r15
    js .L__s3_failure_site_37
    cmp byte ptr [rbp - 2282], 0
    je .L__s3_failure_site_39
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_40
    cmp byte ptr [rbp + r10 - 2651], 0
    je .L__s3_failure_site_38
    movsx rax, byte ptr [rbp + r10 - 2561]
    mov r12, rax
    mov byte ptr [rbp - 2283], 1
    dec r15
    js .L__s3_failure_site_41
    cmp byte ptr [rbp - 2283], 0
    je .L__s3_failure_site_43
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b17_switch_negative_4
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b16_switch_neutral_5
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b17_switch_positive_6
    jmp .L__s3_failure_site_42
.L_s3_f21_agent_energy_residual_b17_switch_negative_4:
    dec r15
    js .L__s3_failure_site_44
    mov r12, 1
    mov byte ptr [rbp - 2284], 1
    dec r15
    js .L__s3_failure_site_45
    mov r13, 0
    mov byte ptr [rbp - 2285], 1
    dec r15
    js .L__s3_failure_site_46
    cmp byte ptr [rbp - 2285], 0
    je .L__s3_failure_site_47
    mov rax, r13
    cmp byte ptr [rbp - 2284], 0
    je .L__s3_failure_site_48
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_49
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_50
    jmp .L_s3_f21_agent_energy_residual_b17_switch_continue_7
.L_s3_f21_agent_energy_residual_b16_switch_neutral_5:
    dec r15
    js .L__s3_failure_site_51
    mov r12, 0
    mov byte ptr [rbp - 2286], 1
    dec r15
    js .L__s3_failure_site_52
    cmp byte ptr [rbp - 2286], 0
    je .L__s3_failure_site_54
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_55
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_53
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2287], 1
    dec r15
    js .L__s3_failure_site_56
    mov r13, 0
    mov byte ptr [rbp - 2288], 1
    dec r15
    js .L__s3_failure_site_57
    cmp byte ptr [rbp - 2288], 0
    je .L__s3_failure_site_58
    mov rax, r13
    cmp byte ptr [rbp - 2287], 0
    je .L__s3_failure_site_59
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_60
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_61
    jmp .L_s3_f21_agent_energy_residual_b17_switch_continue_7
.L_s3_f21_agent_energy_residual_b17_switch_positive_6:
    dec r15
    js .L__s3_failure_site_62
    mov r12, 0
    mov byte ptr [rbp - 2289], 1
    dec r15
    js .L__s3_failure_site_63
    cmp byte ptr [rbp - 2289], 0
    je .L__s3_failure_site_65
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_66
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_64
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2290], 1
    dec r15
    js .L__s3_failure_site_67
    mov r13, 0
    mov byte ptr [rbp - 2291], 1
    dec r15
    js .L__s3_failure_site_68
    cmp byte ptr [rbp - 2291], 0
    je .L__s3_failure_site_69
    mov rax, r13
    cmp byte ptr [rbp - 2290], 0
    je .L__s3_failure_site_70
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_71
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_72
    jmp .L_s3_f21_agent_energy_residual_b17_switch_continue_7
.L_s3_f21_agent_energy_residual_b17_switch_continue_7:
    dec r15
    js .L__s3_failure_site_73
    mov r12, 364
    mov byte ptr [rbp - 2292], 1
    dec r15
    js .L__s3_failure_site_74
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_75
    mov rax, rdx
    cmp byte ptr [rbp - 2292], 0
    je .L__s3_failure_site_76
    mov r10, r12
    dec r15
    js .L__s3_failure_site_77
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b9_rel_neg_8
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_10
    jmp .L_s3_f21_agent_energy_residual_b10_rel_zero_9
.L_s3_f21_agent_energy_residual_b9_rel_neg_8:
    dec r15
    js .L__s3_failure_site_78
    mov r12, 0
    mov byte ptr [rbp - 2294], 1
    dec r15
    js .L__s3_failure_site_79
    mov r13, 0
    mov byte ptr [rbp - 2295], 1
    dec r15
    js .L__s3_failure_site_80
    cmp byte ptr [rbp - 2294], 0
    je .L__s3_failure_site_81
    mov rax, r12
    cmp byte ptr [rbp - 2295], 0
    je .L__s3_failure_site_82
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_83
    cmp r10, -1
    jl .L__s3_failure_site_84
    cmp r10, 1
    jg .L__s3_failure_site_84
    mov byte ptr [rbp + rax - 2562], r10b
    mov byte ptr [rbp + rax - 2652], 1
    dec r15
    js .L__s3_failure_site_85
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_11
.L_s3_f21_agent_energy_residual_b10_rel_zero_9:
    dec r15
    js .L__s3_failure_site_86
    mov r12, 0
    mov byte ptr [rbp - 2296], 1
    dec r15
    js .L__s3_failure_site_87
    mov r13, 0
    mov byte ptr [rbp - 2297], 1
    dec r15
    js .L__s3_failure_site_88
    cmp byte ptr [rbp - 2296], 0
    je .L__s3_failure_site_89
    mov rax, r12
    cmp byte ptr [rbp - 2297], 0
    je .L__s3_failure_site_90
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_91
    cmp r10, -1
    jl .L__s3_failure_site_92
    cmp r10, 1
    jg .L__s3_failure_site_92
    mov byte ptr [rbp + rax - 2562], r10b
    mov byte ptr [rbp + rax - 2652], 1
    dec r15
    js .L__s3_failure_site_93
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_11
.L_s3_f21_agent_energy_residual_b10_rel_pos_10:
    dec r15
    js .L__s3_failure_site_94
    mov r12, 0
    mov byte ptr [rbp - 2298], 1
    dec r15
    js .L__s3_failure_site_95
    mov r13, -1
    mov byte ptr [rbp - 2299], 1
    dec r15
    js .L__s3_failure_site_96
    cmp byte ptr [rbp - 2298], 0
    je .L__s3_failure_site_97
    mov rax, r12
    cmp byte ptr [rbp - 2299], 0
    je .L__s3_failure_site_98
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_99
    cmp r10, -1
    jl .L__s3_failure_site_100
    cmp r10, 1
    jg .L__s3_failure_site_100
    mov byte ptr [rbp + rax - 2562], r10b
    mov byte ptr [rbp + rax - 2652], 1
    dec r15
    js .L__s3_failure_site_101
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_11
.L_s3_f21_agent_energy_residual_b11_rel_cont_11:
    dec r15
    js .L__s3_failure_site_102
    mov r12, 0
    mov byte ptr [rbp - 2300], 1
    dec r15
    js .L__s3_failure_site_103
    cmp byte ptr [rbp - 2300], 0
    je .L__s3_failure_site_105
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_106
    cmp byte ptr [rbp + r10 - 2652], 0
    je .L__s3_failure_site_104
    movsx rax, byte ptr [rbp + r10 - 2562]
    mov r12, rax
    mov byte ptr [rbp - 2301], 1
    dec r15
    js .L__s3_failure_site_107
    cmp byte ptr [rbp - 2301], 0
    je .L__s3_failure_site_109
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_12
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_13
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_14
    jmp .L__s3_failure_site_108
.L_s3_f21_agent_energy_residual_b18_switch_negative_12:
    dec r15
    js .L__s3_failure_site_110
    mov r12, 1
    mov byte ptr [rbp - 2302], 1
    dec r15
    js .L__s3_failure_site_111
    mov r13, 0
    mov byte ptr [rbp - 2303], 1
    dec r15
    js .L__s3_failure_site_112
    cmp byte ptr [rbp - 2303], 0
    je .L__s3_failure_site_113
    mov rax, r13
    cmp byte ptr [rbp - 2302], 0
    je .L__s3_failure_site_114
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_115
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_116
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_15
.L_s3_f21_agent_energy_residual_b17_switch_neutral_13:
    dec r15
    js .L__s3_failure_site_117
    mov r12, 0
    mov byte ptr [rbp - 2304], 1
    dec r15
    js .L__s3_failure_site_118
    cmp byte ptr [rbp - 2304], 0
    je .L__s3_failure_site_120
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_121
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_119
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2305], 1
    dec r15
    js .L__s3_failure_site_122
    mov r13, 0
    mov byte ptr [rbp - 2306], 1
    dec r15
    js .L__s3_failure_site_123
    cmp byte ptr [rbp - 2306], 0
    je .L__s3_failure_site_124
    mov rax, r13
    cmp byte ptr [rbp - 2305], 0
    je .L__s3_failure_site_125
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_126
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_127
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_15
.L_s3_f21_agent_energy_residual_b18_switch_positive_14:
    dec r15
    js .L__s3_failure_site_128
    mov r12, 0
    mov byte ptr [rbp - 2307], 1
    dec r15
    js .L__s3_failure_site_129
    cmp byte ptr [rbp - 2307], 0
    je .L__s3_failure_site_131
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_132
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_130
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2308], 1
    dec r15
    js .L__s3_failure_site_133
    mov r13, 0
    mov byte ptr [rbp - 2309], 1
    dec r15
    js .L__s3_failure_site_134
    cmp byte ptr [rbp - 2309], 0
    je .L__s3_failure_site_135
    mov rax, r13
    cmp byte ptr [rbp - 2308], 0
    je .L__s3_failure_site_136
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_137
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_138
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_15
.L_s3_f21_agent_energy_residual_b18_switch_continue_15:
    dec r15
    js .L__s3_failure_site_139
    mov r12, 0
    mov byte ptr [rbp - 2310], 1
    dec r15
    js .L__s3_failure_site_140
    cmp byte ptr [rbp - 2310], 0
    je .L__s3_failure_site_142
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_143
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_141
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2311], 1
    dec r15
    js .L__s3_failure_site_144
    mov r13, 0
    mov byte ptr [rbp - 2312], 1
    dec r15
    js .L__s3_failure_site_145
    cmp byte ptr [rbp - 2311], 0
    je .L__s3_failure_site_146
    mov rax, r12
    cmp byte ptr [rbp - 2312], 0
    je .L__s3_failure_site_147
    mov r10, r13
    dec r15
    js .L__s3_failure_site_148
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_16
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_18
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_17
.L_s3_f21_agent_energy_residual_b10_rel_neg_16:
    dec r15
    js .L__s3_failure_site_149
    mov r12, 0
    mov byte ptr [rbp - 2314], 1
    dec r15
    js .L__s3_failure_site_150
    mov r13, 0
    mov byte ptr [rbp - 2315], 1
    dec r15
    js .L__s3_failure_site_151
    cmp byte ptr [rbp - 2314], 0
    je .L__s3_failure_site_152
    mov rax, r12
    cmp byte ptr [rbp - 2315], 0
    je .L__s3_failure_site_153
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_154
    cmp r10, -1
    jl .L__s3_failure_site_155
    cmp r10, 1
    jg .L__s3_failure_site_155
    mov byte ptr [rbp + rax - 2563], r10b
    mov byte ptr [rbp + rax - 2653], 1
    dec r15
    js .L__s3_failure_site_156
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_19
.L_s3_f21_agent_energy_residual_b11_rel_zero_17:
    dec r15
    js .L__s3_failure_site_157
    mov r12, 0
    mov byte ptr [rbp - 2316], 1
    dec r15
    js .L__s3_failure_site_158
    mov r13, -1
    mov byte ptr [rbp - 2317], 1
    dec r15
    js .L__s3_failure_site_159
    cmp byte ptr [rbp - 2316], 0
    je .L__s3_failure_site_160
    mov rax, r12
    cmp byte ptr [rbp - 2317], 0
    je .L__s3_failure_site_161
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_162
    cmp r10, -1
    jl .L__s3_failure_site_163
    cmp r10, 1
    jg .L__s3_failure_site_163
    mov byte ptr [rbp + rax - 2563], r10b
    mov byte ptr [rbp + rax - 2653], 1
    dec r15
    js .L__s3_failure_site_164
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_19
.L_s3_f21_agent_energy_residual_b10_rel_pos_18:
    dec r15
    js .L__s3_failure_site_165
    mov r12, 0
    mov byte ptr [rbp - 2318], 1
    dec r15
    js .L__s3_failure_site_166
    mov r13, 0
    mov byte ptr [rbp - 2319], 1
    dec r15
    js .L__s3_failure_site_167
    cmp byte ptr [rbp - 2318], 0
    je .L__s3_failure_site_168
    mov rax, r12
    cmp byte ptr [rbp - 2319], 0
    je .L__s3_failure_site_169
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_170
    cmp r10, -1
    jl .L__s3_failure_site_171
    cmp r10, 1
    jg .L__s3_failure_site_171
    mov byte ptr [rbp + rax - 2563], r10b
    mov byte ptr [rbp + rax - 2653], 1
    dec r15
    js .L__s3_failure_site_172
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_19
.L_s3_f21_agent_energy_residual_b11_rel_cont_19:
    dec r15
    js .L__s3_failure_site_173
    mov r12, 0
    mov byte ptr [rbp - 2320], 1
    dec r15
    js .L__s3_failure_site_174
    cmp byte ptr [rbp - 2320], 0
    je .L__s3_failure_site_176
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_177
    cmp byte ptr [rbp + r10 - 2653], 0
    je .L__s3_failure_site_175
    movsx rax, byte ptr [rbp + r10 - 2563]
    mov r12, rax
    mov byte ptr [rbp - 2321], 1
    dec r15
    js .L__s3_failure_site_178
    cmp byte ptr [rbp - 2321], 0
    je .L__s3_failure_site_180
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_20
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_21
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_22
    jmp .L__s3_failure_site_179
.L_s3_f21_agent_energy_residual_b18_switch_negative_20:
    dec r15
    js .L__s3_failure_site_181
    cmp byte ptr [rbp - 2266], 0
    je .L__s3_failure_site_182
    mov rax, r8
    mov r12, rax
    mov byte ptr [rbp - 2322], 1
    dec r15
    js .L__s3_failure_site_183
    cmp byte ptr [rbp - 2322], 0
    je .L__s3_failure_site_184
    mov rax, r12
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_185
    mov r10, rdx
    dec r15
    js .L__s3_failure_site_186
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_23
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_25
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_24
.L_s3_f21_agent_energy_residual_b17_switch_neutral_21:
    dec r15
    js .L__s3_failure_site_187
    mov r12, 0
    mov byte ptr [rbp - 2356], 1
    dec r15
    js .L__s3_failure_site_188
    cmp byte ptr [rbp - 2356], 0
    je .L__s3_failure_site_190
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_191
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_189
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2357], 1
    dec r15
    js .L__s3_failure_site_192
    mov r13, 0
    mov byte ptr [rbp - 2358], 1
    dec r15
    js .L__s3_failure_site_193
    cmp byte ptr [rbp - 2358], 0
    je .L__s3_failure_site_194
    mov rax, r13
    cmp byte ptr [rbp - 2357], 0
    je .L__s3_failure_site_195
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_196
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_197
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b18_switch_positive_22:
    dec r15
    js .L__s3_failure_site_198
    mov r12, 0
    mov byte ptr [rbp - 2359], 1
    dec r15
    js .L__s3_failure_site_199
    cmp byte ptr [rbp - 2359], 0
    je .L__s3_failure_site_201
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_202
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_200
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2360], 1
    dec r15
    js .L__s3_failure_site_203
    mov r13, 0
    mov byte ptr [rbp - 2361], 1
    dec r15
    js .L__s3_failure_site_204
    cmp byte ptr [rbp - 2361], 0
    je .L__s3_failure_site_205
    mov rax, r13
    cmp byte ptr [rbp - 2360], 0
    je .L__s3_failure_site_206
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_207
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_208
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b10_rel_neg_23:
    dec r15
    js .L__s3_failure_site_209
    mov r12, 0
    mov byte ptr [rbp - 2324], 1
    dec r15
    js .L__s3_failure_site_210
    mov r13, 0
    mov byte ptr [rbp - 2325], 1
    dec r15
    js .L__s3_failure_site_211
    cmp byte ptr [rbp - 2324], 0
    je .L__s3_failure_site_212
    mov rax, r12
    cmp byte ptr [rbp - 2325], 0
    je .L__s3_failure_site_213
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_214
    cmp r10, -1
    jl .L__s3_failure_site_215
    cmp r10, 1
    jg .L__s3_failure_site_215
    mov byte ptr [rbp + rax - 2564], r10b
    mov byte ptr [rbp + rax - 2654], 1
    dec r15
    js .L__s3_failure_site_216
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_26
.L_s3_f21_agent_energy_residual_b11_rel_zero_24:
    dec r15
    js .L__s3_failure_site_217
    mov r12, 0
    mov byte ptr [rbp - 2326], 1
    dec r15
    js .L__s3_failure_site_218
    mov r13, -1
    mov byte ptr [rbp - 2327], 1
    dec r15
    js .L__s3_failure_site_219
    cmp byte ptr [rbp - 2326], 0
    je .L__s3_failure_site_220
    mov rax, r12
    cmp byte ptr [rbp - 2327], 0
    je .L__s3_failure_site_221
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_222
    cmp r10, -1
    jl .L__s3_failure_site_223
    cmp r10, 1
    jg .L__s3_failure_site_223
    mov byte ptr [rbp + rax - 2564], r10b
    mov byte ptr [rbp + rax - 2654], 1
    dec r15
    js .L__s3_failure_site_224
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_26
.L_s3_f21_agent_energy_residual_b10_rel_pos_25:
    dec r15
    js .L__s3_failure_site_225
    mov r12, 0
    mov byte ptr [rbp - 2328], 1
    dec r15
    js .L__s3_failure_site_226
    mov r13, 0
    mov byte ptr [rbp - 2329], 1
    dec r15
    js .L__s3_failure_site_227
    cmp byte ptr [rbp - 2328], 0
    je .L__s3_failure_site_228
    mov rax, r12
    cmp byte ptr [rbp - 2329], 0
    je .L__s3_failure_site_229
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_230
    cmp r10, -1
    jl .L__s3_failure_site_231
    cmp r10, 1
    jg .L__s3_failure_site_231
    mov byte ptr [rbp + rax - 2564], r10b
    mov byte ptr [rbp + rax - 2654], 1
    dec r15
    js .L__s3_failure_site_232
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_26
.L_s3_f21_agent_energy_residual_b11_rel_cont_26:
    dec r15
    js .L__s3_failure_site_233
    mov r12, 0
    mov byte ptr [rbp - 2330], 1
    dec r15
    js .L__s3_failure_site_234
    cmp byte ptr [rbp - 2330], 0
    je .L__s3_failure_site_236
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_237
    cmp byte ptr [rbp + r10 - 2654], 0
    je .L__s3_failure_site_235
    movsx rax, byte ptr [rbp + r10 - 2564]
    mov r12, rax
    mov byte ptr [rbp - 2331], 1
    dec r15
    js .L__s3_failure_site_238
    cmp byte ptr [rbp - 2331], 0
    je .L__s3_failure_site_240
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_27
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_28
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_29
    jmp .L__s3_failure_site_239
.L_s3_f21_agent_energy_residual_b18_switch_negative_27:
    dec r15
    js .L__s3_failure_site_241
    mov r12, 0
    mov byte ptr [rbp - 2332], 1
    dec r15
    js .L__s3_failure_site_242
    cmp byte ptr [rbp - 2332], 0
    je .L__s3_failure_site_244
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_245
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_243
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2333], 1
    dec r15
    js .L__s3_failure_site_246
    mov r13, 0
    mov byte ptr [rbp - 2334], 1
    dec r15
    js .L__s3_failure_site_247
    cmp byte ptr [rbp - 2334], 0
    je .L__s3_failure_site_248
    mov rax, r13
    cmp byte ptr [rbp - 2333], 0
    je .L__s3_failure_site_249
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_250
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_251
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_30
.L_s3_f21_agent_energy_residual_b17_switch_neutral_28:
    dec r15
    js .L__s3_failure_site_252
    mov r12, 1
    mov byte ptr [rbp - 2335], 1
    dec r15
    js .L__s3_failure_site_253
    mov r13, 0
    mov byte ptr [rbp - 2336], 1
    dec r15
    js .L__s3_failure_site_254
    cmp byte ptr [rbp - 2336], 0
    je .L__s3_failure_site_255
    mov rax, r13
    cmp byte ptr [rbp - 2335], 0
    je .L__s3_failure_site_256
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_257
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_258
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_30
.L_s3_f21_agent_energy_residual_b18_switch_positive_29:
    dec r15
    js .L__s3_failure_site_259
    mov r12, 1
    mov byte ptr [rbp - 2337], 1
    dec r15
    js .L__s3_failure_site_260
    mov r13, 0
    mov byte ptr [rbp - 2338], 1
    dec r15
    js .L__s3_failure_site_261
    cmp byte ptr [rbp - 2338], 0
    je .L__s3_failure_site_262
    mov rax, r13
    cmp byte ptr [rbp - 2337], 0
    je .L__s3_failure_site_263
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_264
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_265
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_30
.L_s3_f21_agent_energy_residual_b18_switch_continue_30:
    dec r15
    js .L__s3_failure_site_266
    cmp byte ptr [rbp - 2268], 0
    je .L__s3_failure_site_267
    mov rax, rbx
    mov r12, rax
    mov byte ptr [rbp - 2339], 1
    dec r15
    js .L__s3_failure_site_268
    cmp byte ptr [rbp - 2339], 0
    je .L__s3_failure_site_269
    mov rax, r12
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_270
    mov r10, rdx
    dec r15
    js .L__s3_failure_site_271
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_31
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_33
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_32
.L_s3_f21_agent_energy_residual_b10_rel_neg_31:
    dec r15
    js .L__s3_failure_site_272
    mov r12, 0
    mov byte ptr [rbp - 2341], 1
    dec r15
    js .L__s3_failure_site_273
    mov r13, 0
    mov byte ptr [rbp - 2342], 1
    dec r15
    js .L__s3_failure_site_274
    cmp byte ptr [rbp - 2341], 0
    je .L__s3_failure_site_275
    mov rax, r12
    cmp byte ptr [rbp - 2342], 0
    je .L__s3_failure_site_276
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_277
    cmp r10, -1
    jl .L__s3_failure_site_278
    cmp r10, 1
    jg .L__s3_failure_site_278
    mov byte ptr [rbp + rax - 2565], r10b
    mov byte ptr [rbp + rax - 2655], 1
    dec r15
    js .L__s3_failure_site_279
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_34
.L_s3_f21_agent_energy_residual_b11_rel_zero_32:
    dec r15
    js .L__s3_failure_site_280
    mov r12, 0
    mov byte ptr [rbp - 2343], 1
    dec r15
    js .L__s3_failure_site_281
    mov r13, -1
    mov byte ptr [rbp - 2344], 1
    dec r15
    js .L__s3_failure_site_282
    cmp byte ptr [rbp - 2343], 0
    je .L__s3_failure_site_283
    mov rax, r12
    cmp byte ptr [rbp - 2344], 0
    je .L__s3_failure_site_284
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_285
    cmp r10, -1
    jl .L__s3_failure_site_286
    cmp r10, 1
    jg .L__s3_failure_site_286
    mov byte ptr [rbp + rax - 2565], r10b
    mov byte ptr [rbp + rax - 2655], 1
    dec r15
    js .L__s3_failure_site_287
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_34
.L_s3_f21_agent_energy_residual_b10_rel_pos_33:
    dec r15
    js .L__s3_failure_site_288
    mov r12, 0
    mov byte ptr [rbp - 2345], 1
    dec r15
    js .L__s3_failure_site_289
    mov r13, 0
    mov byte ptr [rbp - 2346], 1
    dec r15
    js .L__s3_failure_site_290
    cmp byte ptr [rbp - 2345], 0
    je .L__s3_failure_site_291
    mov rax, r12
    cmp byte ptr [rbp - 2346], 0
    je .L__s3_failure_site_292
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_293
    cmp r10, -1
    jl .L__s3_failure_site_294
    cmp r10, 1
    jg .L__s3_failure_site_294
    mov byte ptr [rbp + rax - 2565], r10b
    mov byte ptr [rbp + rax - 2655], 1
    dec r15
    js .L__s3_failure_site_295
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_34
.L_s3_f21_agent_energy_residual_b11_rel_cont_34:
    dec r15
    js .L__s3_failure_site_296
    mov r12, 0
    mov byte ptr [rbp - 2347], 1
    dec r15
    js .L__s3_failure_site_297
    cmp byte ptr [rbp - 2347], 0
    je .L__s3_failure_site_299
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_300
    cmp byte ptr [rbp + r10 - 2655], 0
    je .L__s3_failure_site_298
    movsx rax, byte ptr [rbp + r10 - 2565]
    mov r12, rax
    mov byte ptr [rbp - 2348], 1
    dec r15
    js .L__s3_failure_site_301
    cmp byte ptr [rbp - 2348], 0
    je .L__s3_failure_site_303
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_35
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_36
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_37
    jmp .L__s3_failure_site_302
.L_s3_f21_agent_energy_residual_b18_switch_negative_35:
    dec r15
    js .L__s3_failure_site_304
    mov r12, 0
    mov byte ptr [rbp - 2349], 1
    dec r15
    js .L__s3_failure_site_305
    cmp byte ptr [rbp - 2349], 0
    je .L__s3_failure_site_307
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_308
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_306
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2350], 1
    dec r15
    js .L__s3_failure_site_309
    mov r13, 0
    mov byte ptr [rbp - 2351], 1
    dec r15
    js .L__s3_failure_site_310
    cmp byte ptr [rbp - 2351], 0
    je .L__s3_failure_site_311
    mov rax, r13
    cmp byte ptr [rbp - 2350], 0
    je .L__s3_failure_site_312
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_313
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_314
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b17_switch_neutral_36:
    dec r15
    js .L__s3_failure_site_315
    mov r12, 1
    mov byte ptr [rbp - 2352], 1
    dec r15
    js .L__s3_failure_site_316
    mov r13, 0
    mov byte ptr [rbp - 2353], 1
    dec r15
    js .L__s3_failure_site_317
    cmp byte ptr [rbp - 2353], 0
    je .L__s3_failure_site_318
    mov rax, r13
    cmp byte ptr [rbp - 2352], 0
    je .L__s3_failure_site_319
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_320
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_321
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b18_switch_positive_37:
    dec r15
    js .L__s3_failure_site_322
    mov r12, 1
    mov byte ptr [rbp - 2354], 1
    dec r15
    js .L__s3_failure_site_323
    mov r13, 0
    mov byte ptr [rbp - 2355], 1
    dec r15
    js .L__s3_failure_site_324
    cmp byte ptr [rbp - 2355], 0
    je .L__s3_failure_site_325
    mov rax, r13
    cmp byte ptr [rbp - 2354], 0
    je .L__s3_failure_site_326
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_327
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_328
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_39
.L_s3_f21_agent_energy_residual_b18_switch_continue_39:
    dec r15
    js .L__s3_failure_site_329
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_330
    mov rax, rsi
    mov r12, rax
    mov byte ptr [rbp - 2362], 1
    dec r15
    js .L__s3_failure_site_331
    mov r13, 3
    mov byte ptr [rbp - 2363], 1
    dec r15
    js .L__s3_failure_site_332
    cmp byte ptr [rbp - 2362], 0
    je .L__s3_failure_site_333
    mov rax, r12
    cmp byte ptr [rbp - 2363], 0
    je .L__s3_failure_site_334
    mov r10, r13
    dec r15
    js .L__s3_failure_site_335
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_40
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_42
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_41
.L_s3_f21_agent_energy_residual_b10_rel_neg_40:
    dec r15
    js .L__s3_failure_site_336
    mov r12, 0
    mov byte ptr [rbp - 2365], 1
    dec r15
    js .L__s3_failure_site_337
    mov r13, -1
    mov byte ptr [rbp - 2366], 1
    dec r15
    js .L__s3_failure_site_338
    cmp byte ptr [rbp - 2365], 0
    je .L__s3_failure_site_339
    mov rax, r12
    cmp byte ptr [rbp - 2366], 0
    je .L__s3_failure_site_340
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_341
    cmp r10, -1
    jl .L__s3_failure_site_342
    cmp r10, 1
    jg .L__s3_failure_site_342
    mov byte ptr [rbp + rax - 2566], r10b
    mov byte ptr [rbp + rax - 2656], 1
    dec r15
    js .L__s3_failure_site_343
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_43
.L_s3_f21_agent_energy_residual_b11_rel_zero_41:
    dec r15
    js .L__s3_failure_site_344
    mov r12, 0
    mov byte ptr [rbp - 2367], 1
    dec r15
    js .L__s3_failure_site_345
    mov r13, 0
    mov byte ptr [rbp - 2368], 1
    dec r15
    js .L__s3_failure_site_346
    cmp byte ptr [rbp - 2367], 0
    je .L__s3_failure_site_347
    mov rax, r12
    cmp byte ptr [rbp - 2368], 0
    je .L__s3_failure_site_348
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_349
    cmp r10, -1
    jl .L__s3_failure_site_350
    cmp r10, 1
    jg .L__s3_failure_site_350
    mov byte ptr [rbp + rax - 2566], r10b
    mov byte ptr [rbp + rax - 2656], 1
    dec r15
    js .L__s3_failure_site_351
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_43
.L_s3_f21_agent_energy_residual_b10_rel_pos_42:
    dec r15
    js .L__s3_failure_site_352
    mov r12, 0
    mov byte ptr [rbp - 2369], 1
    dec r15
    js .L__s3_failure_site_353
    mov r13, 0
    mov byte ptr [rbp - 2370], 1
    dec r15
    js .L__s3_failure_site_354
    cmp byte ptr [rbp - 2369], 0
    je .L__s3_failure_site_355
    mov rax, r12
    cmp byte ptr [rbp - 2370], 0
    je .L__s3_failure_site_356
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_357
    cmp r10, -1
    jl .L__s3_failure_site_358
    cmp r10, 1
    jg .L__s3_failure_site_358
    mov byte ptr [rbp + rax - 2566], r10b
    mov byte ptr [rbp + rax - 2656], 1
    dec r15
    js .L__s3_failure_site_359
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_43
.L_s3_f21_agent_energy_residual_b11_rel_cont_43:
    dec r15
    js .L__s3_failure_site_360
    mov r12, 0
    mov byte ptr [rbp - 2371], 1
    dec r15
    js .L__s3_failure_site_361
    cmp byte ptr [rbp - 2371], 0
    je .L__s3_failure_site_363
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_364
    cmp byte ptr [rbp + r10 - 2656], 0
    je .L__s3_failure_site_362
    movsx rax, byte ptr [rbp + r10 - 2566]
    mov r12, rax
    mov byte ptr [rbp - 2372], 1
    dec r15
    js .L__s3_failure_site_365
    cmp byte ptr [rbp - 2372], 0
    je .L__s3_failure_site_367
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_44
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_45
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_46
    jmp .L__s3_failure_site_366
.L_s3_f21_agent_energy_residual_b18_switch_negative_44:
    dec r15
    js .L__s3_failure_site_368
    mov r12, 0
    mov byte ptr [rbp - 2373], 1
    dec r15
    js .L__s3_failure_site_369
    cmp byte ptr [rbp - 2373], 0
    je .L__s3_failure_site_371
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_372
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_370
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2374], 1
    dec r15
    js .L__s3_failure_site_373
    mov r13, 0
    mov byte ptr [rbp - 2375], 1
    dec r15
    js .L__s3_failure_site_374
    cmp byte ptr [rbp - 2374], 0
    je .L__s3_failure_site_375
    mov rax, r12
    cmp byte ptr [rbp - 2375], 0
    je .L__s3_failure_site_376
    mov r10, r13
    dec r15
    js .L__s3_failure_site_377
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_47
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_49
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_48
.L_s3_f21_agent_energy_residual_b17_switch_neutral_45:
    dec r15
    js .L__s3_failure_site_378
    mov r12, 0
    mov byte ptr [rbp - 2393], 1
    dec r15
    js .L__s3_failure_site_379
    cmp byte ptr [rbp - 2393], 0
    je .L__s3_failure_site_381
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_382
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_380
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2394], 1
    dec r15
    js .L__s3_failure_site_383
    mov r13, 0
    mov byte ptr [rbp - 2395], 1
    dec r15
    js .L__s3_failure_site_384
    cmp byte ptr [rbp - 2395], 0
    je .L__s3_failure_site_385
    mov rax, r13
    cmp byte ptr [rbp - 2394], 0
    je .L__s3_failure_site_386
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_387
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_388
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b18_switch_positive_46:
    dec r15
    js .L__s3_failure_site_389
    mov r12, 0
    mov byte ptr [rbp - 2396], 1
    dec r15
    js .L__s3_failure_site_390
    cmp byte ptr [rbp - 2396], 0
    je .L__s3_failure_site_392
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_393
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_391
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2397], 1
    dec r15
    js .L__s3_failure_site_394
    mov r13, 0
    mov byte ptr [rbp - 2398], 1
    dec r15
    js .L__s3_failure_site_395
    cmp byte ptr [rbp - 2398], 0
    je .L__s3_failure_site_396
    mov rax, r13
    cmp byte ptr [rbp - 2397], 0
    je .L__s3_failure_site_397
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_398
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_399
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b10_rel_neg_47:
    dec r15
    js .L__s3_failure_site_400
    mov r12, 0
    mov byte ptr [rbp - 2377], 1
    dec r15
    js .L__s3_failure_site_401
    mov r13, 0
    mov byte ptr [rbp - 2378], 1
    dec r15
    js .L__s3_failure_site_402
    cmp byte ptr [rbp - 2377], 0
    je .L__s3_failure_site_403
    mov rax, r12
    cmp byte ptr [rbp - 2378], 0
    je .L__s3_failure_site_404
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_405
    cmp r10, -1
    jl .L__s3_failure_site_406
    cmp r10, 1
    jg .L__s3_failure_site_406
    mov byte ptr [rbp + rax - 2567], r10b
    mov byte ptr [rbp + rax - 2657], 1
    dec r15
    js .L__s3_failure_site_407
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_50
.L_s3_f21_agent_energy_residual_b11_rel_zero_48:
    dec r15
    js .L__s3_failure_site_408
    mov r12, 0
    mov byte ptr [rbp - 2379], 1
    dec r15
    js .L__s3_failure_site_409
    mov r13, -1
    mov byte ptr [rbp - 2380], 1
    dec r15
    js .L__s3_failure_site_410
    cmp byte ptr [rbp - 2379], 0
    je .L__s3_failure_site_411
    mov rax, r12
    cmp byte ptr [rbp - 2380], 0
    je .L__s3_failure_site_412
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_413
    cmp r10, -1
    jl .L__s3_failure_site_414
    cmp r10, 1
    jg .L__s3_failure_site_414
    mov byte ptr [rbp + rax - 2567], r10b
    mov byte ptr [rbp + rax - 2657], 1
    dec r15
    js .L__s3_failure_site_415
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_50
.L_s3_f21_agent_energy_residual_b10_rel_pos_49:
    dec r15
    js .L__s3_failure_site_416
    mov r12, 0
    mov byte ptr [rbp - 2381], 1
    dec r15
    js .L__s3_failure_site_417
    mov r13, 0
    mov byte ptr [rbp - 2382], 1
    dec r15
    js .L__s3_failure_site_418
    cmp byte ptr [rbp - 2381], 0
    je .L__s3_failure_site_419
    mov rax, r12
    cmp byte ptr [rbp - 2382], 0
    je .L__s3_failure_site_420
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_421
    cmp r10, -1
    jl .L__s3_failure_site_422
    cmp r10, 1
    jg .L__s3_failure_site_422
    mov byte ptr [rbp + rax - 2567], r10b
    mov byte ptr [rbp + rax - 2657], 1
    dec r15
    js .L__s3_failure_site_423
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_50
.L_s3_f21_agent_energy_residual_b11_rel_cont_50:
    dec r15
    js .L__s3_failure_site_424
    mov r12, 0
    mov byte ptr [rbp - 2383], 1
    dec r15
    js .L__s3_failure_site_425
    cmp byte ptr [rbp - 2383], 0
    je .L__s3_failure_site_427
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_428
    cmp byte ptr [rbp + r10 - 2657], 0
    je .L__s3_failure_site_426
    movsx rax, byte ptr [rbp + r10 - 2567]
    mov r12, rax
    mov byte ptr [rbp - 2384], 1
    dec r15
    js .L__s3_failure_site_429
    cmp byte ptr [rbp - 2384], 0
    je .L__s3_failure_site_431
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_51
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_52
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_53
    jmp .L__s3_failure_site_430
.L_s3_f21_agent_energy_residual_b18_switch_negative_51:
    dec r15
    js .L__s3_failure_site_432
    mov r12, 2
    mov byte ptr [rbp - 2385], 1
    dec r15
    js .L__s3_failure_site_433
    mov r13, 0
    mov byte ptr [rbp - 2386], 1
    dec r15
    js .L__s3_failure_site_434
    cmp byte ptr [rbp - 2386], 0
    je .L__s3_failure_site_435
    mov rax, r13
    cmp byte ptr [rbp - 2385], 0
    je .L__s3_failure_site_436
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_437
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_438
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b17_switch_neutral_52:
    dec r15
    js .L__s3_failure_site_439
    mov r12, 0
    mov byte ptr [rbp - 2387], 1
    dec r15
    js .L__s3_failure_site_440
    cmp byte ptr [rbp - 2387], 0
    je .L__s3_failure_site_442
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_443
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_441
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2388], 1
    dec r15
    js .L__s3_failure_site_444
    mov r13, 0
    mov byte ptr [rbp - 2389], 1
    dec r15
    js .L__s3_failure_site_445
    cmp byte ptr [rbp - 2389], 0
    je .L__s3_failure_site_446
    mov rax, r13
    cmp byte ptr [rbp - 2388], 0
    je .L__s3_failure_site_447
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_448
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_449
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b18_switch_positive_53:
    dec r15
    js .L__s3_failure_site_450
    mov r12, 0
    mov byte ptr [rbp - 2390], 1
    dec r15
    js .L__s3_failure_site_451
    cmp byte ptr [rbp - 2390], 0
    je .L__s3_failure_site_453
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_454
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_452
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2391], 1
    dec r15
    js .L__s3_failure_site_455
    mov r13, 0
    mov byte ptr [rbp - 2392], 1
    dec r15
    js .L__s3_failure_site_456
    cmp byte ptr [rbp - 2392], 0
    je .L__s3_failure_site_457
    mov rax, r13
    cmp byte ptr [rbp - 2391], 0
    je .L__s3_failure_site_458
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_459
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_460
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_55
.L_s3_f21_agent_energy_residual_b18_switch_continue_55:
    dec r15
    js .L__s3_failure_site_461
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_462
    mov rax, rsi
    mov r12, rax
    mov byte ptr [rbp - 2399], 1
    dec r15
    js .L__s3_failure_site_463
    mov r13, 3
    mov byte ptr [rbp - 2400], 1
    dec r15
    js .L__s3_failure_site_464
    cmp byte ptr [rbp - 2399], 0
    je .L__s3_failure_site_465
    mov rax, r12
    cmp byte ptr [rbp - 2400], 0
    je .L__s3_failure_site_466
    mov r10, r13
    dec r15
    js .L__s3_failure_site_467
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_56
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_58
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_57
.L_s3_f21_agent_energy_residual_b10_rel_neg_56:
    dec r15
    js .L__s3_failure_site_468
    mov r12, 0
    mov byte ptr [rbp - 2402], 1
    dec r15
    js .L__s3_failure_site_469
    mov r13, 0
    mov byte ptr [rbp - 2403], 1
    dec r15
    js .L__s3_failure_site_470
    cmp byte ptr [rbp - 2402], 0
    je .L__s3_failure_site_471
    mov rax, r12
    cmp byte ptr [rbp - 2403], 0
    je .L__s3_failure_site_472
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_473
    cmp r10, -1
    jl .L__s3_failure_site_474
    cmp r10, 1
    jg .L__s3_failure_site_474
    mov byte ptr [rbp + rax - 2568], r10b
    mov byte ptr [rbp + rax - 2658], 1
    dec r15
    js .L__s3_failure_site_475
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_59
.L_s3_f21_agent_energy_residual_b11_rel_zero_57:
    dec r15
    js .L__s3_failure_site_476
    mov r12, 0
    mov byte ptr [rbp - 2404], 1
    dec r15
    js .L__s3_failure_site_477
    mov r13, 0
    mov byte ptr [rbp - 2405], 1
    dec r15
    js .L__s3_failure_site_478
    cmp byte ptr [rbp - 2404], 0
    je .L__s3_failure_site_479
    mov rax, r12
    cmp byte ptr [rbp - 2405], 0
    je .L__s3_failure_site_480
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_481
    cmp r10, -1
    jl .L__s3_failure_site_482
    cmp r10, 1
    jg .L__s3_failure_site_482
    mov byte ptr [rbp + rax - 2568], r10b
    mov byte ptr [rbp + rax - 2658], 1
    dec r15
    js .L__s3_failure_site_483
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_59
.L_s3_f21_agent_energy_residual_b10_rel_pos_58:
    dec r15
    js .L__s3_failure_site_484
    mov r12, 0
    mov byte ptr [rbp - 2406], 1
    dec r15
    js .L__s3_failure_site_485
    mov r13, -1
    mov byte ptr [rbp - 2407], 1
    dec r15
    js .L__s3_failure_site_486
    cmp byte ptr [rbp - 2406], 0
    je .L__s3_failure_site_487
    mov rax, r12
    cmp byte ptr [rbp - 2407], 0
    je .L__s3_failure_site_488
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_489
    cmp r10, -1
    jl .L__s3_failure_site_490
    cmp r10, 1
    jg .L__s3_failure_site_490
    mov byte ptr [rbp + rax - 2568], r10b
    mov byte ptr [rbp + rax - 2658], 1
    dec r15
    js .L__s3_failure_site_491
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_59
.L_s3_f21_agent_energy_residual_b11_rel_cont_59:
    dec r15
    js .L__s3_failure_site_492
    mov r12, 0
    mov byte ptr [rbp - 2408], 1
    dec r15
    js .L__s3_failure_site_493
    cmp byte ptr [rbp - 2408], 0
    je .L__s3_failure_site_495
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_496
    cmp byte ptr [rbp + r10 - 2658], 0
    je .L__s3_failure_site_494
    movsx rax, byte ptr [rbp + r10 - 2568]
    mov r12, rax
    mov byte ptr [rbp - 2409], 1
    dec r15
    js .L__s3_failure_site_497
    cmp byte ptr [rbp - 2409], 0
    je .L__s3_failure_site_499
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_60
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_61
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_62
    jmp .L__s3_failure_site_498
.L_s3_f21_agent_energy_residual_b18_switch_negative_60:
    dec r15
    js .L__s3_failure_site_500
    mov r12, 1
    mov byte ptr [rbp - 2410], 1
    dec r15
    js .L__s3_failure_site_501
    mov r13, 0
    mov byte ptr [rbp - 2411], 1
    dec r15
    js .L__s3_failure_site_502
    cmp byte ptr [rbp - 2411], 0
    je .L__s3_failure_site_503
    mov rax, r13
    cmp byte ptr [rbp - 2410], 0
    je .L__s3_failure_site_504
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_505
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_506
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_63
.L_s3_f21_agent_energy_residual_b17_switch_neutral_61:
    dec r15
    js .L__s3_failure_site_507
    mov r12, 0
    mov byte ptr [rbp - 2412], 1
    dec r15
    js .L__s3_failure_site_508
    cmp byte ptr [rbp - 2412], 0
    je .L__s3_failure_site_510
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_511
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_509
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2413], 1
    dec r15
    js .L__s3_failure_site_512
    mov r13, 0
    mov byte ptr [rbp - 2414], 1
    dec r15
    js .L__s3_failure_site_513
    cmp byte ptr [rbp - 2414], 0
    je .L__s3_failure_site_514
    mov rax, r13
    cmp byte ptr [rbp - 2413], 0
    je .L__s3_failure_site_515
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_516
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_517
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_63
.L_s3_f21_agent_energy_residual_b18_switch_positive_62:
    dec r15
    js .L__s3_failure_site_518
    mov r12, 0
    mov byte ptr [rbp - 2415], 1
    dec r15
    js .L__s3_failure_site_519
    cmp byte ptr [rbp - 2415], 0
    je .L__s3_failure_site_521
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_522
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_520
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2416], 1
    dec r15
    js .L__s3_failure_site_523
    mov r13, 0
    mov byte ptr [rbp - 2417], 1
    dec r15
    js .L__s3_failure_site_524
    cmp byte ptr [rbp - 2417], 0
    je .L__s3_failure_site_525
    mov rax, r13
    cmp byte ptr [rbp - 2416], 0
    je .L__s3_failure_site_526
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_527
    mov qword ptr [rbp + rax*8 - 2560], r10
    mov byte ptr [rbp + rax - 2650], 1
    dec r15
    js .L__s3_failure_site_528
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_63
.L_s3_f21_agent_energy_residual_b18_switch_continue_63:
    dec r15
    js .L__s3_failure_site_529
    mov r12, 0
    mov byte ptr [rbp - 2418], 1
    dec r15
    js .L__s3_failure_site_530
    cmp byte ptr [rbp - 2418], 0
    je .L__s3_failure_site_532
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_533
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_531
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov r12, rax
    mov byte ptr [rbp - 2419], 1
    dec r15
    js .L__s3_failure_site_534
    mov r13, 0
    mov byte ptr [rbp - 2420], 1
    dec r15
    js .L__s3_failure_site_535
    cmp byte ptr [rbp - 2419], 0
    je .L__s3_failure_site_536
    mov rax, r12
    cmp byte ptr [rbp - 2420], 0
    je .L__s3_failure_site_537
    mov r10, r13
    dec r15
    js .L__s3_failure_site_538
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_64
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_66
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_65
.L_s3_f21_agent_energy_residual_b10_rel_neg_64:
    dec r15
    js .L__s3_failure_site_539
    mov r12, 0
    mov byte ptr [rbp - 2422], 1
    dec r15
    js .L__s3_failure_site_540
    mov r13, 0
    mov byte ptr [rbp - 2423], 1
    dec r15
    js .L__s3_failure_site_541
    cmp byte ptr [rbp - 2422], 0
    je .L__s3_failure_site_542
    mov rax, r12
    cmp byte ptr [rbp - 2423], 0
    je .L__s3_failure_site_543
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_544
    cmp r10, -1
    jl .L__s3_failure_site_545
    cmp r10, 1
    jg .L__s3_failure_site_545
    mov byte ptr [rbp + rax - 2569], r10b
    mov byte ptr [rbp + rax - 2659], 1
    dec r15
    js .L__s3_failure_site_546
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_67
.L_s3_f21_agent_energy_residual_b11_rel_zero_65:
    dec r15
    js .L__s3_failure_site_547
    mov r12, 0
    mov byte ptr [rbp - 2424], 1
    dec r15
    js .L__s3_failure_site_548
    mov r13, -1
    mov byte ptr [rbp - 2425], 1
    dec r15
    js .L__s3_failure_site_549
    cmp byte ptr [rbp - 2424], 0
    je .L__s3_failure_site_550
    mov rax, r12
    cmp byte ptr [rbp - 2425], 0
    je .L__s3_failure_site_551
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_552
    cmp r10, -1
    jl .L__s3_failure_site_553
    cmp r10, 1
    jg .L__s3_failure_site_553
    mov byte ptr [rbp + rax - 2569], r10b
    mov byte ptr [rbp + rax - 2659], 1
    dec r15
    js .L__s3_failure_site_554
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_67
.L_s3_f21_agent_energy_residual_b10_rel_pos_66:
    dec r15
    js .L__s3_failure_site_555
    mov r12, 0
    mov byte ptr [rbp - 2426], 1
    dec r15
    js .L__s3_failure_site_556
    mov r13, 0
    mov byte ptr [rbp - 2427], 1
    dec r15
    js .L__s3_failure_site_557
    cmp byte ptr [rbp - 2426], 0
    je .L__s3_failure_site_558
    mov rax, r12
    cmp byte ptr [rbp - 2427], 0
    je .L__s3_failure_site_559
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_560
    cmp r10, -1
    jl .L__s3_failure_site_561
    cmp r10, 1
    jg .L__s3_failure_site_561
    mov byte ptr [rbp + rax - 2569], r10b
    mov byte ptr [rbp + rax - 2659], 1
    dec r15
    js .L__s3_failure_site_562
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_67
.L_s3_f21_agent_energy_residual_b11_rel_cont_67:
    dec r15
    js .L__s3_failure_site_563
    mov r12, 0
    mov byte ptr [rbp - 2428], 1
    dec r15
    js .L__s3_failure_site_564
    cmp byte ptr [rbp - 2428], 0
    je .L__s3_failure_site_566
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_567
    cmp byte ptr [rbp + r10 - 2659], 0
    je .L__s3_failure_site_565
    movsx rax, byte ptr [rbp + r10 - 2569]
    mov r12, rax
    mov byte ptr [rbp - 2429], 1
    dec r15
    js .L__s3_failure_site_568
    cmp byte ptr [rbp - 2429], 0
    je .L__s3_failure_site_570
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_68
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_69
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_70
    jmp .L__s3_failure_site_569
.L_s3_f21_agent_energy_residual_b18_switch_negative_68:
    dec r15
    js .L__s3_failure_site_571
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2430], 1
    dec r15
    js .L__s3_failure_site_572
    mov r13, 0
    mov byte ptr [rbp - 2431], 1
    dec r15
    js .L__s3_failure_site_573
    cmp byte ptr [rbp - 2431], 0
    je .L__s3_failure_site_574
    mov rax, r13
    cmp byte ptr [rbp - 2430], 0
    je .L__s3_failure_site_575
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_576
    mov qword ptr [rbp + rax*8 - 2584], r10
    mov byte ptr [rbp + rax - 2660], 1
    dec r15
    js .L__s3_failure_site_577
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2432], 1
    dec r15
    js .L__s3_failure_site_578
    mov r13, 0
    mov byte ptr [rbp - 2433], 1
    dec r15
    js .L__s3_failure_site_579
    cmp byte ptr [rbp - 2433], 0
    je .L__s3_failure_site_580
    mov rax, r13
    cmp byte ptr [rbp - 2432], 0
    je .L__s3_failure_site_581
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_582
    mov qword ptr [rbp + rax*8 - 2592], r10
    mov byte ptr [rbp + rax - 2661], 1
    dec r15
    js .L__s3_failure_site_583
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2434], 1
    dec r15
    js .L__s3_failure_site_584
    mov r13, 0
    mov byte ptr [rbp - 2435], 1
    dec r15
    js .L__s3_failure_site_585
    cmp byte ptr [rbp - 2435], 0
    je .L__s3_failure_site_586
    mov rax, r13
    cmp byte ptr [rbp - 2434], 0
    je .L__s3_failure_site_587
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_588
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    dec r15
    js .L__s3_failure_site_589
    mov r12, 0
    mov byte ptr [rbp - 2436], 1
    dec r15
    js .L__s3_failure_site_590
    mov r13, 0
    mov byte ptr [rbp - 2437], 1
    dec r15
    js .L__s3_failure_site_591
    cmp byte ptr [rbp - 2437], 0
    je .L__s3_failure_site_592
    mov rax, r13
    cmp byte ptr [rbp - 2436], 0
    je .L__s3_failure_site_593
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_594
    mov qword ptr [rbp + rax*8 - 2608], r10
    mov byte ptr [rbp + rax - 2663], 1
    dec r15
    js .L__s3_failure_site_595
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_71
.L_s3_f21_agent_energy_residual_b17_switch_neutral_69:
    dec r15
    js .L__s3_failure_site_596
    mov rdi, 0
    mov byte ptr [rbp - 2544], 1
    dec r15
    js .L__s3_failure_site_597
    cmp byte ptr [rbp - 2544], 0
    je .L__s3_failure_site_599
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_600
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_598
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov rdi, rax
    mov byte ptr [rbp - 2545], 1
    dec r15
    js .L__s3_failure_site_601
    cmp byte ptr [rbp - 2545], 0
    je .L__s3_failure_site_602
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2680]
    mov r12, qword ptr [rbp - 2688]
    mov r13, qword ptr [rbp - 2696]
    mov r15, qword ptr [rbp - 2704]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f21_agent_energy_residual_b18_switch_positive_70:
    dec r15
    js .L__s3_failure_site_603
    mov rdi, 0
    mov byte ptr [rbp - 2546], 1
    dec r15
    js .L__s3_failure_site_604
    cmp byte ptr [rbp - 2546], 0
    je .L__s3_failure_site_606
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_607
    cmp byte ptr [rbp + r10 - 2650], 0
    je .L__s3_failure_site_605
    mov rax, qword ptr [rbp + r10*8 - 2560]
    mov rdi, rax
    mov byte ptr [rbp - 2547], 1
    dec r15
    js .L__s3_failure_site_608
    cmp byte ptr [rbp - 2547], 0
    je .L__s3_failure_site_609
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2680]
    mov r12, qword ptr [rbp - 2688]
    mov r13, qword ptr [rbp - 2696]
    mov r15, qword ptr [rbp - 2704]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f21_agent_energy_residual_b18_while_condition_71:
    dec r15
    js .L__s3_failure_site_610
    mov r12, 0
    mov byte ptr [rbp - 2438], 1
    dec r15
    js .L__s3_failure_site_611
    cmp byte ptr [rbp - 2438], 0
    je .L__s3_failure_site_613
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_614
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_612
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r12, rax
    mov byte ptr [rbp - 2439], 1
    dec r15
    js .L__s3_failure_site_615
    cmp byte ptr [rbp - 2439], 0
    je .L__s3_failure_site_616
    mov rax, r12
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_617
    mov r10, rdx
    dec r15
    js .L__s3_failure_site_618
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_76
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_78
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_77
.L_s3_f21_agent_energy_residual_b13_while_body_72:
    dec r15
    js .L__s3_failure_site_619
    mov r12, 0
    mov byte ptr [rbp - 2449], 1
    dec r15
    js .L__s3_failure_site_620
    cmp byte ptr [rbp - 2449], 0
    je .L__s3_failure_site_622
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_623
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_621
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r12, rax
    mov byte ptr [rbp - 2450], 1
    dec r15
    js .L__s3_failure_site_624
    cmp byte ptr [rbp - 2265], 0
    je .L__s3_failure_site_626
    mov r10, rcx
    cmp byte ptr [rbp - 2266], 0
    je .L__s3_failure_site_627
    mov r11, r8
    cmp byte ptr [rbp - 2450], 0
    je .L__s3_failure_site_628
    mov rax, r12
    cmp rax, r11
    jae .L__s3_failure_site_625
    mov r11, qword ptr [r10 + rax * 8]
    mov r12, r11
    mov byte ptr [rbp - 2451], 1
    dec r15
    js .L__s3_failure_site_629
    mov r13, 0
    mov byte ptr [rbp - 2452], 1
    dec r15
    js .L__s3_failure_site_630
    cmp byte ptr [rbp - 2452], 0
    je .L__s3_failure_site_632
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_633
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_631
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r13, rax
    mov byte ptr [rbp - 2453], 1
    dec r15
    js .L__s3_failure_site_634
    cmp byte ptr [rbp - 2267], 0
    je .L__s3_failure_site_636
    mov r10, r9
    cmp byte ptr [rbp - 2268], 0
    je .L__s3_failure_site_637
    mov r11, rbx
    cmp byte ptr [rbp - 2453], 0
    je .L__s3_failure_site_638
    mov rax, r13
    cmp rax, r11
    jae .L__s3_failure_site_635
    mov r11, qword ptr [r10 + rax * 8]
    mov r13, r11
    mov byte ptr [rbp - 2454], 1
    dec r15
    js .L__s3_failure_site_639
    cmp byte ptr [rbp - 2451], 0
    je .L__s3_failure_site_640
    mov rax, r12
    cmp byte ptr [rbp - 2454], 0
    je .L__s3_failure_site_641
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2455], 1
    dec r15
    js .L__s3_failure_site_642
    mov r13, 0
    mov byte ptr [rbp - 2456], 1
    dec r15
    js .L__s3_failure_site_643
    cmp byte ptr [rbp - 2456], 0
    je .L__s3_failure_site_644
    mov rax, r13
    cmp byte ptr [rbp - 2455], 0
    je .L__s3_failure_site_645
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_646
    mov qword ptr [rbp + rax*8 - 2624], r10
    mov byte ptr [rbp + rax - 2665], 1
    dec r15
    js .L__s3_failure_site_647
    mov r12, 0
    mov byte ptr [rbp - 2457], 1
    dec r15
    js .L__s3_failure_site_648
    cmp byte ptr [rbp - 2457], 0
    je .L__s3_failure_site_650
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_651
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_649
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2458], 1
    dec r15
    js .L__s3_failure_site_652
    mov r13, 0
    mov byte ptr [rbp - 2459], 1
    dec r15
    js .L__s3_failure_site_653
    cmp byte ptr [rbp - 2459], 0
    je .L__s3_failure_site_654
    mov rax, r13
    cmp byte ptr [rbp - 2458], 0
    je .L__s3_failure_site_655
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_656
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    dec r15
    js .L__s3_failure_site_657
    mov r12, 0
    mov byte ptr [rbp - 2460], 1
    dec r15
    js .L__s3_failure_site_658
    cmp byte ptr [rbp - 2460], 0
    je .L__s3_failure_site_660
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_661
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_659
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2461], 1
    dec r15
    js .L__s3_failure_site_662
    movabs rax, 0
    mov r13, rax
    mov byte ptr [rbp - 2462], 1
    dec r15
    js .L__s3_failure_site_663
    cmp byte ptr [rbp - 2461], 0
    je .L__s3_failure_site_664
    mov rax, r12
    cmp byte ptr [rbp - 2462], 0
    je .L__s3_failure_site_665
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
    dec r15
    js .L__s3_failure_site_666
    cmp byte ptr [rbp - 2463], 0
    je .L__s3_failure_site_668
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_80
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_81
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_82
    jmp .L__s3_failure_site_667
.L_s3_f21_agent_energy_residual_b15_while_exit_0_73:
    dec r15
    js .L__s3_failure_site_669
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_75
.L_s3_f21_agent_energy_residual_b15_while_exit_1_74:
    dec r15
    js .L__s3_failure_site_670
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_75
.L_s3_f21_agent_energy_residual_b13_while_exit_75:
    dec r15
    js .L__s3_failure_site_671
    movabs rax, 0
    mov rcx, rax
    mov byte ptr [rbp - 2506], 1
    dec r15
    js .L__s3_failure_site_672
    mov r8, 0
    mov byte ptr [rbp - 2507], 1
    dec r15
    js .L__s3_failure_site_673
    cmp byte ptr [rbp - 2507], 0
    je .L__s3_failure_site_674
    mov rax, r8
    cmp byte ptr [rbp - 2506], 0
    je .L__s3_failure_site_675
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_676
    mov qword ptr [rbp + rax*8 - 2640], r10
    mov byte ptr [rbp + rax - 2667], 1
    dec r15
    js .L__s3_failure_site_677
    mov rcx, 0
    mov byte ptr [rbp - 2508], 1
    dec r15
    js .L__s3_failure_site_678
    mov r8, 0
    mov byte ptr [rbp - 2509], 1
    dec r15
    js .L__s3_failure_site_679
    cmp byte ptr [rbp - 2509], 0
    je .L__s3_failure_site_680
    mov rax, r8
    cmp byte ptr [rbp - 2508], 0
    je .L__s3_failure_site_681
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_682
    mov qword ptr [rbp + rax*8 - 2648], r10
    mov byte ptr [rbp + rax - 2668], 1
    dec r15
    js .L__s3_failure_site_683
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_88
.L_s3_f21_agent_energy_residual_b10_rel_neg_76:
    dec r15
    js .L__s3_failure_site_684
    mov r12, 0
    mov byte ptr [rbp - 2441], 1
    dec r15
    js .L__s3_failure_site_685
    mov r13, -1
    mov byte ptr [rbp - 2442], 1
    dec r15
    js .L__s3_failure_site_686
    cmp byte ptr [rbp - 2441], 0
    je .L__s3_failure_site_687
    mov rax, r12
    cmp byte ptr [rbp - 2442], 0
    je .L__s3_failure_site_688
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_689
    cmp r10, -1
    jl .L__s3_failure_site_690
    cmp r10, 1
    jg .L__s3_failure_site_690
    mov byte ptr [rbp + rax - 2609], r10b
    mov byte ptr [rbp + rax - 2664], 1
    dec r15
    js .L__s3_failure_site_691
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_79
.L_s3_f21_agent_energy_residual_b11_rel_zero_77:
    dec r15
    js .L__s3_failure_site_692
    mov r12, 0
    mov byte ptr [rbp - 2443], 1
    dec r15
    js .L__s3_failure_site_693
    mov r13, 0
    mov byte ptr [rbp - 2444], 1
    dec r15
    js .L__s3_failure_site_694
    cmp byte ptr [rbp - 2443], 0
    je .L__s3_failure_site_695
    mov rax, r12
    cmp byte ptr [rbp - 2444], 0
    je .L__s3_failure_site_696
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_697
    cmp r10, -1
    jl .L__s3_failure_site_698
    cmp r10, 1
    jg .L__s3_failure_site_698
    mov byte ptr [rbp + rax - 2609], r10b
    mov byte ptr [rbp + rax - 2664], 1
    dec r15
    js .L__s3_failure_site_699
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_79
.L_s3_f21_agent_energy_residual_b10_rel_pos_78:
    dec r15
    js .L__s3_failure_site_700
    mov r12, 0
    mov byte ptr [rbp - 2445], 1
    dec r15
    js .L__s3_failure_site_701
    mov r13, 0
    mov byte ptr [rbp - 2446], 1
    dec r15
    js .L__s3_failure_site_702
    cmp byte ptr [rbp - 2445], 0
    je .L__s3_failure_site_703
    mov rax, r12
    cmp byte ptr [rbp - 2446], 0
    je .L__s3_failure_site_704
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_705
    cmp r10, -1
    jl .L__s3_failure_site_706
    cmp r10, 1
    jg .L__s3_failure_site_706
    mov byte ptr [rbp + rax - 2609], r10b
    mov byte ptr [rbp + rax - 2664], 1
    dec r15
    js .L__s3_failure_site_707
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_79
.L_s3_f21_agent_energy_residual_b11_rel_cont_79:
    dec r15
    js .L__s3_failure_site_708
    mov r12, 0
    mov byte ptr [rbp - 2447], 1
    dec r15
    js .L__s3_failure_site_709
    cmp byte ptr [rbp - 2447], 0
    je .L__s3_failure_site_711
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_712
    cmp byte ptr [rbp + r10 - 2664], 0
    je .L__s3_failure_site_710
    movsx rax, byte ptr [rbp + r10 - 2609]
    mov r12, rax
    mov byte ptr [rbp - 2448], 1
    dec r15
    js .L__s3_failure_site_713
    cmp byte ptr [rbp - 2448], 0
    je .L__s3_failure_site_715
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b13_while_body_72
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b15_while_exit_0_73
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b15_while_exit_1_74
    jmp .L__s3_failure_site_714
.L_s3_f21_agent_energy_residual_b18_switch_negative_80:
    dec r15
    js .L__s3_failure_site_716
    movabs rax, 0
    mov r12, rax
    mov byte ptr [rbp - 2464], 1
    dec r15
    js .L__s3_failure_site_717
    mov r13, 0
    mov byte ptr [rbp - 2465], 1
    dec r15
    js .L__s3_failure_site_718
    cmp byte ptr [rbp - 2465], 0
    je .L__s3_failure_site_720
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_721
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_719
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r13, rax
    mov byte ptr [rbp - 2466], 1
    dec r15
    js .L__s3_failure_site_722
    cmp byte ptr [rbp - 2464], 0
    je .L__s3_failure_site_723
    mov rax, r12
    cmp byte ptr [rbp - 2466], 0
    je .L__s3_failure_site_724
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2467], 1
    dec r15
    js .L__s3_failure_site_725
    mov r13, 0
    mov byte ptr [rbp - 2468], 1
    dec r15
    js .L__s3_failure_site_726
    cmp byte ptr [rbp - 2468], 0
    je .L__s3_failure_site_727
    mov rax, r13
    cmp byte ptr [rbp - 2467], 0
    je .L__s3_failure_site_728
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_729
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    dec r15
    js .L__s3_failure_site_730
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_83
.L_s3_f21_agent_energy_residual_b17_switch_neutral_81:
    dec r15
    js .L__s3_failure_site_731
    mov r12, 0
    mov byte ptr [rbp - 2469], 1
    dec r15
    js .L__s3_failure_site_732
    cmp byte ptr [rbp - 2469], 0
    je .L__s3_failure_site_734
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_735
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_733
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2470], 1
    dec r15
    js .L__s3_failure_site_736
    mov r13, 0
    mov byte ptr [rbp - 2471], 1
    dec r15
    js .L__s3_failure_site_737
    cmp byte ptr [rbp - 2471], 0
    je .L__s3_failure_site_738
    mov rax, r13
    cmp byte ptr [rbp - 2470], 0
    je .L__s3_failure_site_739
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_740
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    dec r15
    js .L__s3_failure_site_741
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_83
.L_s3_f21_agent_energy_residual_b18_switch_positive_82:
    dec r15
    js .L__s3_failure_site_742
    mov r12, 0
    mov byte ptr [rbp - 2472], 1
    dec r15
    js .L__s3_failure_site_743
    cmp byte ptr [rbp - 2472], 0
    je .L__s3_failure_site_745
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_746
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_744
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r12, rax
    mov byte ptr [rbp - 2473], 1
    dec r15
    js .L__s3_failure_site_747
    mov r13, 0
    mov byte ptr [rbp - 2474], 1
    dec r15
    js .L__s3_failure_site_748
    cmp byte ptr [rbp - 2474], 0
    je .L__s3_failure_site_749
    mov rax, r13
    cmp byte ptr [rbp - 2473], 0
    je .L__s3_failure_site_750
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_751
    mov qword ptr [rbp + rax*8 - 2632], r10
    mov byte ptr [rbp + rax - 2666], 1
    dec r15
    js .L__s3_failure_site_752
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_83
.L_s3_f21_agent_energy_residual_b18_switch_continue_83:
    dec r15
    js .L__s3_failure_site_753
    mov r12, 0
    mov byte ptr [rbp - 2475], 1
    dec r15
    js .L__s3_failure_site_754
    cmp byte ptr [rbp - 2475], 0
    je .L__s3_failure_site_756
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_757
    cmp byte ptr [rbp + r10 - 2660], 0
    je .L__s3_failure_site_755
    mov rax, qword ptr [rbp + r10*8 - 2584]
    mov r12, rax
    mov byte ptr [rbp - 2476], 1
    dec r15
    js .L__s3_failure_site_758
    mov r13, 0
    mov byte ptr [rbp - 2477], 1
    dec r15
    js .L__s3_failure_site_759
    cmp byte ptr [rbp - 2477], 0
    je .L__s3_failure_site_761
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_762
    cmp byte ptr [rbp + r10 - 2665], 0
    je .L__s3_failure_site_760
    mov rax, qword ptr [rbp + r10*8 - 2624]
    mov r13, rax
    mov byte ptr [rbp - 2478], 1
    dec r15
    js .L__s3_failure_site_763
    cmp byte ptr [rbp - 2476], 0
    je .L__s3_failure_site_764
    mov rax, r12
    cmp byte ptr [rbp - 2478], 0
    je .L__s3_failure_site_765
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2479], 1
    dec r15
    js .L__s3_failure_site_766
    mov r13, 0
    mov byte ptr [rbp - 2480], 1
    dec r15
    js .L__s3_failure_site_767
    cmp byte ptr [rbp - 2480], 0
    je .L__s3_failure_site_768
    mov rax, r13
    cmp byte ptr [rbp - 2479], 0
    je .L__s3_failure_site_769
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_770
    mov qword ptr [rbp + rax*8 - 2584], r10
    mov byte ptr [rbp + rax - 2660], 1
    dec r15
    js .L__s3_failure_site_771
    mov r12, 0
    mov byte ptr [rbp - 2481], 1
    dec r15
    js .L__s3_failure_site_772
    cmp byte ptr [rbp - 2481], 0
    je .L__s3_failure_site_774
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_775
    cmp byte ptr [rbp + r10 - 2661], 0
    je .L__s3_failure_site_773
    mov rax, qword ptr [rbp + r10*8 - 2592]
    mov r12, rax
    mov byte ptr [rbp - 2482], 1
    dec r15
    js .L__s3_failure_site_776
    mov r13, 0
    mov byte ptr [rbp - 2483], 1
    dec r15
    js .L__s3_failure_site_777
    cmp byte ptr [rbp - 2483], 0
    je .L__s3_failure_site_779
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_780
    cmp byte ptr [rbp + r10 - 2666], 0
    je .L__s3_failure_site_778
    mov rax, qword ptr [rbp + r10*8 - 2632]
    mov r13, rax
    mov byte ptr [rbp - 2484], 1
    dec r15
    js .L__s3_failure_site_781
    cmp byte ptr [rbp - 2482], 0
    je .L__s3_failure_site_782
    mov rax, r12
    cmp byte ptr [rbp - 2484], 0
    je .L__s3_failure_site_783
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov r12, rax
    mov byte ptr [rbp - 2485], 1
    dec r15
    js .L__s3_failure_site_784
    mov r13, 0
    mov byte ptr [rbp - 2486], 1
    dec r15
    js .L__s3_failure_site_785
    cmp byte ptr [rbp - 2486], 0
    je .L__s3_failure_site_786
    mov rax, r13
    cmp byte ptr [rbp - 2485], 0
    je .L__s3_failure_site_787
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_788
    mov qword ptr [rbp + rax*8 - 2592], r10
    mov byte ptr [rbp + rax - 2661], 1
    dec r15
    js .L__s3_failure_site_789
    mov r12, 0
    mov byte ptr [rbp - 2487], 1
    dec r15
    js .L__s3_failure_site_790
    cmp byte ptr [rbp - 2487], 0
    je .L__s3_failure_site_792
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_793
    cmp byte ptr [rbp + r10 - 2666], 0
    je .L__s3_failure_site_791
    mov rax, qword ptr [rbp + r10*8 - 2632]
    mov r12, rax
    mov byte ptr [rbp - 2488], 1
    dec r15
    js .L__s3_failure_site_794
    mov r13, 0
    mov byte ptr [rbp - 2489], 1
    dec r15
    js .L__s3_failure_site_795
    cmp byte ptr [rbp - 2489], 0
    je .L__s3_failure_site_797
    mov r10, r13
    cmp r10, 1
    jae .L__s3_failure_site_798
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_796
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov r13, rax
    mov byte ptr [rbp - 2490], 1
    dec r15
    js .L__s3_failure_site_799
    cmp byte ptr [rbp - 2488], 0
    je .L__s3_failure_site_800
    mov rax, r12
    cmp byte ptr [rbp - 2490], 0
    je .L__s3_failure_site_801
    mov r10, r13
    movq xmm0, rax
    movq xmm1, r10
    ucomisd xmm0, xmm1
    seta al
    movzx r11, al
    neg r11
    mov r12, r11
    mov byte ptr [rbp - 2491], 1
    dec r15
    js .L__s3_failure_site_802
    cmp byte ptr [rbp - 2491], 0
    je .L__s3_failure_site_804
    mov rax, r12
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b18_switch_negative_84
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b17_switch_neutral_85
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b18_switch_positive_86
    jmp .L__s3_failure_site_803
.L_s3_f21_agent_energy_residual_b18_switch_negative_84:
    dec r15
    js .L__s3_failure_site_805
    mov r12, 0
    mov byte ptr [rbp - 2492], 1
    dec r15
    js .L__s3_failure_site_806
    cmp byte ptr [rbp - 2492], 0
    je .L__s3_failure_site_808
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_809
    cmp byte ptr [rbp + r10 - 2666], 0
    je .L__s3_failure_site_807
    mov rax, qword ptr [rbp + r10*8 - 2632]
    mov r12, rax
    mov byte ptr [rbp - 2493], 1
    dec r15
    js .L__s3_failure_site_810
    mov r13, 0
    mov byte ptr [rbp - 2494], 1
    dec r15
    js .L__s3_failure_site_811
    cmp byte ptr [rbp - 2494], 0
    je .L__s3_failure_site_812
    mov rax, r13
    cmp byte ptr [rbp - 2493], 0
    je .L__s3_failure_site_813
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_814
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    dec r15
    js .L__s3_failure_site_815
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_87
.L_s3_f21_agent_energy_residual_b17_switch_neutral_85:
    dec r15
    js .L__s3_failure_site_816
    mov r12, 0
    mov byte ptr [rbp - 2495], 1
    dec r15
    js .L__s3_failure_site_817
    cmp byte ptr [rbp - 2495], 0
    je .L__s3_failure_site_819
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_820
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_818
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov r12, rax
    mov byte ptr [rbp - 2496], 1
    dec r15
    js .L__s3_failure_site_821
    mov r13, 0
    mov byte ptr [rbp - 2497], 1
    dec r15
    js .L__s3_failure_site_822
    cmp byte ptr [rbp - 2497], 0
    je .L__s3_failure_site_823
    mov rax, r13
    cmp byte ptr [rbp - 2496], 0
    je .L__s3_failure_site_824
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_825
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    dec r15
    js .L__s3_failure_site_826
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_87
.L_s3_f21_agent_energy_residual_b18_switch_positive_86:
    dec r15
    js .L__s3_failure_site_827
    mov r12, 0
    mov byte ptr [rbp - 2498], 1
    dec r15
    js .L__s3_failure_site_828
    cmp byte ptr [rbp - 2498], 0
    je .L__s3_failure_site_830
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_831
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_829
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov r12, rax
    mov byte ptr [rbp - 2499], 1
    dec r15
    js .L__s3_failure_site_832
    mov r13, 0
    mov byte ptr [rbp - 2500], 1
    dec r15
    js .L__s3_failure_site_833
    cmp byte ptr [rbp - 2500], 0
    je .L__s3_failure_site_834
    mov rax, r13
    cmp byte ptr [rbp - 2499], 0
    je .L__s3_failure_site_835
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_836
    mov qword ptr [rbp + rax*8 - 2600], r10
    mov byte ptr [rbp + rax - 2662], 1
    dec r15
    js .L__s3_failure_site_837
    jmp .L_s3_f21_agent_energy_residual_b18_switch_continue_87
.L_s3_f21_agent_energy_residual_b18_switch_continue_87:
    dec r15
    js .L__s3_failure_site_838
    mov r12, 0
    mov byte ptr [rbp - 2501], 1
    dec r15
    js .L__s3_failure_site_839
    cmp byte ptr [rbp - 2501], 0
    je .L__s3_failure_site_841
    mov r10, r12
    cmp r10, 1
    jae .L__s3_failure_site_842
    cmp byte ptr [rbp + r10 - 2663], 0
    je .L__s3_failure_site_840
    mov rax, qword ptr [rbp + r10*8 - 2608]
    mov r12, rax
    mov byte ptr [rbp - 2502], 1
    dec r15
    js .L__s3_failure_site_843
    mov r13, 1
    mov byte ptr [rbp - 2503], 1
    dec r15
    js .L__s3_failure_site_844
    cmp byte ptr [rbp - 2502], 0
    je .L__s3_failure_site_846
    mov rax, r12
    cmp byte ptr [rbp - 2503], 0
    je .L__s3_failure_site_847
    mov r10, r13
    add rax, r10
    jo .L__s3_failure_site_845
    mov r12, rax
    mov byte ptr [rbp - 2504], 1
    dec r15
    js .L__s3_failure_site_848
    mov r13, 0
    mov byte ptr [rbp - 2505], 1
    dec r15
    js .L__s3_failure_site_849
    cmp byte ptr [rbp - 2505], 0
    je .L__s3_failure_site_850
    mov rax, r13
    cmp byte ptr [rbp - 2504], 0
    je .L__s3_failure_site_851
    mov r10, r12
    cmp rax, 1
    jae .L__s3_failure_site_852
    mov qword ptr [rbp + rax*8 - 2608], r10
    mov byte ptr [rbp + rax - 2663], 1
    dec r15
    js .L__s3_failure_site_853
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_71
.L_s3_f21_agent_energy_residual_b18_while_condition_88:
    dec r15
    js .L__s3_failure_site_854
    mov rcx, 0
    mov byte ptr [rbp - 2510], 1
    dec r15
    js .L__s3_failure_site_855
    cmp byte ptr [rbp - 2510], 0
    je .L__s3_failure_site_857
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_858
    cmp byte ptr [rbp + r10 - 2668], 0
    je .L__s3_failure_site_856
    mov rax, qword ptr [rbp + r10*8 - 2648]
    mov rcx, rax
    mov byte ptr [rbp - 2511], 1
    dec r15
    js .L__s3_failure_site_859
    cmp byte ptr [rbp - 2511], 0
    je .L__s3_failure_site_860
    mov rax, rcx
    cmp byte ptr [rbp - 2269], 0
    je .L__s3_failure_site_861
    mov r10, rdx
    dec r15
    js .L__s3_failure_site_862
    cmp rax, r10
    jl .L_s3_f21_agent_energy_residual_b10_rel_neg_93
    jg .L_s3_f21_agent_energy_residual_b10_rel_pos_95
    jmp .L_s3_f21_agent_energy_residual_b11_rel_zero_94
.L_s3_f21_agent_energy_residual_b13_while_body_89:
    dec r15
    js .L__s3_failure_site_863
    mov rcx, 0
    mov byte ptr [rbp - 2521], 1
    dec r15
    js .L__s3_failure_site_864
    cmp byte ptr [rbp - 2521], 0
    je .L__s3_failure_site_866
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_867
    cmp byte ptr [rbp + r10 - 2667], 0
    je .L__s3_failure_site_865
    mov rax, qword ptr [rbp + r10*8 - 2640]
    mov rcx, rax
    mov byte ptr [rbp - 2522], 1
    dec r15
    js .L__s3_failure_site_868
    movabs rax, 4607182418800017408
    mov r8, rax
    mov byte ptr [rbp - 2523], 1
    dec r15
    js .L__s3_failure_site_869
    cmp byte ptr [rbp - 2522], 0
    je .L__s3_failure_site_870
    mov rax, rcx
    cmp byte ptr [rbp - 2523], 0
    je .L__s3_failure_site_871
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 2524], 1
    dec r15
    js .L__s3_failure_site_872
    mov r8, 0
    mov byte ptr [rbp - 2525], 1
    dec r15
    js .L__s3_failure_site_873
    cmp byte ptr [rbp - 2525], 0
    je .L__s3_failure_site_874
    mov rax, r8
    cmp byte ptr [rbp - 2524], 0
    je .L__s3_failure_site_875
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_876
    mov qword ptr [rbp + rax*8 - 2640], r10
    mov byte ptr [rbp + rax - 2667], 1
    dec r15
    js .L__s3_failure_site_877
    mov rcx, 0
    mov byte ptr [rbp - 2526], 1
    dec r15
    js .L__s3_failure_site_878
    cmp byte ptr [rbp - 2526], 0
    je .L__s3_failure_site_880
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_881
    cmp byte ptr [rbp + r10 - 2668], 0
    je .L__s3_failure_site_879
    mov rax, qword ptr [rbp + r10*8 - 2648]
    mov rcx, rax
    mov byte ptr [rbp - 2527], 1
    dec r15
    js .L__s3_failure_site_882
    mov r8, 1
    mov byte ptr [rbp - 2528], 1
    dec r15
    js .L__s3_failure_site_883
    cmp byte ptr [rbp - 2527], 0
    je .L__s3_failure_site_885
    mov rax, rcx
    cmp byte ptr [rbp - 2528], 0
    je .L__s3_failure_site_886
    mov r10, r8
    add rax, r10
    jo .L__s3_failure_site_884
    mov rcx, rax
    mov byte ptr [rbp - 2529], 1
    dec r15
    js .L__s3_failure_site_887
    mov r8, 0
    mov byte ptr [rbp - 2530], 1
    dec r15
    js .L__s3_failure_site_888
    cmp byte ptr [rbp - 2530], 0
    je .L__s3_failure_site_889
    mov rax, r8
    cmp byte ptr [rbp - 2529], 0
    je .L__s3_failure_site_890
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_891
    mov qword ptr [rbp + rax*8 - 2648], r10
    mov byte ptr [rbp + rax - 2668], 1
    dec r15
    js .L__s3_failure_site_892
    jmp .L_s3_f21_agent_energy_residual_b18_while_condition_88
.L_s3_f21_agent_energy_residual_b15_while_exit_0_90:
    dec r15
    js .L__s3_failure_site_893
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_92
.L_s3_f21_agent_energy_residual_b15_while_exit_1_91:
    dec r15
    js .L__s3_failure_site_894
    jmp .L_s3_f21_agent_energy_residual_b13_while_exit_92
.L_s3_f21_agent_energy_residual_b13_while_exit_92:
    dec r15
    js .L__s3_failure_site_895
    mov rdx, 0
    mov byte ptr [rbp - 2531], 1
    dec r15
    js .L__s3_failure_site_896
    mov rcx, 0
    mov byte ptr [rbp - 2532], 1
    dec r15
    js .L__s3_failure_site_897
    cmp byte ptr [rbp - 2532], 0
    je .L__s3_failure_site_899
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_900
    cmp byte ptr [rbp + r10 - 2660], 0
    je .L__s3_failure_site_898
    mov rax, qword ptr [rbp + r10*8 - 2584]
    mov rcx, rax
    mov byte ptr [rbp - 2533], 1
    dec r15
    js .L__s3_failure_site_901
    cmp byte ptr [rbp - 2270], 0
    je .L__s3_failure_site_903
    mov r10, rdi
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_904
    mov r11, rsi
    cmp byte ptr [rbp - 2531], 0
    je .L__s3_failure_site_905
    mov rax, rdx
    cmp byte ptr [rbp - 2533], 0
    je .L__s3_failure_site_906
    cmp rax, r11
    jae .L__s3_failure_site_902
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_907
    mov rdx, 1
    mov byte ptr [rbp - 2534], 1
    dec r15
    js .L__s3_failure_site_908
    mov rcx, 0
    mov byte ptr [rbp - 2535], 1
    dec r15
    js .L__s3_failure_site_909
    cmp byte ptr [rbp - 2535], 0
    je .L__s3_failure_site_911
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_912
    cmp byte ptr [rbp + r10 - 2662], 0
    je .L__s3_failure_site_910
    mov rax, qword ptr [rbp + r10*8 - 2600]
    mov rcx, rax
    mov byte ptr [rbp - 2536], 1
    dec r15
    js .L__s3_failure_site_913
    cmp byte ptr [rbp - 2270], 0
    je .L__s3_failure_site_915
    mov r10, rdi
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_916
    mov r11, rsi
    cmp byte ptr [rbp - 2534], 0
    je .L__s3_failure_site_917
    mov rax, rdx
    cmp byte ptr [rbp - 2536], 0
    je .L__s3_failure_site_918
    cmp rax, r11
    jae .L__s3_failure_site_914
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_919
    mov rdx, 2
    mov byte ptr [rbp - 2537], 1
    dec r15
    js .L__s3_failure_site_920
    mov rcx, 0
    mov byte ptr [rbp - 2538], 1
    dec r15
    js .L__s3_failure_site_921
    cmp byte ptr [rbp - 2538], 0
    je .L__s3_failure_site_923
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_924
    cmp byte ptr [rbp + r10 - 2661], 0
    je .L__s3_failure_site_922
    mov rax, qword ptr [rbp + r10*8 - 2592]
    mov rcx, rax
    mov byte ptr [rbp - 2539], 1
    dec r15
    js .L__s3_failure_site_925
    mov r8, 0
    mov byte ptr [rbp - 2540], 1
    dec r15
    js .L__s3_failure_site_926
    cmp byte ptr [rbp - 2540], 0
    je .L__s3_failure_site_928
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_929
    cmp byte ptr [rbp + r10 - 2667], 0
    je .L__s3_failure_site_927
    mov rax, qword ptr [rbp + r10*8 - 2640]
    mov r8, rax
    mov byte ptr [rbp - 2541], 1
    dec r15
    js .L__s3_failure_site_930
    cmp byte ptr [rbp - 2539], 0
    je .L__s3_failure_site_931
    mov rax, rcx
    cmp byte ptr [rbp - 2541], 0
    je .L__s3_failure_site_932
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 2542], 1
    dec r15
    js .L__s3_failure_site_933
    cmp byte ptr [rbp - 2270], 0
    je .L__s3_failure_site_935
    mov r10, rdi
    cmp byte ptr [rbp - 2271], 0
    je .L__s3_failure_site_936
    mov r11, rsi
    cmp byte ptr [rbp - 2537], 0
    je .L__s3_failure_site_937
    mov rax, rdx
    cmp byte ptr [rbp - 2542], 0
    je .L__s3_failure_site_938
    cmp rax, r11
    jae .L__s3_failure_site_934
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_939
    mov rdi, 0
    mov byte ptr [rbp - 2543], 1
    dec r15
    js .L__s3_failure_site_940
    cmp byte ptr [rbp - 2543], 0
    je .L__s3_failure_site_941
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2680]
    mov r12, qword ptr [rbp - 2688]
    mov r13, qword ptr [rbp - 2696]
    mov r15, qword ptr [rbp - 2704]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f21_agent_energy_residual_b10_rel_neg_93:
    dec r15
    js .L__s3_failure_site_942
    mov rcx, 0
    mov byte ptr [rbp - 2513], 1
    dec r15
    js .L__s3_failure_site_943
    mov r8, -1
    mov byte ptr [rbp - 2514], 1
    dec r15
    js .L__s3_failure_site_944
    cmp byte ptr [rbp - 2513], 0
    je .L__s3_failure_site_945
    mov rax, rcx
    cmp byte ptr [rbp - 2514], 0
    je .L__s3_failure_site_946
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_947
    cmp r10, -1
    jl .L__s3_failure_site_948
    cmp r10, 1
    jg .L__s3_failure_site_948
    mov byte ptr [rbp + rax - 2649], r10b
    mov byte ptr [rbp + rax - 2669], 1
    dec r15
    js .L__s3_failure_site_949
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_96
.L_s3_f21_agent_energy_residual_b11_rel_zero_94:
    dec r15
    js .L__s3_failure_site_950
    mov rcx, 0
    mov byte ptr [rbp - 2515], 1
    dec r15
    js .L__s3_failure_site_951
    mov r8, 0
    mov byte ptr [rbp - 2516], 1
    dec r15
    js .L__s3_failure_site_952
    cmp byte ptr [rbp - 2515], 0
    je .L__s3_failure_site_953
    mov rax, rcx
    cmp byte ptr [rbp - 2516], 0
    je .L__s3_failure_site_954
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_955
    cmp r10, -1
    jl .L__s3_failure_site_956
    cmp r10, 1
    jg .L__s3_failure_site_956
    mov byte ptr [rbp + rax - 2649], r10b
    mov byte ptr [rbp + rax - 2669], 1
    dec r15
    js .L__s3_failure_site_957
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_96
.L_s3_f21_agent_energy_residual_b10_rel_pos_95:
    dec r15
    js .L__s3_failure_site_958
    mov rcx, 0
    mov byte ptr [rbp - 2517], 1
    dec r15
    js .L__s3_failure_site_959
    mov r8, 0
    mov byte ptr [rbp - 2518], 1
    dec r15
    js .L__s3_failure_site_960
    cmp byte ptr [rbp - 2517], 0
    je .L__s3_failure_site_961
    mov rax, rcx
    cmp byte ptr [rbp - 2518], 0
    je .L__s3_failure_site_962
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_963
    cmp r10, -1
    jl .L__s3_failure_site_964
    cmp r10, 1
    jg .L__s3_failure_site_964
    mov byte ptr [rbp + rax - 2649], r10b
    mov byte ptr [rbp + rax - 2669], 1
    dec r15
    js .L__s3_failure_site_965
    jmp .L_s3_f21_agent_energy_residual_b11_rel_cont_96
.L_s3_f21_agent_energy_residual_b11_rel_cont_96:
    dec r15
    js .L__s3_failure_site_966
    mov rcx, 0
    mov byte ptr [rbp - 2519], 1
    dec r15
    js .L__s3_failure_site_967
    cmp byte ptr [rbp - 2519], 0
    je .L__s3_failure_site_969
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_970
    cmp byte ptr [rbp + r10 - 2669], 0
    je .L__s3_failure_site_968
    movsx rax, byte ptr [rbp + r10 - 2649]
    mov rcx, rax
    mov byte ptr [rbp - 2520], 1
    dec r15
    js .L__s3_failure_site_971
    cmp byte ptr [rbp - 2520], 0
    je .L__s3_failure_site_973
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f21_agent_energy_residual_b13_while_body_89
    cmp rax, 0
    je .L_s3_f21_agent_energy_residual_b15_while_exit_0_90
    cmp rax, 1
    je .L_s3_f21_agent_energy_residual_b15_while_exit_1_91
    jmp .L__s3_failure_site_972
.size agent_energy_residual, .-agent_energy_residual

.globl s3_main
.type s3_main, @function
s3_main:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_974
    push rbp
    mov rbp, rsp
    sub rsp, 32
    mov qword ptr [rbp - 24], r15
    mov r15, qword ptr [rip + __s3_instruction_remaining]
    jmp .L_s3_f4_main_b5_entry
.L_s3_f4_main_b5_entry:
    dec r15
    js .L__s3_failure_site_975
    mov rdi, 0
    dec r15
    js .L__s3_failure_site_976
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov r15, qword ptr [rbp - 24]
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
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_2:
    lea rsi, [rip + .L__s3_failure_prefix_2]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_3:
    lea rsi, [rip + .L__s3_failure_prefix_3]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_4:
    lea rsi, [rip + .L__s3_failure_prefix_4]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_5:
    lea rsi, [rip + .L__s3_failure_prefix_5]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_6:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_6]
    mov edx, 102
    lea rcx, [rip + .L__s3_failure_suffix_6]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_7:
    lea rsi, [rip + .L__s3_failure_prefix_7]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_8:
    lea rsi, [rip + .L__s3_failure_prefix_8]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_9:
    lea rsi, [rip + .L__s3_failure_prefix_9]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_10:
    lea rsi, [rip + .L__s3_failure_prefix_10]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_11:
    lea rsi, [rip + .L__s3_failure_prefix_11]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_12:
    lea rsi, [rip + .L__s3_failure_prefix_12]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_13:
    lea rsi, [rip + .L__s3_failure_prefix_13]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_14:
    lea rsi, [rip + .L__s3_failure_prefix_14]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_15:
    lea rsi, [rip + .L__s3_failure_prefix_15]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_16:
    lea rsi, [rip + .L__s3_failure_prefix_16]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_17:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_17]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_17]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_18:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_18]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_18]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_19:
    lea rsi, [rip + .L__s3_failure_prefix_19]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_20:
    lea rsi, [rip + .L__s3_failure_prefix_20]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_21:
    lea rsi, [rip + .L__s3_failure_prefix_21]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_22:
    lea rsi, [rip + .L__s3_failure_prefix_22]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_23:
    lea rsi, [rip + .L__s3_failure_prefix_23]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_24:
    lea rsi, [rip + .L__s3_failure_prefix_24]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_25:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_25]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_25]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_26:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_26]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_26]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_27:
    lea rsi, [rip + .L__s3_failure_prefix_27]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_28:
    lea rsi, [rip + .L__s3_failure_prefix_28]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_29:
    lea rsi, [rip + .L__s3_failure_prefix_29]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_30:
    lea rsi, [rip + .L__s3_failure_prefix_30]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_31:
    lea rsi, [rip + .L__s3_failure_prefix_31]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_32:
    lea rsi, [rip + .L__s3_failure_prefix_32]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_33:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_33]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_33]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_34:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_34]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_34]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_35:
    lea rsi, [rip + .L__s3_failure_prefix_35]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_36:
    lea rsi, [rip + .L__s3_failure_prefix_36]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_37:
    lea rsi, [rip + .L__s3_failure_prefix_37]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_38:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_38]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_38]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_39:
    lea rsi, [rip + .L__s3_failure_prefix_39]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_40:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_40]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_40]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_41:
    lea rsi, [rip + .L__s3_failure_prefix_41]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_42:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_42]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_42]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_43:
    lea rsi, [rip + .L__s3_failure_prefix_43]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_44:
    lea rsi, [rip + .L__s3_failure_prefix_44]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_45:
    lea rsi, [rip + .L__s3_failure_prefix_45]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_46:
    lea rsi, [rip + .L__s3_failure_prefix_46]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_47:
    lea rsi, [rip + .L__s3_failure_prefix_47]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_48:
    lea rsi, [rip + .L__s3_failure_prefix_48]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_49:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_49]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_49]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_50:
    lea rsi, [rip + .L__s3_failure_prefix_50]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_51:
    lea rsi, [rip + .L__s3_failure_prefix_51]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_52:
    lea rsi, [rip + .L__s3_failure_prefix_52]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_53:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_53]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_53]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_54:
    lea rsi, [rip + .L__s3_failure_prefix_54]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_55:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_55]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_55]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_56:
    lea rsi, [rip + .L__s3_failure_prefix_56]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_57:
    lea rsi, [rip + .L__s3_failure_prefix_57]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_58:
    lea rsi, [rip + .L__s3_failure_prefix_58]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_59:
    lea rsi, [rip + .L__s3_failure_prefix_59]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_60:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_60]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_60]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_61:
    lea rsi, [rip + .L__s3_failure_prefix_61]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_62:
    lea rsi, [rip + .L__s3_failure_prefix_62]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_63:
    lea rsi, [rip + .L__s3_failure_prefix_63]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_64:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_64]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_64]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_65:
    lea rsi, [rip + .L__s3_failure_prefix_65]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_66:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_66]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_66]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_67:
    lea rsi, [rip + .L__s3_failure_prefix_67]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_68:
    lea rsi, [rip + .L__s3_failure_prefix_68]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_69:
    lea rsi, [rip + .L__s3_failure_prefix_69]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_70:
    lea rsi, [rip + .L__s3_failure_prefix_70]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_71:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_71]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_71]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_72:
    lea rsi, [rip + .L__s3_failure_prefix_72]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_73:
    lea rsi, [rip + .L__s3_failure_prefix_73]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_74:
    lea rsi, [rip + .L__s3_failure_prefix_74]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_75:
    lea rsi, [rip + .L__s3_failure_prefix_75]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_76:
    lea rsi, [rip + .L__s3_failure_prefix_76]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_77:
    lea rsi, [rip + .L__s3_failure_prefix_77]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_78:
    lea rsi, [rip + .L__s3_failure_prefix_78]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_79:
    lea rsi, [rip + .L__s3_failure_prefix_79]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_80:
    lea rsi, [rip + .L__s3_failure_prefix_80]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_81:
    lea rsi, [rip + .L__s3_failure_prefix_81]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_82:
    lea rsi, [rip + .L__s3_failure_prefix_82]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_83:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_83]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_83]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_84:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_84]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_84]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_85:
    lea rsi, [rip + .L__s3_failure_prefix_85]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_86:
    lea rsi, [rip + .L__s3_failure_prefix_86]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_87:
    lea rsi, [rip + .L__s3_failure_prefix_87]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_88:
    lea rsi, [rip + .L__s3_failure_prefix_88]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_89:
    lea rsi, [rip + .L__s3_failure_prefix_89]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_90:
    lea rsi, [rip + .L__s3_failure_prefix_90]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_91:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_91]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_91]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_92:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_92]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_92]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_93:
    lea rsi, [rip + .L__s3_failure_prefix_93]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_94:
    lea rsi, [rip + .L__s3_failure_prefix_94]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_95:
    lea rsi, [rip + .L__s3_failure_prefix_95]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_96:
    lea rsi, [rip + .L__s3_failure_prefix_96]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_97:
    lea rsi, [rip + .L__s3_failure_prefix_97]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_98:
    lea rsi, [rip + .L__s3_failure_prefix_98]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_99:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_99]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_99]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_100:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_100]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_100]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_101:
    lea rsi, [rip + .L__s3_failure_prefix_101]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_102:
    lea rsi, [rip + .L__s3_failure_prefix_102]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_103:
    lea rsi, [rip + .L__s3_failure_prefix_103]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_104:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_104]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_104]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_105:
    lea rsi, [rip + .L__s3_failure_prefix_105]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_106:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_106]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_106]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_107:
    lea rsi, [rip + .L__s3_failure_prefix_107]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_108:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_108]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_108]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_109:
    lea rsi, [rip + .L__s3_failure_prefix_109]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_110:
    lea rsi, [rip + .L__s3_failure_prefix_110]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_111:
    lea rsi, [rip + .L__s3_failure_prefix_111]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_112:
    lea rsi, [rip + .L__s3_failure_prefix_112]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_113:
    lea rsi, [rip + .L__s3_failure_prefix_113]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_114:
    lea rsi, [rip + .L__s3_failure_prefix_114]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_115:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_115]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_115]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_116:
    lea rsi, [rip + .L__s3_failure_prefix_116]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_117:
    lea rsi, [rip + .L__s3_failure_prefix_117]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_118:
    lea rsi, [rip + .L__s3_failure_prefix_118]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_119:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_119]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_119]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_120:
    lea rsi, [rip + .L__s3_failure_prefix_120]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_121:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_121]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_121]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_122:
    lea rsi, [rip + .L__s3_failure_prefix_122]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_123:
    lea rsi, [rip + .L__s3_failure_prefix_123]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_124:
    lea rsi, [rip + .L__s3_failure_prefix_124]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_125:
    lea rsi, [rip + .L__s3_failure_prefix_125]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_126:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_126]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_126]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_127:
    lea rsi, [rip + .L__s3_failure_prefix_127]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_128:
    lea rsi, [rip + .L__s3_failure_prefix_128]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_129:
    lea rsi, [rip + .L__s3_failure_prefix_129]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_130:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_130]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_130]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_131:
    lea rsi, [rip + .L__s3_failure_prefix_131]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_132:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_132]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_132]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_133:
    lea rsi, [rip + .L__s3_failure_prefix_133]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_134:
    lea rsi, [rip + .L__s3_failure_prefix_134]
    mov edx, 156
    jmp __s3_fail_message
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
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_139:
    lea rsi, [rip + .L__s3_failure_prefix_139]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_140:
    lea rsi, [rip + .L__s3_failure_prefix_140]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_141:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_141]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_141]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_142:
    lea rsi, [rip + .L__s3_failure_prefix_142]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_143:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_143]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_143]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_144:
    lea rsi, [rip + .L__s3_failure_prefix_144]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_145:
    lea rsi, [rip + .L__s3_failure_prefix_145]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_146:
    lea rsi, [rip + .L__s3_failure_prefix_146]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_147:
    lea rsi, [rip + .L__s3_failure_prefix_147]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_148:
    lea rsi, [rip + .L__s3_failure_prefix_148]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_149:
    lea rsi, [rip + .L__s3_failure_prefix_149]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_150:
    lea rsi, [rip + .L__s3_failure_prefix_150]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_151:
    lea rsi, [rip + .L__s3_failure_prefix_151]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_152:
    lea rsi, [rip + .L__s3_failure_prefix_152]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_153:
    lea rsi, [rip + .L__s3_failure_prefix_153]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_154:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_154]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_154]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_155:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_155]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_155]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_156:
    lea rsi, [rip + .L__s3_failure_prefix_156]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_157:
    lea rsi, [rip + .L__s3_failure_prefix_157]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_158:
    lea rsi, [rip + .L__s3_failure_prefix_158]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_159:
    lea rsi, [rip + .L__s3_failure_prefix_159]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_160:
    lea rsi, [rip + .L__s3_failure_prefix_160]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_161:
    lea rsi, [rip + .L__s3_failure_prefix_161]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_162:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_162]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_162]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_163:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_163]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_163]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_164:
    lea rsi, [rip + .L__s3_failure_prefix_164]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_165:
    lea rsi, [rip + .L__s3_failure_prefix_165]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_166:
    lea rsi, [rip + .L__s3_failure_prefix_166]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_167:
    lea rsi, [rip + .L__s3_failure_prefix_167]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_168:
    lea rsi, [rip + .L__s3_failure_prefix_168]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_169:
    lea rsi, [rip + .L__s3_failure_prefix_169]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_170:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_170]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_170]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_171:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_171]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_171]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_172:
    lea rsi, [rip + .L__s3_failure_prefix_172]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_173:
    lea rsi, [rip + .L__s3_failure_prefix_173]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_174:
    lea rsi, [rip + .L__s3_failure_prefix_174]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_175:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_175]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_175]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_176:
    lea rsi, [rip + .L__s3_failure_prefix_176]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_177:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_177]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_177]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_178:
    lea rsi, [rip + .L__s3_failure_prefix_178]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_179:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_179]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_179]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_180:
    lea rsi, [rip + .L__s3_failure_prefix_180]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_181:
    lea rsi, [rip + .L__s3_failure_prefix_181]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_182:
    lea rsi, [rip + .L__s3_failure_prefix_182]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_183:
    lea rsi, [rip + .L__s3_failure_prefix_183]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_184:
    lea rsi, [rip + .L__s3_failure_prefix_184]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_185:
    lea rsi, [rip + .L__s3_failure_prefix_185]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_186:
    lea rsi, [rip + .L__s3_failure_prefix_186]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_187:
    lea rsi, [rip + .L__s3_failure_prefix_187]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_188:
    lea rsi, [rip + .L__s3_failure_prefix_188]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_189:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_189]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_189]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_190:
    lea rsi, [rip + .L__s3_failure_prefix_190]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_191:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_191]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_191]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_192:
    lea rsi, [rip + .L__s3_failure_prefix_192]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_193:
    lea rsi, [rip + .L__s3_failure_prefix_193]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_194:
    lea rsi, [rip + .L__s3_failure_prefix_194]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_195:
    lea rsi, [rip + .L__s3_failure_prefix_195]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_196:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_196]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_196]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_197:
    lea rsi, [rip + .L__s3_failure_prefix_197]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_198:
    lea rsi, [rip + .L__s3_failure_prefix_198]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_199:
    lea rsi, [rip + .L__s3_failure_prefix_199]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_200:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_200]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_200]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_201:
    lea rsi, [rip + .L__s3_failure_prefix_201]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_202:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_202]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_202]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_203:
    lea rsi, [rip + .L__s3_failure_prefix_203]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_204:
    lea rsi, [rip + .L__s3_failure_prefix_204]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_205:
    lea rsi, [rip + .L__s3_failure_prefix_205]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_206:
    lea rsi, [rip + .L__s3_failure_prefix_206]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_207:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_207]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_207]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_208:
    lea rsi, [rip + .L__s3_failure_prefix_208]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_209:
    lea rsi, [rip + .L__s3_failure_prefix_209]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_210:
    lea rsi, [rip + .L__s3_failure_prefix_210]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_211:
    lea rsi, [rip + .L__s3_failure_prefix_211]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_212:
    lea rsi, [rip + .L__s3_failure_prefix_212]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_213:
    lea rsi, [rip + .L__s3_failure_prefix_213]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_214:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_214]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_214]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_215:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_215]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_215]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_216:
    lea rsi, [rip + .L__s3_failure_prefix_216]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_217:
    lea rsi, [rip + .L__s3_failure_prefix_217]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_218:
    lea rsi, [rip + .L__s3_failure_prefix_218]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_219:
    lea rsi, [rip + .L__s3_failure_prefix_219]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_220:
    lea rsi, [rip + .L__s3_failure_prefix_220]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_221:
    lea rsi, [rip + .L__s3_failure_prefix_221]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_222:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_222]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_222]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_223:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_223]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_223]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_224:
    lea rsi, [rip + .L__s3_failure_prefix_224]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_225:
    lea rsi, [rip + .L__s3_failure_prefix_225]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_226:
    lea rsi, [rip + .L__s3_failure_prefix_226]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_227:
    lea rsi, [rip + .L__s3_failure_prefix_227]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_228:
    lea rsi, [rip + .L__s3_failure_prefix_228]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_229:
    lea rsi, [rip + .L__s3_failure_prefix_229]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_230:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_230]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_230]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_231:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_231]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_231]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_232:
    lea rsi, [rip + .L__s3_failure_prefix_232]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_233:
    lea rsi, [rip + .L__s3_failure_prefix_233]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_234:
    lea rsi, [rip + .L__s3_failure_prefix_234]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_235:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_235]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_235]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_236:
    lea rsi, [rip + .L__s3_failure_prefix_236]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_237:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_237]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_237]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_238:
    lea rsi, [rip + .L__s3_failure_prefix_238]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_239:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_239]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_239]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_240:
    lea rsi, [rip + .L__s3_failure_prefix_240]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_241:
    lea rsi, [rip + .L__s3_failure_prefix_241]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_242:
    lea rsi, [rip + .L__s3_failure_prefix_242]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_243:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_243]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_243]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_244:
    lea rsi, [rip + .L__s3_failure_prefix_244]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_245:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_245]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_245]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_246:
    lea rsi, [rip + .L__s3_failure_prefix_246]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_247:
    lea rsi, [rip + .L__s3_failure_prefix_247]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_248:
    lea rsi, [rip + .L__s3_failure_prefix_248]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_249:
    lea rsi, [rip + .L__s3_failure_prefix_249]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_250:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_250]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_250]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_251:
    lea rsi, [rip + .L__s3_failure_prefix_251]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_252:
    lea rsi, [rip + .L__s3_failure_prefix_252]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_253:
    lea rsi, [rip + .L__s3_failure_prefix_253]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_254:
    lea rsi, [rip + .L__s3_failure_prefix_254]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_255:
    lea rsi, [rip + .L__s3_failure_prefix_255]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_256:
    lea rsi, [rip + .L__s3_failure_prefix_256]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_257:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_257]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_257]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_258:
    lea rsi, [rip + .L__s3_failure_prefix_258]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_259:
    lea rsi, [rip + .L__s3_failure_prefix_259]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_260:
    lea rsi, [rip + .L__s3_failure_prefix_260]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_261:
    lea rsi, [rip + .L__s3_failure_prefix_261]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_262:
    lea rsi, [rip + .L__s3_failure_prefix_262]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_263:
    lea rsi, [rip + .L__s3_failure_prefix_263]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_264:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_264]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_264]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_265:
    lea rsi, [rip + .L__s3_failure_prefix_265]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_266:
    lea rsi, [rip + .L__s3_failure_prefix_266]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_267:
    lea rsi, [rip + .L__s3_failure_prefix_267]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_268:
    lea rsi, [rip + .L__s3_failure_prefix_268]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_269:
    lea rsi, [rip + .L__s3_failure_prefix_269]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_270:
    lea rsi, [rip + .L__s3_failure_prefix_270]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_271:
    lea rsi, [rip + .L__s3_failure_prefix_271]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_272:
    lea rsi, [rip + .L__s3_failure_prefix_272]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_273:
    lea rsi, [rip + .L__s3_failure_prefix_273]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_274:
    lea rsi, [rip + .L__s3_failure_prefix_274]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_275:
    lea rsi, [rip + .L__s3_failure_prefix_275]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_276:
    lea rsi, [rip + .L__s3_failure_prefix_276]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_277:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_277]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_277]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_278:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_278]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_278]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_279:
    lea rsi, [rip + .L__s3_failure_prefix_279]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_280:
    lea rsi, [rip + .L__s3_failure_prefix_280]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_281:
    lea rsi, [rip + .L__s3_failure_prefix_281]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_282:
    lea rsi, [rip + .L__s3_failure_prefix_282]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_283:
    lea rsi, [rip + .L__s3_failure_prefix_283]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_284:
    lea rsi, [rip + .L__s3_failure_prefix_284]
    mov edx, 150
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
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_288:
    lea rsi, [rip + .L__s3_failure_prefix_288]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_289:
    lea rsi, [rip + .L__s3_failure_prefix_289]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_290:
    lea rsi, [rip + .L__s3_failure_prefix_290]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_291:
    lea rsi, [rip + .L__s3_failure_prefix_291]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_292:
    lea rsi, [rip + .L__s3_failure_prefix_292]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_293:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_293]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_293]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_294:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_294]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_294]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_295:
    lea rsi, [rip + .L__s3_failure_prefix_295]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_296:
    lea rsi, [rip + .L__s3_failure_prefix_296]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_297:
    lea rsi, [rip + .L__s3_failure_prefix_297]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_298:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_298]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_298]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_299:
    lea rsi, [rip + .L__s3_failure_prefix_299]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_300:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_300]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_300]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_301:
    lea rsi, [rip + .L__s3_failure_prefix_301]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_302:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_302]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_302]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_303:
    lea rsi, [rip + .L__s3_failure_prefix_303]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_304:
    lea rsi, [rip + .L__s3_failure_prefix_304]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_305:
    lea rsi, [rip + .L__s3_failure_prefix_305]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_306:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_306]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_306]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_307:
    lea rsi, [rip + .L__s3_failure_prefix_307]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_308:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_308]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_308]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_309:
    lea rsi, [rip + .L__s3_failure_prefix_309]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_310:
    lea rsi, [rip + .L__s3_failure_prefix_310]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_311:
    lea rsi, [rip + .L__s3_failure_prefix_311]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_312:
    lea rsi, [rip + .L__s3_failure_prefix_312]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_313:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_313]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_313]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_314:
    lea rsi, [rip + .L__s3_failure_prefix_314]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_315:
    lea rsi, [rip + .L__s3_failure_prefix_315]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_316:
    lea rsi, [rip + .L__s3_failure_prefix_316]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_317:
    lea rsi, [rip + .L__s3_failure_prefix_317]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_318:
    lea rsi, [rip + .L__s3_failure_prefix_318]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_319:
    lea rsi, [rip + .L__s3_failure_prefix_319]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_320:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_320]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_320]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_321:
    lea rsi, [rip + .L__s3_failure_prefix_321]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_322:
    lea rsi, [rip + .L__s3_failure_prefix_322]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_323:
    lea rsi, [rip + .L__s3_failure_prefix_323]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_324:
    lea rsi, [rip + .L__s3_failure_prefix_324]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_325:
    lea rsi, [rip + .L__s3_failure_prefix_325]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_326:
    lea rsi, [rip + .L__s3_failure_prefix_326]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_327:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_327]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_327]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_328:
    lea rsi, [rip + .L__s3_failure_prefix_328]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_329:
    lea rsi, [rip + .L__s3_failure_prefix_329]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_330:
    lea rsi, [rip + .L__s3_failure_prefix_330]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_331:
    lea rsi, [rip + .L__s3_failure_prefix_331]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_332:
    lea rsi, [rip + .L__s3_failure_prefix_332]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_333:
    lea rsi, [rip + .L__s3_failure_prefix_333]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_334:
    lea rsi, [rip + .L__s3_failure_prefix_334]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_335:
    lea rsi, [rip + .L__s3_failure_prefix_335]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_336:
    lea rsi, [rip + .L__s3_failure_prefix_336]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_337:
    lea rsi, [rip + .L__s3_failure_prefix_337]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_338:
    lea rsi, [rip + .L__s3_failure_prefix_338]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_339:
    lea rsi, [rip + .L__s3_failure_prefix_339]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_340:
    lea rsi, [rip + .L__s3_failure_prefix_340]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_341:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_341]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_341]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_342:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_342]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_342]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_343:
    lea rsi, [rip + .L__s3_failure_prefix_343]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_344:
    lea rsi, [rip + .L__s3_failure_prefix_344]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_345:
    lea rsi, [rip + .L__s3_failure_prefix_345]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_346:
    lea rsi, [rip + .L__s3_failure_prefix_346]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_347:
    lea rsi, [rip + .L__s3_failure_prefix_347]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_348:
    lea rsi, [rip + .L__s3_failure_prefix_348]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_349:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_349]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_349]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_350:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_350]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_350]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_351:
    lea rsi, [rip + .L__s3_failure_prefix_351]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_352:
    lea rsi, [rip + .L__s3_failure_prefix_352]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_353:
    lea rsi, [rip + .L__s3_failure_prefix_353]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_354:
    lea rsi, [rip + .L__s3_failure_prefix_354]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_355:
    lea rsi, [rip + .L__s3_failure_prefix_355]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_356:
    lea rsi, [rip + .L__s3_failure_prefix_356]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_357:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_357]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_357]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_358:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_358]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_358]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_359:
    lea rsi, [rip + .L__s3_failure_prefix_359]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_360:
    lea rsi, [rip + .L__s3_failure_prefix_360]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_361:
    lea rsi, [rip + .L__s3_failure_prefix_361]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_362:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_362]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_362]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_363:
    lea rsi, [rip + .L__s3_failure_prefix_363]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_364:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_364]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_364]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_365:
    lea rsi, [rip + .L__s3_failure_prefix_365]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_366:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_366]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_366]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_367:
    lea rsi, [rip + .L__s3_failure_prefix_367]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_368:
    lea rsi, [rip + .L__s3_failure_prefix_368]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_369:
    lea rsi, [rip + .L__s3_failure_prefix_369]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_370:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_370]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_370]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_371:
    lea rsi, [rip + .L__s3_failure_prefix_371]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_372:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_372]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_372]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_373:
    lea rsi, [rip + .L__s3_failure_prefix_373]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_374:
    lea rsi, [rip + .L__s3_failure_prefix_374]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_375:
    lea rsi, [rip + .L__s3_failure_prefix_375]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_376:
    lea rsi, [rip + .L__s3_failure_prefix_376]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_377:
    lea rsi, [rip + .L__s3_failure_prefix_377]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_378:
    lea rsi, [rip + .L__s3_failure_prefix_378]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_379:
    lea rsi, [rip + .L__s3_failure_prefix_379]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_380:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_380]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_380]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_381:
    lea rsi, [rip + .L__s3_failure_prefix_381]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_382:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_382]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_382]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_383:
    lea rsi, [rip + .L__s3_failure_prefix_383]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_384:
    lea rsi, [rip + .L__s3_failure_prefix_384]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_385:
    lea rsi, [rip + .L__s3_failure_prefix_385]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_386:
    lea rsi, [rip + .L__s3_failure_prefix_386]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_387:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_387]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_387]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_388:
    lea rsi, [rip + .L__s3_failure_prefix_388]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_389:
    lea rsi, [rip + .L__s3_failure_prefix_389]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_390:
    lea rsi, [rip + .L__s3_failure_prefix_390]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_391:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_391]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_391]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_392:
    lea rsi, [rip + .L__s3_failure_prefix_392]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_393:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_393]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_393]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_394:
    lea rsi, [rip + .L__s3_failure_prefix_394]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_395:
    lea rsi, [rip + .L__s3_failure_prefix_395]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_396:
    lea rsi, [rip + .L__s3_failure_prefix_396]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_397:
    lea rsi, [rip + .L__s3_failure_prefix_397]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_398:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_398]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_398]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_399:
    lea rsi, [rip + .L__s3_failure_prefix_399]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_400:
    lea rsi, [rip + .L__s3_failure_prefix_400]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_401:
    lea rsi, [rip + .L__s3_failure_prefix_401]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_402:
    lea rsi, [rip + .L__s3_failure_prefix_402]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_403:
    lea rsi, [rip + .L__s3_failure_prefix_403]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_404:
    lea rsi, [rip + .L__s3_failure_prefix_404]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_405:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_405]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_405]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_406:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_406]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_406]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_407:
    lea rsi, [rip + .L__s3_failure_prefix_407]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_408:
    lea rsi, [rip + .L__s3_failure_prefix_408]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_409:
    lea rsi, [rip + .L__s3_failure_prefix_409]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_410:
    lea rsi, [rip + .L__s3_failure_prefix_410]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_411:
    lea rsi, [rip + .L__s3_failure_prefix_411]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_412:
    lea rsi, [rip + .L__s3_failure_prefix_412]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_413:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_413]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_413]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_414:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_414]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_414]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_415:
    lea rsi, [rip + .L__s3_failure_prefix_415]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_416:
    lea rsi, [rip + .L__s3_failure_prefix_416]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_417:
    lea rsi, [rip + .L__s3_failure_prefix_417]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_418:
    lea rsi, [rip + .L__s3_failure_prefix_418]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_419:
    lea rsi, [rip + .L__s3_failure_prefix_419]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_420:
    lea rsi, [rip + .L__s3_failure_prefix_420]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_421:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_421]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_421]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_422:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_422]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_422]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_423:
    lea rsi, [rip + .L__s3_failure_prefix_423]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_424:
    lea rsi, [rip + .L__s3_failure_prefix_424]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_425:
    lea rsi, [rip + .L__s3_failure_prefix_425]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_426:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_426]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_426]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_427:
    lea rsi, [rip + .L__s3_failure_prefix_427]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_428:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_428]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_428]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_429:
    lea rsi, [rip + .L__s3_failure_prefix_429]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_430:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_430]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_430]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_431:
    lea rsi, [rip + .L__s3_failure_prefix_431]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_432:
    lea rsi, [rip + .L__s3_failure_prefix_432]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_433:
    lea rsi, [rip + .L__s3_failure_prefix_433]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_434:
    lea rsi, [rip + .L__s3_failure_prefix_434]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_435:
    lea rsi, [rip + .L__s3_failure_prefix_435]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_436:
    lea rsi, [rip + .L__s3_failure_prefix_436]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_437:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_437]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_437]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_438:
    lea rsi, [rip + .L__s3_failure_prefix_438]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_439:
    lea rsi, [rip + .L__s3_failure_prefix_439]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_440:
    lea rsi, [rip + .L__s3_failure_prefix_440]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_441:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_441]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_441]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_442:
    lea rsi, [rip + .L__s3_failure_prefix_442]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_443:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_443]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_443]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_444:
    lea rsi, [rip + .L__s3_failure_prefix_444]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_445:
    lea rsi, [rip + .L__s3_failure_prefix_445]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_446:
    lea rsi, [rip + .L__s3_failure_prefix_446]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_447:
    lea rsi, [rip + .L__s3_failure_prefix_447]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_448:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_448]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_448]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_449:
    lea rsi, [rip + .L__s3_failure_prefix_449]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_450:
    lea rsi, [rip + .L__s3_failure_prefix_450]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_451:
    lea rsi, [rip + .L__s3_failure_prefix_451]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_452:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_452]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_452]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_453:
    lea rsi, [rip + .L__s3_failure_prefix_453]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_454:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_454]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_454]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_455:
    lea rsi, [rip + .L__s3_failure_prefix_455]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_456:
    lea rsi, [rip + .L__s3_failure_prefix_456]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_457:
    lea rsi, [rip + .L__s3_failure_prefix_457]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_458:
    lea rsi, [rip + .L__s3_failure_prefix_458]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_459:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_459]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_459]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_460:
    lea rsi, [rip + .L__s3_failure_prefix_460]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_461:
    lea rsi, [rip + .L__s3_failure_prefix_461]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_462:
    lea rsi, [rip + .L__s3_failure_prefix_462]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_463:
    lea rsi, [rip + .L__s3_failure_prefix_463]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_464:
    lea rsi, [rip + .L__s3_failure_prefix_464]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_465:
    lea rsi, [rip + .L__s3_failure_prefix_465]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_466:
    lea rsi, [rip + .L__s3_failure_prefix_466]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_467:
    lea rsi, [rip + .L__s3_failure_prefix_467]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_468:
    lea rsi, [rip + .L__s3_failure_prefix_468]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_469:
    lea rsi, [rip + .L__s3_failure_prefix_469]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_470:
    lea rsi, [rip + .L__s3_failure_prefix_470]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_471:
    lea rsi, [rip + .L__s3_failure_prefix_471]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_472:
    lea rsi, [rip + .L__s3_failure_prefix_472]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_473:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_473]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_473]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_474:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_474]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_474]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_475:
    lea rsi, [rip + .L__s3_failure_prefix_475]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_476:
    lea rsi, [rip + .L__s3_failure_prefix_476]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_477:
    lea rsi, [rip + .L__s3_failure_prefix_477]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_478:
    lea rsi, [rip + .L__s3_failure_prefix_478]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_479:
    lea rsi, [rip + .L__s3_failure_prefix_479]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_480:
    lea rsi, [rip + .L__s3_failure_prefix_480]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_481:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_481]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_481]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_482:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_482]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_482]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_483:
    lea rsi, [rip + .L__s3_failure_prefix_483]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_484:
    lea rsi, [rip + .L__s3_failure_prefix_484]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_485:
    lea rsi, [rip + .L__s3_failure_prefix_485]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_486:
    lea rsi, [rip + .L__s3_failure_prefix_486]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_487:
    lea rsi, [rip + .L__s3_failure_prefix_487]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_488:
    lea rsi, [rip + .L__s3_failure_prefix_488]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_489:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_489]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_489]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_490:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_490]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_490]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_491:
    lea rsi, [rip + .L__s3_failure_prefix_491]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_492:
    lea rsi, [rip + .L__s3_failure_prefix_492]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_493:
    lea rsi, [rip + .L__s3_failure_prefix_493]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_494:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_494]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_494]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_495:
    lea rsi, [rip + .L__s3_failure_prefix_495]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_496:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_496]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_496]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_497:
    lea rsi, [rip + .L__s3_failure_prefix_497]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_498:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_498]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_498]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_499:
    lea rsi, [rip + .L__s3_failure_prefix_499]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_500:
    lea rsi, [rip + .L__s3_failure_prefix_500]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_501:
    lea rsi, [rip + .L__s3_failure_prefix_501]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_502:
    lea rsi, [rip + .L__s3_failure_prefix_502]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_503:
    lea rsi, [rip + .L__s3_failure_prefix_503]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_504:
    lea rsi, [rip + .L__s3_failure_prefix_504]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_505:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_505]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_505]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_506:
    lea rsi, [rip + .L__s3_failure_prefix_506]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_507:
    lea rsi, [rip + .L__s3_failure_prefix_507]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_508:
    lea rsi, [rip + .L__s3_failure_prefix_508]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_509:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_509]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_509]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_510:
    lea rsi, [rip + .L__s3_failure_prefix_510]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_511:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_511]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_511]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_512:
    lea rsi, [rip + .L__s3_failure_prefix_512]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_513:
    lea rsi, [rip + .L__s3_failure_prefix_513]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_514:
    lea rsi, [rip + .L__s3_failure_prefix_514]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_515:
    lea rsi, [rip + .L__s3_failure_prefix_515]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_516:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_516]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_516]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_517:
    lea rsi, [rip + .L__s3_failure_prefix_517]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_518:
    lea rsi, [rip + .L__s3_failure_prefix_518]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_519:
    lea rsi, [rip + .L__s3_failure_prefix_519]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_520:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_520]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_520]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_521:
    lea rsi, [rip + .L__s3_failure_prefix_521]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_522:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_522]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_522]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_523:
    lea rsi, [rip + .L__s3_failure_prefix_523]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_524:
    lea rsi, [rip + .L__s3_failure_prefix_524]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_525:
    lea rsi, [rip + .L__s3_failure_prefix_525]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_526:
    lea rsi, [rip + .L__s3_failure_prefix_526]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_527:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_527]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_527]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_528:
    lea rsi, [rip + .L__s3_failure_prefix_528]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_529:
    lea rsi, [rip + .L__s3_failure_prefix_529]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_530:
    lea rsi, [rip + .L__s3_failure_prefix_530]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_531:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_531]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_531]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_532:
    lea rsi, [rip + .L__s3_failure_prefix_532]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_533:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_533]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_533]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_534:
    lea rsi, [rip + .L__s3_failure_prefix_534]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_535:
    lea rsi, [rip + .L__s3_failure_prefix_535]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_536:
    lea rsi, [rip + .L__s3_failure_prefix_536]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_537:
    lea rsi, [rip + .L__s3_failure_prefix_537]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_538:
    lea rsi, [rip + .L__s3_failure_prefix_538]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_539:
    lea rsi, [rip + .L__s3_failure_prefix_539]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_540:
    lea rsi, [rip + .L__s3_failure_prefix_540]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_541:
    lea rsi, [rip + .L__s3_failure_prefix_541]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_542:
    lea rsi, [rip + .L__s3_failure_prefix_542]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_543:
    lea rsi, [rip + .L__s3_failure_prefix_543]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_544:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_544]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_544]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_545:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_545]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_545]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_546:
    lea rsi, [rip + .L__s3_failure_prefix_546]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_547:
    lea rsi, [rip + .L__s3_failure_prefix_547]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_548:
    lea rsi, [rip + .L__s3_failure_prefix_548]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_549:
    lea rsi, [rip + .L__s3_failure_prefix_549]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_550:
    lea rsi, [rip + .L__s3_failure_prefix_550]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_551:
    lea rsi, [rip + .L__s3_failure_prefix_551]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_552:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_552]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_552]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_553:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_553]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_553]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_554:
    lea rsi, [rip + .L__s3_failure_prefix_554]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_555:
    lea rsi, [rip + .L__s3_failure_prefix_555]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_556:
    lea rsi, [rip + .L__s3_failure_prefix_556]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_557:
    lea rsi, [rip + .L__s3_failure_prefix_557]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_558:
    lea rsi, [rip + .L__s3_failure_prefix_558]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_559:
    lea rsi, [rip + .L__s3_failure_prefix_559]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_560:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_560]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_560]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_561:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_561]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_561]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_562:
    lea rsi, [rip + .L__s3_failure_prefix_562]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_563:
    lea rsi, [rip + .L__s3_failure_prefix_563]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_564:
    lea rsi, [rip + .L__s3_failure_prefix_564]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_565:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_565]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_565]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_566:
    lea rsi, [rip + .L__s3_failure_prefix_566]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_567:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_567]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_567]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_568:
    lea rsi, [rip + .L__s3_failure_prefix_568]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_569:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_569]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_569]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_570:
    lea rsi, [rip + .L__s3_failure_prefix_570]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_571:
    lea rsi, [rip + .L__s3_failure_prefix_571]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_572:
    lea rsi, [rip + .L__s3_failure_prefix_572]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_573:
    lea rsi, [rip + .L__s3_failure_prefix_573]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_574:
    lea rsi, [rip + .L__s3_failure_prefix_574]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_575:
    lea rsi, [rip + .L__s3_failure_prefix_575]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_576:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_576]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_576]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_577:
    lea rsi, [rip + .L__s3_failure_prefix_577]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_578:
    lea rsi, [rip + .L__s3_failure_prefix_578]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_579:
    lea rsi, [rip + .L__s3_failure_prefix_579]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_580:
    lea rsi, [rip + .L__s3_failure_prefix_580]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_581:
    lea rsi, [rip + .L__s3_failure_prefix_581]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_582:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_582]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_582]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_583:
    lea rsi, [rip + .L__s3_failure_prefix_583]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_584:
    lea rsi, [rip + .L__s3_failure_prefix_584]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_585:
    lea rsi, [rip + .L__s3_failure_prefix_585]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_586:
    lea rsi, [rip + .L__s3_failure_prefix_586]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_587:
    lea rsi, [rip + .L__s3_failure_prefix_587]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_588:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_588]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_588]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_589:
    lea rsi, [rip + .L__s3_failure_prefix_589]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_590:
    lea rsi, [rip + .L__s3_failure_prefix_590]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_591:
    lea rsi, [rip + .L__s3_failure_prefix_591]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_592:
    lea rsi, [rip + .L__s3_failure_prefix_592]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_593:
    lea rsi, [rip + .L__s3_failure_prefix_593]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_594:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_594]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_594]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_595:
    lea rsi, [rip + .L__s3_failure_prefix_595]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_596:
    lea rsi, [rip + .L__s3_failure_prefix_596]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_597:
    lea rsi, [rip + .L__s3_failure_prefix_597]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_598:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_598]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_598]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_599:
    lea rsi, [rip + .L__s3_failure_prefix_599]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_600:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_600]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_600]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_601:
    lea rsi, [rip + .L__s3_failure_prefix_601]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_602:
    lea rsi, [rip + .L__s3_failure_prefix_602]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_603:
    lea rsi, [rip + .L__s3_failure_prefix_603]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_604:
    lea rsi, [rip + .L__s3_failure_prefix_604]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_605:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_605]
    mov edx, 131
    lea rcx, [rip + .L__s3_failure_suffix_605]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_606:
    lea rsi, [rip + .L__s3_failure_prefix_606]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_607:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_607]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_607]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_608:
    lea rsi, [rip + .L__s3_failure_prefix_608]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_609:
    lea rsi, [rip + .L__s3_failure_prefix_609]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_610:
    lea rsi, [rip + .L__s3_failure_prefix_610]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_611:
    lea rsi, [rip + .L__s3_failure_prefix_611]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_612:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_612]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_612]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_613:
    lea rsi, [rip + .L__s3_failure_prefix_613]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_614:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_614]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_614]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_615:
    lea rsi, [rip + .L__s3_failure_prefix_615]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_616:
    lea rsi, [rip + .L__s3_failure_prefix_616]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_617:
    lea rsi, [rip + .L__s3_failure_prefix_617]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_618:
    lea rsi, [rip + .L__s3_failure_prefix_618]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_619:
    lea rsi, [rip + .L__s3_failure_prefix_619]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_620:
    lea rsi, [rip + .L__s3_failure_prefix_620]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_621:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_621]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_621]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_622:
    lea rsi, [rip + .L__s3_failure_prefix_622]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_623:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_623]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_623]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_624:
    lea rsi, [rip + .L__s3_failure_prefix_624]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_625:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_625]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_625]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_626:
    lea rsi, [rip + .L__s3_failure_prefix_626]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_627:
    lea rsi, [rip + .L__s3_failure_prefix_627]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_628:
    lea rsi, [rip + .L__s3_failure_prefix_628]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_629:
    lea rsi, [rip + .L__s3_failure_prefix_629]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_630:
    lea rsi, [rip + .L__s3_failure_prefix_630]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_631:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_631]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_631]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_632:
    lea rsi, [rip + .L__s3_failure_prefix_632]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_633:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_633]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_633]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_634:
    lea rsi, [rip + .L__s3_failure_prefix_634]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_635:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_635]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_635]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_636:
    lea rsi, [rip + .L__s3_failure_prefix_636]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_637:
    lea rsi, [rip + .L__s3_failure_prefix_637]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_638:
    lea rsi, [rip + .L__s3_failure_prefix_638]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_639:
    lea rsi, [rip + .L__s3_failure_prefix_639]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_640:
    lea rsi, [rip + .L__s3_failure_prefix_640]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_641:
    lea rsi, [rip + .L__s3_failure_prefix_641]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_642:
    lea rsi, [rip + .L__s3_failure_prefix_642]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_643:
    lea rsi, [rip + .L__s3_failure_prefix_643]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_644:
    lea rsi, [rip + .L__s3_failure_prefix_644]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_645:
    lea rsi, [rip + .L__s3_failure_prefix_645]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_646:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_646]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_646]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_647:
    lea rsi, [rip + .L__s3_failure_prefix_647]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_648:
    lea rsi, [rip + .L__s3_failure_prefix_648]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_649:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_649]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_649]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_650:
    lea rsi, [rip + .L__s3_failure_prefix_650]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_651:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_651]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_651]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_652:
    lea rsi, [rip + .L__s3_failure_prefix_652]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_653:
    lea rsi, [rip + .L__s3_failure_prefix_653]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_654:
    lea rsi, [rip + .L__s3_failure_prefix_654]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_655:
    lea rsi, [rip + .L__s3_failure_prefix_655]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_656:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_656]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_656]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_657:
    lea rsi, [rip + .L__s3_failure_prefix_657]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_658:
    lea rsi, [rip + .L__s3_failure_prefix_658]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_659:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_659]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_659]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_660:
    lea rsi, [rip + .L__s3_failure_prefix_660]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_661:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_661]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_661]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_662:
    lea rsi, [rip + .L__s3_failure_prefix_662]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_663:
    lea rsi, [rip + .L__s3_failure_prefix_663]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_664:
    lea rsi, [rip + .L__s3_failure_prefix_664]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_665:
    lea rsi, [rip + .L__s3_failure_prefix_665]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_666:
    lea rsi, [rip + .L__s3_failure_prefix_666]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_667:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_667]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_667]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_668:
    lea rsi, [rip + .L__s3_failure_prefix_668]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_669:
    lea rsi, [rip + .L__s3_failure_prefix_669]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_670:
    lea rsi, [rip + .L__s3_failure_prefix_670]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_671:
    lea rsi, [rip + .L__s3_failure_prefix_671]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_672:
    lea rsi, [rip + .L__s3_failure_prefix_672]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_673:
    lea rsi, [rip + .L__s3_failure_prefix_673]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_674:
    lea rsi, [rip + .L__s3_failure_prefix_674]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_675:
    lea rsi, [rip + .L__s3_failure_prefix_675]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_676:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_676]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_676]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_677:
    lea rsi, [rip + .L__s3_failure_prefix_677]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_678:
    lea rsi, [rip + .L__s3_failure_prefix_678]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_679:
    lea rsi, [rip + .L__s3_failure_prefix_679]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_680:
    lea rsi, [rip + .L__s3_failure_prefix_680]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_681:
    lea rsi, [rip + .L__s3_failure_prefix_681]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_682:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_682]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_682]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_683:
    lea rsi, [rip + .L__s3_failure_prefix_683]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_684:
    lea rsi, [rip + .L__s3_failure_prefix_684]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_685:
    lea rsi, [rip + .L__s3_failure_prefix_685]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_686:
    lea rsi, [rip + .L__s3_failure_prefix_686]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_687:
    lea rsi, [rip + .L__s3_failure_prefix_687]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_688:
    lea rsi, [rip + .L__s3_failure_prefix_688]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_689:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_689]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_689]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_690:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_690]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_690]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_691:
    lea rsi, [rip + .L__s3_failure_prefix_691]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_692:
    lea rsi, [rip + .L__s3_failure_prefix_692]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_693:
    lea rsi, [rip + .L__s3_failure_prefix_693]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_694:
    lea rsi, [rip + .L__s3_failure_prefix_694]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_695:
    lea rsi, [rip + .L__s3_failure_prefix_695]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_696:
    lea rsi, [rip + .L__s3_failure_prefix_696]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_697:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_697]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_697]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_698:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_698]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_698]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_699:
    lea rsi, [rip + .L__s3_failure_prefix_699]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_700:
    lea rsi, [rip + .L__s3_failure_prefix_700]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_701:
    lea rsi, [rip + .L__s3_failure_prefix_701]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_702:
    lea rsi, [rip + .L__s3_failure_prefix_702]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_703:
    lea rsi, [rip + .L__s3_failure_prefix_703]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_704:
    lea rsi, [rip + .L__s3_failure_prefix_704]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_705:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_705]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_705]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_706:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_706]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_706]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_707:
    lea rsi, [rip + .L__s3_failure_prefix_707]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_708:
    lea rsi, [rip + .L__s3_failure_prefix_708]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_709:
    lea rsi, [rip + .L__s3_failure_prefix_709]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_710:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_710]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_710]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_711:
    lea rsi, [rip + .L__s3_failure_prefix_711]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_712:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_712]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_712]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_713:
    lea rsi, [rip + .L__s3_failure_prefix_713]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_714:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_714]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_714]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_715:
    lea rsi, [rip + .L__s3_failure_prefix_715]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_716:
    lea rsi, [rip + .L__s3_failure_prefix_716]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_717:
    lea rsi, [rip + .L__s3_failure_prefix_717]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_718:
    lea rsi, [rip + .L__s3_failure_prefix_718]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_719:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_719]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_719]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_720:
    lea rsi, [rip + .L__s3_failure_prefix_720]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_721:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_721]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_721]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_722:
    lea rsi, [rip + .L__s3_failure_prefix_722]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_723:
    lea rsi, [rip + .L__s3_failure_prefix_723]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_724:
    lea rsi, [rip + .L__s3_failure_prefix_724]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_725:
    lea rsi, [rip + .L__s3_failure_prefix_725]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_726:
    lea rsi, [rip + .L__s3_failure_prefix_726]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_727:
    lea rsi, [rip + .L__s3_failure_prefix_727]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_728:
    lea rsi, [rip + .L__s3_failure_prefix_728]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_729:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_729]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_729]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_730:
    lea rsi, [rip + .L__s3_failure_prefix_730]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_731:
    lea rsi, [rip + .L__s3_failure_prefix_731]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_732:
    lea rsi, [rip + .L__s3_failure_prefix_732]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_733:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_733]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_733]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_734:
    lea rsi, [rip + .L__s3_failure_prefix_734]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_735:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_735]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_735]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_736:
    lea rsi, [rip + .L__s3_failure_prefix_736]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_737:
    lea rsi, [rip + .L__s3_failure_prefix_737]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_738:
    lea rsi, [rip + .L__s3_failure_prefix_738]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_739:
    lea rsi, [rip + .L__s3_failure_prefix_739]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_740:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_740]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_740]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_741:
    lea rsi, [rip + .L__s3_failure_prefix_741]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_742:
    lea rsi, [rip + .L__s3_failure_prefix_742]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_743:
    lea rsi, [rip + .L__s3_failure_prefix_743]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_744:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_744]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_744]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_745:
    lea rsi, [rip + .L__s3_failure_prefix_745]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_746:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_746]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_746]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_747:
    lea rsi, [rip + .L__s3_failure_prefix_747]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_748:
    lea rsi, [rip + .L__s3_failure_prefix_748]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_749:
    lea rsi, [rip + .L__s3_failure_prefix_749]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_750:
    lea rsi, [rip + .L__s3_failure_prefix_750]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_751:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_751]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_751]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_752:
    lea rsi, [rip + .L__s3_failure_prefix_752]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_753:
    lea rsi, [rip + .L__s3_failure_prefix_753]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_754:
    lea rsi, [rip + .L__s3_failure_prefix_754]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_755:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_755]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_755]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_756:
    lea rsi, [rip + .L__s3_failure_prefix_756]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_757:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_757]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_757]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_758:
    lea rsi, [rip + .L__s3_failure_prefix_758]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_759:
    lea rsi, [rip + .L__s3_failure_prefix_759]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_760:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_760]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_760]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_761:
    lea rsi, [rip + .L__s3_failure_prefix_761]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_762:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_762]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_762]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_763:
    lea rsi, [rip + .L__s3_failure_prefix_763]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_764:
    lea rsi, [rip + .L__s3_failure_prefix_764]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_765:
    lea rsi, [rip + .L__s3_failure_prefix_765]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_766:
    lea rsi, [rip + .L__s3_failure_prefix_766]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_767:
    lea rsi, [rip + .L__s3_failure_prefix_767]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_768:
    lea rsi, [rip + .L__s3_failure_prefix_768]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_769:
    lea rsi, [rip + .L__s3_failure_prefix_769]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_770:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_770]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_770]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_771:
    lea rsi, [rip + .L__s3_failure_prefix_771]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_772:
    lea rsi, [rip + .L__s3_failure_prefix_772]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_773:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_773]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_773]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_774:
    lea rsi, [rip + .L__s3_failure_prefix_774]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_775:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_775]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_775]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_776:
    lea rsi, [rip + .L__s3_failure_prefix_776]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_777:
    lea rsi, [rip + .L__s3_failure_prefix_777]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_778:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_778]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_778]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_779:
    lea rsi, [rip + .L__s3_failure_prefix_779]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_780:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_780]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_780]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_781:
    lea rsi, [rip + .L__s3_failure_prefix_781]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_782:
    lea rsi, [rip + .L__s3_failure_prefix_782]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_783:
    lea rsi, [rip + .L__s3_failure_prefix_783]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_784:
    lea rsi, [rip + .L__s3_failure_prefix_784]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_785:
    lea rsi, [rip + .L__s3_failure_prefix_785]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_786:
    lea rsi, [rip + .L__s3_failure_prefix_786]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_787:
    lea rsi, [rip + .L__s3_failure_prefix_787]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_788:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_788]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_788]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_789:
    lea rsi, [rip + .L__s3_failure_prefix_789]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_790:
    lea rsi, [rip + .L__s3_failure_prefix_790]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_791:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_791]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_791]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_792:
    lea rsi, [rip + .L__s3_failure_prefix_792]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_793:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_793]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_793]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_794:
    lea rsi, [rip + .L__s3_failure_prefix_794]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_795:
    lea rsi, [rip + .L__s3_failure_prefix_795]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_796:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_796]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_796]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_797:
    lea rsi, [rip + .L__s3_failure_prefix_797]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_798:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_798]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_798]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_799:
    lea rsi, [rip + .L__s3_failure_prefix_799]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_800:
    lea rsi, [rip + .L__s3_failure_prefix_800]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_801:
    lea rsi, [rip + .L__s3_failure_prefix_801]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_802:
    lea rsi, [rip + .L__s3_failure_prefix_802]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_803:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_803]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_803]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_804:
    lea rsi, [rip + .L__s3_failure_prefix_804]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_805:
    lea rsi, [rip + .L__s3_failure_prefix_805]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_806:
    lea rsi, [rip + .L__s3_failure_prefix_806]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_807:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_807]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_807]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_808:
    lea rsi, [rip + .L__s3_failure_prefix_808]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_809:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_809]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_809]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_810:
    lea rsi, [rip + .L__s3_failure_prefix_810]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_811:
    lea rsi, [rip + .L__s3_failure_prefix_811]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_812:
    lea rsi, [rip + .L__s3_failure_prefix_812]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_813:
    lea rsi, [rip + .L__s3_failure_prefix_813]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_814:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_814]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_814]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_815:
    lea rsi, [rip + .L__s3_failure_prefix_815]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_816:
    lea rsi, [rip + .L__s3_failure_prefix_816]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_817:
    lea rsi, [rip + .L__s3_failure_prefix_817]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_818:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_818]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_818]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_819:
    lea rsi, [rip + .L__s3_failure_prefix_819]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_820:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_820]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_820]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_821:
    lea rsi, [rip + .L__s3_failure_prefix_821]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_822:
    lea rsi, [rip + .L__s3_failure_prefix_822]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_823:
    lea rsi, [rip + .L__s3_failure_prefix_823]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_824:
    lea rsi, [rip + .L__s3_failure_prefix_824]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_825:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_825]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_825]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_826:
    lea rsi, [rip + .L__s3_failure_prefix_826]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_827:
    lea rsi, [rip + .L__s3_failure_prefix_827]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_828:
    lea rsi, [rip + .L__s3_failure_prefix_828]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_829:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_829]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_829]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_830:
    lea rsi, [rip + .L__s3_failure_prefix_830]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_831:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_831]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_831]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_832:
    lea rsi, [rip + .L__s3_failure_prefix_832]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_833:
    lea rsi, [rip + .L__s3_failure_prefix_833]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_834:
    lea rsi, [rip + .L__s3_failure_prefix_834]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_835:
    lea rsi, [rip + .L__s3_failure_prefix_835]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_836:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_836]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_836]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_837:
    lea rsi, [rip + .L__s3_failure_prefix_837]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_838:
    lea rsi, [rip + .L__s3_failure_prefix_838]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_839:
    lea rsi, [rip + .L__s3_failure_prefix_839]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_840:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_840]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_840]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_841:
    lea rsi, [rip + .L__s3_failure_prefix_841]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_842:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_842]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_842]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_843:
    lea rsi, [rip + .L__s3_failure_prefix_843]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_844:
    lea rsi, [rip + .L__s3_failure_prefix_844]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_845:
    lea rsi, [rip + .L__s3_failure_prefix_845]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_846:
    lea rsi, [rip + .L__s3_failure_prefix_846]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_847:
    lea rsi, [rip + .L__s3_failure_prefix_847]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_848:
    lea rsi, [rip + .L__s3_failure_prefix_848]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_849:
    lea rsi, [rip + .L__s3_failure_prefix_849]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_850:
    lea rsi, [rip + .L__s3_failure_prefix_850]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_851:
    lea rsi, [rip + .L__s3_failure_prefix_851]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_852:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_852]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_852]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_853:
    lea rsi, [rip + .L__s3_failure_prefix_853]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_854:
    lea rsi, [rip + .L__s3_failure_prefix_854]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_855:
    lea rsi, [rip + .L__s3_failure_prefix_855]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_856:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_856]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_856]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_857:
    lea rsi, [rip + .L__s3_failure_prefix_857]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_858:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_858]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_858]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_859:
    lea rsi, [rip + .L__s3_failure_prefix_859]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_860:
    lea rsi, [rip + .L__s3_failure_prefix_860]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_861:
    lea rsi, [rip + .L__s3_failure_prefix_861]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_862:
    lea rsi, [rip + .L__s3_failure_prefix_862]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_863:
    lea rsi, [rip + .L__s3_failure_prefix_863]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_864:
    lea rsi, [rip + .L__s3_failure_prefix_864]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_865:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_865]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_865]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_866:
    lea rsi, [rip + .L__s3_failure_prefix_866]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_867:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_867]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_867]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_868:
    lea rsi, [rip + .L__s3_failure_prefix_868]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_869:
    lea rsi, [rip + .L__s3_failure_prefix_869]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_870:
    lea rsi, [rip + .L__s3_failure_prefix_870]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_871:
    lea rsi, [rip + .L__s3_failure_prefix_871]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_872:
    lea rsi, [rip + .L__s3_failure_prefix_872]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_873:
    lea rsi, [rip + .L__s3_failure_prefix_873]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_874:
    lea rsi, [rip + .L__s3_failure_prefix_874]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_875:
    lea rsi, [rip + .L__s3_failure_prefix_875]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_876:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_876]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_876]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_877:
    lea rsi, [rip + .L__s3_failure_prefix_877]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_878:
    lea rsi, [rip + .L__s3_failure_prefix_878]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_879:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_879]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_879]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_880:
    lea rsi, [rip + .L__s3_failure_prefix_880]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_881:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_881]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_881]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_882:
    lea rsi, [rip + .L__s3_failure_prefix_882]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_883:
    lea rsi, [rip + .L__s3_failure_prefix_883]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_884:
    lea rsi, [rip + .L__s3_failure_prefix_884]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_885:
    lea rsi, [rip + .L__s3_failure_prefix_885]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_886:
    lea rsi, [rip + .L__s3_failure_prefix_886]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_887:
    lea rsi, [rip + .L__s3_failure_prefix_887]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_888:
    lea rsi, [rip + .L__s3_failure_prefix_888]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_889:
    lea rsi, [rip + .L__s3_failure_prefix_889]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_890:
    lea rsi, [rip + .L__s3_failure_prefix_890]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_891:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_891]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_891]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_892:
    lea rsi, [rip + .L__s3_failure_prefix_892]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_893:
    lea rsi, [rip + .L__s3_failure_prefix_893]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_894:
    lea rsi, [rip + .L__s3_failure_prefix_894]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_895:
    lea rsi, [rip + .L__s3_failure_prefix_895]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_896:
    lea rsi, [rip + .L__s3_failure_prefix_896]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_897:
    lea rsi, [rip + .L__s3_failure_prefix_897]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_898:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_898]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_898]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_899:
    lea rsi, [rip + .L__s3_failure_prefix_899]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_900:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_900]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_900]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_901:
    lea rsi, [rip + .L__s3_failure_prefix_901]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_902:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_902]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_902]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_903:
    lea rsi, [rip + .L__s3_failure_prefix_903]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_904:
    lea rsi, [rip + .L__s3_failure_prefix_904]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_905:
    lea rsi, [rip + .L__s3_failure_prefix_905]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_906:
    lea rsi, [rip + .L__s3_failure_prefix_906]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_907:
    lea rsi, [rip + .L__s3_failure_prefix_907]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_908:
    lea rsi, [rip + .L__s3_failure_prefix_908]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_909:
    lea rsi, [rip + .L__s3_failure_prefix_909]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_910:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_910]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_910]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_911:
    lea rsi, [rip + .L__s3_failure_prefix_911]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_912:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_912]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_912]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_913:
    lea rsi, [rip + .L__s3_failure_prefix_913]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_914:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_914]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_914]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_915:
    lea rsi, [rip + .L__s3_failure_prefix_915]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_916:
    lea rsi, [rip + .L__s3_failure_prefix_916]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_917:
    lea rsi, [rip + .L__s3_failure_prefix_917]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_918:
    lea rsi, [rip + .L__s3_failure_prefix_918]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_919:
    lea rsi, [rip + .L__s3_failure_prefix_919]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_920:
    lea rsi, [rip + .L__s3_failure_prefix_920]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_921:
    lea rsi, [rip + .L__s3_failure_prefix_921]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_922:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_922]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_922]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_923:
    lea rsi, [rip + .L__s3_failure_prefix_923]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_924:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_924]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_924]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_925:
    lea rsi, [rip + .L__s3_failure_prefix_925]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_926:
    lea rsi, [rip + .L__s3_failure_prefix_926]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_927:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_927]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_927]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_928:
    lea rsi, [rip + .L__s3_failure_prefix_928]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_929:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_929]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_929]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_930:
    lea rsi, [rip + .L__s3_failure_prefix_930]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_931:
    lea rsi, [rip + .L__s3_failure_prefix_931]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_932:
    lea rsi, [rip + .L__s3_failure_prefix_932]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_933:
    lea rsi, [rip + .L__s3_failure_prefix_933]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_934:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_934]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_934]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_935:
    lea rsi, [rip + .L__s3_failure_prefix_935]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_936:
    lea rsi, [rip + .L__s3_failure_prefix_936]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_937:
    lea rsi, [rip + .L__s3_failure_prefix_937]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_938:
    lea rsi, [rip + .L__s3_failure_prefix_938]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_939:
    lea rsi, [rip + .L__s3_failure_prefix_939]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_940:
    lea rsi, [rip + .L__s3_failure_prefix_940]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_941:
    lea rsi, [rip + .L__s3_failure_prefix_941]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_942:
    lea rsi, [rip + .L__s3_failure_prefix_942]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_943:
    lea rsi, [rip + .L__s3_failure_prefix_943]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_944:
    lea rsi, [rip + .L__s3_failure_prefix_944]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_945:
    lea rsi, [rip + .L__s3_failure_prefix_945]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_946:
    lea rsi, [rip + .L__s3_failure_prefix_946]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_947:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_947]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_947]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_948:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_948]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_948]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_949:
    lea rsi, [rip + .L__s3_failure_prefix_949]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_950:
    lea rsi, [rip + .L__s3_failure_prefix_950]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_951:
    lea rsi, [rip + .L__s3_failure_prefix_951]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_952:
    lea rsi, [rip + .L__s3_failure_prefix_952]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_953:
    lea rsi, [rip + .L__s3_failure_prefix_953]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_954:
    lea rsi, [rip + .L__s3_failure_prefix_954]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_955:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_955]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_955]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_956:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_956]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_956]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_957:
    lea rsi, [rip + .L__s3_failure_prefix_957]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_958:
    lea rsi, [rip + .L__s3_failure_prefix_958]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_959:
    lea rsi, [rip + .L__s3_failure_prefix_959]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_960:
    lea rsi, [rip + .L__s3_failure_prefix_960]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_961:
    lea rsi, [rip + .L__s3_failure_prefix_961]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_962:
    lea rsi, [rip + .L__s3_failure_prefix_962]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_963:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_963]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_963]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_964:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_964]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_964]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_965:
    lea rsi, [rip + .L__s3_failure_prefix_965]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_966:
    lea rsi, [rip + .L__s3_failure_prefix_966]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_967:
    lea rsi, [rip + .L__s3_failure_prefix_967]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_968:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_968]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_968]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_969:
    lea rsi, [rip + .L__s3_failure_prefix_969]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_970:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_970]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_970]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_971:
    lea rsi, [rip + .L__s3_failure_prefix_971]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_972:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_972]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_972]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_973:
    lea rsi, [rip + .L__s3_failure_prefix_973]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_974:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_974]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_974]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_975:
    lea rsi, [rip + .L__s3_failure_prefix_975]
    mov edx, 127
    jmp __s3_fail_message
.L__s3_failure_site_976:
    lea rsi, [rip + .L__s3_failure_prefix_976]
    mov edx, 124
    jmp __s3_fail_message

.section .rodata
.L__s3_failure_prefix_0:
    .ascii "runtime error [frame limit] in function 'agent_energy_residual'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_0:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_1:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 4:23 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_2:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 4:5 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_3:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 4:5 (block entry, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_4:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 4:5 (block entry, TSTORE): register r8 is uninitialized\n"
.L__s3_failure_prefix_5:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 4:5 (block entry, TSTORE): register r7 is uninitialized\n"
.L__s3_failure_prefix_6:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 4:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_6:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_7:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:20 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_8:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block entry, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_9:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block entry, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_10:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block entry, TCMP): register r9 is uninitialized\n"
.L__s3_failure_prefix_11:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block entry, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_12:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_13:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_14:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_15:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): register r11 is uninitialized\n"
.L__s3_failure_prefix_16:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): register r12 is uninitialized\n"
.L__s3_failure_prefix_17:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): index "
.L__s3_failure_suffix_17:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_18:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TSTORE): trit result "
.L__s3_failure_suffix_18:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_19:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_neg_0, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_20:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_21:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_22:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_23:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): register r13 is uninitialized\n"
.L__s3_failure_prefix_24:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): register r14 is uninitialized\n"
.L__s3_failure_prefix_25:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): index "
.L__s3_failure_suffix_25:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_26:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TSTORE): trit result "
.L__s3_failure_suffix_26:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_27:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_zero_1, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_28:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_29:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_30:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_31:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): register r15 is uninitialized\n"
.L__s3_failure_prefix_32:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): register r16 is uninitialized\n"
.L__s3_failure_prefix_33:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): index "
.L__s3_failure_suffix_33:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_34:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TSTORE): trit result "
.L__s3_failure_suffix_34:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_35:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_pos_2, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_36:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_37:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_38:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TLOAD): index "
.L__s3_failure_suffix_38:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_39:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TLOAD): register r17 is uninitialized\n"
.L__s3_failure_prefix_40:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 5:17 (block rel_cont_3, TLOAD): index "
.L__s3_failure_suffix_40:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_41:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 5:5 (block rel_cont_3, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_42:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 5:5 (block rel_cont_3, TBR3): value "
.L__s3_failure_suffix_42:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_43:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 5:5 (block rel_cont_3, TBR3): register r18 is uninitialized\n"
.L__s3_failure_prefix_44:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 7:22 (block switch_negative_4, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_45:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_46:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_47:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TSTORE): register r20 is uninitialized\n"
.L__s3_failure_prefix_48:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TSTORE): register r19 is uninitialized\n"
.L__s3_failure_prefix_49:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 7:13 (block switch_negative_4, TSTORE): index "
.L__s3_failure_suffix_49:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_50:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 6:9 (block switch_negative_4, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_51:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_52:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_53:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TLOAD): index "
.L__s3_failure_suffix_53:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_54:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TLOAD): register r21 is uninitialized\n"
.L__s3_failure_prefix_55:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 9:22 (block switch_neutral_5, TLOAD): index "
.L__s3_failure_suffix_55:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_56:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_57:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_58:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TSTORE): register r23 is uninitialized\n"
.L__s3_failure_prefix_59:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TSTORE): register r22 is uninitialized\n"
.L__s3_failure_prefix_60:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 9:13 (block switch_neutral_5, TSTORE): index "
.L__s3_failure_suffix_60:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_61:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 8:9 (block switch_neutral_5, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_62:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_63:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_64:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TLOAD): index "
.L__s3_failure_suffix_64:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_65:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TLOAD): register r24 is uninitialized\n"
.L__s3_failure_prefix_66:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 11:22 (block switch_positive_6, TLOAD): index "
.L__s3_failure_suffix_66:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_67:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_68:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_69:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TSTORE): register r26 is uninitialized\n"
.L__s3_failure_prefix_70:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TSTORE): register r25 is uninitialized\n"
.L__s3_failure_prefix_71:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 11:13 (block switch_positive_6, TSTORE): index "
.L__s3_failure_suffix_71:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_72:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 10:9 (block switch_positive_6, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_73:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:19 (block switch_continue_7, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_74:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block switch_continue_7, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_75:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block switch_continue_7, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_76:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block switch_continue_7, TCMP): register r27 is uninitialized\n"
.L__s3_failure_prefix_77:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block switch_continue_7, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_78:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_79:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_80:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_81:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): register r29 is uninitialized\n"
.L__s3_failure_prefix_82:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): register r30 is uninitialized\n"
.L__s3_failure_prefix_83:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): index "
.L__s3_failure_suffix_83:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_84:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TSTORE): trit result "
.L__s3_failure_suffix_84:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_85:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_neg_8, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_86:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_87:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_88:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_89:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): register r31 is uninitialized\n"
.L__s3_failure_prefix_90:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): register r32 is uninitialized\n"
.L__s3_failure_prefix_91:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): index "
.L__s3_failure_suffix_91:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_92:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TSTORE): trit result "
.L__s3_failure_suffix_92:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_93:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_zero_9, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_94:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_95:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_96:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_97:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): register r33 is uninitialized\n"
.L__s3_failure_prefix_98:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): register r34 is uninitialized\n"
.L__s3_failure_prefix_99:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): index "
.L__s3_failure_suffix_99:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_100:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TSTORE): trit result "
.L__s3_failure_suffix_100:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_101:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_pos_10, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_102:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_103:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_104:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TLOAD): index "
.L__s3_failure_suffix_104:
    .ascii " is uninitialized in m2\n"
.L__s3_failure_prefix_105:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TLOAD): register r35 is uninitialized\n"
.L__s3_failure_prefix_106:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 12:17 (block rel_cont_11, TLOAD): index "
.L__s3_failure_suffix_106:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_107:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 12:5 (block rel_cont_11, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_108:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 12:5 (block rel_cont_11, TBR3): value "
.L__s3_failure_suffix_108:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_109:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 12:5 (block rel_cont_11, TBR3): register r36 is uninitialized\n"
.L__s3_failure_prefix_110:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 14:22 (block switch_negative_12, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_111:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_112:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_113:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TSTORE): register r38 is uninitialized\n"
.L__s3_failure_prefix_114:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TSTORE): register r37 is uninitialized\n"
.L__s3_failure_prefix_115:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 14:13 (block switch_negative_12, TSTORE): index "
.L__s3_failure_suffix_115:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_116:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 13:9 (block switch_negative_12, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_117:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_118:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_119:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_119:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_120:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TLOAD): register r39 is uninitialized\n"
.L__s3_failure_prefix_121:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 16:22 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_121:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_122:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_123:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_124:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TSTORE): register r41 is uninitialized\n"
.L__s3_failure_prefix_125:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TSTORE): register r40 is uninitialized\n"
.L__s3_failure_prefix_126:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 16:13 (block switch_neutral_13, TSTORE): index "
.L__s3_failure_suffix_126:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_127:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 15:9 (block switch_neutral_13, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_128:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_129:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_130:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TLOAD): index "
.L__s3_failure_suffix_130:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_131:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TLOAD): register r42 is uninitialized\n"
.L__s3_failure_prefix_132:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 18:22 (block switch_positive_14, TLOAD): index "
.L__s3_failure_suffix_132:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_133:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_134:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_135:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TSTORE): register r44 is uninitialized\n"
.L__s3_failure_prefix_136:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TSTORE): register r43 is uninitialized\n"
.L__s3_failure_prefix_137:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 18:13 (block switch_positive_14, TSTORE): index "
.L__s3_failure_suffix_137:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_138:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 17:9 (block switch_positive_14, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_139:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_140:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_141:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TLOAD): index "
.L__s3_failure_suffix_141:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_142:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TLOAD): register r45 is uninitialized\n"
.L__s3_failure_prefix_143:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:11 (block switch_continue_15, TLOAD): index "
.L__s3_failure_suffix_143:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_144:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:21 (block switch_continue_15, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_145:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block switch_continue_15, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_146:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block switch_continue_15, TCMP): register r46 is uninitialized\n"
.L__s3_failure_prefix_147:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block switch_continue_15, TCMP): register r47 is uninitialized\n"
.L__s3_failure_prefix_148:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block switch_continue_15, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_149:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_150:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_151:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_152:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): register r49 is uninitialized\n"
.L__s3_failure_prefix_153:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): register r50 is uninitialized\n"
.L__s3_failure_prefix_154:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): index "
.L__s3_failure_suffix_154:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_155:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TSTORE): trit result "
.L__s3_failure_suffix_155:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_156:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_neg_16, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_157:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_158:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_159:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_160:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): register r51 is uninitialized\n"
.L__s3_failure_prefix_161:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): register r52 is uninitialized\n"
.L__s3_failure_prefix_162:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): index "
.L__s3_failure_suffix_162:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_163:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TSTORE): trit result "
.L__s3_failure_suffix_163:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_164:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_zero_17, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_165:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_166:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_167:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_168:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): register r53 is uninitialized\n"
.L__s3_failure_prefix_169:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): register r54 is uninitialized\n"
.L__s3_failure_prefix_170:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): index "
.L__s3_failure_suffix_170:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_171:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TSTORE): trit result "
.L__s3_failure_suffix_171:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_172:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_pos_18, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_173:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_174:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_175:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TLOAD): index "
.L__s3_failure_suffix_175:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_176:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TLOAD): register r55 is uninitialized\n"
.L__s3_failure_prefix_177:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 20:18 (block rel_cont_19, TLOAD): index "
.L__s3_failure_suffix_177:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_178:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 20:5 (block rel_cont_19, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_179:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 20:5 (block rel_cont_19, TBR3): value "
.L__s3_failure_suffix_179:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_180:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 20:5 (block rel_cont_19, TBR3): register r56 is uninitialized\n"
.L__s3_failure_prefix_181:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:19 (block switch_negative_20, TSLEN): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_182:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:19 (block switch_negative_20, TSLEN): register r1 is uninitialized\n"
.L__s3_failure_prefix_183:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block switch_negative_20, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_184:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block switch_negative_20, TCMP): register r57 is uninitialized\n"
.L__s3_failure_prefix_185:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block switch_negative_20, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_186:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block switch_negative_20, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_187:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_188:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_189:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TLOAD): index "
.L__s3_failure_suffix_189:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_190:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TLOAD): register r91 is uninitialized\n"
.L__s3_failure_prefix_191:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 37:22 (block switch_neutral_21, TLOAD): index "
.L__s3_failure_suffix_191:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_192:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_193:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_194:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TSTORE): register r93 is uninitialized\n"
.L__s3_failure_prefix_195:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TSTORE): register r92 is uninitialized\n"
.L__s3_failure_prefix_196:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 37:13 (block switch_neutral_21, TSTORE): index "
.L__s3_failure_suffix_196:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_197:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 36:9 (block switch_neutral_21, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_198:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_199:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_200:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TLOAD): index "
.L__s3_failure_suffix_200:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_201:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TLOAD): register r94 is uninitialized\n"
.L__s3_failure_prefix_202:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 39:22 (block switch_positive_22, TLOAD): index "
.L__s3_failure_suffix_202:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_203:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_204:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_205:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TSTORE): register r96 is uninitialized\n"
.L__s3_failure_prefix_206:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TSTORE): register r95 is uninitialized\n"
.L__s3_failure_prefix_207:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 39:13 (block switch_positive_22, TSTORE): index "
.L__s3_failure_suffix_207:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_208:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 38:9 (block switch_positive_22, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_209:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_210:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_211:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_212:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): register r59 is uninitialized\n"
.L__s3_failure_prefix_213:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): register r60 is uninitialized\n"
.L__s3_failure_prefix_214:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): index "
.L__s3_failure_suffix_214:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_215:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TSTORE): trit result "
.L__s3_failure_suffix_215:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_216:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_neg_23, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_217:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_218:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_219:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_220:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): register r61 is uninitialized\n"
.L__s3_failure_prefix_221:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): register r62 is uninitialized\n"
.L__s3_failure_prefix_222:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): index "
.L__s3_failure_suffix_222:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_223:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TSTORE): trit result "
.L__s3_failure_suffix_223:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_224:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_zero_24, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_225:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_226:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_227:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_228:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): register r63 is uninitialized\n"
.L__s3_failure_prefix_229:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): register r64 is uninitialized\n"
.L__s3_failure_prefix_230:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): index "
.L__s3_failure_suffix_230:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_231:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TSTORE): trit result "
.L__s3_failure_suffix_231:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_232:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_pos_25, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_233:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_234:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_235:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TLOAD): index "
.L__s3_failure_suffix_235:
    .ascii " is uninitialized in m4\n"
.L__s3_failure_prefix_236:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TLOAD): register r65 is uninitialized\n"
.L__s3_failure_prefix_237:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 22:31 (block rel_cont_26, TLOAD): index "
.L__s3_failure_suffix_237:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_238:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 22:13 (block rel_cont_26, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_239:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 22:13 (block rel_cont_26, TBR3): value "
.L__s3_failure_suffix_239:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_240:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 22:13 (block rel_cont_26, TBR3): register r66 is uninitialized\n"
.L__s3_failure_prefix_241:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_242:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_243:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TLOAD): index "
.L__s3_failure_suffix_243:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_244:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TLOAD): register r67 is uninitialized\n"
.L__s3_failure_prefix_245:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 24:30 (block switch_negative_27, TLOAD): index "
.L__s3_failure_suffix_245:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_246:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_247:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_248:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TSTORE): register r69 is uninitialized\n"
.L__s3_failure_prefix_249:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TSTORE): register r68 is uninitialized\n"
.L__s3_failure_prefix_250:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 24:21 (block switch_negative_27, TSTORE): index "
.L__s3_failure_suffix_250:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_251:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 23:17 (block switch_negative_27, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_252:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 26:30 (block switch_neutral_28, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_253:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_254:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_255:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TSTORE): register r71 is uninitialized\n"
.L__s3_failure_prefix_256:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TSTORE): register r70 is uninitialized\n"
.L__s3_failure_prefix_257:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 26:21 (block switch_neutral_28, TSTORE): index "
.L__s3_failure_suffix_257:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_258:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 25:17 (block switch_neutral_28, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_259:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 28:30 (block switch_positive_29, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_260:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_261:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_262:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TSTORE): register r73 is uninitialized\n"
.L__s3_failure_prefix_263:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TSTORE): register r72 is uninitialized\n"
.L__s3_failure_prefix_264:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 28:21 (block switch_positive_29, TSTORE): index "
.L__s3_failure_suffix_264:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_265:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 27:17 (block switch_positive_29, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_266:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:19 (block switch_continue_30, TSLEN): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_267:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:19 (block switch_continue_30, TSLEN): register r3 is uninitialized\n"
.L__s3_failure_prefix_268:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block switch_continue_30, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_269:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block switch_continue_30, TCMP): register r74 is uninitialized\n"
.L__s3_failure_prefix_270:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block switch_continue_30, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_271:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block switch_continue_30, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_272:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_273:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_274:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_275:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): register r76 is uninitialized\n"
.L__s3_failure_prefix_276:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): register r77 is uninitialized\n"
.L__s3_failure_prefix_277:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): index "
.L__s3_failure_suffix_277:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_278:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TSTORE): trit result "
.L__s3_failure_suffix_278:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_279:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_neg_31, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_280:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_281:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_282:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_283:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): register r78 is uninitialized\n"
.L__s3_failure_prefix_284:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): register r79 is uninitialized\n"
.L__s3_failure_prefix_285:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): index "
.L__s3_failure_suffix_285:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_286:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TSTORE): trit result "
.L__s3_failure_suffix_286:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_287:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_zero_32, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_288:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_289:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_290:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_291:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): register r80 is uninitialized\n"
.L__s3_failure_prefix_292:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): register r81 is uninitialized\n"
.L__s3_failure_prefix_293:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): index "
.L__s3_failure_suffix_293:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_294:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TSTORE): trit result "
.L__s3_failure_suffix_294:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_295:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_pos_33, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_296:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_297:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_298:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TLOAD): index "
.L__s3_failure_suffix_298:
    .ascii " is uninitialized in m5\n"
.L__s3_failure_prefix_299:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TLOAD): register r82 is uninitialized\n"
.L__s3_failure_prefix_300:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 29:29 (block rel_cont_34, TLOAD): index "
.L__s3_failure_suffix_300:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_301:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 29:13 (block rel_cont_34, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_302:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 29:13 (block rel_cont_34, TBR3): value "
.L__s3_failure_suffix_302:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_303:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 29:13 (block rel_cont_34, TBR3): register r83 is uninitialized\n"
.L__s3_failure_prefix_304:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_305:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_306:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TLOAD): index "
.L__s3_failure_suffix_306:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_307:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TLOAD): register r84 is uninitialized\n"
.L__s3_failure_prefix_308:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 31:30 (block switch_negative_35, TLOAD): index "
.L__s3_failure_suffix_308:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_309:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_310:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_311:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TSTORE): register r86 is uninitialized\n"
.L__s3_failure_prefix_312:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TSTORE): register r85 is uninitialized\n"
.L__s3_failure_prefix_313:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 31:21 (block switch_negative_35, TSTORE): index "
.L__s3_failure_suffix_313:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_314:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 30:17 (block switch_negative_35, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_315:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 33:30 (block switch_neutral_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_316:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_317:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_318:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TSTORE): register r88 is uninitialized\n"
.L__s3_failure_prefix_319:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TSTORE): register r87 is uninitialized\n"
.L__s3_failure_prefix_320:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 33:21 (block switch_neutral_36, TSTORE): index "
.L__s3_failure_suffix_320:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_321:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 32:17 (block switch_neutral_36, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_322:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 35:30 (block switch_positive_37, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_323:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_324:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_325:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TSTORE): register r90 is uninitialized\n"
.L__s3_failure_prefix_326:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TSTORE): register r89 is uninitialized\n"
.L__s3_failure_prefix_327:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 35:21 (block switch_positive_37, TSTORE): index "
.L__s3_failure_suffix_327:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_328:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 34:17 (block switch_positive_37, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_329:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:11 (block switch_continue_39, TSLEN): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_330:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:11 (block switch_continue_39, TSLEN): register r6 is uninitialized\n"
.L__s3_failure_prefix_331:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:25 (block switch_continue_39, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_332:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block switch_continue_39, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_333:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block switch_continue_39, TCMP): register r97 is uninitialized\n"
.L__s3_failure_prefix_334:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block switch_continue_39, TCMP): register r98 is uninitialized\n"
.L__s3_failure_prefix_335:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block switch_continue_39, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_336:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_337:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_338:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_339:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): register r100 is uninitialized\n"
.L__s3_failure_prefix_340:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): register r101 is uninitialized\n"
.L__s3_failure_prefix_341:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): index "
.L__s3_failure_suffix_341:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_342:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TSTORE): trit result "
.L__s3_failure_suffix_342:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_343:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_neg_40, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_344:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_345:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_346:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_347:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): register r102 is uninitialized\n"
.L__s3_failure_prefix_348:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): register r103 is uninitialized\n"
.L__s3_failure_prefix_349:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): index "
.L__s3_failure_suffix_349:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_350:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TSTORE): trit result "
.L__s3_failure_suffix_350:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_351:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_zero_41, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_352:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_353:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_354:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_355:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): register r104 is uninitialized\n"
.L__s3_failure_prefix_356:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): register r105 is uninitialized\n"
.L__s3_failure_prefix_357:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): index "
.L__s3_failure_suffix_357:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_358:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TSTORE): trit result "
.L__s3_failure_suffix_358:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_359:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_pos_42, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_360:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_361:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_362:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TLOAD): index "
.L__s3_failure_suffix_362:
    .ascii " is uninitialized in m6\n"
.L__s3_failure_prefix_363:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TLOAD): register r106 is uninitialized\n"
.L__s3_failure_prefix_364:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 41:23 (block rel_cont_43, TLOAD): index "
.L__s3_failure_suffix_364:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_365:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 41:5 (block rel_cont_43, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_366:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 41:5 (block rel_cont_43, TBR3): value "
.L__s3_failure_suffix_366:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_367:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 41:5 (block rel_cont_43, TBR3): register r107 is uninitialized\n"
.L__s3_failure_prefix_368:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_369:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_370:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TLOAD): index "
.L__s3_failure_suffix_370:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_371:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TLOAD): register r108 is uninitialized\n"
.L__s3_failure_prefix_372:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:19 (block switch_negative_44, TLOAD): index "
.L__s3_failure_suffix_372:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_373:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:29 (block switch_negative_44, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_374:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block switch_negative_44, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_375:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block switch_negative_44, TCMP): register r109 is uninitialized\n"
.L__s3_failure_prefix_376:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block switch_negative_44, TCMP): register r110 is uninitialized\n"
.L__s3_failure_prefix_377:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block switch_negative_44, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_378:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_379:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_380:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TLOAD): index "
.L__s3_failure_suffix_380:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_381:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TLOAD): register r128 is uninitialized\n"
.L__s3_failure_prefix_382:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 51:22 (block switch_neutral_45, TLOAD): index "
.L__s3_failure_suffix_382:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_383:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_384:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_385:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TSTORE): register r130 is uninitialized\n"
.L__s3_failure_prefix_386:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TSTORE): register r129 is uninitialized\n"
.L__s3_failure_prefix_387:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 51:13 (block switch_neutral_45, TSTORE): index "
.L__s3_failure_suffix_387:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_388:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 50:9 (block switch_neutral_45, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_389:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_390:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_391:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TLOAD): index "
.L__s3_failure_suffix_391:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_392:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TLOAD): register r131 is uninitialized\n"
.L__s3_failure_prefix_393:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 53:22 (block switch_positive_46, TLOAD): index "
.L__s3_failure_suffix_393:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_394:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_395:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_396:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TSTORE): register r133 is uninitialized\n"
.L__s3_failure_prefix_397:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TSTORE): register r132 is uninitialized\n"
.L__s3_failure_prefix_398:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 53:13 (block switch_positive_46, TSTORE): index "
.L__s3_failure_suffix_398:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_399:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 52:9 (block switch_positive_46, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_400:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_401:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_402:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_403:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): register r112 is uninitialized\n"
.L__s3_failure_prefix_404:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): register r113 is uninitialized\n"
.L__s3_failure_prefix_405:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): index "
.L__s3_failure_suffix_405:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_406:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TSTORE): trit result "
.L__s3_failure_suffix_406:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_407:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_neg_47, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_408:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_409:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_410:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_411:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): register r114 is uninitialized\n"
.L__s3_failure_prefix_412:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): register r115 is uninitialized\n"
.L__s3_failure_prefix_413:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): index "
.L__s3_failure_suffix_413:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_414:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TSTORE): trit result "
.L__s3_failure_suffix_414:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_415:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_zero_48, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_416:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_417:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_418:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_419:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): register r116 is uninitialized\n"
.L__s3_failure_prefix_420:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): register r117 is uninitialized\n"
.L__s3_failure_prefix_421:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): index "
.L__s3_failure_suffix_421:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_422:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TSTORE): trit result "
.L__s3_failure_suffix_422:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_423:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_pos_49, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_424:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_425:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_426:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TLOAD): index "
.L__s3_failure_suffix_426:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_427:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TLOAD): register r118 is uninitialized\n"
.L__s3_failure_prefix_428:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 43:26 (block rel_cont_50, TLOAD): index "
.L__s3_failure_suffix_428:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_429:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 43:13 (block rel_cont_50, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_430:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 43:13 (block rel_cont_50, TBR3): value "
.L__s3_failure_suffix_430:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_431:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 43:13 (block rel_cont_50, TBR3): register r119 is uninitialized\n"
.L__s3_failure_prefix_432:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 45:30 (block switch_negative_51, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_433:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_434:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_435:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TSTORE): register r121 is uninitialized\n"
.L__s3_failure_prefix_436:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TSTORE): register r120 is uninitialized\n"
.L__s3_failure_prefix_437:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 45:21 (block switch_negative_51, TSTORE): index "
.L__s3_failure_suffix_437:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_438:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 44:17 (block switch_negative_51, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_439:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_440:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_441:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TLOAD): index "
.L__s3_failure_suffix_441:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_442:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TLOAD): register r122 is uninitialized\n"
.L__s3_failure_prefix_443:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 47:30 (block switch_neutral_52, TLOAD): index "
.L__s3_failure_suffix_443:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_444:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_445:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_446:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TSTORE): register r124 is uninitialized\n"
.L__s3_failure_prefix_447:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TSTORE): register r123 is uninitialized\n"
.L__s3_failure_prefix_448:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 47:21 (block switch_neutral_52, TSTORE): index "
.L__s3_failure_suffix_448:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_449:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 46:17 (block switch_neutral_52, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_450:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_451:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_452:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TLOAD): index "
.L__s3_failure_suffix_452:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_453:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TLOAD): register r125 is uninitialized\n"
.L__s3_failure_prefix_454:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 49:30 (block switch_positive_53, TLOAD): index "
.L__s3_failure_suffix_454:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_455:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_456:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_457:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TSTORE): register r127 is uninitialized\n"
.L__s3_failure_prefix_458:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TSTORE): register r126 is uninitialized\n"
.L__s3_failure_prefix_459:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 49:21 (block switch_positive_53, TSTORE): index "
.L__s3_failure_suffix_459:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_460:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 48:17 (block switch_positive_53, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_461:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:11 (block switch_continue_55, TSLEN): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_462:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:11 (block switch_continue_55, TSLEN): register r6 is uninitialized\n"
.L__s3_failure_prefix_463:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:25 (block switch_continue_55, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_464:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block switch_continue_55, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_465:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block switch_continue_55, TCMP): register r134 is uninitialized\n"
.L__s3_failure_prefix_466:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block switch_continue_55, TCMP): register r135 is uninitialized\n"
.L__s3_failure_prefix_467:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block switch_continue_55, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_468:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_469:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_470:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_471:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): register r137 is uninitialized\n"
.L__s3_failure_prefix_472:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): register r138 is uninitialized\n"
.L__s3_failure_prefix_473:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): index "
.L__s3_failure_suffix_473:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_474:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TSTORE): trit result "
.L__s3_failure_suffix_474:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_475:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_neg_56, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_476:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_477:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_478:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_479:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): register r139 is uninitialized\n"
.L__s3_failure_prefix_480:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): register r140 is uninitialized\n"
.L__s3_failure_prefix_481:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): index "
.L__s3_failure_suffix_481:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_482:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TSTORE): trit result "
.L__s3_failure_suffix_482:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_483:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_zero_57, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_484:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_485:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_486:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_487:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): register r141 is uninitialized\n"
.L__s3_failure_prefix_488:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): register r142 is uninitialized\n"
.L__s3_failure_prefix_489:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): index "
.L__s3_failure_suffix_489:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_490:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TSTORE): trit result "
.L__s3_failure_suffix_490:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_491:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_pos_58, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_492:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_493:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_494:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TLOAD): index "
.L__s3_failure_suffix_494:
    .ascii " is uninitialized in m8\n"
.L__s3_failure_prefix_495:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TLOAD): register r143 is uninitialized\n"
.L__s3_failure_prefix_496:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 54:23 (block rel_cont_59, TLOAD): index "
.L__s3_failure_suffix_496:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_497:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 54:5 (block rel_cont_59, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_498:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 54:5 (block rel_cont_59, TBR3): value "
.L__s3_failure_suffix_498:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_499:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 54:5 (block rel_cont_59, TBR3): register r144 is uninitialized\n"
.L__s3_failure_prefix_500:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 56:22 (block switch_negative_60, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_501:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_502:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_503:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TSTORE): register r146 is uninitialized\n"
.L__s3_failure_prefix_504:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TSTORE): register r145 is uninitialized\n"
.L__s3_failure_prefix_505:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 56:13 (block switch_negative_60, TSTORE): index "
.L__s3_failure_suffix_505:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_506:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 55:9 (block switch_negative_60, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_507:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_508:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_509:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TLOAD): index "
.L__s3_failure_suffix_509:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_510:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TLOAD): register r147 is uninitialized\n"
.L__s3_failure_prefix_511:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 58:22 (block switch_neutral_61, TLOAD): index "
.L__s3_failure_suffix_511:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_512:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_513:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_514:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TSTORE): register r149 is uninitialized\n"
.L__s3_failure_prefix_515:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TSTORE): register r148 is uninitialized\n"
.L__s3_failure_prefix_516:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 58:13 (block switch_neutral_61, TSTORE): index "
.L__s3_failure_suffix_516:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_517:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 57:9 (block switch_neutral_61, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_518:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_519:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_520:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TLOAD): index "
.L__s3_failure_suffix_520:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_521:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TLOAD): register r150 is uninitialized\n"
.L__s3_failure_prefix_522:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 60:22 (block switch_positive_62, TLOAD): index "
.L__s3_failure_suffix_522:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_523:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_524:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_525:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TSTORE): register r152 is uninitialized\n"
.L__s3_failure_prefix_526:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TSTORE): register r151 is uninitialized\n"
.L__s3_failure_prefix_527:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 60:13 (block switch_positive_62, TSTORE): index "
.L__s3_failure_suffix_527:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_528:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 59:9 (block switch_positive_62, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_529:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_530:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_531:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TLOAD): index "
.L__s3_failure_suffix_531:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_532:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TLOAD): register r153 is uninitialized\n"
.L__s3_failure_prefix_533:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:11 (block switch_continue_63, TLOAD): index "
.L__s3_failure_suffix_533:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_534:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:21 (block switch_continue_63, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_535:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block switch_continue_63, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_536:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block switch_continue_63, TCMP): register r154 is uninitialized\n"
.L__s3_failure_prefix_537:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block switch_continue_63, TCMP): register r155 is uninitialized\n"
.L__s3_failure_prefix_538:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block switch_continue_63, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_539:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_540:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_541:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_542:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): register r157 is uninitialized\n"
.L__s3_failure_prefix_543:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): register r158 is uninitialized\n"
.L__s3_failure_prefix_544:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): index "
.L__s3_failure_suffix_544:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_545:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TSTORE): trit result "
.L__s3_failure_suffix_545:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_546:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_neg_64, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_547:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_548:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_549:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_550:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): register r159 is uninitialized\n"
.L__s3_failure_prefix_551:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): register r160 is uninitialized\n"
.L__s3_failure_prefix_552:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): index "
.L__s3_failure_suffix_552:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_553:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TSTORE): trit result "
.L__s3_failure_suffix_553:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_554:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_zero_65, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_555:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_556:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_557:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_558:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): register r161 is uninitialized\n"
.L__s3_failure_prefix_559:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): register r162 is uninitialized\n"
.L__s3_failure_prefix_560:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): index "
.L__s3_failure_suffix_560:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_561:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TSTORE): trit result "
.L__s3_failure_suffix_561:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_562:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_pos_66, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_563:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_564:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_565:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TLOAD): index "
.L__s3_failure_suffix_565:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_566:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TLOAD): register r163 is uninitialized\n"
.L__s3_failure_prefix_567:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 62:18 (block rel_cont_67, TLOAD): index "
.L__s3_failure_suffix_567:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_568:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 62:5 (block rel_cont_67, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_569:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 62:5 (block rel_cont_67, TBR3): value "
.L__s3_failure_suffix_569:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_570:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 62:5 (block rel_cont_67, TBR3): register r164 is uninitialized\n"
.L__s3_failure_prefix_571:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 64:35 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_572:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_573:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_574:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TSTORE): register r166 is uninitialized\n"
.L__s3_failure_prefix_575:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TSTORE): register r165 is uninitialized\n"
.L__s3_failure_prefix_576:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 64:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_576:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_577:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 65:37 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_578:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_579:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_580:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TSTORE): register r168 is uninitialized\n"
.L__s3_failure_prefix_581:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TSTORE): register r167 is uninitialized\n"
.L__s3_failure_prefix_582:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 65:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_582:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_583:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 66:41 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_584:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_585:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_586:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TSTORE): register r170 is uninitialized\n"
.L__s3_failure_prefix_587:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TSTORE): register r169 is uninitialized\n"
.L__s3_failure_prefix_588:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 66:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_588:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_589:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 67:30 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_590:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_591:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_592:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TSTORE): register r172 is uninitialized\n"
.L__s3_failure_prefix_593:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TSTORE): register r171 is uninitialized\n"
.L__s3_failure_prefix_594:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 67:13 (block switch_negative_68, TSTORE): index "
.L__s3_failure_suffix_594:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_595:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:13 (block switch_negative_68, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_596:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_597:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_598:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TLOAD): index "
.L__s3_failure_suffix_598:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_599:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TLOAD): register r279 is uninitialized\n"
.L__s3_failure_prefix_600:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 101:20 (block switch_neutral_69, TLOAD): index "
.L__s3_failure_suffix_600:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_601:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 101:13 (block switch_neutral_69, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_602:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 101:13 (block switch_neutral_69, TRET): register r280 is uninitialized\n"
.L__s3_failure_prefix_603:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_604:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_605:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TLOAD): index "
.L__s3_failure_suffix_605:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_606:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TLOAD): register r281 is uninitialized\n"
.L__s3_failure_prefix_607:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 103:20 (block switch_positive_70, TLOAD): index "
.L__s3_failure_suffix_607:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_608:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 103:13 (block switch_positive_70, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_609:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 103:13 (block switch_positive_70, TRET): register r282 is uninitialized\n"
.L__s3_failure_prefix_610:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_611:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_612:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TLOAD): index "
.L__s3_failure_suffix_612:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_613:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TLOAD): register r173 is uninitialized\n"
.L__s3_failure_prefix_614:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:19 (block while_condition_71, TLOAD): index "
.L__s3_failure_suffix_614:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_615:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block while_condition_71, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_616:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block while_condition_71, TCMP): register r174 is uninitialized\n"
.L__s3_failure_prefix_617:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block while_condition_71, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_618:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block while_condition_71, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_619:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_620:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_621:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_621:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_622:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TLOAD): register r184 is uninitialized\n"
.L__s3_failure_prefix_623:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:46 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_623:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_624:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_625:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): slice index "
.L__s3_failure_suffix_625:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_626:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_627:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_628:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:39 (block while_body_72, TSLOAD): register r185 is uninitialized\n"
.L__s3_failure_prefix_629:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_630:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_631:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_631:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_632:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TLOAD): register r187 is uninitialized\n"
.L__s3_failure_prefix_633:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:60 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_633:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_634:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_635:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): slice index "
.L__s3_failure_suffix_635:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_636:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_637:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_638:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:55 (block while_body_72, TSLOAD): register r188 is uninitialized\n"
.L__s3_failure_prefix_639:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:53 (block while_body_72, TNDIFF): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_640:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:53 (block while_body_72, TNDIFF): register r186 is uninitialized\n"
.L__s3_failure_prefix_641:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:53 (block while_body_72, TNDIFF): register r189 is uninitialized\n"
.L__s3_failure_prefix_642:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_643:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_644:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TSTORE): register r191 is uninitialized\n"
.L__s3_failure_prefix_645:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TSTORE): register r190 is uninitialized\n"
.L__s3_failure_prefix_646:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 69:17 (block while_body_72, TSTORE): index "
.L__s3_failure_suffix_646:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_647:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_648:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_649:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_649:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_650:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TLOAD): register r192 is uninitialized\n"
.L__s3_failure_prefix_651:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 70:38 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_651:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_652:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_653:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_654:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TSTORE): register r194 is uninitialized\n"
.L__s3_failure_prefix_655:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TSTORE): register r193 is uninitialized\n"
.L__s3_failure_prefix_656:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 70:17 (block while_body_72, TSTORE): index "
.L__s3_failure_suffix_656:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_657:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_658:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_659:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_659:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_660:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TLOAD): register r195 is uninitialized\n"
.L__s3_failure_prefix_661:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 71:23 (block while_body_72, TLOAD): index "
.L__s3_failure_suffix_661:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_662:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 71:36 (block while_body_72, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_663:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 71:34 (block while_body_72, TREL): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_664:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:34 (block while_body_72, TREL): register r196 is uninitialized\n"
.L__s3_failure_prefix_665:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:34 (block while_body_72, TREL): register r197 is uninitialized\n"
.L__s3_failure_prefix_666:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 71:17 (block while_body_72, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_667:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 71:17 (block while_body_72, TBR3): value "
.L__s3_failure_suffix_667:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_668:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 71:17 (block while_body_72, TBR3): register r198 is uninitialized\n"
.L__s3_failure_prefix_669:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:13 (block while_exit_0_73, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_670:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:13 (block while_exit_1_74, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_671:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 90:32 (block while_exit_75, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_672:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_673:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_674:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TSTORE): register r242 is uninitialized\n"
.L__s3_failure_prefix_675:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TSTORE): register r241 is uninitialized\n"
.L__s3_failure_prefix_676:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 90:13 (block while_exit_75, TSTORE): index "
.L__s3_failure_suffix_676:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_677:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 91:38 (block while_exit_75, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_678:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_679:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_680:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TSTORE): register r244 is uninitialized\n"
.L__s3_failure_prefix_681:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TSTORE): register r243 is uninitialized\n"
.L__s3_failure_prefix_682:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 91:13 (block while_exit_75, TSTORE): index "
.L__s3_failure_suffix_682:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_683:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:13 (block while_exit_75, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_684:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_685:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_686:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_687:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): register r176 is uninitialized\n"
.L__s3_failure_prefix_688:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): register r177 is uninitialized\n"
.L__s3_failure_prefix_689:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): index "
.L__s3_failure_suffix_689:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_690:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TSTORE): trit result "
.L__s3_failure_suffix_690:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_691:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_neg_76, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_692:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_693:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_694:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_695:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): register r178 is uninitialized\n"
.L__s3_failure_prefix_696:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): register r179 is uninitialized\n"
.L__s3_failure_prefix_697:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): index "
.L__s3_failure_suffix_697:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_698:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TSTORE): trit result "
.L__s3_failure_suffix_698:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_699:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_zero_77, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_700:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_701:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_702:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_703:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): register r180 is uninitialized\n"
.L__s3_failure_prefix_704:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): register r181 is uninitialized\n"
.L__s3_failure_prefix_705:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): index "
.L__s3_failure_suffix_705:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_706:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TSTORE): trit result "
.L__s3_failure_suffix_706:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_707:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_pos_78, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_708:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_709:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_710:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TLOAD): index "
.L__s3_failure_suffix_710:
    .ascii " is uninitialized in m14\n"
.L__s3_failure_prefix_711:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TLOAD): register r182 is uninitialized\n"
.L__s3_failure_prefix_712:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 68:25 (block rel_cont_79, TLOAD): index "
.L__s3_failure_suffix_712:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_713:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:13 (block rel_cont_79, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_714:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 68:13 (block rel_cont_79, TBR3): value "
.L__s3_failure_suffix_714:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_715:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 68:13 (block rel_cont_79, TBR3): register r183 is uninitialized\n"
.L__s3_failure_prefix_716:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 73:37 (block switch_negative_80, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_717:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_718:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_719:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TLOAD): index "
.L__s3_failure_suffix_719:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_720:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TLOAD): register r200 is uninitialized\n"
.L__s3_failure_prefix_721:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 73:43 (block switch_negative_80, TLOAD): index "
.L__s3_failure_suffix_721:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_722:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 73:41 (block switch_negative_80, TNDIFF): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_723:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:41 (block switch_negative_80, TNDIFF): register r199 is uninitialized\n"
.L__s3_failure_prefix_724:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:41 (block switch_negative_80, TNDIFF): register r201 is uninitialized\n"
.L__s3_failure_prefix_725:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_726:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_727:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TSTORE): register r203 is uninitialized\n"
.L__s3_failure_prefix_728:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TSTORE): register r202 is uninitialized\n"
.L__s3_failure_prefix_729:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 73:25 (block switch_negative_80, TSTORE): index "
.L__s3_failure_suffix_729:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_730:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 72:21 (block switch_negative_80, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_731:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_732:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_733:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TLOAD): index "
.L__s3_failure_suffix_733:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_734:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TLOAD): register r204 is uninitialized\n"
.L__s3_failure_prefix_735:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 75:37 (block switch_neutral_81, TLOAD): index "
.L__s3_failure_suffix_735:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_736:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_737:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_738:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TSTORE): register r206 is uninitialized\n"
.L__s3_failure_prefix_739:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TSTORE): register r205 is uninitialized\n"
.L__s3_failure_prefix_740:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 75:25 (block switch_neutral_81, TSTORE): index "
.L__s3_failure_suffix_740:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_741:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 74:21 (block switch_neutral_81, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_742:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_743:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_744:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TLOAD): index "
.L__s3_failure_suffix_744:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_745:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TLOAD): register r207 is uninitialized\n"
.L__s3_failure_prefix_746:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 77:37 (block switch_positive_82, TLOAD): index "
.L__s3_failure_suffix_746:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_747:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_748:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_749:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TSTORE): register r209 is uninitialized\n"
.L__s3_failure_prefix_750:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TSTORE): register r208 is uninitialized\n"
.L__s3_failure_prefix_751:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 77:25 (block switch_positive_82, TSTORE): index "
.L__s3_failure_suffix_751:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_752:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 76:21 (block switch_positive_82, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_753:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_754:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_755:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_755:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_756:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TLOAD): register r210 is uninitialized\n"
.L__s3_failure_prefix_757:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 79:30 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_757:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_758:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_759:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_760:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_760:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_761:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TLOAD): register r212 is uninitialized\n"
.L__s3_failure_prefix_762:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 79:43 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_762:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_763:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 79:41 (block switch_continue_83, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_764:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:41 (block switch_continue_83, TADD): register r211 is uninitialized\n"
.L__s3_failure_prefix_765:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:41 (block switch_continue_83, TADD): register r213 is uninitialized\n"
.L__s3_failure_prefix_766:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_767:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_768:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TSTORE): register r215 is uninitialized\n"
.L__s3_failure_prefix_769:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TSTORE): register r214 is uninitialized\n"
.L__s3_failure_prefix_770:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 79:17 (block switch_continue_83, TSTORE): index "
.L__s3_failure_suffix_770:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_771:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_772:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_773:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_773:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_774:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TLOAD): register r216 is uninitialized\n"
.L__s3_failure_prefix_775:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 80:32 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_775:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_776:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_777:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_778:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_778:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_779:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TLOAD): register r218 is uninitialized\n"
.L__s3_failure_prefix_780:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 80:47 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_780:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_781:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 80:45 (block switch_continue_83, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_782:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:45 (block switch_continue_83, TADD): register r217 is uninitialized\n"
.L__s3_failure_prefix_783:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:45 (block switch_continue_83, TADD): register r219 is uninitialized\n"
.L__s3_failure_prefix_784:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_785:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_786:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TSTORE): register r221 is uninitialized\n"
.L__s3_failure_prefix_787:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TSTORE): register r220 is uninitialized\n"
.L__s3_failure_prefix_788:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 80:17 (block switch_continue_83, TSTORE): index "
.L__s3_failure_suffix_788:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_789:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_790:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_791:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_791:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_792:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TLOAD): register r222 is uninitialized\n"
.L__s3_failure_prefix_793:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 81:23 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_793:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_794:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_795:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_796:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_796:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_797:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TLOAD): register r224 is uninitialized\n"
.L__s3_failure_prefix_798:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 81:35 (block switch_continue_83, TLOAD): index "
.L__s3_failure_suffix_798:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_799:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 81:33 (block switch_continue_83, TREL): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_800:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:33 (block switch_continue_83, TREL): register r223 is uninitialized\n"
.L__s3_failure_prefix_801:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:33 (block switch_continue_83, TREL): register r225 is uninitialized\n"
.L__s3_failure_prefix_802:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 81:17 (block switch_continue_83, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_803:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 81:17 (block switch_continue_83, TBR3): value "
.L__s3_failure_suffix_803:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_804:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 81:17 (block switch_continue_83, TBR3): register r226 is uninitialized\n"
.L__s3_failure_prefix_805:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_806:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_807:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TLOAD): index "
.L__s3_failure_suffix_807:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_808:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TLOAD): register r227 is uninitialized\n"
.L__s3_failure_prefix_809:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 83:44 (block switch_negative_84, TLOAD): index "
.L__s3_failure_suffix_809:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_810:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_811:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_812:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TSTORE): register r229 is uninitialized\n"
.L__s3_failure_prefix_813:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TSTORE): register r228 is uninitialized\n"
.L__s3_failure_prefix_814:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 83:25 (block switch_negative_84, TSTORE): index "
.L__s3_failure_suffix_814:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_815:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 82:21 (block switch_negative_84, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_816:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_817:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_818:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TLOAD): index "
.L__s3_failure_suffix_818:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_819:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TLOAD): register r230 is uninitialized\n"
.L__s3_failure_prefix_820:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 85:44 (block switch_neutral_85, TLOAD): index "
.L__s3_failure_suffix_820:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_821:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_822:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_823:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TSTORE): register r232 is uninitialized\n"
.L__s3_failure_prefix_824:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TSTORE): register r231 is uninitialized\n"
.L__s3_failure_prefix_825:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 85:25 (block switch_neutral_85, TSTORE): index "
.L__s3_failure_suffix_825:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_826:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 84:21 (block switch_neutral_85, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_827:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_828:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_829:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TLOAD): index "
.L__s3_failure_suffix_829:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_830:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TLOAD): register r233 is uninitialized\n"
.L__s3_failure_prefix_831:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 87:44 (block switch_positive_86, TLOAD): index "
.L__s3_failure_suffix_831:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_832:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_833:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_834:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TSTORE): register r235 is uninitialized\n"
.L__s3_failure_prefix_835:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TSTORE): register r234 is uninitialized\n"
.L__s3_failure_prefix_836:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 87:25 (block switch_positive_86, TSTORE): index "
.L__s3_failure_suffix_836:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_837:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 86:21 (block switch_positive_86, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_838:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_839:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_840:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TLOAD): index "
.L__s3_failure_suffix_840:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_841:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TLOAD): register r236 is uninitialized\n"
.L__s3_failure_prefix_842:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 88:25 (block switch_continue_87, TLOAD): index "
.L__s3_failure_suffix_842:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_843:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 88:33 (block switch_continue_87, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_844:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 88:31 (block switch_continue_87, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_845:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 88:31 (block switch_continue_87, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_846:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:31 (block switch_continue_87, TADD): register r237 is uninitialized\n"
.L__s3_failure_prefix_847:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:31 (block switch_continue_87, TADD): register r238 is uninitialized\n"
.L__s3_failure_prefix_848:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_849:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_850:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TSTORE): register r240 is uninitialized\n"
.L__s3_failure_prefix_851:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TSTORE): register r239 is uninitialized\n"
.L__s3_failure_prefix_852:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 88:17 (block switch_continue_87, TSTORE): index "
.L__s3_failure_suffix_852:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_853:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 68:13 (block switch_continue_87, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_854:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_855:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_856:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TLOAD): index "
.L__s3_failure_suffix_856:
    .ascii " is uninitialized in m18\n"
.L__s3_failure_prefix_857:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TLOAD): register r245 is uninitialized\n"
.L__s3_failure_prefix_858:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:19 (block while_condition_88, TLOAD): index "
.L__s3_failure_suffix_858:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_859:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block while_condition_88, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_860:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block while_condition_88, TCMP): register r246 is uninitialized\n"
.L__s3_failure_prefix_861:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block while_condition_88, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_862:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block while_condition_88, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_863:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_864:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_865:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_865:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_866:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TLOAD): register r256 is uninitialized\n"
.L__s3_failure_prefix_867:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 93:27 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_867:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_868:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 93:37 (block while_body_89, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_869:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 93:35 (block while_body_89, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_870:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:35 (block while_body_89, TADD): register r257 is uninitialized\n"
.L__s3_failure_prefix_871:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:35 (block while_body_89, TADD): register r258 is uninitialized\n"
.L__s3_failure_prefix_872:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_873:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_874:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TSTORE): register r260 is uninitialized\n"
.L__s3_failure_prefix_875:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TSTORE): register r259 is uninitialized\n"
.L__s3_failure_prefix_876:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 93:17 (block while_body_89, TSTORE): index "
.L__s3_failure_suffix_876:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_877:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_878:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_879:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_879:
    .ascii " is uninitialized in m18\n"
.L__s3_failure_prefix_880:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TLOAD): register r261 is uninitialized\n"
.L__s3_failure_prefix_881:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 94:33 (block while_body_89, TLOAD): index "
.L__s3_failure_suffix_881:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_882:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 94:49 (block while_body_89, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_883:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 94:47 (block while_body_89, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_884:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 94:47 (block while_body_89, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_885:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:47 (block while_body_89, TADD): register r262 is uninitialized\n"
.L__s3_failure_prefix_886:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:47 (block while_body_89, TADD): register r263 is uninitialized\n"
.L__s3_failure_prefix_887:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_888:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_889:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TSTORE): register r265 is uninitialized\n"
.L__s3_failure_prefix_890:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TSTORE): register r264 is uninitialized\n"
.L__s3_failure_prefix_891:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 94:17 (block while_body_89, TSTORE): index "
.L__s3_failure_suffix_891:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_892:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:13 (block while_body_89, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_893:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:13 (block while_exit_0_90, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_894:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:13 (block while_exit_1_91, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_895:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 96:20 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_896:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_897:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_898:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_898:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_899:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TLOAD): register r267 is uninitialized\n"
.L__s3_failure_prefix_900:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 96:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_900:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_901:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_902:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): slice index "
.L__s3_failure_suffix_902:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_903:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_904:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_905:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r266 is uninitialized\n"
.L__s3_failure_prefix_906:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 96:13 (block while_exit_92, TSSTORE): register r268 is uninitialized\n"
.L__s3_failure_prefix_907:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 97:20 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_908:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_909:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_910:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_910:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_911:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TLOAD): register r270 is uninitialized\n"
.L__s3_failure_prefix_912:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 97:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_912:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_913:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_914:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): slice index "
.L__s3_failure_suffix_914:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_915:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_916:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_917:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r269 is uninitialized\n"
.L__s3_failure_prefix_918:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 97:13 (block while_exit_92, TSSTORE): register r271 is uninitialized\n"
.L__s3_failure_prefix_919:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 98:20 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_920:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_921:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_922:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_922:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_923:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TLOAD): register r273 is uninitialized\n"
.L__s3_failure_prefix_924:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 98:25 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_924:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_925:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_926:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_927:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_927:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_928:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TLOAD): register r275 is uninitialized\n"
.L__s3_failure_prefix_929:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 98:40 (block while_exit_92, TLOAD): index "
.L__s3_failure_suffix_929:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_930:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 98:38 (block while_exit_92, TDIV): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_931:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:38 (block while_exit_92, TDIV): register r274 is uninitialized\n"
.L__s3_failure_prefix_932:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:38 (block while_exit_92, TDIV): register r276 is uninitialized\n"
.L__s3_failure_prefix_933:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_934:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): slice index "
.L__s3_failure_suffix_934:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_935:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_936:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_937:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r272 is uninitialized\n"
.L__s3_failure_prefix_938:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 98:13 (block while_exit_92, TSSTORE): register r277 is uninitialized\n"
.L__s3_failure_prefix_939:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 99:20 (block while_exit_92, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_940:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 99:13 (block while_exit_92, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_941:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 99:13 (block while_exit_92, TRET): register r278 is uninitialized\n"
.L__s3_failure_prefix_942:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_943:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_944:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_945:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): register r248 is uninitialized\n"
.L__s3_failure_prefix_946:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): register r249 is uninitialized\n"
.L__s3_failure_prefix_947:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): index "
.L__s3_failure_suffix_947:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_948:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TSTORE): trit result "
.L__s3_failure_suffix_948:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_949:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_neg_93, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_950:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_951:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_952:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_953:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): register r250 is uninitialized\n"
.L__s3_failure_prefix_954:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): register r251 is uninitialized\n"
.L__s3_failure_prefix_955:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): index "
.L__s3_failure_suffix_955:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_956:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TSTORE): trit result "
.L__s3_failure_suffix_956:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_957:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_zero_94, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_958:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_959:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_960:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_961:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): register r252 is uninitialized\n"
.L__s3_failure_prefix_962:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): register r253 is uninitialized\n"
.L__s3_failure_prefix_963:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): index "
.L__s3_failure_suffix_963:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_964:
    .ascii "runtime error [overflow] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TSTORE): trit result "
.L__s3_failure_suffix_964:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_965:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_pos_95, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_966:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_967:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_968:
    .ascii "runtime error [uninitialized memory] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TLOAD): index "
.L__s3_failure_suffix_968:
    .ascii " is uninitialized in m19\n"
.L__s3_failure_prefix_969:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TLOAD): register r254 is uninitialized\n"
.L__s3_failure_prefix_970:
    .ascii "runtime error [bounds] in function 'agent_energy_residual'\nat source 92:33 (block rel_cont_96, TLOAD): index "
.L__s3_failure_suffix_970:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_971:
    .ascii "runtime error [instruction limit] in function 'agent_energy_residual'\nat source 92:13 (block rel_cont_96, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_972:
    .ascii "runtime error [invalid trit state] in function 'agent_energy_residual'\nat source 92:13 (block rel_cont_96, TBR3): value "
.L__s3_failure_suffix_972:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_973:
    .ascii "runtime error [uninitialized register] in function 'agent_energy_residual'\nat source 92:13 (block rel_cont_96, TBR3): register r255 is uninitialized\n"
.L__s3_failure_prefix_974:
    .ascii "runtime error [frame limit] in function 'main'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_974:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_975:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 106:12 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_976:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 106:5 (block entry, TRET): instruction limit 100000 exceeded\n"

.section .data
.align 8
.local __s3_instruction_remaining
__s3_instruction_remaining:
    .quad 100000

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
