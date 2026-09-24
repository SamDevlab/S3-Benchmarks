.intel_syntax noprefix
# Generated deterministically by the S3 Linux x86-64 backend.
.section .text
.globl s3_xsbench_binary_search
.type s3_xsbench_binary_search, @function
s3_xsbench_binary_search:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_0
    push rbp
    mov rbp, rsp
    sub rsp, 672
    mov qword ptr [rbp - 584], rbx
    mov qword ptr [rbp - 592], r12
    mov qword ptr [rbp - 600], r13
    mov qword ptr [rbp - 608], r14
    mov qword ptr [rbp - 616], r15
    mov qword ptr [rbp - 8], rdi
    mov qword ptr [rbp - 16], rsi
    mov qword ptr [rbp - 24], rdx
    mov qword ptr [rbp - 32], rcx
    mov qword ptr [rbp - 40], r8
    mov rdi, qword ptr [rbp - 8]
    mov rsi, qword ptr [rbp - 16]
    mov rdx, qword ptr [rbp - 24]
    mov rcx, qword ptr [rbp - 32]
    mov r8, qword ptr [rbp - 40]
    mov r10, rdi
    mov r11, rcx
    mov byte ptr [rbp - 457], 0
    mov byte ptr [rbp - 458], 0
    mov byte ptr [rbp - 459], 0
    mov byte ptr [rbp - 460], 0
    mov byte ptr [rbp - 461], 0
    mov byte ptr [rbp - 462], 0
    mov byte ptr [rbp - 463], 0
    mov byte ptr [rbp - 464], 0
    mov byte ptr [rbp - 465], 0
    mov byte ptr [rbp - 466], 0
    mov byte ptr [rbp - 467], 0
    mov byte ptr [rbp - 468], 0
    mov byte ptr [rbp - 469], 0
    mov byte ptr [rbp - 470], 0
    mov byte ptr [rbp - 471], 0
    mov byte ptr [rbp - 472], 0
    mov byte ptr [rbp - 473], 0
    mov byte ptr [rbp - 474], 0
    mov byte ptr [rbp - 475], 0
    mov byte ptr [rbp - 476], 0
    mov byte ptr [rbp - 477], 0
    mov byte ptr [rbp - 478], 0
    mov byte ptr [rbp - 479], 0
    mov byte ptr [rbp - 480], 0
    mov byte ptr [rbp - 481], 0
    mov byte ptr [rbp - 482], 0
    mov byte ptr [rbp - 483], 0
    mov byte ptr [rbp - 484], 0
    mov byte ptr [rbp - 485], 0
    mov byte ptr [rbp - 486], 0
    mov byte ptr [rbp - 487], 0
    mov byte ptr [rbp - 488], 0
    mov byte ptr [rbp - 489], 0
    mov byte ptr [rbp - 490], 0
    mov byte ptr [rbp - 491], 0
    mov byte ptr [rbp - 492], 0
    mov byte ptr [rbp - 493], 0
    mov byte ptr [rbp - 494], 0
    mov byte ptr [rbp - 495], 0
    mov byte ptr [rbp - 496], 0
    mov byte ptr [rbp - 497], 0
    mov byte ptr [rbp - 498], 0
    mov byte ptr [rbp - 499], 0
    mov byte ptr [rbp - 500], 0
    mov byte ptr [rbp - 501], 0
    mov byte ptr [rbp - 502], 0
    mov byte ptr [rbp - 503], 0
    mov byte ptr [rbp - 504], 0
    mov byte ptr [rbp - 505], 0
    mov byte ptr [rbp - 506], 0
    mov byte ptr [rbp - 507], 0
    mov byte ptr [rbp - 508], 0
    mov byte ptr [rbp - 509], 0
    mov byte ptr [rbp - 510], 0
    mov byte ptr [rbp - 511], 0
    mov byte ptr [rbp - 512], 0
    mov byte ptr [rbp - 513], 0
    lea rdi, [rbp - 569]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 570]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 571]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 572]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 573]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 574]
    mov ecx, 1
    xor eax, eax
    rep stosb
    mov rdi, r10
    mov rcx, r11
    mov byte ptr [rbp - 457], 1
    mov byte ptr [rbp - 458], 1
    mov byte ptr [rbp - 459], 1
    mov byte ptr [rbp - 460], 1
    mov byte ptr [rbp - 461], 1
    jmp .L_s3_f21_xsbench_binary_search_b5_entry
.L_s3_f21_xsbench_binary_search_b5_entry:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 462], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_2
    inc qword ptr [rip + __s3_instruction_count]
    mov rbx, 0
    mov byte ptr [rbp - 463], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_3
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 463], 0
    je .L__s3_failure_site_4
    mov rax, rbx
    cmp byte ptr [rbp - 462], 0
    je .L__s3_failure_site_5
    mov r10, r9
    cmp rax, 1
    jae .L__s3_failure_site_6
    mov qword ptr [rbp + rax*8 - 528], r10
    mov byte ptr [rbp + rax - 569], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_7
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 464], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_8
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 464], 0
    je .L__s3_failure_site_9
    mov rax, r9
    cmp byte ptr [rbp - 461], 0
    je .L__s3_failure_site_10
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_11
    mov qword ptr [rbp + rax*8 - 536], r10
    mov byte ptr [rbp + rax - 570], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_12
    inc qword ptr [rip + __s3_instruction_count]
    mov r8, 0
    mov byte ptr [rbp - 465], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_13
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 466], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_14
    inc qword ptr [rip + __s3_instruction_count]
    mov rbx, 0
    mov byte ptr [rbp - 467], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_15
    inc qword ptr [rip + __s3_instruction_count]
    mov r12, 0
    mov byte ptr [rbp - 468], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_16
    inc qword ptr [rip + __s3_instruction_count]
    mov r13, 0
    mov byte ptr [rbp - 469], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_17
    inc qword ptr [rip + __s3_instruction_count]
    mov r14, 0
    mov byte ptr [rbp - 470], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_18
    inc qword ptr [rip + __s3_instruction_count]
    mov r15, -1
    mov byte ptr [rbp - 471], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_19
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 128], 0
    mov byte ptr [rbp - 472], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_20
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 136], 0
    mov byte ptr [rbp - 473], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_21
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 144], 0
    mov byte ptr [rbp - 474], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_22
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 152], 0
    mov byte ptr [rbp - 475], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_23
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 160], 0
    mov byte ptr [rbp - 476], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_24
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 168], 0
    mov byte ptr [rbp - 477], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_25
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 176], 0
    mov byte ptr [rbp - 478], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_26
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 184], 2
    mov byte ptr [rbp - 479], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_27
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 192], 0
    mov byte ptr [rbp - 480], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_28
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 200], 4
    mov byte ptr [rbp - 481], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_29
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 208], 5
    mov byte ptr [rbp - 482], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_30
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 216], 0
    mov byte ptr [rbp - 483], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_31
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 224], 0
    mov byte ptr [rbp - 484], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_32
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 232], 0
    mov byte ptr [rbp - 485], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_33
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 240], 0
    mov byte ptr [rbp - 486], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_34
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 248], 0
    mov byte ptr [rbp - 487], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_35
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 256], 0
    mov byte ptr [rbp - 488], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_36
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 264], 0
    mov byte ptr [rbp - 489], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_37
    inc qword ptr [rip + __s3_instruction_count]
    mov qword ptr [rbp - 272], 1
    mov byte ptr [rbp - 490], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_38
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b17_while_condition_0
.L_s3_f21_xsbench_binary_search_b17_while_condition_0:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_39
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 488], 0
    je .L__s3_failure_site_41
    mov r10, qword ptr [rbp - 256]
    cmp r10, 1
    jae .L__s3_failure_site_42
    cmp byte ptr [rbp + r10 - 570], 0
    je .L__s3_failure_site_40
    mov rax, qword ptr [rbp + r10*8 - 536]
    mov qword ptr [rbp - 280], rax
    mov byte ptr [rbp - 491], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_43
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 489], 0
    je .L__s3_failure_site_45
    mov r10, qword ptr [rbp - 264]
    cmp r10, 1
    jae .L__s3_failure_site_46
    cmp byte ptr [rbp + r10 - 569], 0
    je .L__s3_failure_site_44
    mov rax, qword ptr [rbp + r10*8 - 528]
    mov qword ptr [rbp - 288], rax
    mov byte ptr [rbp - 492], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_47
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 491], 0
    je .L__s3_failure_site_49
    mov rax, qword ptr [rbp - 280]
    cmp byte ptr [rbp - 492], 0
    je .L__s3_failure_site_50
    mov r10, qword ptr [rbp - 288]
    sub rax, r10
    jo .L__s3_failure_site_48
    mov qword ptr [rbp - 296], rax
    mov byte ptr [rbp - 493], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_51
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 493], 0
    je .L__s3_failure_site_52
    mov rax, qword ptr [rbp - 296]
    cmp byte ptr [rbp - 490], 0
    je .L__s3_failure_site_53
    mov r10, qword ptr [rbp - 272]
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_54
    inc qword ptr [rip + __s3_instruction_count]
    cmp rax, r10
    jl .L_s3_f21_xsbench_binary_search_b9_rel_neg_5
    jg .L_s3_f21_xsbench_binary_search_b9_rel_pos_7
    jmp .L_s3_f21_xsbench_binary_search_b10_rel_zero_6
.L_s3_f21_xsbench_binary_search_b12_while_body_1:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_55
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 476], 0
    je .L__s3_failure_site_57
    mov r10, qword ptr [rbp - 160]
    cmp r10, 1
    jae .L__s3_failure_site_58
    cmp byte ptr [rbp + r10 - 569], 0
    je .L__s3_failure_site_56
    mov rax, qword ptr [rbp + r10*8 - 528]
    mov qword ptr [rbp - 312], rax
    mov byte ptr [rbp - 495], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_59
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 477], 0
    je .L__s3_failure_site_61
    mov r10, qword ptr [rbp - 168]
    cmp r10, 1
    jae .L__s3_failure_site_62
    cmp byte ptr [rbp + r10 - 570], 0
    je .L__s3_failure_site_60
    mov rax, qword ptr [rbp + r10*8 - 536]
    mov qword ptr [rbp - 320], rax
    mov byte ptr [rbp - 496], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_63
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 478], 0
    je .L__s3_failure_site_65
    mov r10, qword ptr [rbp - 176]
    cmp r10, 1
    jae .L__s3_failure_site_66
    cmp byte ptr [rbp + r10 - 569], 0
    je .L__s3_failure_site_64
    mov rax, qword ptr [rbp + r10*8 - 528]
    mov qword ptr [rbp - 328], rax
    mov byte ptr [rbp - 497], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_67
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 496], 0
    je .L__s3_failure_site_69
    mov rax, qword ptr [rbp - 320]
    cmp byte ptr [rbp - 497], 0
    je .L__s3_failure_site_70
    mov r10, qword ptr [rbp - 328]
    sub rax, r10
    jo .L__s3_failure_site_68
    mov qword ptr [rbp - 336], rax
    mov byte ptr [rbp - 498], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_71
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 498], 0
    je .L__s3_failure_site_74
    mov rax, qword ptr [rbp - 336]
    cmp byte ptr [rbp - 479], 0
    je .L__s3_failure_site_75
    mov r10, qword ptr [rbp - 184]
    cmp r10, 0
    je .L__s3_failure_site_73
    movabs r11, -9223372036854775808
    cmp rax, r11
    jne .L__s3_idiv_safe_74
    cmp r10, -1
    je .L__s3_failure_site_72
.L__s3_idiv_safe_74:
    cqo
    idiv r10
    mov qword ptr [rbp - 344], rax
    mov byte ptr [rbp - 499], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_76
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 495], 0
    je .L__s3_failure_site_78
    mov rax, qword ptr [rbp - 312]
    cmp byte ptr [rbp - 499], 0
    je .L__s3_failure_site_79
    mov r10, qword ptr [rbp - 344]
    add rax, r10
    jo .L__s3_failure_site_77
    mov qword ptr [rbp - 352], rax
    mov byte ptr [rbp - 500], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_80
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 480], 0
    je .L__s3_failure_site_81
    mov rax, qword ptr [rbp - 192]
    cmp byte ptr [rbp - 500], 0
    je .L__s3_failure_site_82
    mov r10, qword ptr [rbp - 352]
    cmp rax, 1
    jae .L__s3_failure_site_83
    mov qword ptr [rbp + rax*8 - 552], r10
    mov byte ptr [rbp + rax - 572], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_84
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 459], 0
    je .L__s3_failure_site_86
    mov rax, rdx
    cmp byte ptr [rbp - 482], 0
    je .L__s3_failure_site_87
    mov r10, qword ptr [rbp - 208]
    imul rax, r10
    jo .L__s3_failure_site_85
    mov qword ptr [rbp - 360], rax
    mov byte ptr [rbp - 501], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_88
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 481], 0
    je .L__s3_failure_site_90
    mov rax, qword ptr [rbp - 200]
    cmp byte ptr [rbp - 501], 0
    je .L__s3_failure_site_91
    mov r10, qword ptr [rbp - 360]
    add rax, r10
    jo .L__s3_failure_site_89
    mov qword ptr [rbp - 368], rax
    mov byte ptr [rbp - 502], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_92
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 483], 0
    je .L__s3_failure_site_94
    mov r10, qword ptr [rbp - 216]
    cmp r10, 1
    jae .L__s3_failure_site_95
    cmp byte ptr [rbp + r10 - 572], 0
    je .L__s3_failure_site_93
    mov rax, qword ptr [rbp + r10*8 - 552]
    mov qword ptr [rbp - 376], rax
    mov byte ptr [rbp - 503], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_96
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 502], 0
    je .L__s3_failure_site_98
    mov rax, qword ptr [rbp - 368]
    cmp byte ptr [rbp - 503], 0
    je .L__s3_failure_site_99
    mov r10, qword ptr [rbp - 376]
    add rax, r10
    jo .L__s3_failure_site_97
    mov qword ptr [rbp - 384], rax
    mov byte ptr [rbp - 504], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_100
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 484], 0
    je .L__s3_failure_site_101
    mov rax, qword ptr [rbp - 224]
    cmp byte ptr [rbp - 504], 0
    je .L__s3_failure_site_102
    mov r10, qword ptr [rbp - 384]
    cmp rax, 1
    jae .L__s3_failure_site_103
    mov qword ptr [rbp + rax*8 - 560], r10
    mov byte ptr [rbp + rax - 573], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_104
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 485], 0
    je .L__s3_failure_site_106
    mov r10, qword ptr [rbp - 232]
    cmp r10, 1
    jae .L__s3_failure_site_107
    cmp byte ptr [rbp + r10 - 573], 0
    je .L__s3_failure_site_105
    mov rax, qword ptr [rbp + r10*8 - 560]
    mov qword ptr [rbp - 392], rax
    mov byte ptr [rbp - 505], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_108
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 457], 0
    je .L__s3_failure_site_110
    mov r10, rdi
    cmp byte ptr [rbp - 458], 0
    je .L__s3_failure_site_111
    mov r11, rsi
    cmp byte ptr [rbp - 505], 0
    je .L__s3_failure_site_112
    mov rax, qword ptr [rbp - 392]
    cmp rax, r11
    jae .L__s3_failure_site_109
    mov r11, qword ptr [r10 + rax * 8]
    mov qword ptr [rbp - 400], r11
    mov byte ptr [rbp - 506], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_113
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 486], 0
    je .L__s3_failure_site_114
    mov rax, qword ptr [rbp - 240]
    cmp byte ptr [rbp - 506], 0
    je .L__s3_failure_site_115
    mov r10, qword ptr [rbp - 400]
    cmp rax, 1
    jae .L__s3_failure_site_116
    mov qword ptr [rbp + rax*8 - 568], r10
    mov byte ptr [rbp + rax - 574], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_117
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 487], 0
    je .L__s3_failure_site_119
    mov r10, qword ptr [rbp - 248]
    cmp r10, 1
    jae .L__s3_failure_site_120
    cmp byte ptr [rbp + r10 - 574], 0
    je .L__s3_failure_site_118
    mov rax, qword ptr [rbp + r10*8 - 568]
    mov qword ptr [rbp - 408], rax
    mov byte ptr [rbp - 507], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_121
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 507], 0
    je .L__s3_failure_site_122
    mov rax, qword ptr [rbp - 408]
    cmp byte ptr [rbp - 460], 0
    je .L__s3_failure_site_123
    mov r10, rcx
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_124
    inc qword ptr [rip + __s3_instruction_count]
    cmp rax, r10
    jl .L_s3_f21_xsbench_binary_search_b17_switch_negative_9
    jg .L_s3_f21_xsbench_binary_search_b18_switch_positive_11
    jmp .L_s3_f21_xsbench_binary_search_b17_switch_neutral_10
.L_s3_f21_xsbench_binary_search_b14_while_exit_0_2:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_125
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b12_while_exit_4
.L_s3_f21_xsbench_binary_search_b14_while_exit_1_3:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_126
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b12_while_exit_4
.L_s3_f21_xsbench_binary_search_b12_while_exit_4:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_127
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 509], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_128
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 509], 0
    je .L__s3_failure_site_130
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_131
    cmp byte ptr [rbp + r10 - 569], 0
    je .L__s3_failure_site_129
    mov rax, qword ptr [rbp + r10*8 - 528]
    mov rdi, rax
    mov byte ptr [rbp - 510], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_132
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 510], 0
    je .L__s3_failure_site_133
    mov rax, rdi
    mov rbx, qword ptr [rbp - 584]
    mov r12, qword ptr [rbp - 592]
    mov r13, qword ptr [rbp - 600]
    mov r14, qword ptr [rbp - 608]
    mov r15, qword ptr [rbp - 616]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f21_xsbench_binary_search_b9_rel_neg_5:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_134
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 468], 0
    je .L__s3_failure_site_135
    mov rax, r12
    cmp byte ptr [rbp - 469], 0
    je .L__s3_failure_site_136
    mov r10, r13
    cmp rax, 1
    jae .L__s3_failure_site_137
    cmp r10, -1
    jl .L__s3_failure_site_138
    cmp r10, 1
    jg .L__s3_failure_site_138
    mov byte ptr [rbp + rax - 537], r10b
    mov byte ptr [rbp + rax - 571], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_139
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b10_rel_cont_8
.L_s3_f21_xsbench_binary_search_b10_rel_zero_6:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_140
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 472], 0
    je .L__s3_failure_site_141
    mov rax, qword ptr [rbp - 128]
    cmp byte ptr [rbp - 473], 0
    je .L__s3_failure_site_142
    mov r10, qword ptr [rbp - 136]
    cmp rax, 1
    jae .L__s3_failure_site_143
    cmp r10, -1
    jl .L__s3_failure_site_144
    cmp r10, 1
    jg .L__s3_failure_site_144
    mov byte ptr [rbp + rax - 537], r10b
    mov byte ptr [rbp + rax - 571], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_145
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b10_rel_cont_8
.L_s3_f21_xsbench_binary_search_b9_rel_pos_7:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_146
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 470], 0
    je .L__s3_failure_site_147
    mov rax, r14
    cmp byte ptr [rbp - 471], 0
    je .L__s3_failure_site_148
    mov r10, r15
    cmp rax, 1
    jae .L__s3_failure_site_149
    cmp r10, -1
    jl .L__s3_failure_site_150
    cmp r10, 1
    jg .L__s3_failure_site_150
    mov byte ptr [rbp + rax - 537], r10b
    mov byte ptr [rbp + rax - 571], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_151
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b10_rel_cont_8
.L_s3_f21_xsbench_binary_search_b10_rel_cont_8:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_152
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 467], 0
    je .L__s3_failure_site_154
    mov r10, rbx
    cmp r10, 1
    jae .L__s3_failure_site_155
    cmp byte ptr [rbp + r10 - 571], 0
    je .L__s3_failure_site_153
    movsx rax, byte ptr [rbp + r10 - 537]
    mov qword ptr [rbp - 440], rax
    mov byte ptr [rbp - 511], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_156
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 511], 0
    je .L__s3_failure_site_158
    mov rax, qword ptr [rbp - 440]
    cmp rax, -1
    je .L_s3_f21_xsbench_binary_search_b12_while_body_1
    cmp rax, 0
    je .L_s3_f21_xsbench_binary_search_b14_while_exit_0_2
    cmp rax, 1
    je .L_s3_f21_xsbench_binary_search_b14_while_exit_1_3
    jmp .L__s3_failure_site_157
.L_s3_f21_xsbench_binary_search_b17_switch_negative_9:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_159
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 465], 0
    je .L__s3_failure_site_161
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_162
    cmp byte ptr [rbp + r10 - 572], 0
    je .L__s3_failure_site_160
    mov rax, qword ptr [rbp + r10*8 - 552]
    mov qword ptr [rbp - 448], rax
    mov byte ptr [rbp - 512], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_163
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 466], 0
    je .L__s3_failure_site_164
    mov rax, r9
    cmp byte ptr [rbp - 512], 0
    je .L__s3_failure_site_165
    mov r10, qword ptr [rbp - 448]
    cmp rax, 1
    jae .L__s3_failure_site_166
    mov qword ptr [rbp + rax*8 - 528], r10
    mov byte ptr [rbp + rax - 569], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_167
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b17_while_condition_0
.L_s3_f21_xsbench_binary_search_b17_switch_neutral_10:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_168
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b17_switch_negative_9
.L_s3_f21_xsbench_binary_search_b18_switch_positive_11:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_169
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 474], 0
    je .L__s3_failure_site_171
    mov r10, qword ptr [rbp - 144]
    cmp r10, 1
    jae .L__s3_failure_site_172
    cmp byte ptr [rbp + r10 - 572], 0
    je .L__s3_failure_site_170
    mov rax, qword ptr [rbp + r10*8 - 552]
    mov qword ptr [rbp - 456], rax
    mov byte ptr [rbp - 513], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_173
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 475], 0
    je .L__s3_failure_site_174
    mov rax, qword ptr [rbp - 152]
    cmp byte ptr [rbp - 513], 0
    je .L__s3_failure_site_175
    mov r10, qword ptr [rbp - 456]
    cmp rax, 1
    jae .L__s3_failure_site_176
    mov qword ptr [rbp + rax*8 - 536], r10
    mov byte ptr [rbp + rax - 570], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_177
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f21_xsbench_binary_search_b17_while_condition_0
.size s3_xsbench_binary_search, .-s3_xsbench_binary_search

.globl xs_lookup_batch
.type xs_lookup_batch, @function
xs_lookup_batch:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_178
    push rbp
    mov rbp, rsp
    sub rsp, 3840
    mov qword ptr [rbp - 3760], rbx
    mov qword ptr [rbp - 3768], r12
    mov qword ptr [rbp - 3776], r13
    mov qword ptr [rbp - 3784], r14
    mov qword ptr [rbp - 8], rdi
    mov qword ptr [rbp - 16], rsi
    mov qword ptr [rbp - 24], rdx
    mov qword ptr [rbp - 32], rcx
    mov rbx, qword ptr [rbp - 8]
    mov r12, qword ptr [rbp - 16]
    mov r13, qword ptr [rbp - 24]
    mov r14, qword ptr [rbp - 32]
    mov r10, rdi
    mov r11, rcx
    mov byte ptr [rbp - 2993], 0
    mov byte ptr [rbp - 2994], 0
    mov byte ptr [rbp - 2995], 0
    mov byte ptr [rbp - 2996], 0
    mov byte ptr [rbp - 2997], 0
    mov byte ptr [rbp - 2998], 0
    mov byte ptr [rbp - 2999], 0
    mov byte ptr [rbp - 3000], 0
    mov byte ptr [rbp - 3001], 0
    mov byte ptr [rbp - 3002], 0
    mov byte ptr [rbp - 3003], 0
    mov byte ptr [rbp - 3004], 0
    mov byte ptr [rbp - 3005], 0
    mov byte ptr [rbp - 3006], 0
    mov byte ptr [rbp - 3007], 0
    mov byte ptr [rbp - 3008], 0
    mov byte ptr [rbp - 3009], 0
    mov byte ptr [rbp - 3010], 0
    mov byte ptr [rbp - 3011], 0
    mov byte ptr [rbp - 3012], 0
    mov byte ptr [rbp - 3013], 0
    mov byte ptr [rbp - 3014], 0
    mov byte ptr [rbp - 3015], 0
    mov byte ptr [rbp - 3016], 0
    mov byte ptr [rbp - 3017], 0
    mov byte ptr [rbp - 3018], 0
    mov byte ptr [rbp - 3019], 0
    mov byte ptr [rbp - 3020], 0
    mov byte ptr [rbp - 3021], 0
    mov byte ptr [rbp - 3022], 0
    mov byte ptr [rbp - 3023], 0
    mov byte ptr [rbp - 3024], 0
    mov byte ptr [rbp - 3025], 0
    mov byte ptr [rbp - 3026], 0
    mov byte ptr [rbp - 3027], 0
    mov byte ptr [rbp - 3028], 0
    mov byte ptr [rbp - 3029], 0
    mov byte ptr [rbp - 3030], 0
    mov byte ptr [rbp - 3031], 0
    mov byte ptr [rbp - 3032], 0
    mov byte ptr [rbp - 3033], 0
    mov byte ptr [rbp - 3034], 0
    mov byte ptr [rbp - 3035], 0
    mov byte ptr [rbp - 3036], 0
    mov byte ptr [rbp - 3037], 0
    mov byte ptr [rbp - 3038], 0
    mov byte ptr [rbp - 3039], 0
    mov byte ptr [rbp - 3040], 0
    mov byte ptr [rbp - 3041], 0
    mov byte ptr [rbp - 3042], 0
    mov byte ptr [rbp - 3043], 0
    mov byte ptr [rbp - 3044], 0
    mov byte ptr [rbp - 3045], 0
    mov byte ptr [rbp - 3046], 0
    mov byte ptr [rbp - 3047], 0
    mov byte ptr [rbp - 3048], 0
    mov byte ptr [rbp - 3049], 0
    mov byte ptr [rbp - 3050], 0
    mov byte ptr [rbp - 3051], 0
    mov byte ptr [rbp - 3052], 0
    mov byte ptr [rbp - 3053], 0
    mov byte ptr [rbp - 3054], 0
    mov byte ptr [rbp - 3055], 0
    mov byte ptr [rbp - 3056], 0
    mov byte ptr [rbp - 3057], 0
    mov byte ptr [rbp - 3058], 0
    mov byte ptr [rbp - 3059], 0
    mov byte ptr [rbp - 3060], 0
    mov byte ptr [rbp - 3061], 0
    mov byte ptr [rbp - 3062], 0
    mov byte ptr [rbp - 3063], 0
    mov byte ptr [rbp - 3064], 0
    mov byte ptr [rbp - 3065], 0
    mov byte ptr [rbp - 3066], 0
    mov byte ptr [rbp - 3067], 0
    mov byte ptr [rbp - 3068], 0
    mov byte ptr [rbp - 3069], 0
    mov byte ptr [rbp - 3070], 0
    mov byte ptr [rbp - 3071], 0
    mov byte ptr [rbp - 3072], 0
    mov byte ptr [rbp - 3073], 0
    mov byte ptr [rbp - 3074], 0
    mov byte ptr [rbp - 3075], 0
    mov byte ptr [rbp - 3076], 0
    mov byte ptr [rbp - 3077], 0
    mov byte ptr [rbp - 3078], 0
    mov byte ptr [rbp - 3079], 0
    mov byte ptr [rbp - 3080], 0
    mov byte ptr [rbp - 3081], 0
    mov byte ptr [rbp - 3082], 0
    mov byte ptr [rbp - 3083], 0
    mov byte ptr [rbp - 3084], 0
    mov byte ptr [rbp - 3085], 0
    mov byte ptr [rbp - 3086], 0
    mov byte ptr [rbp - 3087], 0
    mov byte ptr [rbp - 3088], 0
    mov byte ptr [rbp - 3089], 0
    mov byte ptr [rbp - 3090], 0
    mov byte ptr [rbp - 3091], 0
    mov byte ptr [rbp - 3092], 0
    mov byte ptr [rbp - 3093], 0
    mov byte ptr [rbp - 3094], 0
    mov byte ptr [rbp - 3095], 0
    mov byte ptr [rbp - 3096], 0
    mov byte ptr [rbp - 3097], 0
    mov byte ptr [rbp - 3098], 0
    mov byte ptr [rbp - 3099], 0
    mov byte ptr [rbp - 3100], 0
    mov byte ptr [rbp - 3101], 0
    mov byte ptr [rbp - 3102], 0
    mov byte ptr [rbp - 3103], 0
    mov byte ptr [rbp - 3104], 0
    mov byte ptr [rbp - 3105], 0
    mov byte ptr [rbp - 3106], 0
    mov byte ptr [rbp - 3107], 0
    mov byte ptr [rbp - 3108], 0
    mov byte ptr [rbp - 3109], 0
    mov byte ptr [rbp - 3110], 0
    mov byte ptr [rbp - 3111], 0
    mov byte ptr [rbp - 3112], 0
    mov byte ptr [rbp - 3113], 0
    mov byte ptr [rbp - 3114], 0
    mov byte ptr [rbp - 3115], 0
    mov byte ptr [rbp - 3116], 0
    mov byte ptr [rbp - 3117], 0
    mov byte ptr [rbp - 3118], 0
    mov byte ptr [rbp - 3119], 0
    mov byte ptr [rbp - 3120], 0
    mov byte ptr [rbp - 3121], 0
    mov byte ptr [rbp - 3122], 0
    mov byte ptr [rbp - 3123], 0
    mov byte ptr [rbp - 3124], 0
    mov byte ptr [rbp - 3125], 0
    mov byte ptr [rbp - 3126], 0
    mov byte ptr [rbp - 3127], 0
    mov byte ptr [rbp - 3128], 0
    mov byte ptr [rbp - 3129], 0
    mov byte ptr [rbp - 3130], 0
    mov byte ptr [rbp - 3131], 0
    mov byte ptr [rbp - 3132], 0
    mov byte ptr [rbp - 3133], 0
    mov byte ptr [rbp - 3134], 0
    mov byte ptr [rbp - 3135], 0
    mov byte ptr [rbp - 3136], 0
    mov byte ptr [rbp - 3137], 0
    mov byte ptr [rbp - 3138], 0
    mov byte ptr [rbp - 3139], 0
    mov byte ptr [rbp - 3140], 0
    mov byte ptr [rbp - 3141], 0
    mov byte ptr [rbp - 3142], 0
    mov byte ptr [rbp - 3143], 0
    mov byte ptr [rbp - 3144], 0
    mov byte ptr [rbp - 3145], 0
    mov byte ptr [rbp - 3146], 0
    mov byte ptr [rbp - 3147], 0
    mov byte ptr [rbp - 3148], 0
    mov byte ptr [rbp - 3149], 0
    mov byte ptr [rbp - 3150], 0
    mov byte ptr [rbp - 3151], 0
    mov byte ptr [rbp - 3152], 0
    mov byte ptr [rbp - 3153], 0
    mov byte ptr [rbp - 3154], 0
    mov byte ptr [rbp - 3155], 0
    mov byte ptr [rbp - 3156], 0
    mov byte ptr [rbp - 3157], 0
    mov byte ptr [rbp - 3158], 0
    mov byte ptr [rbp - 3159], 0
    mov byte ptr [rbp - 3160], 0
    mov byte ptr [rbp - 3161], 0
    mov byte ptr [rbp - 3162], 0
    mov byte ptr [rbp - 3163], 0
    mov byte ptr [rbp - 3164], 0
    mov byte ptr [rbp - 3165], 0
    mov byte ptr [rbp - 3166], 0
    mov byte ptr [rbp - 3167], 0
    mov byte ptr [rbp - 3168], 0
    mov byte ptr [rbp - 3169], 0
    mov byte ptr [rbp - 3170], 0
    mov byte ptr [rbp - 3171], 0
    mov byte ptr [rbp - 3172], 0
    mov byte ptr [rbp - 3173], 0
    mov byte ptr [rbp - 3174], 0
    mov byte ptr [rbp - 3175], 0
    mov byte ptr [rbp - 3176], 0
    mov byte ptr [rbp - 3177], 0
    mov byte ptr [rbp - 3178], 0
    mov byte ptr [rbp - 3179], 0
    mov byte ptr [rbp - 3180], 0
    mov byte ptr [rbp - 3181], 0
    mov byte ptr [rbp - 3182], 0
    mov byte ptr [rbp - 3183], 0
    mov byte ptr [rbp - 3184], 0
    mov byte ptr [rbp - 3185], 0
    mov byte ptr [rbp - 3186], 0
    mov byte ptr [rbp - 3187], 0
    mov byte ptr [rbp - 3188], 0
    mov byte ptr [rbp - 3189], 0
    mov byte ptr [rbp - 3190], 0
    mov byte ptr [rbp - 3191], 0
    mov byte ptr [rbp - 3192], 0
    mov byte ptr [rbp - 3193], 0
    mov byte ptr [rbp - 3194], 0
    mov byte ptr [rbp - 3195], 0
    mov byte ptr [rbp - 3196], 0
    mov byte ptr [rbp - 3197], 0
    mov byte ptr [rbp - 3198], 0
    mov byte ptr [rbp - 3199], 0
    mov byte ptr [rbp - 3200], 0
    mov byte ptr [rbp - 3201], 0
    mov byte ptr [rbp - 3202], 0
    mov byte ptr [rbp - 3203], 0
    mov byte ptr [rbp - 3204], 0
    mov byte ptr [rbp - 3205], 0
    mov byte ptr [rbp - 3206], 0
    mov byte ptr [rbp - 3207], 0
    mov byte ptr [rbp - 3208], 0
    mov byte ptr [rbp - 3209], 0
    mov byte ptr [rbp - 3210], 0
    mov byte ptr [rbp - 3211], 0
    mov byte ptr [rbp - 3212], 0
    mov byte ptr [rbp - 3213], 0
    mov byte ptr [rbp - 3214], 0
    mov byte ptr [rbp - 3215], 0
    mov byte ptr [rbp - 3216], 0
    mov byte ptr [rbp - 3217], 0
    mov byte ptr [rbp - 3218], 0
    mov byte ptr [rbp - 3219], 0
    mov byte ptr [rbp - 3220], 0
    mov byte ptr [rbp - 3221], 0
    mov byte ptr [rbp - 3222], 0
    mov byte ptr [rbp - 3223], 0
    mov byte ptr [rbp - 3224], 0
    mov byte ptr [rbp - 3225], 0
    mov byte ptr [rbp - 3226], 0
    mov byte ptr [rbp - 3227], 0
    mov byte ptr [rbp - 3228], 0
    mov byte ptr [rbp - 3229], 0
    mov byte ptr [rbp - 3230], 0
    mov byte ptr [rbp - 3231], 0
    mov byte ptr [rbp - 3232], 0
    mov byte ptr [rbp - 3233], 0
    mov byte ptr [rbp - 3234], 0
    mov byte ptr [rbp - 3235], 0
    mov byte ptr [rbp - 3236], 0
    mov byte ptr [rbp - 3237], 0
    mov byte ptr [rbp - 3238], 0
    mov byte ptr [rbp - 3239], 0
    mov byte ptr [rbp - 3240], 0
    mov byte ptr [rbp - 3241], 0
    mov byte ptr [rbp - 3242], 0
    mov byte ptr [rbp - 3243], 0
    mov byte ptr [rbp - 3244], 0
    mov byte ptr [rbp - 3245], 0
    mov byte ptr [rbp - 3246], 0
    mov byte ptr [rbp - 3247], 0
    mov byte ptr [rbp - 3248], 0
    mov byte ptr [rbp - 3249], 0
    mov byte ptr [rbp - 3250], 0
    mov byte ptr [rbp - 3251], 0
    mov byte ptr [rbp - 3252], 0
    mov byte ptr [rbp - 3253], 0
    mov byte ptr [rbp - 3254], 0
    mov byte ptr [rbp - 3255], 0
    mov byte ptr [rbp - 3256], 0
    mov byte ptr [rbp - 3257], 0
    mov byte ptr [rbp - 3258], 0
    mov byte ptr [rbp - 3259], 0
    mov byte ptr [rbp - 3260], 0
    mov byte ptr [rbp - 3261], 0
    mov byte ptr [rbp - 3262], 0
    mov byte ptr [rbp - 3263], 0
    mov byte ptr [rbp - 3264], 0
    mov byte ptr [rbp - 3265], 0
    mov byte ptr [rbp - 3266], 0
    mov byte ptr [rbp - 3267], 0
    mov byte ptr [rbp - 3268], 0
    mov byte ptr [rbp - 3269], 0
    mov byte ptr [rbp - 3270], 0
    mov byte ptr [rbp - 3271], 0
    mov byte ptr [rbp - 3272], 0
    mov byte ptr [rbp - 3273], 0
    mov byte ptr [rbp - 3274], 0
    mov byte ptr [rbp - 3275], 0
    mov byte ptr [rbp - 3276], 0
    mov byte ptr [rbp - 3277], 0
    mov byte ptr [rbp - 3278], 0
    mov byte ptr [rbp - 3279], 0
    mov byte ptr [rbp - 3280], 0
    mov byte ptr [rbp - 3281], 0
    mov byte ptr [rbp - 3282], 0
    mov byte ptr [rbp - 3283], 0
    mov byte ptr [rbp - 3284], 0
    mov byte ptr [rbp - 3285], 0
    mov byte ptr [rbp - 3286], 0
    mov byte ptr [rbp - 3287], 0
    mov byte ptr [rbp - 3288], 0
    mov byte ptr [rbp - 3289], 0
    mov byte ptr [rbp - 3290], 0
    mov byte ptr [rbp - 3291], 0
    mov byte ptr [rbp - 3292], 0
    mov byte ptr [rbp - 3293], 0
    mov byte ptr [rbp - 3294], 0
    mov byte ptr [rbp - 3295], 0
    mov byte ptr [rbp - 3296], 0
    mov byte ptr [rbp - 3297], 0
    mov byte ptr [rbp - 3298], 0
    mov byte ptr [rbp - 3299], 0
    mov byte ptr [rbp - 3300], 0
    mov byte ptr [rbp - 3301], 0
    mov byte ptr [rbp - 3302], 0
    mov byte ptr [rbp - 3303], 0
    mov byte ptr [rbp - 3304], 0
    mov byte ptr [rbp - 3305], 0
    mov byte ptr [rbp - 3306], 0
    mov byte ptr [rbp - 3307], 0
    mov byte ptr [rbp - 3308], 0
    mov byte ptr [rbp - 3309], 0
    mov byte ptr [rbp - 3310], 0
    mov byte ptr [rbp - 3311], 0
    mov byte ptr [rbp - 3312], 0
    mov byte ptr [rbp - 3313], 0
    mov byte ptr [rbp - 3314], 0
    mov byte ptr [rbp - 3315], 0
    mov byte ptr [rbp - 3316], 0
    mov byte ptr [rbp - 3317], 0
    mov byte ptr [rbp - 3318], 0
    mov byte ptr [rbp - 3319], 0
    mov byte ptr [rbp - 3320], 0
    mov byte ptr [rbp - 3321], 0
    mov byte ptr [rbp - 3322], 0
    mov byte ptr [rbp - 3323], 0
    mov byte ptr [rbp - 3324], 0
    mov byte ptr [rbp - 3325], 0
    mov byte ptr [rbp - 3326], 0
    mov byte ptr [rbp - 3327], 0
    mov byte ptr [rbp - 3328], 0
    mov byte ptr [rbp - 3329], 0
    mov byte ptr [rbp - 3330], 0
    mov byte ptr [rbp - 3331], 0
    mov byte ptr [rbp - 3332], 0
    mov byte ptr [rbp - 3333], 0
    mov byte ptr [rbp - 3334], 0
    mov byte ptr [rbp - 3335], 0
    mov byte ptr [rbp - 3336], 0
    mov byte ptr [rbp - 3337], 0
    mov byte ptr [rbp - 3338], 0
    mov byte ptr [rbp - 3339], 0
    mov byte ptr [rbp - 3340], 0
    mov byte ptr [rbp - 3341], 0
    mov byte ptr [rbp - 3342], 0
    mov byte ptr [rbp - 3343], 0
    mov byte ptr [rbp - 3344], 0
    mov byte ptr [rbp - 3345], 0
    mov byte ptr [rbp - 3346], 0
    mov byte ptr [rbp - 3347], 0
    mov byte ptr [rbp - 3348], 0
    mov byte ptr [rbp - 3349], 0
    mov byte ptr [rbp - 3350], 0
    mov byte ptr [rbp - 3351], 0
    mov byte ptr [rbp - 3352], 0
    mov byte ptr [rbp - 3353], 0
    mov byte ptr [rbp - 3354], 0
    mov byte ptr [rbp - 3355], 0
    mov byte ptr [rbp - 3356], 0
    mov byte ptr [rbp - 3357], 0
    mov byte ptr [rbp - 3358], 0
    mov byte ptr [rbp - 3359], 0
    mov byte ptr [rbp - 3360], 0
    mov byte ptr [rbp - 3361], 0
    mov byte ptr [rbp - 3362], 0
    mov byte ptr [rbp - 3363], 0
    mov byte ptr [rbp - 3364], 0
    mov byte ptr [rbp - 3365], 0
    mov byte ptr [rbp - 3366], 0
    lea rdi, [rbp - 3705]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3706]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3707]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3708]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3709]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3710]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3711]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3712]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3713]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3714]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3715]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3716]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3717]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3718]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3719]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3720]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3721]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3722]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3723]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3724]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3725]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3726]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3727]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3728]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3729]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3730]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3731]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3732]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3733]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3734]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3735]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3736]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3737]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3738]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3739]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3740]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3741]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3742]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3743]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3744]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3745]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 3746]
    mov ecx, 1
    xor eax, eax
    rep stosb
    mov rdi, r10
    mov rcx, r11
    mov byte ptr [rbp - 2993], 1
    mov byte ptr [rbp - 2994], 1
    mov byte ptr [rbp - 2995], 1
    mov byte ptr [rbp - 2996], 1
    jmp .L_s3_f15_xs_lookup_batch_b5_entry
.L_s3_f15_xs_lookup_batch_b5_entry:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_179
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 2997], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_180
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 2998], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_181
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2998], 0
    je .L__s3_failure_site_182
    mov rax, rsi
    cmp byte ptr [rbp - 2997], 0
    je .L__s3_failure_site_183
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_184
    mov qword ptr [rbp + rax*8 - 3376], r10
    mov byte ptr [rbp + rax - 3705], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_185
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 0
    mov rdi, rax
    mov byte ptr [rbp - 2999], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_186
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3000], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_187
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3000], 0
    je .L__s3_failure_site_188
    mov rax, rsi
    cmp byte ptr [rbp - 2999], 0
    je .L__s3_failure_site_189
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_190
    mov qword ptr [rbp + rax*8 - 3384], r10
    mov byte ptr [rbp + rax - 3706], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_191
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 35
    mov byte ptr [rbp - 3001], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_192
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2995], 0
    je .L__s3_failure_site_194
    mov r10, r13
    cmp byte ptr [rbp - 2996], 0
    je .L__s3_failure_site_195
    mov r11, r14
    cmp byte ptr [rbp - 3001], 0
    je .L__s3_failure_site_196
    mov rax, rdi
    cmp rax, r11
    jae .L__s3_failure_site_193
    mov r11, qword ptr [r10 + rax * 8]
    mov rdi, r11
    mov byte ptr [rbp - 3002], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_197
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3003], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_198
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3003], 0
    je .L__s3_failure_site_199
    mov rax, rsi
    cmp byte ptr [rbp - 3002], 0
    je .L__s3_failure_site_200
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_201
    mov qword ptr [rbp + rax*8 - 3392], r10
    mov byte ptr [rbp + rax - 3707], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_202
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b17_while_condition_0
.L_s3_f15_xs_lookup_batch_b17_while_condition_0:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_203
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3004], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_204
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3004], 0
    je .L__s3_failure_site_206
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_207
    cmp byte ptr [rbp + r10 - 3705], 0
    je .L__s3_failure_site_205
    mov rax, qword ptr [rbp + r10*8 - 3376]
    mov rdi, rax
    mov byte ptr [rbp - 3005], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_208
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3006], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_209
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3006], 0
    je .L__s3_failure_site_211
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_212
    cmp byte ptr [rbp + r10 - 3707], 0
    je .L__s3_failure_site_210
    mov rax, qword ptr [rbp + r10*8 - 3392]
    mov rsi, rax
    mov byte ptr [rbp - 3007], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_213
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3005], 0
    je .L__s3_failure_site_214
    mov rax, rdi
    cmp byte ptr [rbp - 3007], 0
    je .L__s3_failure_site_215
    mov r10, rsi
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_216
    inc qword ptr [rip + __s3_instruction_count]
    cmp rax, r10
    jl .L_s3_f15_xs_lookup_batch_b9_rel_neg_5
    jg .L_s3_f15_xs_lookup_batch_b9_rel_pos_7
    jmp .L_s3_f15_xs_lookup_batch_b10_rel_zero_6
.L_s3_f15_xs_lookup_batch_b12_while_body_1:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_217
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 19
    mov byte ptr [rbp - 3017], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_218
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3018], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_219
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3018], 0
    je .L__s3_failure_site_221
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_222
    cmp byte ptr [rbp + r10 - 3705], 0
    je .L__s3_failure_site_220
    mov rax, qword ptr [rbp + r10*8 - 3376]
    mov rsi, rax
    mov byte ptr [rbp - 3019], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_223
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3017], 0
    je .L__s3_failure_site_225
    mov rax, rdi
    cmp byte ptr [rbp - 3019], 0
    je .L__s3_failure_site_226
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_224
    mov rdi, rax
    mov byte ptr [rbp - 3020], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_227
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3021], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_228
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3021], 0
    je .L__s3_failure_site_229
    mov rax, rsi
    cmp byte ptr [rbp - 3020], 0
    je .L__s3_failure_site_230
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_231
    mov qword ptr [rbp + rax*8 - 3408], r10
    mov byte ptr [rbp + rax - 3709], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_232
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 27
    mov byte ptr [rbp - 3022], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_233
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3023], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_234
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3023], 0
    je .L__s3_failure_site_236
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_237
    cmp byte ptr [rbp + r10 - 3705], 0
    je .L__s3_failure_site_235
    mov rax, qword ptr [rbp + r10*8 - 3376]
    mov rsi, rax
    mov byte ptr [rbp - 3024], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_238
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3022], 0
    je .L__s3_failure_site_240
    mov rax, rdi
    cmp byte ptr [rbp - 3024], 0
    je .L__s3_failure_site_241
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_239
    mov rdi, rax
    mov byte ptr [rbp - 3025], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_242
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3026], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_243
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3026], 0
    je .L__s3_failure_site_244
    mov rax, rsi
    cmp byte ptr [rbp - 3025], 0
    je .L__s3_failure_site_245
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_246
    mov qword ptr [rbp + rax*8 - 3416], r10
    mov byte ptr [rbp + rax - 3710], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_247
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3027], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_248
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3027], 0
    je .L__s3_failure_site_250
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_251
    cmp byte ptr [rbp + r10 - 3709], 0
    je .L__s3_failure_site_249
    mov rax, qword ptr [rbp + r10*8 - 3408]
    mov rdi, rax
    mov byte ptr [rbp - 3028], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_252
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2995], 0
    je .L__s3_failure_site_254
    mov r10, r13
    cmp byte ptr [rbp - 2996], 0
    je .L__s3_failure_site_255
    mov r11, r14
    cmp byte ptr [rbp - 3028], 0
    je .L__s3_failure_site_256
    mov rax, rdi
    cmp rax, r11
    jae .L__s3_failure_site_253
    mov r11, qword ptr [r10 + rax * 8]
    mov rdi, r11
    mov byte ptr [rbp - 3029], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_257
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3030], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_258
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3030], 0
    je .L__s3_failure_site_259
    mov rax, rsi
    cmp byte ptr [rbp - 3029], 0
    je .L__s3_failure_site_260
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_261
    mov qword ptr [rbp + rax*8 - 3424], r10
    mov byte ptr [rbp + rax - 3711], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_262
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3031], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_263
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3031], 0
    je .L__s3_failure_site_265
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_266
    cmp byte ptr [rbp + r10 - 3711], 0
    je .L__s3_failure_site_264
    mov rax, qword ptr [rbp + r10*8 - 3424]
    mov rdi, rax
    mov byte ptr [rbp - 3032], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_267
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3032], 0
    je .L__s3_failure_site_268
    mov rax, rdi
    pxor xmm0, xmm0
    cvtsi2sd xmm0, rax
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3033], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_269
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 4636737291354636288
    mov rsi, rax
    mov byte ptr [rbp - 3034], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_270
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3033], 0
    je .L__s3_failure_site_271
    mov rax, rdi
    cmp byte ptr [rbp - 3034], 0
    je .L__s3_failure_site_272
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3035], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_273
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3036], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_274
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3036], 0
    je .L__s3_failure_site_275
    mov rax, rsi
    cmp byte ptr [rbp - 3035], 0
    je .L__s3_failure_site_276
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_277
    mov qword ptr [rbp + rax*8 - 3432], r10
    mov byte ptr [rbp + rax - 3712], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_278
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3037], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_279
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3037], 0
    je .L__s3_failure_site_281
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_282
    cmp byte ptr [rbp + r10 - 3710], 0
    je .L__s3_failure_site_280
    mov rax, qword ptr [rbp + r10*8 - 3416]
    mov rdi, rax
    mov byte ptr [rbp - 3038], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_283
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2995], 0
    je .L__s3_failure_site_285
    mov r10, r13
    cmp byte ptr [rbp - 2996], 0
    je .L__s3_failure_site_286
    mov r11, r14
    cmp byte ptr [rbp - 3038], 0
    je .L__s3_failure_site_287
    mov rax, rdi
    cmp rax, r11
    jae .L__s3_failure_site_284
    mov r11, qword ptr [r10 + rax * 8]
    mov rdi, r11
    mov byte ptr [rbp - 3039], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_288
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3040], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_289
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3040], 0
    je .L__s3_failure_site_290
    mov rax, rsi
    cmp byte ptr [rbp - 3039], 0
    je .L__s3_failure_site_291
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_292
    mov qword ptr [rbp + rax*8 - 3440], r10
    mov byte ptr [rbp + rax - 3713], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_293
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3041], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_294
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3042], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_295
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3042], 0
    je .L__s3_failure_site_296
    mov rax, rsi
    cmp byte ptr [rbp - 3041], 0
    je .L__s3_failure_site_297
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_298
    mov qword ptr [rbp + rax*8 - 3448], r10
    mov byte ptr [rbp + rax - 3714], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_299
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 0
    mov rdi, rax
    mov byte ptr [rbp - 3043], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_300
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3044], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_301
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3044], 0
    je .L__s3_failure_site_302
    mov rax, rsi
    cmp byte ptr [rbp - 3043], 0
    je .L__s3_failure_site_303
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_304
    mov qword ptr [rbp + rax*8 - 3456], r10
    mov byte ptr [rbp + rax - 3715], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_305
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 0
    mov rdi, rax
    mov byte ptr [rbp - 3045], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_306
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3046], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_307
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3046], 0
    je .L__s3_failure_site_308
    mov rax, rsi
    cmp byte ptr [rbp - 3045], 0
    je .L__s3_failure_site_309
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_310
    mov qword ptr [rbp + rax*8 - 3464], r10
    mov byte ptr [rbp + rax - 3716], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_311
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 0
    mov rdi, rax
    mov byte ptr [rbp - 3047], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_312
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3048], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_313
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3048], 0
    je .L__s3_failure_site_314
    mov rax, rsi
    cmp byte ptr [rbp - 3047], 0
    je .L__s3_failure_site_315
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_316
    mov qword ptr [rbp + rax*8 - 3472], r10
    mov byte ptr [rbp + rax - 3717], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_317
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 0
    mov rdi, rax
    mov byte ptr [rbp - 3049], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_318
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3050], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_319
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3050], 0
    je .L__s3_failure_site_320
    mov rax, rsi
    cmp byte ptr [rbp - 3049], 0
    je .L__s3_failure_site_321
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_322
    mov qword ptr [rbp + rax*8 - 3480], r10
    mov byte ptr [rbp + rax - 3718], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_323
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 0
    mov rdi, rax
    mov byte ptr [rbp - 3051], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_324
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3052], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_325
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3052], 0
    je .L__s3_failure_site_326
    mov rax, rsi
    cmp byte ptr [rbp - 3051], 0
    je .L__s3_failure_site_327
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_328
    mov qword ptr [rbp + rax*8 - 3488], r10
    mov byte ptr [rbp + rax - 3719], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_329
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b17_while_condition_9
.L_s3_f15_xs_lookup_batch_b14_while_exit_0_2:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_330
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b12_while_exit_4
.L_s3_f15_xs_lookup_batch_b14_while_exit_1_3:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_331
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b12_while_exit_4
.L_s3_f15_xs_lookup_batch_b12_while_exit_4:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_332
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3365], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_333
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3365], 0
    je .L__s3_failure_site_335
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_336
    cmp byte ptr [rbp + r10 - 3706], 0
    je .L__s3_failure_site_334
    mov rax, qword ptr [rbp + r10*8 - 3384]
    mov rdi, rax
    mov byte ptr [rbp - 3366], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_337
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3366], 0
    je .L__s3_failure_site_338
    mov rax, rdi
    movq xmm0, rax
    mov rbx, qword ptr [rbp - 3760]
    mov r12, qword ptr [rbp - 3768]
    mov r13, qword ptr [rbp - 3776]
    mov r14, qword ptr [rbp - 3784]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f15_xs_lookup_batch_b9_rel_neg_5:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_339
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3009], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_340
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, -1
    mov byte ptr [rbp - 3010], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_341
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3009], 0
    je .L__s3_failure_site_342
    mov rax, rdi
    cmp byte ptr [rbp - 3010], 0
    je .L__s3_failure_site_343
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_344
    cmp r10, -1
    jl .L__s3_failure_site_345
    cmp r10, 1
    jg .L__s3_failure_site_345
    mov byte ptr [rbp + rax - 3393], r10b
    mov byte ptr [rbp + rax - 3708], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_346
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b10_rel_cont_8
.L_s3_f15_xs_lookup_batch_b10_rel_zero_6:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_347
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3011], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_348
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3012], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_349
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3011], 0
    je .L__s3_failure_site_350
    mov rax, rdi
    cmp byte ptr [rbp - 3012], 0
    je .L__s3_failure_site_351
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_352
    cmp r10, -1
    jl .L__s3_failure_site_353
    cmp r10, 1
    jg .L__s3_failure_site_353
    mov byte ptr [rbp + rax - 3393], r10b
    mov byte ptr [rbp + rax - 3708], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_354
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b10_rel_cont_8
.L_s3_f15_xs_lookup_batch_b9_rel_pos_7:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_355
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3013], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_356
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3014], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_357
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3013], 0
    je .L__s3_failure_site_358
    mov rax, rdi
    cmp byte ptr [rbp - 3014], 0
    je .L__s3_failure_site_359
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_360
    cmp r10, -1
    jl .L__s3_failure_site_361
    cmp r10, 1
    jg .L__s3_failure_site_361
    mov byte ptr [rbp + rax - 3393], r10b
    mov byte ptr [rbp + rax - 3708], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_362
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b10_rel_cont_8
.L_s3_f15_xs_lookup_batch_b10_rel_cont_8:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_363
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3015], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_364
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3015], 0
    je .L__s3_failure_site_366
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_367
    cmp byte ptr [rbp + r10 - 3708], 0
    je .L__s3_failure_site_365
    movsx rax, byte ptr [rbp + r10 - 3393]
    mov rdi, rax
    mov byte ptr [rbp - 3016], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_368
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3016], 0
    je .L__s3_failure_site_370
    mov rax, rdi
    cmp rax, -1
    je .L_s3_f15_xs_lookup_batch_b12_while_body_1
    cmp rax, 0
    je .L_s3_f15_xs_lookup_batch_b14_while_exit_0_2
    cmp rax, 1
    je .L_s3_f15_xs_lookup_batch_b14_while_exit_1_3
    jmp .L__s3_failure_site_369
.L_s3_f15_xs_lookup_batch_b17_while_condition_9:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_371
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3053], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_372
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3053], 0
    je .L__s3_failure_site_374
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_375
    cmp byte ptr [rbp + r10 - 3714], 0
    je .L__s3_failure_site_373
    mov rax, qword ptr [rbp + r10*8 - 3448]
    mov rdi, rax
    mov byte ptr [rbp - 3054], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_376
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 2
    mov byte ptr [rbp - 3055], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_377
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3054], 0
    je .L__s3_failure_site_378
    mov rax, rdi
    cmp byte ptr [rbp - 3055], 0
    je .L__s3_failure_site_379
    mov r10, rsi
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_380
    inc qword ptr [rip + __s3_instruction_count]
    cmp rax, r10
    jl .L_s3_f15_xs_lookup_batch_b10_rel_neg_14
    jg .L_s3_f15_xs_lookup_batch_b10_rel_pos_16
    jmp .L_s3_f15_xs_lookup_batch_b11_rel_zero_15
.L_s3_f15_xs_lookup_batch_b13_while_body_10:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_381
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3065], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_382
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3065], 0
    je .L__s3_failure_site_384
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_385
    cmp byte ptr [rbp + r10 - 3713], 0
    je .L__s3_failure_site_383
    mov rax, qword ptr [rbp + r10*8 - 3440]
    mov rdi, rax
    mov byte ptr [rbp - 3066], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_386
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 2
    mov byte ptr [rbp - 3067], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_387
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3066], 0
    je .L__s3_failure_site_389
    mov rax, rdi
    cmp byte ptr [rbp - 3067], 0
    je .L__s3_failure_site_390
    mov r10, rsi
    imul rax, r10
    jo .L__s3_failure_site_388
    mov rdi, rax
    mov byte ptr [rbp - 3068], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_391
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3069], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_392
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3069], 0
    je .L__s3_failure_site_394
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_395
    cmp byte ptr [rbp + r10 - 3714], 0
    je .L__s3_failure_site_393
    mov rax, qword ptr [rbp + r10*8 - 3448]
    mov rsi, rax
    mov byte ptr [rbp - 3070], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_396
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3068], 0
    je .L__s3_failure_site_398
    mov rax, rdi
    cmp byte ptr [rbp - 3070], 0
    je .L__s3_failure_site_399
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_397
    mov rdi, rax
    mov byte ptr [rbp - 3071], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_400
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3072], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_401
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3072], 0
    je .L__s3_failure_site_402
    mov rax, rsi
    cmp byte ptr [rbp - 3071], 0
    je .L__s3_failure_site_403
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_404
    mov qword ptr [rbp + rax*8 - 3504], r10
    mov byte ptr [rbp + rax - 3721], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_405
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3073], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_406
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3073], 0
    je .L__s3_failure_site_408
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_409
    cmp byte ptr [rbp + r10 - 3721], 0
    je .L__s3_failure_site_407
    mov rax, qword ptr [rbp + r10*8 - 3504]
    mov rdi, rax
    mov byte ptr [rbp - 3074], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_410
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2995], 0
    je .L__s3_failure_site_412
    mov r10, r13
    cmp byte ptr [rbp - 2996], 0
    je .L__s3_failure_site_413
    mov r11, r14
    cmp byte ptr [rbp - 3074], 0
    je .L__s3_failure_site_414
    mov rax, rdi
    cmp rax, r11
    jae .L__s3_failure_site_411
    mov r11, qword ptr [r10 + rax * 8]
    mov rdi, r11
    mov byte ptr [rbp - 3075], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_415
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3076], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_416
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3076], 0
    je .L__s3_failure_site_417
    mov rax, rsi
    cmp byte ptr [rbp - 3075], 0
    je .L__s3_failure_site_418
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_419
    mov qword ptr [rbp + rax*8 - 3512], r10
    mov byte ptr [rbp + rax - 3722], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_420
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 6
    mov byte ptr [rbp - 3077], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_421
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3078], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_422
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3078], 0
    je .L__s3_failure_site_424
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_425
    cmp byte ptr [rbp + r10 - 3713], 0
    je .L__s3_failure_site_423
    mov rax, qword ptr [rbp + r10*8 - 3440]
    mov rsi, rax
    mov byte ptr [rbp - 3079], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_426
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 2
    mov byte ptr [rbp - 3080], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_427
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3079], 0
    je .L__s3_failure_site_429
    mov rax, rsi
    cmp byte ptr [rbp - 3080], 0
    je .L__s3_failure_site_430
    mov r10, rdx
    imul rax, r10
    jo .L__s3_failure_site_428
    mov rsi, rax
    mov byte ptr [rbp - 3081], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_431
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3077], 0
    je .L__s3_failure_site_433
    mov rax, rdi
    cmp byte ptr [rbp - 3081], 0
    je .L__s3_failure_site_434
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_432
    mov rdi, rax
    mov byte ptr [rbp - 3082], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_435
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3083], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_436
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3083], 0
    je .L__s3_failure_site_438
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_439
    cmp byte ptr [rbp + r10 - 3714], 0
    je .L__s3_failure_site_437
    mov rax, qword ptr [rbp + r10*8 - 3448]
    mov rsi, rax
    mov byte ptr [rbp - 3084], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_440
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3082], 0
    je .L__s3_failure_site_442
    mov rax, rdi
    cmp byte ptr [rbp - 3084], 0
    je .L__s3_failure_site_443
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_441
    mov rdi, rax
    mov byte ptr [rbp - 3085], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_444
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3086], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_445
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3086], 0
    je .L__s3_failure_site_446
    mov rax, rsi
    cmp byte ptr [rbp - 3085], 0
    je .L__s3_failure_site_447
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_448
    mov qword ptr [rbp + rax*8 - 3520], r10
    mov byte ptr [rbp + rax - 3723], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_449
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3087], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_450
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3087], 0
    je .L__s3_failure_site_452
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_453
    cmp byte ptr [rbp + r10 - 3723], 0
    je .L__s3_failure_site_451
    mov rax, qword ptr [rbp + r10*8 - 3520]
    mov rdi, rax
    mov byte ptr [rbp - 3088], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_454
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_456
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_457
    mov r11, r12
    cmp byte ptr [rbp - 3088], 0
    je .L__s3_failure_site_458
    mov rax, rdi
    cmp rax, r11
    jae .L__s3_failure_site_455
    mov r11, qword ptr [r10 + rax * 8]
    mov rdi, r11
    mov byte ptr [rbp - 3089], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_459
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3090], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_460
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3090], 0
    je .L__s3_failure_site_461
    mov rax, rsi
    cmp byte ptr [rbp - 3089], 0
    je .L__s3_failure_site_462
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_463
    mov qword ptr [rbp + rax*8 - 3528], r10
    mov byte ptr [rbp + rax - 3724], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_464
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 10
    mov byte ptr [rbp - 3091], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_465
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3092], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_466
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3092], 0
    je .L__s3_failure_site_468
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_469
    cmp byte ptr [rbp + r10 - 3722], 0
    je .L__s3_failure_site_467
    mov rax, qword ptr [rbp + r10*8 - 3512]
    mov rsi, rax
    mov byte ptr [rbp - 3093], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_470
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 25
    mov byte ptr [rbp - 3094], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_471
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3093], 0
    je .L__s3_failure_site_473
    mov rax, rsi
    cmp byte ptr [rbp - 3094], 0
    je .L__s3_failure_site_474
    mov r10, rdx
    imul rax, r10
    jo .L__s3_failure_site_472
    mov rsi, rax
    mov byte ptr [rbp - 3095], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_475
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3091], 0
    je .L__s3_failure_site_477
    mov rax, rdi
    cmp byte ptr [rbp - 3095], 0
    je .L__s3_failure_site_478
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_476
    mov rdi, rax
    mov byte ptr [rbp - 3096], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_479
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3097], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_480
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3097], 0
    je .L__s3_failure_site_481
    mov rax, rsi
    cmp byte ptr [rbp - 3096], 0
    je .L__s3_failure_site_482
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_483
    mov qword ptr [rbp + rax*8 - 3536], r10
    mov byte ptr [rbp + rax - 3725], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_484
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3098], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_485
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3098], 0
    je .L__s3_failure_site_487
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_488
    cmp byte ptr [rbp + r10 - 3722], 0
    je .L__s3_failure_site_486
    mov rax, qword ptr [rbp + r10*8 - 3512]
    mov rdi, rax
    mov byte ptr [rbp - 3099], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_489
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3100], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_490
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3100], 0
    je .L__s3_failure_site_492
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_493
    cmp byte ptr [rbp + r10 - 3711], 0
    je .L__s3_failure_site_491
    mov rax, qword ptr [rbp + r10*8 - 3424]
    mov rsi, rax
    mov byte ptr [rbp - 3101], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_494
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 4
    mov byte ptr [rbp - 3102], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_495
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2995], 0
    je .L__s3_failure_site_496
    mov qword ptr [rbp - 24], r13
    cmp byte ptr [rbp - 2996], 0
    je .L__s3_failure_site_497
    mov qword ptr [rbp - 32], r14
    cmp byte ptr [rbp - 3099], 0
    je .L__s3_failure_site_498
    mov qword ptr [rbp - 856], rdi
    cmp byte ptr [rbp - 3101], 0
    je .L__s3_failure_site_499
    mov qword ptr [rbp - 872], rsi
    cmp byte ptr [rbp - 3102], 0
    je .L__s3_failure_site_500
    mov qword ptr [rbp - 880], rdx
    mov rdi, qword ptr [rbp - 24]
    mov rsi, qword ptr [rbp - 32]
    mov rdx, qword ptr [rbp - 856]
    mov rcx, qword ptr [rbp - 872]
    mov r8, qword ptr [rbp - 880]
    call s3_xsbench_binary_search
    mov rdi, rax
    mov byte ptr [rbp - 3103], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_501
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3104], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_502
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3104], 0
    je .L__s3_failure_site_503
    mov rax, rsi
    cmp byte ptr [rbp - 3103], 0
    je .L__s3_failure_site_504
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_505
    mov qword ptr [rbp + rax*8 - 3544], r10
    mov byte ptr [rbp + rax - 3726], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_506
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3105], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_507
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3105], 0
    je .L__s3_failure_site_509
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_510
    cmp byte ptr [rbp + r10 - 3726], 0
    je .L__s3_failure_site_508
    mov rax, qword ptr [rbp + r10*8 - 3544]
    mov rdi, rax
    mov byte ptr [rbp - 3106], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_511
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 1
    mov byte ptr [rbp - 3107], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_512
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3106], 0
    je .L__s3_failure_site_514
    mov rax, rdi
    cmp byte ptr [rbp - 3107], 0
    je .L__s3_failure_site_515
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_513
    mov rdi, rax
    mov byte ptr [rbp - 3108], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_516
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3109], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_517
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3109], 0
    je .L__s3_failure_site_518
    mov rax, rsi
    cmp byte ptr [rbp - 3108], 0
    je .L__s3_failure_site_519
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_520
    mov qword ptr [rbp + rax*8 - 3552], r10
    mov byte ptr [rbp + rax - 3727], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_521
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3110], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_522
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3110], 0
    je .L__s3_failure_site_524
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_525
    cmp byte ptr [rbp + r10 - 3725], 0
    je .L__s3_failure_site_523
    mov rax, qword ptr [rbp + r10*8 - 3536]
    mov rdi, rax
    mov byte ptr [rbp - 3111], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_526
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3112], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_527
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3112], 0
    je .L__s3_failure_site_529
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_530
    cmp byte ptr [rbp + r10 - 3726], 0
    je .L__s3_failure_site_528
    mov rax, qword ptr [rbp + r10*8 - 3544]
    mov rsi, rax
    mov byte ptr [rbp - 3113], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_531
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 5
    mov byte ptr [rbp - 3114], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_532
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3113], 0
    je .L__s3_failure_site_534
    mov rax, rsi
    cmp byte ptr [rbp - 3114], 0
    je .L__s3_failure_site_535
    mov r10, rdx
    imul rax, r10
    jo .L__s3_failure_site_533
    mov rsi, rax
    mov byte ptr [rbp - 3115], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_536
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3111], 0
    je .L__s3_failure_site_538
    mov rax, rdi
    cmp byte ptr [rbp - 3115], 0
    je .L__s3_failure_site_539
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_537
    mov rdi, rax
    mov byte ptr [rbp - 3116], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_540
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3117], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_541
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3117], 0
    je .L__s3_failure_site_542
    mov rax, rsi
    cmp byte ptr [rbp - 3116], 0
    je .L__s3_failure_site_543
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_544
    mov qword ptr [rbp + rax*8 - 3560], r10
    mov byte ptr [rbp + rax - 3728], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_545
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3118], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_546
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3118], 0
    je .L__s3_failure_site_548
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_549
    cmp byte ptr [rbp + r10 - 3725], 0
    je .L__s3_failure_site_547
    mov rax, qword ptr [rbp + r10*8 - 3536]
    mov rdi, rax
    mov byte ptr [rbp - 3119], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_550
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3120], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_551
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3120], 0
    je .L__s3_failure_site_553
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_554
    cmp byte ptr [rbp + r10 - 3727], 0
    je .L__s3_failure_site_552
    mov rax, qword ptr [rbp + r10*8 - 3552]
    mov rsi, rax
    mov byte ptr [rbp - 3121], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_555
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 5
    mov byte ptr [rbp - 3122], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_556
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3121], 0
    je .L__s3_failure_site_558
    mov rax, rsi
    cmp byte ptr [rbp - 3122], 0
    je .L__s3_failure_site_559
    mov r10, rdx
    imul rax, r10
    jo .L__s3_failure_site_557
    mov rsi, rax
    mov byte ptr [rbp - 3123], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_560
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3119], 0
    je .L__s3_failure_site_562
    mov rax, rdi
    cmp byte ptr [rbp - 3123], 0
    je .L__s3_failure_site_563
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_561
    mov rdi, rax
    mov byte ptr [rbp - 3124], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_564
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3125], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_565
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3125], 0
    je .L__s3_failure_site_566
    mov rax, rsi
    cmp byte ptr [rbp - 3124], 0
    je .L__s3_failure_site_567
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_568
    mov qword ptr [rbp + rax*8 - 3568], r10
    mov byte ptr [rbp + rax - 3729], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_569
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 4
    mov byte ptr [rbp - 3126], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_570
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3127], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_571
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3127], 0
    je .L__s3_failure_site_573
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_574
    cmp byte ptr [rbp + r10 - 3722], 0
    je .L__s3_failure_site_572
    mov rax, qword ptr [rbp + r10*8 - 3512]
    mov rsi, rax
    mov byte ptr [rbp - 3128], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_575
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 5
    mov byte ptr [rbp - 3129], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_576
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3128], 0
    je .L__s3_failure_site_578
    mov rax, rsi
    cmp byte ptr [rbp - 3129], 0
    je .L__s3_failure_site_579
    mov r10, rdx
    imul rax, r10
    jo .L__s3_failure_site_577
    mov rsi, rax
    mov byte ptr [rbp - 3130], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_580
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3126], 0
    je .L__s3_failure_site_582
    mov rax, rdi
    cmp byte ptr [rbp - 3130], 0
    je .L__s3_failure_site_583
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_581
    mov rdi, rax
    mov byte ptr [rbp - 3131], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_584
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3132], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_585
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3132], 0
    je .L__s3_failure_site_587
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_588
    cmp byte ptr [rbp + r10 - 3726], 0
    je .L__s3_failure_site_586
    mov rax, qword ptr [rbp + r10*8 - 3544]
    mov rsi, rax
    mov byte ptr [rbp - 3133], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_589
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3131], 0
    je .L__s3_failure_site_591
    mov rax, rdi
    cmp byte ptr [rbp - 3133], 0
    je .L__s3_failure_site_592
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_590
    mov rdi, rax
    mov byte ptr [rbp - 3134], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_593
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3135], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_594
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3135], 0
    je .L__s3_failure_site_595
    mov rax, rsi
    cmp byte ptr [rbp - 3134], 0
    je .L__s3_failure_site_596
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_597
    mov qword ptr [rbp + rax*8 - 3576], r10
    mov byte ptr [rbp + rax - 3730], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_598
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 4
    mov byte ptr [rbp - 3136], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_599
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3137], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_600
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3137], 0
    je .L__s3_failure_site_602
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_603
    cmp byte ptr [rbp + r10 - 3722], 0
    je .L__s3_failure_site_601
    mov rax, qword ptr [rbp + r10*8 - 3512]
    mov rsi, rax
    mov byte ptr [rbp - 3138], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_604
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 5
    mov byte ptr [rbp - 3139], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_605
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3138], 0
    je .L__s3_failure_site_607
    mov rax, rsi
    cmp byte ptr [rbp - 3139], 0
    je .L__s3_failure_site_608
    mov r10, rdx
    imul rax, r10
    jo .L__s3_failure_site_606
    mov rsi, rax
    mov byte ptr [rbp - 3140], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_609
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3136], 0
    je .L__s3_failure_site_611
    mov rax, rdi
    cmp byte ptr [rbp - 3140], 0
    je .L__s3_failure_site_612
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_610
    mov rdi, rax
    mov byte ptr [rbp - 3141], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_613
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3142], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_614
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3142], 0
    je .L__s3_failure_site_616
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_617
    cmp byte ptr [rbp + r10 - 3727], 0
    je .L__s3_failure_site_615
    mov rax, qword ptr [rbp + r10*8 - 3552]
    mov rsi, rax
    mov byte ptr [rbp - 3143], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_618
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3141], 0
    je .L__s3_failure_site_620
    mov rax, rdi
    cmp byte ptr [rbp - 3143], 0
    je .L__s3_failure_site_621
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_619
    mov rdi, rax
    mov byte ptr [rbp - 3144], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_622
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3145], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_623
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3145], 0
    je .L__s3_failure_site_624
    mov rax, rsi
    cmp byte ptr [rbp - 3144], 0
    je .L__s3_failure_site_625
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_626
    mov qword ptr [rbp + rax*8 - 3584], r10
    mov byte ptr [rbp + rax - 3731], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_627
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3146], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_628
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3146], 0
    je .L__s3_failure_site_630
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_631
    cmp byte ptr [rbp + r10 - 3730], 0
    je .L__s3_failure_site_629
    mov rax, qword ptr [rbp + r10*8 - 3576]
    mov rdi, rax
    mov byte ptr [rbp - 3147], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_632
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2995], 0
    je .L__s3_failure_site_634
    mov r10, r13
    cmp byte ptr [rbp - 2996], 0
    je .L__s3_failure_site_635
    mov r11, r14
    cmp byte ptr [rbp - 3147], 0
    je .L__s3_failure_site_636
    mov rax, rdi
    cmp rax, r11
    jae .L__s3_failure_site_633
    mov r11, qword ptr [r10 + rax * 8]
    mov rdi, r11
    mov byte ptr [rbp - 3148], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_637
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3149], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_638
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3149], 0
    je .L__s3_failure_site_639
    mov rax, rsi
    cmp byte ptr [rbp - 3148], 0
    je .L__s3_failure_site_640
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_641
    mov qword ptr [rbp + rax*8 - 3592], r10
    mov byte ptr [rbp + rax - 3732], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_642
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3150], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_643
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3150], 0
    je .L__s3_failure_site_645
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_646
    cmp byte ptr [rbp + r10 - 3731], 0
    je .L__s3_failure_site_644
    mov rax, qword ptr [rbp + r10*8 - 3584]
    mov rdi, rax
    mov byte ptr [rbp - 3151], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_647
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2995], 0
    je .L__s3_failure_site_649
    mov r10, r13
    cmp byte ptr [rbp - 2996], 0
    je .L__s3_failure_site_650
    mov r11, r14
    cmp byte ptr [rbp - 3151], 0
    je .L__s3_failure_site_651
    mov rax, rdi
    cmp rax, r11
    jae .L__s3_failure_site_648
    mov r11, qword ptr [r10 + rax * 8]
    mov rdi, r11
    mov byte ptr [rbp - 3152], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_652
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3153], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_653
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3153], 0
    je .L__s3_failure_site_654
    mov rax, rsi
    cmp byte ptr [rbp - 3152], 0
    je .L__s3_failure_site_655
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_656
    mov qword ptr [rbp + rax*8 - 3600], r10
    mov byte ptr [rbp + rax - 3733], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_657
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3154], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_658
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3154], 0
    je .L__s3_failure_site_660
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_661
    cmp byte ptr [rbp + r10 - 3732], 0
    je .L__s3_failure_site_659
    mov rax, qword ptr [rbp + r10*8 - 3592]
    mov rdi, rax
    mov byte ptr [rbp - 3155], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_662
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3155], 0
    je .L__s3_failure_site_663
    mov rax, rdi
    pxor xmm0, xmm0
    cvtsi2sd xmm0, rax
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3156], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_664
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 4636737291354636288
    mov rsi, rax
    mov byte ptr [rbp - 3157], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_665
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3156], 0
    je .L__s3_failure_site_666
    mov rax, rdi
    cmp byte ptr [rbp - 3157], 0
    je .L__s3_failure_site_667
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3158], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_668
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3159], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_669
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3159], 0
    je .L__s3_failure_site_670
    mov rax, rsi
    cmp byte ptr [rbp - 3158], 0
    je .L__s3_failure_site_671
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_672
    mov qword ptr [rbp + rax*8 - 3608], r10
    mov byte ptr [rbp + rax - 3734], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_673
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3160], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_674
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3160], 0
    je .L__s3_failure_site_676
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_677
    cmp byte ptr [rbp + r10 - 3733], 0
    je .L__s3_failure_site_675
    mov rax, qword ptr [rbp + r10*8 - 3600]
    mov rdi, rax
    mov byte ptr [rbp - 3161], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_678
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3161], 0
    je .L__s3_failure_site_679
    mov rax, rdi
    pxor xmm0, xmm0
    cvtsi2sd xmm0, rax
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3162], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_680
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 4636737291354636288
    mov rsi, rax
    mov byte ptr [rbp - 3163], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_681
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3162], 0
    je .L__s3_failure_site_682
    mov rax, rdi
    cmp byte ptr [rbp - 3163], 0
    je .L__s3_failure_site_683
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3164], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_684
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3165], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_685
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3165], 0
    je .L__s3_failure_site_686
    mov rax, rsi
    cmp byte ptr [rbp - 3164], 0
    je .L__s3_failure_site_687
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_688
    mov qword ptr [rbp + rax*8 - 3616], r10
    mov byte ptr [rbp + rax - 3735], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_689
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3166], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_690
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3166], 0
    je .L__s3_failure_site_692
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_693
    cmp byte ptr [rbp + r10 - 3735], 0
    je .L__s3_failure_site_691
    mov rax, qword ptr [rbp + r10*8 - 3616]
    mov rdi, rax
    mov byte ptr [rbp - 3167], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_694
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3168], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_695
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3168], 0
    je .L__s3_failure_site_697
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_698
    cmp byte ptr [rbp + r10 - 3712], 0
    je .L__s3_failure_site_696
    mov rax, qword ptr [rbp + r10*8 - 3432]
    mov rsi, rax
    mov byte ptr [rbp - 3169], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_699
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3167], 0
    je .L__s3_failure_site_700
    mov rax, rdi
    cmp byte ptr [rbp - 3169], 0
    je .L__s3_failure_site_701
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3170], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_702
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3171], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_703
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3171], 0
    je .L__s3_failure_site_705
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_706
    cmp byte ptr [rbp + r10 - 3735], 0
    je .L__s3_failure_site_704
    mov rax, qword ptr [rbp + r10*8 - 3616]
    mov rsi, rax
    mov byte ptr [rbp - 3172], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_707
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3173], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_708
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3173], 0
    je .L__s3_failure_site_710
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_711
    cmp byte ptr [rbp + r10 - 3734], 0
    je .L__s3_failure_site_709
    mov rax, qword ptr [rbp + r10*8 - 3608]
    mov rdx, rax
    mov byte ptr [rbp - 3174], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_712
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3172], 0
    je .L__s3_failure_site_713
    mov rax, rsi
    cmp byte ptr [rbp - 3174], 0
    je .L__s3_failure_site_714
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3175], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_715
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3170], 0
    je .L__s3_failure_site_716
    mov rax, rdi
    cmp byte ptr [rbp - 3175], 0
    je .L__s3_failure_site_717
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3176], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_718
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3177], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_719
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3177], 0
    je .L__s3_failure_site_720
    mov rax, rsi
    cmp byte ptr [rbp - 3176], 0
    je .L__s3_failure_site_721
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_722
    mov qword ptr [rbp + rax*8 - 3624], r10
    mov byte ptr [rbp + rax - 3736], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_723
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3178], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_724
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3178], 0
    je .L__s3_failure_site_726
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_727
    cmp byte ptr [rbp + r10 - 3729], 0
    je .L__s3_failure_site_725
    mov rax, qword ptr [rbp + r10*8 - 3568]
    mov rdi, rax
    mov byte ptr [rbp - 3179], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_728
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3180], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_729
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3180], 0
    je .L__s3_failure_site_730
    mov rax, rsi
    cmp byte ptr [rbp - 3179], 0
    je .L__s3_failure_site_731
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_732
    mov qword ptr [rbp + rax*8 - 3632], r10
    mov byte ptr [rbp + rax - 3737], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_733
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3181], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_734
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3181], 0
    je .L__s3_failure_site_736
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_737
    cmp byte ptr [rbp + r10 - 3728], 0
    je .L__s3_failure_site_735
    mov rax, qword ptr [rbp + r10*8 - 3560]
    mov rdi, rax
    mov byte ptr [rbp - 3182], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_738
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3183], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_739
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3183], 0
    je .L__s3_failure_site_740
    mov rax, rsi
    cmp byte ptr [rbp - 3182], 0
    je .L__s3_failure_site_741
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_742
    mov qword ptr [rbp + rax*8 - 3640], r10
    mov byte ptr [rbp + rax - 3738], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_743
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3184], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_744
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3184], 0
    je .L__s3_failure_site_746
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_747
    cmp byte ptr [rbp + r10 - 3729], 0
    je .L__s3_failure_site_745
    mov rax, qword ptr [rbp + r10*8 - 3568]
    mov rdi, rax
    mov byte ptr [rbp - 3185], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_748
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 1
    mov byte ptr [rbp - 3186], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_749
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3185], 0
    je .L__s3_failure_site_751
    mov rax, rdi
    cmp byte ptr [rbp - 3186], 0
    je .L__s3_failure_site_752
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_750
    mov rdi, rax
    mov byte ptr [rbp - 3187], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_753
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3188], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_754
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3188], 0
    je .L__s3_failure_site_755
    mov rax, rsi
    cmp byte ptr [rbp - 3187], 0
    je .L__s3_failure_site_756
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_757
    mov qword ptr [rbp + rax*8 - 3648], r10
    mov byte ptr [rbp + rax - 3739], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_758
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3189], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_759
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3189], 0
    je .L__s3_failure_site_761
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_762
    cmp byte ptr [rbp + r10 - 3728], 0
    je .L__s3_failure_site_760
    mov rax, qword ptr [rbp + r10*8 - 3560]
    mov rdi, rax
    mov byte ptr [rbp - 3190], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_763
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 1
    mov byte ptr [rbp - 3191], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_764
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3190], 0
    je .L__s3_failure_site_766
    mov rax, rdi
    cmp byte ptr [rbp - 3191], 0
    je .L__s3_failure_site_767
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_765
    mov rdi, rax
    mov byte ptr [rbp - 3192], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_768
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3193], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_769
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3193], 0
    je .L__s3_failure_site_770
    mov rax, rsi
    cmp byte ptr [rbp - 3192], 0
    je .L__s3_failure_site_771
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_772
    mov qword ptr [rbp + rax*8 - 3656], r10
    mov byte ptr [rbp + rax - 3740], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_773
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3194], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_774
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3194], 0
    je .L__s3_failure_site_776
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_777
    cmp byte ptr [rbp + r10 - 3729], 0
    je .L__s3_failure_site_775
    mov rax, qword ptr [rbp + r10*8 - 3568]
    mov rdi, rax
    mov byte ptr [rbp - 3195], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_778
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 2
    mov byte ptr [rbp - 3196], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_779
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3195], 0
    je .L__s3_failure_site_781
    mov rax, rdi
    cmp byte ptr [rbp - 3196], 0
    je .L__s3_failure_site_782
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_780
    mov rdi, rax
    mov byte ptr [rbp - 3197], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_783
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3198], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_784
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3198], 0
    je .L__s3_failure_site_785
    mov rax, rsi
    cmp byte ptr [rbp - 3197], 0
    je .L__s3_failure_site_786
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_787
    mov qword ptr [rbp + rax*8 - 3664], r10
    mov byte ptr [rbp + rax - 3741], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_788
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3199], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_789
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3199], 0
    je .L__s3_failure_site_791
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_792
    cmp byte ptr [rbp + r10 - 3728], 0
    je .L__s3_failure_site_790
    mov rax, qword ptr [rbp + r10*8 - 3560]
    mov rdi, rax
    mov byte ptr [rbp - 3200], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_793
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 2
    mov byte ptr [rbp - 3201], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_794
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3200], 0
    je .L__s3_failure_site_796
    mov rax, rdi
    cmp byte ptr [rbp - 3201], 0
    je .L__s3_failure_site_797
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_795
    mov rdi, rax
    mov byte ptr [rbp - 3202], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_798
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3203], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_799
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3203], 0
    je .L__s3_failure_site_800
    mov rax, rsi
    cmp byte ptr [rbp - 3202], 0
    je .L__s3_failure_site_801
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_802
    mov qword ptr [rbp + rax*8 - 3672], r10
    mov byte ptr [rbp + rax - 3742], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_803
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3204], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_804
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3204], 0
    je .L__s3_failure_site_806
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_807
    cmp byte ptr [rbp + r10 - 3729], 0
    je .L__s3_failure_site_805
    mov rax, qword ptr [rbp + r10*8 - 3568]
    mov rdi, rax
    mov byte ptr [rbp - 3205], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_808
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 3
    mov byte ptr [rbp - 3206], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_809
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3205], 0
    je .L__s3_failure_site_811
    mov rax, rdi
    cmp byte ptr [rbp - 3206], 0
    je .L__s3_failure_site_812
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_810
    mov rdi, rax
    mov byte ptr [rbp - 3207], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_813
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3208], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_814
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3208], 0
    je .L__s3_failure_site_815
    mov rax, rsi
    cmp byte ptr [rbp - 3207], 0
    je .L__s3_failure_site_816
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_817
    mov qword ptr [rbp + rax*8 - 3680], r10
    mov byte ptr [rbp + rax - 3743], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_818
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3209], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_819
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3209], 0
    je .L__s3_failure_site_821
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_822
    cmp byte ptr [rbp + r10 - 3728], 0
    je .L__s3_failure_site_820
    mov rax, qword ptr [rbp + r10*8 - 3560]
    mov rdi, rax
    mov byte ptr [rbp - 3210], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_823
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 3
    mov byte ptr [rbp - 3211], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_824
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3210], 0
    je .L__s3_failure_site_826
    mov rax, rdi
    cmp byte ptr [rbp - 3211], 0
    je .L__s3_failure_site_827
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_825
    mov rdi, rax
    mov byte ptr [rbp - 3212], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_828
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3213], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_829
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3213], 0
    je .L__s3_failure_site_830
    mov rax, rsi
    cmp byte ptr [rbp - 3212], 0
    je .L__s3_failure_site_831
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_832
    mov qword ptr [rbp + rax*8 - 3688], r10
    mov byte ptr [rbp + rax - 3744], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_833
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3214], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_834
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3214], 0
    je .L__s3_failure_site_836
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_837
    cmp byte ptr [rbp + r10 - 3729], 0
    je .L__s3_failure_site_835
    mov rax, qword ptr [rbp + r10*8 - 3568]
    mov rdi, rax
    mov byte ptr [rbp - 3215], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_838
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 4
    mov byte ptr [rbp - 3216], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_839
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3215], 0
    je .L__s3_failure_site_841
    mov rax, rdi
    cmp byte ptr [rbp - 3216], 0
    je .L__s3_failure_site_842
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_840
    mov rdi, rax
    mov byte ptr [rbp - 3217], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_843
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3218], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_844
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3218], 0
    je .L__s3_failure_site_845
    mov rax, rsi
    cmp byte ptr [rbp - 3217], 0
    je .L__s3_failure_site_846
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_847
    mov qword ptr [rbp + rax*8 - 3696], r10
    mov byte ptr [rbp + rax - 3745], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_848
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3219], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_849
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3219], 0
    je .L__s3_failure_site_851
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_852
    cmp byte ptr [rbp + r10 - 3728], 0
    je .L__s3_failure_site_850
    mov rax, qword ptr [rbp + r10*8 - 3560]
    mov rdi, rax
    mov byte ptr [rbp - 3220], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_853
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 4
    mov byte ptr [rbp - 3221], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_854
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3220], 0
    je .L__s3_failure_site_856
    mov rax, rdi
    cmp byte ptr [rbp - 3221], 0
    je .L__s3_failure_site_857
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_855
    mov rdi, rax
    mov byte ptr [rbp - 3222], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_858
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3223], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_859
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3223], 0
    je .L__s3_failure_site_860
    mov rax, rsi
    cmp byte ptr [rbp - 3222], 0
    je .L__s3_failure_site_861
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_862
    mov qword ptr [rbp + rax*8 - 3704], r10
    mov byte ptr [rbp + rax - 3746], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_863
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3224], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_864
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3224], 0
    je .L__s3_failure_site_866
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_867
    cmp byte ptr [rbp + r10 - 3715], 0
    je .L__s3_failure_site_865
    mov rax, qword ptr [rbp + r10*8 - 3456]
    mov rdi, rax
    mov byte ptr [rbp - 3225], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_868
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3226], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_869
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3226], 0
    je .L__s3_failure_site_871
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_872
    cmp byte ptr [rbp + r10 - 3724], 0
    je .L__s3_failure_site_870
    mov rax, qword ptr [rbp + r10*8 - 3528]
    mov rsi, rax
    mov byte ptr [rbp - 3227], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_873
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3228], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_874
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3228], 0
    je .L__s3_failure_site_876
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_877
    cmp byte ptr [rbp + r10 - 3737], 0
    je .L__s3_failure_site_875
    mov rax, qword ptr [rbp + r10*8 - 3632]
    mov rdx, rax
    mov byte ptr [rbp - 3229], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_878
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_880
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_881
    mov r11, r12
    cmp byte ptr [rbp - 3229], 0
    je .L__s3_failure_site_882
    mov rax, rdx
    cmp rax, r11
    jae .L__s3_failure_site_879
    mov r11, qword ptr [r10 + rax * 8]
    mov rdx, r11
    mov byte ptr [rbp - 3230], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_883
    inc qword ptr [rip + __s3_instruction_count]
    mov rcx, 0
    mov byte ptr [rbp - 3231], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_884
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3231], 0
    je .L__s3_failure_site_886
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_887
    cmp byte ptr [rbp + r10 - 3736], 0
    je .L__s3_failure_site_885
    mov rax, qword ptr [rbp + r10*8 - 3624]
    mov rcx, rax
    mov byte ptr [rbp - 3232], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_888
    inc qword ptr [rip + __s3_instruction_count]
    mov r8, 0
    mov byte ptr [rbp - 3233], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_889
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3233], 0
    je .L__s3_failure_site_891
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_892
    cmp byte ptr [rbp + r10 - 3737], 0
    je .L__s3_failure_site_890
    mov rax, qword ptr [rbp + r10*8 - 3632]
    mov r8, rax
    mov byte ptr [rbp - 3234], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_893
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_895
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_896
    mov r11, r12
    cmp byte ptr [rbp - 3234], 0
    je .L__s3_failure_site_897
    mov rax, r8
    cmp rax, r11
    jae .L__s3_failure_site_894
    mov r11, qword ptr [r10 + rax * 8]
    mov r8, r11
    mov byte ptr [rbp - 3235], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_898
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 3236], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_899
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3236], 0
    je .L__s3_failure_site_901
    mov r10, r9
    cmp r10, 1
    jae .L__s3_failure_site_902
    cmp byte ptr [rbp + r10 - 3738], 0
    je .L__s3_failure_site_900
    mov rax, qword ptr [rbp + r10*8 - 3640]
    mov r9, rax
    mov byte ptr [rbp - 3237], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_903
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_905
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_906
    mov r11, r12
    cmp byte ptr [rbp - 3237], 0
    je .L__s3_failure_site_907
    mov rax, r9
    cmp rax, r11
    jae .L__s3_failure_site_904
    mov r11, qword ptr [r10 + rax * 8]
    mov r9, r11
    mov byte ptr [rbp - 3238], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_908
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3235], 0
    je .L__s3_failure_site_909
    mov rax, r8
    cmp byte ptr [rbp - 3238], 0
    je .L__s3_failure_site_910
    mov r10, r9
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r8, rax
    mov byte ptr [rbp - 3239], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_911
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3232], 0
    je .L__s3_failure_site_912
    mov rax, rcx
    cmp byte ptr [rbp - 3239], 0
    je .L__s3_failure_site_913
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 3240], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_914
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3230], 0
    je .L__s3_failure_site_915
    mov rax, rdx
    cmp byte ptr [rbp - 3240], 0
    je .L__s3_failure_site_916
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 3241], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_917
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3227], 0
    je .L__s3_failure_site_918
    mov rax, rsi
    cmp byte ptr [rbp - 3241], 0
    je .L__s3_failure_site_919
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3242], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_920
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3225], 0
    je .L__s3_failure_site_921
    mov rax, rdi
    cmp byte ptr [rbp - 3242], 0
    je .L__s3_failure_site_922
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3243], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_923
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3244], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_924
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3244], 0
    je .L__s3_failure_site_925
    mov rax, rsi
    cmp byte ptr [rbp - 3243], 0
    je .L__s3_failure_site_926
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_927
    mov qword ptr [rbp + rax*8 - 3456], r10
    mov byte ptr [rbp + rax - 3715], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_928
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3245], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_929
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3245], 0
    je .L__s3_failure_site_931
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_932
    cmp byte ptr [rbp + r10 - 3716], 0
    je .L__s3_failure_site_930
    mov rax, qword ptr [rbp + r10*8 - 3464]
    mov rdi, rax
    mov byte ptr [rbp - 3246], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_933
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3247], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_934
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3247], 0
    je .L__s3_failure_site_936
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_937
    cmp byte ptr [rbp + r10 - 3724], 0
    je .L__s3_failure_site_935
    mov rax, qword ptr [rbp + r10*8 - 3528]
    mov rsi, rax
    mov byte ptr [rbp - 3248], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_938
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3249], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_939
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3249], 0
    je .L__s3_failure_site_941
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_942
    cmp byte ptr [rbp + r10 - 3739], 0
    je .L__s3_failure_site_940
    mov rax, qword ptr [rbp + r10*8 - 3648]
    mov rdx, rax
    mov byte ptr [rbp - 3250], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_943
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_945
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_946
    mov r11, r12
    cmp byte ptr [rbp - 3250], 0
    je .L__s3_failure_site_947
    mov rax, rdx
    cmp rax, r11
    jae .L__s3_failure_site_944
    mov r11, qword ptr [r10 + rax * 8]
    mov rdx, r11
    mov byte ptr [rbp - 3251], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_948
    inc qword ptr [rip + __s3_instruction_count]
    mov rcx, 0
    mov byte ptr [rbp - 3252], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_949
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3252], 0
    je .L__s3_failure_site_951
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_952
    cmp byte ptr [rbp + r10 - 3736], 0
    je .L__s3_failure_site_950
    mov rax, qword ptr [rbp + r10*8 - 3624]
    mov rcx, rax
    mov byte ptr [rbp - 3253], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_953
    inc qword ptr [rip + __s3_instruction_count]
    mov r8, 0
    mov byte ptr [rbp - 3254], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_954
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3254], 0
    je .L__s3_failure_site_956
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_957
    cmp byte ptr [rbp + r10 - 3739], 0
    je .L__s3_failure_site_955
    mov rax, qword ptr [rbp + r10*8 - 3648]
    mov r8, rax
    mov byte ptr [rbp - 3255], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_958
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_960
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_961
    mov r11, r12
    cmp byte ptr [rbp - 3255], 0
    je .L__s3_failure_site_962
    mov rax, r8
    cmp rax, r11
    jae .L__s3_failure_site_959
    mov r11, qword ptr [r10 + rax * 8]
    mov r8, r11
    mov byte ptr [rbp - 3256], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_963
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 3257], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_964
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3257], 0
    je .L__s3_failure_site_966
    mov r10, r9
    cmp r10, 1
    jae .L__s3_failure_site_967
    cmp byte ptr [rbp + r10 - 3740], 0
    je .L__s3_failure_site_965
    mov rax, qword ptr [rbp + r10*8 - 3656]
    mov r9, rax
    mov byte ptr [rbp - 3258], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_968
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_970
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_971
    mov r11, r12
    cmp byte ptr [rbp - 3258], 0
    je .L__s3_failure_site_972
    mov rax, r9
    cmp rax, r11
    jae .L__s3_failure_site_969
    mov r11, qword ptr [r10 + rax * 8]
    mov r9, r11
    mov byte ptr [rbp - 3259], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_973
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3256], 0
    je .L__s3_failure_site_974
    mov rax, r8
    cmp byte ptr [rbp - 3259], 0
    je .L__s3_failure_site_975
    mov r10, r9
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r8, rax
    mov byte ptr [rbp - 3260], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_976
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3253], 0
    je .L__s3_failure_site_977
    mov rax, rcx
    cmp byte ptr [rbp - 3260], 0
    je .L__s3_failure_site_978
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 3261], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_979
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3251], 0
    je .L__s3_failure_site_980
    mov rax, rdx
    cmp byte ptr [rbp - 3261], 0
    je .L__s3_failure_site_981
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 3262], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_982
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3248], 0
    je .L__s3_failure_site_983
    mov rax, rsi
    cmp byte ptr [rbp - 3262], 0
    je .L__s3_failure_site_984
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3263], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_985
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3246], 0
    je .L__s3_failure_site_986
    mov rax, rdi
    cmp byte ptr [rbp - 3263], 0
    je .L__s3_failure_site_987
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3264], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_988
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3265], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_989
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3265], 0
    je .L__s3_failure_site_990
    mov rax, rsi
    cmp byte ptr [rbp - 3264], 0
    je .L__s3_failure_site_991
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_992
    mov qword ptr [rbp + rax*8 - 3464], r10
    mov byte ptr [rbp + rax - 3716], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_993
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3266], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_994
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3266], 0
    je .L__s3_failure_site_996
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_997
    cmp byte ptr [rbp + r10 - 3717], 0
    je .L__s3_failure_site_995
    mov rax, qword ptr [rbp + r10*8 - 3472]
    mov rdi, rax
    mov byte ptr [rbp - 3267], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_998
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3268], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_999
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3268], 0
    je .L__s3_failure_site_1001
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_1002
    cmp byte ptr [rbp + r10 - 3724], 0
    je .L__s3_failure_site_1000
    mov rax, qword ptr [rbp + r10*8 - 3528]
    mov rsi, rax
    mov byte ptr [rbp - 3269], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1003
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3270], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1004
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3270], 0
    je .L__s3_failure_site_1006
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_1007
    cmp byte ptr [rbp + r10 - 3741], 0
    je .L__s3_failure_site_1005
    mov rax, qword ptr [rbp + r10*8 - 3664]
    mov rdx, rax
    mov byte ptr [rbp - 3271], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1008
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1010
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1011
    mov r11, r12
    cmp byte ptr [rbp - 3271], 0
    je .L__s3_failure_site_1012
    mov rax, rdx
    cmp rax, r11
    jae .L__s3_failure_site_1009
    mov r11, qword ptr [r10 + rax * 8]
    mov rdx, r11
    mov byte ptr [rbp - 3272], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1013
    inc qword ptr [rip + __s3_instruction_count]
    mov rcx, 0
    mov byte ptr [rbp - 3273], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1014
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3273], 0
    je .L__s3_failure_site_1016
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_1017
    cmp byte ptr [rbp + r10 - 3736], 0
    je .L__s3_failure_site_1015
    mov rax, qword ptr [rbp + r10*8 - 3624]
    mov rcx, rax
    mov byte ptr [rbp - 3274], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1018
    inc qword ptr [rip + __s3_instruction_count]
    mov r8, 0
    mov byte ptr [rbp - 3275], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1019
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3275], 0
    je .L__s3_failure_site_1021
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_1022
    cmp byte ptr [rbp + r10 - 3741], 0
    je .L__s3_failure_site_1020
    mov rax, qword ptr [rbp + r10*8 - 3664]
    mov r8, rax
    mov byte ptr [rbp - 3276], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1023
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1025
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1026
    mov r11, r12
    cmp byte ptr [rbp - 3276], 0
    je .L__s3_failure_site_1027
    mov rax, r8
    cmp rax, r11
    jae .L__s3_failure_site_1024
    mov r11, qword ptr [r10 + rax * 8]
    mov r8, r11
    mov byte ptr [rbp - 3277], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1028
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 3278], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1029
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3278], 0
    je .L__s3_failure_site_1031
    mov r10, r9
    cmp r10, 1
    jae .L__s3_failure_site_1032
    cmp byte ptr [rbp + r10 - 3742], 0
    je .L__s3_failure_site_1030
    mov rax, qword ptr [rbp + r10*8 - 3672]
    mov r9, rax
    mov byte ptr [rbp - 3279], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1033
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1035
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1036
    mov r11, r12
    cmp byte ptr [rbp - 3279], 0
    je .L__s3_failure_site_1037
    mov rax, r9
    cmp rax, r11
    jae .L__s3_failure_site_1034
    mov r11, qword ptr [r10 + rax * 8]
    mov r9, r11
    mov byte ptr [rbp - 3280], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1038
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3277], 0
    je .L__s3_failure_site_1039
    mov rax, r8
    cmp byte ptr [rbp - 3280], 0
    je .L__s3_failure_site_1040
    mov r10, r9
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r8, rax
    mov byte ptr [rbp - 3281], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1041
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3274], 0
    je .L__s3_failure_site_1042
    mov rax, rcx
    cmp byte ptr [rbp - 3281], 0
    je .L__s3_failure_site_1043
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 3282], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1044
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3272], 0
    je .L__s3_failure_site_1045
    mov rax, rdx
    cmp byte ptr [rbp - 3282], 0
    je .L__s3_failure_site_1046
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 3283], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1047
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3269], 0
    je .L__s3_failure_site_1048
    mov rax, rsi
    cmp byte ptr [rbp - 3283], 0
    je .L__s3_failure_site_1049
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3284], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1050
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3267], 0
    je .L__s3_failure_site_1051
    mov rax, rdi
    cmp byte ptr [rbp - 3284], 0
    je .L__s3_failure_site_1052
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3285], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1053
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3286], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1054
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3286], 0
    je .L__s3_failure_site_1055
    mov rax, rsi
    cmp byte ptr [rbp - 3285], 0
    je .L__s3_failure_site_1056
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_1057
    mov qword ptr [rbp + rax*8 - 3472], r10
    mov byte ptr [rbp + rax - 3717], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1058
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3287], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1059
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3287], 0
    je .L__s3_failure_site_1061
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_1062
    cmp byte ptr [rbp + r10 - 3718], 0
    je .L__s3_failure_site_1060
    mov rax, qword ptr [rbp + r10*8 - 3480]
    mov rdi, rax
    mov byte ptr [rbp - 3288], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1063
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3289], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1064
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3289], 0
    je .L__s3_failure_site_1066
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_1067
    cmp byte ptr [rbp + r10 - 3724], 0
    je .L__s3_failure_site_1065
    mov rax, qword ptr [rbp + r10*8 - 3528]
    mov rsi, rax
    mov byte ptr [rbp - 3290], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1068
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3291], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1069
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3291], 0
    je .L__s3_failure_site_1071
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_1072
    cmp byte ptr [rbp + r10 - 3743], 0
    je .L__s3_failure_site_1070
    mov rax, qword ptr [rbp + r10*8 - 3680]
    mov rdx, rax
    mov byte ptr [rbp - 3292], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1073
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1075
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1076
    mov r11, r12
    cmp byte ptr [rbp - 3292], 0
    je .L__s3_failure_site_1077
    mov rax, rdx
    cmp rax, r11
    jae .L__s3_failure_site_1074
    mov r11, qword ptr [r10 + rax * 8]
    mov rdx, r11
    mov byte ptr [rbp - 3293], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1078
    inc qword ptr [rip + __s3_instruction_count]
    mov rcx, 0
    mov byte ptr [rbp - 3294], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1079
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3294], 0
    je .L__s3_failure_site_1081
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_1082
    cmp byte ptr [rbp + r10 - 3736], 0
    je .L__s3_failure_site_1080
    mov rax, qword ptr [rbp + r10*8 - 3624]
    mov rcx, rax
    mov byte ptr [rbp - 3295], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1083
    inc qword ptr [rip + __s3_instruction_count]
    mov r8, 0
    mov byte ptr [rbp - 3296], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1084
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3296], 0
    je .L__s3_failure_site_1086
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_1087
    cmp byte ptr [rbp + r10 - 3743], 0
    je .L__s3_failure_site_1085
    mov rax, qword ptr [rbp + r10*8 - 3680]
    mov r8, rax
    mov byte ptr [rbp - 3297], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1088
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1090
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1091
    mov r11, r12
    cmp byte ptr [rbp - 3297], 0
    je .L__s3_failure_site_1092
    mov rax, r8
    cmp rax, r11
    jae .L__s3_failure_site_1089
    mov r11, qword ptr [r10 + rax * 8]
    mov r8, r11
    mov byte ptr [rbp - 3298], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1093
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 3299], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1094
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3299], 0
    je .L__s3_failure_site_1096
    mov r10, r9
    cmp r10, 1
    jae .L__s3_failure_site_1097
    cmp byte ptr [rbp + r10 - 3744], 0
    je .L__s3_failure_site_1095
    mov rax, qword ptr [rbp + r10*8 - 3688]
    mov r9, rax
    mov byte ptr [rbp - 3300], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1098
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1100
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1101
    mov r11, r12
    cmp byte ptr [rbp - 3300], 0
    je .L__s3_failure_site_1102
    mov rax, r9
    cmp rax, r11
    jae .L__s3_failure_site_1099
    mov r11, qword ptr [r10 + rax * 8]
    mov r9, r11
    mov byte ptr [rbp - 3301], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1103
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3298], 0
    je .L__s3_failure_site_1104
    mov rax, r8
    cmp byte ptr [rbp - 3301], 0
    je .L__s3_failure_site_1105
    mov r10, r9
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r8, rax
    mov byte ptr [rbp - 3302], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1106
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3295], 0
    je .L__s3_failure_site_1107
    mov rax, rcx
    cmp byte ptr [rbp - 3302], 0
    je .L__s3_failure_site_1108
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 3303], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1109
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3293], 0
    je .L__s3_failure_site_1110
    mov rax, rdx
    cmp byte ptr [rbp - 3303], 0
    je .L__s3_failure_site_1111
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 3304], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1112
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3290], 0
    je .L__s3_failure_site_1113
    mov rax, rsi
    cmp byte ptr [rbp - 3304], 0
    je .L__s3_failure_site_1114
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3305], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1115
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3288], 0
    je .L__s3_failure_site_1116
    mov rax, rdi
    cmp byte ptr [rbp - 3305], 0
    je .L__s3_failure_site_1117
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3306], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1118
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3307], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1119
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3307], 0
    je .L__s3_failure_site_1120
    mov rax, rsi
    cmp byte ptr [rbp - 3306], 0
    je .L__s3_failure_site_1121
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_1122
    mov qword ptr [rbp + rax*8 - 3480], r10
    mov byte ptr [rbp + rax - 3718], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1123
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3308], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1124
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3308], 0
    je .L__s3_failure_site_1126
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_1127
    cmp byte ptr [rbp + r10 - 3719], 0
    je .L__s3_failure_site_1125
    mov rax, qword ptr [rbp + r10*8 - 3488]
    mov rdi, rax
    mov byte ptr [rbp - 3309], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1128
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3310], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1129
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3310], 0
    je .L__s3_failure_site_1131
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_1132
    cmp byte ptr [rbp + r10 - 3724], 0
    je .L__s3_failure_site_1130
    mov rax, qword ptr [rbp + r10*8 - 3528]
    mov rsi, rax
    mov byte ptr [rbp - 3311], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1133
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3312], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1134
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3312], 0
    je .L__s3_failure_site_1136
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_1137
    cmp byte ptr [rbp + r10 - 3745], 0
    je .L__s3_failure_site_1135
    mov rax, qword ptr [rbp + r10*8 - 3696]
    mov rdx, rax
    mov byte ptr [rbp - 3313], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1138
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1140
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1141
    mov r11, r12
    cmp byte ptr [rbp - 3313], 0
    je .L__s3_failure_site_1142
    mov rax, rdx
    cmp rax, r11
    jae .L__s3_failure_site_1139
    mov r11, qword ptr [r10 + rax * 8]
    mov rdx, r11
    mov byte ptr [rbp - 3314], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1143
    inc qword ptr [rip + __s3_instruction_count]
    mov rcx, 0
    mov byte ptr [rbp - 3315], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1144
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3315], 0
    je .L__s3_failure_site_1146
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_1147
    cmp byte ptr [rbp + r10 - 3736], 0
    je .L__s3_failure_site_1145
    mov rax, qword ptr [rbp + r10*8 - 3624]
    mov rcx, rax
    mov byte ptr [rbp - 3316], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1148
    inc qword ptr [rip + __s3_instruction_count]
    mov r8, 0
    mov byte ptr [rbp - 3317], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1149
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3317], 0
    je .L__s3_failure_site_1151
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_1152
    cmp byte ptr [rbp + r10 - 3745], 0
    je .L__s3_failure_site_1150
    mov rax, qword ptr [rbp + r10*8 - 3696]
    mov r8, rax
    mov byte ptr [rbp - 3318], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1153
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1155
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1156
    mov r11, r12
    cmp byte ptr [rbp - 3318], 0
    je .L__s3_failure_site_1157
    mov rax, r8
    cmp rax, r11
    jae .L__s3_failure_site_1154
    mov r11, qword ptr [r10 + rax * 8]
    mov r8, r11
    mov byte ptr [rbp - 3319], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1158
    inc qword ptr [rip + __s3_instruction_count]
    mov r9, 0
    mov byte ptr [rbp - 3320], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1159
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3320], 0
    je .L__s3_failure_site_1161
    mov r10, r9
    cmp r10, 1
    jae .L__s3_failure_site_1162
    cmp byte ptr [rbp + r10 - 3746], 0
    je .L__s3_failure_site_1160
    mov rax, qword ptr [rbp + r10*8 - 3704]
    mov r9, rax
    mov byte ptr [rbp - 3321], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1163
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 2993], 0
    je .L__s3_failure_site_1165
    mov r10, rbx
    cmp byte ptr [rbp - 2994], 0
    je .L__s3_failure_site_1166
    mov r11, r12
    cmp byte ptr [rbp - 3321], 0
    je .L__s3_failure_site_1167
    mov rax, r9
    cmp rax, r11
    jae .L__s3_failure_site_1164
    mov r11, qword ptr [r10 + rax * 8]
    mov r9, r11
    mov byte ptr [rbp - 3322], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1168
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3319], 0
    je .L__s3_failure_site_1169
    mov rax, r8
    cmp byte ptr [rbp - 3322], 0
    je .L__s3_failure_site_1170
    mov r10, r9
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r8, rax
    mov byte ptr [rbp - 3323], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1171
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3316], 0
    je .L__s3_failure_site_1172
    mov rax, rcx
    cmp byte ptr [rbp - 3323], 0
    je .L__s3_failure_site_1173
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 3324], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1174
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3314], 0
    je .L__s3_failure_site_1175
    mov rax, rdx
    cmp byte ptr [rbp - 3324], 0
    je .L__s3_failure_site_1176
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 3325], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1177
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3311], 0
    je .L__s3_failure_site_1178
    mov rax, rsi
    cmp byte ptr [rbp - 3325], 0
    je .L__s3_failure_site_1179
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3326], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1180
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3309], 0
    je .L__s3_failure_site_1181
    mov rax, rdi
    cmp byte ptr [rbp - 3326], 0
    je .L__s3_failure_site_1182
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3327], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1183
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3328], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1184
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3328], 0
    je .L__s3_failure_site_1185
    mov rax, rsi
    cmp byte ptr [rbp - 3327], 0
    je .L__s3_failure_site_1186
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_1187
    mov qword ptr [rbp + rax*8 - 3488], r10
    mov byte ptr [rbp + rax - 3719], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1188
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3329], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1189
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3329], 0
    je .L__s3_failure_site_1191
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_1192
    cmp byte ptr [rbp + r10 - 3714], 0
    je .L__s3_failure_site_1190
    mov rax, qword ptr [rbp + r10*8 - 3448]
    mov rdi, rax
    mov byte ptr [rbp - 3330], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1193
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 1
    mov byte ptr [rbp - 3331], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1194
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3330], 0
    je .L__s3_failure_site_1196
    mov rax, rdi
    cmp byte ptr [rbp - 3331], 0
    je .L__s3_failure_site_1197
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_1195
    mov rdi, rax
    mov byte ptr [rbp - 3332], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1198
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3333], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1199
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3333], 0
    je .L__s3_failure_site_1200
    mov rax, rsi
    cmp byte ptr [rbp - 3332], 0
    je .L__s3_failure_site_1201
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_1202
    mov qword ptr [rbp + rax*8 - 3448], r10
    mov byte ptr [rbp + rax - 3714], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1203
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b17_while_condition_9
.L_s3_f15_xs_lookup_batch_b15_while_exit_0_11:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1204
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b13_while_exit_13
.L_s3_f15_xs_lookup_batch_b15_while_exit_1_12:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1205
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b13_while_exit_13
.L_s3_f15_xs_lookup_batch_b13_while_exit_13:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1206
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3334], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1207
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3334], 0
    je .L__s3_failure_site_1209
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_1210
    cmp byte ptr [rbp + r10 - 3706], 0
    je .L__s3_failure_site_1208
    mov rax, qword ptr [rbp + r10*8 - 3384]
    mov rdi, rax
    mov byte ptr [rbp - 3335], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1211
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3336], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1212
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3336], 0
    je .L__s3_failure_site_1214
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_1215
    cmp byte ptr [rbp + r10 - 3715], 0
    je .L__s3_failure_site_1213
    mov rax, qword ptr [rbp + r10*8 - 3456]
    mov rsi, rax
    mov byte ptr [rbp - 3337], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1216
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3335], 0
    je .L__s3_failure_site_1217
    mov rax, rdi
    cmp byte ptr [rbp - 3337], 0
    je .L__s3_failure_site_1218
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3338], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1219
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 4613937818241073152
    mov rsi, rax
    mov byte ptr [rbp - 3339], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1220
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3340], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1221
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3340], 0
    je .L__s3_failure_site_1223
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_1224
    cmp byte ptr [rbp + r10 - 3716], 0
    je .L__s3_failure_site_1222
    mov rax, qword ptr [rbp + r10*8 - 3464]
    mov rdx, rax
    mov byte ptr [rbp - 3341], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1225
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3339], 0
    je .L__s3_failure_site_1226
    mov rax, rsi
    cmp byte ptr [rbp - 3341], 0
    je .L__s3_failure_site_1227
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3342], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1228
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3338], 0
    je .L__s3_failure_site_1229
    mov rax, rdi
    cmp byte ptr [rbp - 3342], 0
    je .L__s3_failure_site_1230
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3343], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1231
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 4617315517961601024
    mov rsi, rax
    mov byte ptr [rbp - 3344], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1232
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3345], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1233
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3345], 0
    je .L__s3_failure_site_1235
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_1236
    cmp byte ptr [rbp + r10 - 3717], 0
    je .L__s3_failure_site_1234
    mov rax, qword ptr [rbp + r10*8 - 3472]
    mov rdx, rax
    mov byte ptr [rbp - 3346], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1237
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3344], 0
    je .L__s3_failure_site_1238
    mov rax, rsi
    cmp byte ptr [rbp - 3346], 0
    je .L__s3_failure_site_1239
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3347], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1240
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3343], 0
    je .L__s3_failure_site_1241
    mov rax, rdi
    cmp byte ptr [rbp - 3347], 0
    je .L__s3_failure_site_1242
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3348], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1243
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 4619567317775286272
    mov rsi, rax
    mov byte ptr [rbp - 3349], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1244
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3350], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1245
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3350], 0
    je .L__s3_failure_site_1247
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_1248
    cmp byte ptr [rbp + r10 - 3718], 0
    je .L__s3_failure_site_1246
    mov rax, qword ptr [rbp + r10*8 - 3480]
    mov rdx, rax
    mov byte ptr [rbp - 3351], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1249
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3349], 0
    je .L__s3_failure_site_1250
    mov rax, rsi
    cmp byte ptr [rbp - 3351], 0
    je .L__s3_failure_site_1251
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3352], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1252
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3348], 0
    je .L__s3_failure_site_1253
    mov rax, rdi
    cmp byte ptr [rbp - 3352], 0
    je .L__s3_failure_site_1254
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3353], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1255
    inc qword ptr [rip + __s3_instruction_count]
    movabs rax, 4622382067542392832
    mov rsi, rax
    mov byte ptr [rbp - 3354], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1256
    inc qword ptr [rip + __s3_instruction_count]
    mov rdx, 0
    mov byte ptr [rbp - 3355], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1257
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3355], 0
    je .L__s3_failure_site_1259
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_1260
    cmp byte ptr [rbp + r10 - 3719], 0
    je .L__s3_failure_site_1258
    mov rax, qword ptr [rbp + r10*8 - 3488]
    mov rdx, rax
    mov byte ptr [rbp - 3356], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1261
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3354], 0
    je .L__s3_failure_site_1262
    mov rax, rsi
    cmp byte ptr [rbp - 3356], 0
    je .L__s3_failure_site_1263
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 3357], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1264
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3353], 0
    je .L__s3_failure_site_1265
    mov rax, rdi
    cmp byte ptr [rbp - 3357], 0
    je .L__s3_failure_site_1266
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 3358], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1267
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3359], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1268
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3359], 0
    je .L__s3_failure_site_1269
    mov rax, rsi
    cmp byte ptr [rbp - 3358], 0
    je .L__s3_failure_site_1270
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_1271
    mov qword ptr [rbp + rax*8 - 3384], r10
    mov byte ptr [rbp + rax - 3706], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1272
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3360], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1273
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3360], 0
    je .L__s3_failure_site_1275
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_1276
    cmp byte ptr [rbp + r10 - 3705], 0
    je .L__s3_failure_site_1274
    mov rax, qword ptr [rbp + r10*8 - 3376]
    mov rdi, rax
    mov byte ptr [rbp - 3361], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1277
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 1
    mov byte ptr [rbp - 3362], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1278
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3361], 0
    je .L__s3_failure_site_1280
    mov rax, rdi
    cmp byte ptr [rbp - 3362], 0
    je .L__s3_failure_site_1281
    mov r10, rsi
    add rax, r10
    jo .L__s3_failure_site_1279
    mov rdi, rax
    mov byte ptr [rbp - 3363], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1282
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3364], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1283
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3364], 0
    je .L__s3_failure_site_1284
    mov rax, rsi
    cmp byte ptr [rbp - 3363], 0
    je .L__s3_failure_site_1285
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_1286
    mov qword ptr [rbp + rax*8 - 3376], r10
    mov byte ptr [rbp + rax - 3705], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1287
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b17_while_condition_0
.L_s3_f15_xs_lookup_batch_b10_rel_neg_14:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1288
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3057], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1289
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, -1
    mov byte ptr [rbp - 3058], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1290
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3057], 0
    je .L__s3_failure_site_1291
    mov rax, rdi
    cmp byte ptr [rbp - 3058], 0
    je .L__s3_failure_site_1292
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_1293
    cmp r10, -1
    jl .L__s3_failure_site_1294
    cmp r10, 1
    jg .L__s3_failure_site_1294
    mov byte ptr [rbp + rax - 3489], r10b
    mov byte ptr [rbp + rax - 3720], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1295
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b11_rel_cont_17
.L_s3_f15_xs_lookup_batch_b11_rel_zero_15:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1296
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3059], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1297
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3060], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1298
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3059], 0
    je .L__s3_failure_site_1299
    mov rax, rdi
    cmp byte ptr [rbp - 3060], 0
    je .L__s3_failure_site_1300
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_1301
    cmp r10, -1
    jl .L__s3_failure_site_1302
    cmp r10, 1
    jg .L__s3_failure_site_1302
    mov byte ptr [rbp + rax - 3489], r10b
    mov byte ptr [rbp + rax - 3720], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1303
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b11_rel_cont_17
.L_s3_f15_xs_lookup_batch_b10_rel_pos_16:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1304
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3061], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1305
    inc qword ptr [rip + __s3_instruction_count]
    mov rsi, 0
    mov byte ptr [rbp - 3062], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1306
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3061], 0
    je .L__s3_failure_site_1307
    mov rax, rdi
    cmp byte ptr [rbp - 3062], 0
    je .L__s3_failure_site_1308
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_1309
    cmp r10, -1
    jl .L__s3_failure_site_1310
    cmp r10, 1
    jg .L__s3_failure_site_1310
    mov byte ptr [rbp + rax - 3489], r10b
    mov byte ptr [rbp + rax - 3720], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1311
    inc qword ptr [rip + __s3_instruction_count]
    jmp .L_s3_f15_xs_lookup_batch_b11_rel_cont_17
.L_s3_f15_xs_lookup_batch_b11_rel_cont_17:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1312
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 3063], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1313
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3063], 0
    je .L__s3_failure_site_1315
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_1316
    cmp byte ptr [rbp + r10 - 3720], 0
    je .L__s3_failure_site_1314
    movsx rax, byte ptr [rbp + r10 - 3489]
    mov rdi, rax
    mov byte ptr [rbp - 3064], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1317
    inc qword ptr [rip + __s3_instruction_count]
    cmp byte ptr [rbp - 3064], 0
    je .L__s3_failure_site_1319
    mov rax, rdi
    cmp rax, -1
    je .L_s3_f15_xs_lookup_batch_b13_while_body_10
    cmp rax, 0
    je .L_s3_f15_xs_lookup_batch_b15_while_exit_0_11
    cmp rax, 1
    je .L_s3_f15_xs_lookup_batch_b15_while_exit_1_12
    jmp .L__s3_failure_site_1318
.size xs_lookup_batch, .-xs_lookup_batch

.globl s3_main
.type s3_main, @function
s3_main:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_1320
    push rbp
    mov rbp, rsp
    sub rsp, 32
    mov byte ptr [rbp - 9], 0
    jmp .L_s3_f4_main_b5_entry
.L_s3_f4_main_b5_entry:
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1321
    inc qword ptr [rip + __s3_instruction_count]
    mov rdi, 0
    mov byte ptr [rbp - 9], 1
    movabs r11, 10000000000
    cmp qword ptr [rip + __s3_instruction_count], r11
    jae .L__s3_failure_site_1322
    inc qword ptr [rip + __s3_instruction_count]
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
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_2:
    lea rsi, [rip + .L__s3_failure_prefix_2]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_3:
    lea rsi, [rip + .L__s3_failure_prefix_3]
    mov edx, 146
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
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_8:
    lea rsi, [rip + .L__s3_failure_prefix_8]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_9:
    lea rsi, [rip + .L__s3_failure_prefix_9]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_10:
    lea rsi, [rip + .L__s3_failure_prefix_10]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_11:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_11]
    mov edx, 102
    lea rcx, [rip + .L__s3_failure_suffix_11]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_12:
    lea rsi, [rip + .L__s3_failure_prefix_12]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_13:
    lea rsi, [rip + .L__s3_failure_prefix_13]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_14:
    lea rsi, [rip + .L__s3_failure_prefix_14]
    mov edx, 147
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
    lea rsi, [rip + .L__s3_failure_prefix_17]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_18:
    lea rsi, [rip + .L__s3_failure_prefix_18]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_19:
    lea rsi, [rip + .L__s3_failure_prefix_19]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_20:
    lea rsi, [rip + .L__s3_failure_prefix_20]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_21:
    lea rsi, [rip + .L__s3_failure_prefix_21]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_22:
    lea rsi, [rip + .L__s3_failure_prefix_22]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_23:
    lea rsi, [rip + .L__s3_failure_prefix_23]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_24:
    lea rsi, [rip + .L__s3_failure_prefix_24]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_25:
    lea rsi, [rip + .L__s3_failure_prefix_25]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_26:
    lea rsi, [rip + .L__s3_failure_prefix_26]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_27:
    lea rsi, [rip + .L__s3_failure_prefix_27]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_28:
    lea rsi, [rip + .L__s3_failure_prefix_28]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_29:
    lea rsi, [rip + .L__s3_failure_prefix_29]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_30:
    lea rsi, [rip + .L__s3_failure_prefix_30]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_31:
    lea rsi, [rip + .L__s3_failure_prefix_31]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_32:
    lea rsi, [rip + .L__s3_failure_prefix_32]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_33:
    lea rsi, [rip + .L__s3_failure_prefix_33]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_34:
    lea rsi, [rip + .L__s3_failure_prefix_34]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_35:
    lea rsi, [rip + .L__s3_failure_prefix_35]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_36:
    lea rsi, [rip + .L__s3_failure_prefix_36]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_37:
    lea rsi, [rip + .L__s3_failure_prefix_37]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_38:
    lea rsi, [rip + .L__s3_failure_prefix_38]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_39:
    lea rsi, [rip + .L__s3_failure_prefix_39]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_40:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_40]
    mov edx, 128
    lea rcx, [rip + .L__s3_failure_suffix_40]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_41:
    lea rsi, [rip + .L__s3_failure_prefix_41]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_42:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_42]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_42]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_43:
    lea rsi, [rip + .L__s3_failure_prefix_43]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_44:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_44]
    mov edx, 128
    lea rcx, [rip + .L__s3_failure_suffix_44]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_45:
    lea rsi, [rip + .L__s3_failure_prefix_45]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_46:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_46]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_46]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_47:
    lea rsi, [rip + .L__s3_failure_prefix_47]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_48:
    lea rsi, [rip + .L__s3_failure_prefix_48]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_49:
    lea rsi, [rip + .L__s3_failure_prefix_49]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_50:
    lea rsi, [rip + .L__s3_failure_prefix_50]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_51:
    lea rsi, [rip + .L__s3_failure_prefix_51]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_52:
    lea rsi, [rip + .L__s3_failure_prefix_52]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_53:
    lea rsi, [rip + .L__s3_failure_prefix_53]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_54:
    lea rsi, [rip + .L__s3_failure_prefix_54]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_55:
    lea rsi, [rip + .L__s3_failure_prefix_55]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_56:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_56]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_56]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_57:
    lea rsi, [rip + .L__s3_failure_prefix_57]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_58:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_58]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_58]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_59:
    lea rsi, [rip + .L__s3_failure_prefix_59]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_60:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_60]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_60]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_61:
    lea rsi, [rip + .L__s3_failure_prefix_61]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_62:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_62]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_62]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_63:
    lea rsi, [rip + .L__s3_failure_prefix_63]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_64:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_64]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_64]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_65:
    lea rsi, [rip + .L__s3_failure_prefix_65]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_66:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_66]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_66]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_67:
    lea rsi, [rip + .L__s3_failure_prefix_67]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_68:
    lea rsi, [rip + .L__s3_failure_prefix_68]
    mov edx, 131
    jmp __s3_fail_message
.L__s3_failure_site_69:
    lea rsi, [rip + .L__s3_failure_prefix_69]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_70:
    lea rsi, [rip + .L__s3_failure_prefix_70]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_71:
    lea rsi, [rip + .L__s3_failure_prefix_71]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_72:
    lea rsi, [rip + .L__s3_failure_prefix_72]
    mov edx, 126
    jmp __s3_fail_message
.L__s3_failure_site_73:
    lea rsi, [rip + .L__s3_failure_prefix_73]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_74:
    lea rsi, [rip + .L__s3_failure_prefix_74]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_75:
    lea rsi, [rip + .L__s3_failure_prefix_75]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_76:
    lea rsi, [rip + .L__s3_failure_prefix_76]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_77:
    lea rsi, [rip + .L__s3_failure_prefix_77]
    mov edx, 126
    jmp __s3_fail_message
.L__s3_failure_site_78:
    lea rsi, [rip + .L__s3_failure_prefix_78]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_79:
    lea rsi, [rip + .L__s3_failure_prefix_79]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_80:
    lea rsi, [rip + .L__s3_failure_prefix_80]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_81:
    lea rsi, [rip + .L__s3_failure_prefix_81]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_82:
    lea rsi, [rip + .L__s3_failure_prefix_82]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_83:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_83]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_83]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_84:
    lea rsi, [rip + .L__s3_failure_prefix_84]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_85:
    lea rsi, [rip + .L__s3_failure_prefix_85]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_86:
    lea rsi, [rip + .L__s3_failure_prefix_86]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_87:
    lea rsi, [rip + .L__s3_failure_prefix_87]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_88:
    lea rsi, [rip + .L__s3_failure_prefix_88]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_89:
    lea rsi, [rip + .L__s3_failure_prefix_89]
    mov edx, 126
    jmp __s3_fail_message
.L__s3_failure_site_90:
    lea rsi, [rip + .L__s3_failure_prefix_90]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_91:
    lea rsi, [rip + .L__s3_failure_prefix_91]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_92:
    lea rsi, [rip + .L__s3_failure_prefix_92]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_93:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_93]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_93]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_94:
    lea rsi, [rip + .L__s3_failure_prefix_94]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_95:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_95]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_95]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_96:
    lea rsi, [rip + .L__s3_failure_prefix_96]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_97:
    lea rsi, [rip + .L__s3_failure_prefix_97]
    mov edx, 126
    jmp __s3_fail_message
.L__s3_failure_site_98:
    lea rsi, [rip + .L__s3_failure_prefix_98]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_99:
    lea rsi, [rip + .L__s3_failure_prefix_99]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_100:
    lea rsi, [rip + .L__s3_failure_prefix_100]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_101:
    lea rsi, [rip + .L__s3_failure_prefix_101]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_102:
    lea rsi, [rip + .L__s3_failure_prefix_102]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_103:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_103]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_103]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_104:
    lea rsi, [rip + .L__s3_failure_prefix_104]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_105:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_105]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_105]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_106:
    lea rsi, [rip + .L__s3_failure_prefix_106]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_107:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_107]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_107]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_108:
    lea rsi, [rip + .L__s3_failure_prefix_108]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_109:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_109]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_109]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_110:
    lea rsi, [rip + .L__s3_failure_prefix_110]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_111:
    lea rsi, [rip + .L__s3_failure_prefix_111]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_112:
    lea rsi, [rip + .L__s3_failure_prefix_112]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_113:
    lea rsi, [rip + .L__s3_failure_prefix_113]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_114:
    lea rsi, [rip + .L__s3_failure_prefix_114]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_115:
    lea rsi, [rip + .L__s3_failure_prefix_115]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_116:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_116]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_116]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_117:
    lea rsi, [rip + .L__s3_failure_prefix_117]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_118:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_118]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_118]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_119:
    lea rsi, [rip + .L__s3_failure_prefix_119]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_120:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_120]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_120]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_121:
    lea rsi, [rip + .L__s3_failure_prefix_121]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_122:
    lea rsi, [rip + .L__s3_failure_prefix_122]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_123:
    lea rsi, [rip + .L__s3_failure_prefix_123]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_124:
    lea rsi, [rip + .L__s3_failure_prefix_124]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_125:
    lea rsi, [rip + .L__s3_failure_prefix_125]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_126:
    lea rsi, [rip + .L__s3_failure_prefix_126]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_127:
    lea rsi, [rip + .L__s3_failure_prefix_127]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_128:
    lea rsi, [rip + .L__s3_failure_prefix_128]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_129:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_129]
    mov edx, 124
    lea rcx, [rip + .L__s3_failure_suffix_129]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_130:
    lea rsi, [rip + .L__s3_failure_prefix_130]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_131:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_131]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_131]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_132:
    lea rsi, [rip + .L__s3_failure_prefix_132]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_133:
    lea rsi, [rip + .L__s3_failure_prefix_133]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_134:
    lea rsi, [rip + .L__s3_failure_prefix_134]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_135:
    lea rsi, [rip + .L__s3_failure_prefix_135]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_136:
    lea rsi, [rip + .L__s3_failure_prefix_136]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_137:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_137]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_137]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_138:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_138]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_138]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_139:
    lea rsi, [rip + .L__s3_failure_prefix_139]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_140:
    lea rsi, [rip + .L__s3_failure_prefix_140]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_141:
    lea rsi, [rip + .L__s3_failure_prefix_141]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_142:
    lea rsi, [rip + .L__s3_failure_prefix_142]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_143:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_143]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_143]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_144:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_144]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_144]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_145:
    lea rsi, [rip + .L__s3_failure_prefix_145]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_146:
    lea rsi, [rip + .L__s3_failure_prefix_146]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_147:
    lea rsi, [rip + .L__s3_failure_prefix_147]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_148:
    lea rsi, [rip + .L__s3_failure_prefix_148]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_149:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_149]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_149]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_150:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_150]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_150]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_151:
    lea rsi, [rip + .L__s3_failure_prefix_151]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_152:
    lea rsi, [rip + .L__s3_failure_prefix_152]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_153:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_153]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_153]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_154:
    lea rsi, [rip + .L__s3_failure_prefix_154]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_155:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_155]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_155]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_156:
    lea rsi, [rip + .L__s3_failure_prefix_156]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_157:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_157]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_157]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_158:
    lea rsi, [rip + .L__s3_failure_prefix_158]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_159:
    lea rsi, [rip + .L__s3_failure_prefix_159]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_160:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_160]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_160]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_161:
    lea rsi, [rip + .L__s3_failure_prefix_161]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_162:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_162]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_162]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_163:
    lea rsi, [rip + .L__s3_failure_prefix_163]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_164:
    lea rsi, [rip + .L__s3_failure_prefix_164]
    mov edx, 155
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
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_168:
    lea rsi, [rip + .L__s3_failure_prefix_168]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_169:
    lea rsi, [rip + .L__s3_failure_prefix_169]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_170:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_170]
    mov edx, 130
    lea rcx, [rip + .L__s3_failure_suffix_170]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_171:
    lea rsi, [rip + .L__s3_failure_prefix_171]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_172:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_172]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_172]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_173:
    lea rsi, [rip + .L__s3_failure_prefix_173]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_174:
    lea rsi, [rip + .L__s3_failure_prefix_174]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_175:
    lea rsi, [rip + .L__s3_failure_prefix_175]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_176:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_176]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_176]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_177:
    lea rsi, [rip + .L__s3_failure_prefix_177]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_178:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_178]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_178]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_179:
    lea rsi, [rip + .L__s3_failure_prefix_179]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_180:
    lea rsi, [rip + .L__s3_failure_prefix_180]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_181:
    lea rsi, [rip + .L__s3_failure_prefix_181]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_182:
    lea rsi, [rip + .L__s3_failure_prefix_182]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_183:
    lea rsi, [rip + .L__s3_failure_prefix_183]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_184:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_184]
    mov edx, 97
    lea rcx, [rip + .L__s3_failure_suffix_184]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_185:
    lea rsi, [rip + .L__s3_failure_prefix_185]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_186:
    lea rsi, [rip + .L__s3_failure_prefix_186]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_187:
    lea rsi, [rip + .L__s3_failure_prefix_187]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_188:
    lea rsi, [rip + .L__s3_failure_prefix_188]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_189:
    lea rsi, [rip + .L__s3_failure_prefix_189]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_190:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_190]
    mov edx, 97
    lea rcx, [rip + .L__s3_failure_suffix_190]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_191:
    lea rsi, [rip + .L__s3_failure_prefix_191]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_192:
    lea rsi, [rip + .L__s3_failure_prefix_192]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_193:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_193]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_193]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_194:
    lea rsi, [rip + .L__s3_failure_prefix_194]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_195:
    lea rsi, [rip + .L__s3_failure_prefix_195]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_196:
    lea rsi, [rip + .L__s3_failure_prefix_196]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_197:
    lea rsi, [rip + .L__s3_failure_prefix_197]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_198:
    lea rsi, [rip + .L__s3_failure_prefix_198]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_199:
    lea rsi, [rip + .L__s3_failure_prefix_199]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_200:
    lea rsi, [rip + .L__s3_failure_prefix_200]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_201:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_201]
    mov edx, 97
    lea rcx, [rip + .L__s3_failure_suffix_201]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_202:
    lea rsi, [rip + .L__s3_failure_prefix_202]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_203:
    lea rsi, [rip + .L__s3_failure_prefix_203]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_204:
    lea rsi, [rip + .L__s3_failure_prefix_204]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_205:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_205]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_205]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_206:
    lea rsi, [rip + .L__s3_failure_prefix_206]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_207:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_207]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_207]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_208:
    lea rsi, [rip + .L__s3_failure_prefix_208]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_209:
    lea rsi, [rip + .L__s3_failure_prefix_209]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_210:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_210]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_210]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_211:
    lea rsi, [rip + .L__s3_failure_prefix_211]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_212:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_212]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_212]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_213:
    lea rsi, [rip + .L__s3_failure_prefix_213]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_214:
    lea rsi, [rip + .L__s3_failure_prefix_214]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_215:
    lea rsi, [rip + .L__s3_failure_prefix_215]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_216:
    lea rsi, [rip + .L__s3_failure_prefix_216]
    mov edx, 152
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
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_220:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_220]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_220]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_221:
    lea rsi, [rip + .L__s3_failure_prefix_221]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_222:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_222]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_222]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_223:
    lea rsi, [rip + .L__s3_failure_prefix_223]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_224:
    lea rsi, [rip + .L__s3_failure_prefix_224]
    mov edx, 121
    jmp __s3_fail_message
.L__s3_failure_site_225:
    lea rsi, [rip + .L__s3_failure_prefix_225]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_226:
    lea rsi, [rip + .L__s3_failure_prefix_226]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_227:
    lea rsi, [rip + .L__s3_failure_prefix_227]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_228:
    lea rsi, [rip + .L__s3_failure_prefix_228]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_229:
    lea rsi, [rip + .L__s3_failure_prefix_229]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_230:
    lea rsi, [rip + .L__s3_failure_prefix_230]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_231:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_231]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_231]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_232:
    lea rsi, [rip + .L__s3_failure_prefix_232]
    mov edx, 149
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
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_235]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_236:
    lea rsi, [rip + .L__s3_failure_prefix_236]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_237:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_237]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_237]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_238:
    lea rsi, [rip + .L__s3_failure_prefix_238]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_239:
    lea rsi, [rip + .L__s3_failure_prefix_239]
    mov edx, 121
    jmp __s3_fail_message
.L__s3_failure_site_240:
    lea rsi, [rip + .L__s3_failure_prefix_240]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_241:
    lea rsi, [rip + .L__s3_failure_prefix_241]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_242:
    lea rsi, [rip + .L__s3_failure_prefix_242]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_243:
    lea rsi, [rip + .L__s3_failure_prefix_243]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_244:
    lea rsi, [rip + .L__s3_failure_prefix_244]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_245:
    lea rsi, [rip + .L__s3_failure_prefix_245]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_246:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_246]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_246]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_247:
    lea rsi, [rip + .L__s3_failure_prefix_247]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_248:
    lea rsi, [rip + .L__s3_failure_prefix_248]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_249:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_249]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_249]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_250:
    lea rsi, [rip + .L__s3_failure_prefix_250]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_251:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_251]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_251]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_252:
    lea rsi, [rip + .L__s3_failure_prefix_252]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_253:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_253]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_253]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_254:
    lea rsi, [rip + .L__s3_failure_prefix_254]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_255:
    lea rsi, [rip + .L__s3_failure_prefix_255]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_256:
    lea rsi, [rip + .L__s3_failure_prefix_256]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_257:
    lea rsi, [rip + .L__s3_failure_prefix_257]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_258:
    lea rsi, [rip + .L__s3_failure_prefix_258]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_259:
    lea rsi, [rip + .L__s3_failure_prefix_259]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_260:
    lea rsi, [rip + .L__s3_failure_prefix_260]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_261:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_261]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_261]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_262:
    lea rsi, [rip + .L__s3_failure_prefix_262]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_263:
    lea rsi, [rip + .L__s3_failure_prefix_263]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_264:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_264]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_264]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_265:
    lea rsi, [rip + .L__s3_failure_prefix_265]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_266:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_266]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_266]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_267:
    lea rsi, [rip + .L__s3_failure_prefix_267]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_268:
    lea rsi, [rip + .L__s3_failure_prefix_268]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_269:
    lea rsi, [rip + .L__s3_failure_prefix_269]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_270:
    lea rsi, [rip + .L__s3_failure_prefix_270]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_271:
    lea rsi, [rip + .L__s3_failure_prefix_271]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_272:
    lea rsi, [rip + .L__s3_failure_prefix_272]
    mov edx, 143
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
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_276:
    lea rsi, [rip + .L__s3_failure_prefix_276]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_277:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_277]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_277]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_278:
    lea rsi, [rip + .L__s3_failure_prefix_278]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_279:
    lea rsi, [rip + .L__s3_failure_prefix_279]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_280:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_280]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_280]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_281:
    lea rsi, [rip + .L__s3_failure_prefix_281]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_282:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_282]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_282]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_283:
    lea rsi, [rip + .L__s3_failure_prefix_283]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_284:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_284]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_284]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_285:
    lea rsi, [rip + .L__s3_failure_prefix_285]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_286:
    lea rsi, [rip + .L__s3_failure_prefix_286]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_287:
    lea rsi, [rip + .L__s3_failure_prefix_287]
    mov edx, 145
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
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_291:
    lea rsi, [rip + .L__s3_failure_prefix_291]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_292:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_292]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_292]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_293:
    lea rsi, [rip + .L__s3_failure_prefix_293]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_294:
    lea rsi, [rip + .L__s3_failure_prefix_294]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_295:
    lea rsi, [rip + .L__s3_failure_prefix_295]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_296:
    lea rsi, [rip + .L__s3_failure_prefix_296]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_297:
    lea rsi, [rip + .L__s3_failure_prefix_297]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_298:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_298]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_298]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_299:
    lea rsi, [rip + .L__s3_failure_prefix_299]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_300:
    lea rsi, [rip + .L__s3_failure_prefix_300]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_301:
    lea rsi, [rip + .L__s3_failure_prefix_301]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_302:
    lea rsi, [rip + .L__s3_failure_prefix_302]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_303:
    lea rsi, [rip + .L__s3_failure_prefix_303]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_304:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_304]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_304]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_305:
    lea rsi, [rip + .L__s3_failure_prefix_305]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_306:
    lea rsi, [rip + .L__s3_failure_prefix_306]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_307:
    lea rsi, [rip + .L__s3_failure_prefix_307]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_308:
    lea rsi, [rip + .L__s3_failure_prefix_308]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_309:
    lea rsi, [rip + .L__s3_failure_prefix_309]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_310:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_310]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_310]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_311:
    lea rsi, [rip + .L__s3_failure_prefix_311]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_312:
    lea rsi, [rip + .L__s3_failure_prefix_312]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_313:
    lea rsi, [rip + .L__s3_failure_prefix_313]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_314:
    lea rsi, [rip + .L__s3_failure_prefix_314]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_315:
    lea rsi, [rip + .L__s3_failure_prefix_315]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_316:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_316]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_316]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_317:
    lea rsi, [rip + .L__s3_failure_prefix_317]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_318:
    lea rsi, [rip + .L__s3_failure_prefix_318]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_319:
    lea rsi, [rip + .L__s3_failure_prefix_319]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_320:
    lea rsi, [rip + .L__s3_failure_prefix_320]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_321:
    lea rsi, [rip + .L__s3_failure_prefix_321]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_322:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_322]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_322]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_323:
    lea rsi, [rip + .L__s3_failure_prefix_323]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_324:
    lea rsi, [rip + .L__s3_failure_prefix_324]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_325:
    lea rsi, [rip + .L__s3_failure_prefix_325]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_326:
    lea rsi, [rip + .L__s3_failure_prefix_326]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_327:
    lea rsi, [rip + .L__s3_failure_prefix_327]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_328:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_328]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_328]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_329:
    lea rsi, [rip + .L__s3_failure_prefix_329]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_330:
    lea rsi, [rip + .L__s3_failure_prefix_330]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_331:
    lea rsi, [rip + .L__s3_failure_prefix_331]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_332:
    lea rsi, [rip + .L__s3_failure_prefix_332]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_333:
    lea rsi, [rip + .L__s3_failure_prefix_333]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_334:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_334]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_334]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_335:
    lea rsi, [rip + .L__s3_failure_prefix_335]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_336:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_336]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_336]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_337:
    lea rsi, [rip + .L__s3_failure_prefix_337]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_338:
    lea rsi, [rip + .L__s3_failure_prefix_338]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_339:
    lea rsi, [rip + .L__s3_failure_prefix_339]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_340:
    lea rsi, [rip + .L__s3_failure_prefix_340]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_341:
    lea rsi, [rip + .L__s3_failure_prefix_341]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_342:
    lea rsi, [rip + .L__s3_failure_prefix_342]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_343:
    lea rsi, [rip + .L__s3_failure_prefix_343]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_344:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_344]
    mov edx, 102
    lea rcx, [rip + .L__s3_failure_suffix_344]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_345:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_345]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_345]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_346:
    lea rsi, [rip + .L__s3_failure_prefix_346]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_347:
    lea rsi, [rip + .L__s3_failure_prefix_347]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_348:
    lea rsi, [rip + .L__s3_failure_prefix_348]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_349:
    lea rsi, [rip + .L__s3_failure_prefix_349]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_350:
    lea rsi, [rip + .L__s3_failure_prefix_350]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_351:
    lea rsi, [rip + .L__s3_failure_prefix_351]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_352:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_352]
    mov edx, 103
    lea rcx, [rip + .L__s3_failure_suffix_352]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_353:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_353]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_353]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_354:
    lea rsi, [rip + .L__s3_failure_prefix_354]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_355:
    lea rsi, [rip + .L__s3_failure_prefix_355]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_356:
    lea rsi, [rip + .L__s3_failure_prefix_356]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_357:
    lea rsi, [rip + .L__s3_failure_prefix_357]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_358:
    lea rsi, [rip + .L__s3_failure_prefix_358]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_359:
    lea rsi, [rip + .L__s3_failure_prefix_359]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_360:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_360]
    mov edx, 102
    lea rcx, [rip + .L__s3_failure_suffix_360]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_361:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_361]
    mov edx, 110
    lea rcx, [rip + .L__s3_failure_suffix_361]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_362:
    lea rsi, [rip + .L__s3_failure_prefix_362]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_363:
    lea rsi, [rip + .L__s3_failure_prefix_363]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_364:
    lea rsi, [rip + .L__s3_failure_prefix_364]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_365:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_365]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_365]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_366:
    lea rsi, [rip + .L__s3_failure_prefix_366]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_367:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_367]
    mov edx, 102
    lea rcx, [rip + .L__s3_failure_suffix_367]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_368:
    lea rsi, [rip + .L__s3_failure_prefix_368]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_369:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_369]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_369]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_370:
    lea rsi, [rip + .L__s3_failure_prefix_370]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_371:
    lea rsi, [rip + .L__s3_failure_prefix_371]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_372:
    lea rsi, [rip + .L__s3_failure_prefix_372]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_373:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_373]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_373]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_374:
    lea rsi, [rip + .L__s3_failure_prefix_374]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_375:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_375]
    mov edx, 109
    lea rcx, [rip + .L__s3_failure_suffix_375]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_376:
    lea rsi, [rip + .L__s3_failure_prefix_376]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_377:
    lea rsi, [rip + .L__s3_failure_prefix_377]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_378:
    lea rsi, [rip + .L__s3_failure_prefix_378]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_379:
    lea rsi, [rip + .L__s3_failure_prefix_379]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_380:
    lea rsi, [rip + .L__s3_failure_prefix_380]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_381:
    lea rsi, [rip + .L__s3_failure_prefix_381]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_382:
    lea rsi, [rip + .L__s3_failure_prefix_382]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_383:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_383]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_383]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_384:
    lea rsi, [rip + .L__s3_failure_prefix_384]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_385:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_385]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_385]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_386:
    lea rsi, [rip + .L__s3_failure_prefix_386]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_387:
    lea rsi, [rip + .L__s3_failure_prefix_387]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_388:
    lea rsi, [rip + .L__s3_failure_prefix_388]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_389:
    lea rsi, [rip + .L__s3_failure_prefix_389]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_390:
    lea rsi, [rip + .L__s3_failure_prefix_390]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_391:
    lea rsi, [rip + .L__s3_failure_prefix_391]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_392:
    lea rsi, [rip + .L__s3_failure_prefix_392]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_393:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_393]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_393]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_394:
    lea rsi, [rip + .L__s3_failure_prefix_394]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_395:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_395]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_395]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_396:
    lea rsi, [rip + .L__s3_failure_prefix_396]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_397:
    lea rsi, [rip + .L__s3_failure_prefix_397]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_398:
    lea rsi, [rip + .L__s3_failure_prefix_398]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_399:
    lea rsi, [rip + .L__s3_failure_prefix_399]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_400:
    lea rsi, [rip + .L__s3_failure_prefix_400]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_401:
    lea rsi, [rip + .L__s3_failure_prefix_401]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_402:
    lea rsi, [rip + .L__s3_failure_prefix_402]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_403:
    lea rsi, [rip + .L__s3_failure_prefix_403]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_404:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_404]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_404]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_405:
    lea rsi, [rip + .L__s3_failure_prefix_405]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_406:
    lea rsi, [rip + .L__s3_failure_prefix_406]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_407:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_407]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_407]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_408:
    lea rsi, [rip + .L__s3_failure_prefix_408]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_409:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_409]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_409]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_410:
    lea rsi, [rip + .L__s3_failure_prefix_410]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_411:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_411]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_411]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_412:
    lea rsi, [rip + .L__s3_failure_prefix_412]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_413:
    lea rsi, [rip + .L__s3_failure_prefix_413]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_414:
    lea rsi, [rip + .L__s3_failure_prefix_414]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_415:
    lea rsi, [rip + .L__s3_failure_prefix_415]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_416:
    lea rsi, [rip + .L__s3_failure_prefix_416]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_417:
    lea rsi, [rip + .L__s3_failure_prefix_417]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_418:
    lea rsi, [rip + .L__s3_failure_prefix_418]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_419:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_419]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_419]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_420:
    lea rsi, [rip + .L__s3_failure_prefix_420]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_421:
    lea rsi, [rip + .L__s3_failure_prefix_421]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_422:
    lea rsi, [rip + .L__s3_failure_prefix_422]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_423:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_423]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_423]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_424:
    lea rsi, [rip + .L__s3_failure_prefix_424]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_425:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_425]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_425]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_426:
    lea rsi, [rip + .L__s3_failure_prefix_426]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_427:
    lea rsi, [rip + .L__s3_failure_prefix_427]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_428:
    lea rsi, [rip + .L__s3_failure_prefix_428]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_429:
    lea rsi, [rip + .L__s3_failure_prefix_429]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_430:
    lea rsi, [rip + .L__s3_failure_prefix_430]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_431:
    lea rsi, [rip + .L__s3_failure_prefix_431]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_432:
    lea rsi, [rip + .L__s3_failure_prefix_432]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_433:
    lea rsi, [rip + .L__s3_failure_prefix_433]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_434:
    lea rsi, [rip + .L__s3_failure_prefix_434]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_435:
    lea rsi, [rip + .L__s3_failure_prefix_435]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_436:
    lea rsi, [rip + .L__s3_failure_prefix_436]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_437:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_437]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_437]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_438:
    lea rsi, [rip + .L__s3_failure_prefix_438]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_439:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_439]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_439]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_440:
    lea rsi, [rip + .L__s3_failure_prefix_440]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_441:
    lea rsi, [rip + .L__s3_failure_prefix_441]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_442:
    lea rsi, [rip + .L__s3_failure_prefix_442]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_443:
    lea rsi, [rip + .L__s3_failure_prefix_443]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_444:
    lea rsi, [rip + .L__s3_failure_prefix_444]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_445:
    lea rsi, [rip + .L__s3_failure_prefix_445]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_446:
    lea rsi, [rip + .L__s3_failure_prefix_446]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_447:
    lea rsi, [rip + .L__s3_failure_prefix_447]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_448:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_448]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_448]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_449:
    lea rsi, [rip + .L__s3_failure_prefix_449]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_450:
    lea rsi, [rip + .L__s3_failure_prefix_450]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_451:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_451]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_451]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_452:
    lea rsi, [rip + .L__s3_failure_prefix_452]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_453:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_453]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_453]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_454:
    lea rsi, [rip + .L__s3_failure_prefix_454]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_455:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_455]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_455]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_456:
    lea rsi, [rip + .L__s3_failure_prefix_456]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_457:
    lea rsi, [rip + .L__s3_failure_prefix_457]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_458:
    lea rsi, [rip + .L__s3_failure_prefix_458]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_459:
    lea rsi, [rip + .L__s3_failure_prefix_459]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_460:
    lea rsi, [rip + .L__s3_failure_prefix_460]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_461:
    lea rsi, [rip + .L__s3_failure_prefix_461]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_462:
    lea rsi, [rip + .L__s3_failure_prefix_462]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_463:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_463]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_463]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_464:
    lea rsi, [rip + .L__s3_failure_prefix_464]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_465:
    lea rsi, [rip + .L__s3_failure_prefix_465]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_466:
    lea rsi, [rip + .L__s3_failure_prefix_466]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_467:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_467]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_467]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_468:
    lea rsi, [rip + .L__s3_failure_prefix_468]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_469:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_469]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_469]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_470:
    lea rsi, [rip + .L__s3_failure_prefix_470]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_471:
    lea rsi, [rip + .L__s3_failure_prefix_471]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_472:
    lea rsi, [rip + .L__s3_failure_prefix_472]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_473:
    lea rsi, [rip + .L__s3_failure_prefix_473]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_474:
    lea rsi, [rip + .L__s3_failure_prefix_474]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_475:
    lea rsi, [rip + .L__s3_failure_prefix_475]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_476:
    lea rsi, [rip + .L__s3_failure_prefix_476]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_477:
    lea rsi, [rip + .L__s3_failure_prefix_477]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_478:
    lea rsi, [rip + .L__s3_failure_prefix_478]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_479:
    lea rsi, [rip + .L__s3_failure_prefix_479]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_480:
    lea rsi, [rip + .L__s3_failure_prefix_480]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_481:
    lea rsi, [rip + .L__s3_failure_prefix_481]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_482:
    lea rsi, [rip + .L__s3_failure_prefix_482]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_483:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_483]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_483]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_484:
    lea rsi, [rip + .L__s3_failure_prefix_484]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_485:
    lea rsi, [rip + .L__s3_failure_prefix_485]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_486:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_486]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_486]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_487:
    lea rsi, [rip + .L__s3_failure_prefix_487]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_488:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_488]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_488]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_489:
    lea rsi, [rip + .L__s3_failure_prefix_489]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_490:
    lea rsi, [rip + .L__s3_failure_prefix_490]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_491:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_491]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_491]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_492:
    lea rsi, [rip + .L__s3_failure_prefix_492]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_493:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_493]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_493]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_494:
    lea rsi, [rip + .L__s3_failure_prefix_494]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_495:
    lea rsi, [rip + .L__s3_failure_prefix_495]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_496:
    lea rsi, [rip + .L__s3_failure_prefix_496]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_497:
    lea rsi, [rip + .L__s3_failure_prefix_497]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_498:
    lea rsi, [rip + .L__s3_failure_prefix_498]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_499:
    lea rsi, [rip + .L__s3_failure_prefix_499]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_500:
    lea rsi, [rip + .L__s3_failure_prefix_500]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_501:
    lea rsi, [rip + .L__s3_failure_prefix_501]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_502:
    lea rsi, [rip + .L__s3_failure_prefix_502]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_503:
    lea rsi, [rip + .L__s3_failure_prefix_503]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_504:
    lea rsi, [rip + .L__s3_failure_prefix_504]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_505:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_505]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_505]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_506:
    lea rsi, [rip + .L__s3_failure_prefix_506]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_507:
    lea rsi, [rip + .L__s3_failure_prefix_507]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_508:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_508]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_508]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_509:
    lea rsi, [rip + .L__s3_failure_prefix_509]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_510:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_510]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_510]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_511:
    lea rsi, [rip + .L__s3_failure_prefix_511]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_512:
    lea rsi, [rip + .L__s3_failure_prefix_512]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_513:
    lea rsi, [rip + .L__s3_failure_prefix_513]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_514:
    lea rsi, [rip + .L__s3_failure_prefix_514]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_515:
    lea rsi, [rip + .L__s3_failure_prefix_515]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_516:
    lea rsi, [rip + .L__s3_failure_prefix_516]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_517:
    lea rsi, [rip + .L__s3_failure_prefix_517]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_518:
    lea rsi, [rip + .L__s3_failure_prefix_518]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_519:
    lea rsi, [rip + .L__s3_failure_prefix_519]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_520:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_520]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_520]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_521:
    lea rsi, [rip + .L__s3_failure_prefix_521]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_522:
    lea rsi, [rip + .L__s3_failure_prefix_522]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_523:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_523]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_523]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_524:
    lea rsi, [rip + .L__s3_failure_prefix_524]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_525:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_525]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_525]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_526:
    lea rsi, [rip + .L__s3_failure_prefix_526]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_527:
    lea rsi, [rip + .L__s3_failure_prefix_527]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_528:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_528]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_528]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_529:
    lea rsi, [rip + .L__s3_failure_prefix_529]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_530:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_530]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_530]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_531:
    lea rsi, [rip + .L__s3_failure_prefix_531]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_532:
    lea rsi, [rip + .L__s3_failure_prefix_532]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_533:
    lea rsi, [rip + .L__s3_failure_prefix_533]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_534:
    lea rsi, [rip + .L__s3_failure_prefix_534]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_535:
    lea rsi, [rip + .L__s3_failure_prefix_535]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_536:
    lea rsi, [rip + .L__s3_failure_prefix_536]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_537:
    lea rsi, [rip + .L__s3_failure_prefix_537]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_538:
    lea rsi, [rip + .L__s3_failure_prefix_538]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_539:
    lea rsi, [rip + .L__s3_failure_prefix_539]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_540:
    lea rsi, [rip + .L__s3_failure_prefix_540]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_541:
    lea rsi, [rip + .L__s3_failure_prefix_541]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_542:
    lea rsi, [rip + .L__s3_failure_prefix_542]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_543:
    lea rsi, [rip + .L__s3_failure_prefix_543]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_544:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_544]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_544]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_545:
    lea rsi, [rip + .L__s3_failure_prefix_545]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_546:
    lea rsi, [rip + .L__s3_failure_prefix_546]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_547:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_547]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_547]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_548:
    lea rsi, [rip + .L__s3_failure_prefix_548]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_549:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_549]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_549]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_550:
    lea rsi, [rip + .L__s3_failure_prefix_550]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_551:
    lea rsi, [rip + .L__s3_failure_prefix_551]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_552:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_552]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_552]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_553:
    lea rsi, [rip + .L__s3_failure_prefix_553]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_554:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_554]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_554]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_555:
    lea rsi, [rip + .L__s3_failure_prefix_555]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_556:
    lea rsi, [rip + .L__s3_failure_prefix_556]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_557:
    lea rsi, [rip + .L__s3_failure_prefix_557]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_558:
    lea rsi, [rip + .L__s3_failure_prefix_558]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_559:
    lea rsi, [rip + .L__s3_failure_prefix_559]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_560:
    lea rsi, [rip + .L__s3_failure_prefix_560]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_561:
    lea rsi, [rip + .L__s3_failure_prefix_561]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_562:
    lea rsi, [rip + .L__s3_failure_prefix_562]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_563:
    lea rsi, [rip + .L__s3_failure_prefix_563]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_564:
    lea rsi, [rip + .L__s3_failure_prefix_564]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_565:
    lea rsi, [rip + .L__s3_failure_prefix_565]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_566:
    lea rsi, [rip + .L__s3_failure_prefix_566]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_567:
    lea rsi, [rip + .L__s3_failure_prefix_567]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_568:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_568]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_568]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_569:
    lea rsi, [rip + .L__s3_failure_prefix_569]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_570:
    lea rsi, [rip + .L__s3_failure_prefix_570]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_571:
    lea rsi, [rip + .L__s3_failure_prefix_571]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_572:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_572]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_572]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_573:
    lea rsi, [rip + .L__s3_failure_prefix_573]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_574:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_574]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_574]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_575:
    lea rsi, [rip + .L__s3_failure_prefix_575]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_576:
    lea rsi, [rip + .L__s3_failure_prefix_576]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_577:
    lea rsi, [rip + .L__s3_failure_prefix_577]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_578:
    lea rsi, [rip + .L__s3_failure_prefix_578]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_579:
    lea rsi, [rip + .L__s3_failure_prefix_579]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_580:
    lea rsi, [rip + .L__s3_failure_prefix_580]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_581:
    lea rsi, [rip + .L__s3_failure_prefix_581]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_582:
    lea rsi, [rip + .L__s3_failure_prefix_582]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_583:
    lea rsi, [rip + .L__s3_failure_prefix_583]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_584:
    lea rsi, [rip + .L__s3_failure_prefix_584]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_585:
    lea rsi, [rip + .L__s3_failure_prefix_585]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_586:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_586]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_586]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_587:
    lea rsi, [rip + .L__s3_failure_prefix_587]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_588:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_588]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_588]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_589:
    lea rsi, [rip + .L__s3_failure_prefix_589]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_590:
    lea rsi, [rip + .L__s3_failure_prefix_590]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_591:
    lea rsi, [rip + .L__s3_failure_prefix_591]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_592:
    lea rsi, [rip + .L__s3_failure_prefix_592]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_593:
    lea rsi, [rip + .L__s3_failure_prefix_593]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_594:
    lea rsi, [rip + .L__s3_failure_prefix_594]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_595:
    lea rsi, [rip + .L__s3_failure_prefix_595]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_596:
    lea rsi, [rip + .L__s3_failure_prefix_596]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_597:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_597]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_597]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_598:
    lea rsi, [rip + .L__s3_failure_prefix_598]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_599:
    lea rsi, [rip + .L__s3_failure_prefix_599]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_600:
    lea rsi, [rip + .L__s3_failure_prefix_600]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_601:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_601]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_601]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_602:
    lea rsi, [rip + .L__s3_failure_prefix_602]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_603:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_603]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_603]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_604:
    lea rsi, [rip + .L__s3_failure_prefix_604]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_605:
    lea rsi, [rip + .L__s3_failure_prefix_605]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_606:
    lea rsi, [rip + .L__s3_failure_prefix_606]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_607:
    lea rsi, [rip + .L__s3_failure_prefix_607]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_608:
    lea rsi, [rip + .L__s3_failure_prefix_608]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_609:
    lea rsi, [rip + .L__s3_failure_prefix_609]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_610:
    lea rsi, [rip + .L__s3_failure_prefix_610]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_611:
    lea rsi, [rip + .L__s3_failure_prefix_611]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_612:
    lea rsi, [rip + .L__s3_failure_prefix_612]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_613:
    lea rsi, [rip + .L__s3_failure_prefix_613]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_614:
    lea rsi, [rip + .L__s3_failure_prefix_614]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_615:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_615]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_615]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_616:
    lea rsi, [rip + .L__s3_failure_prefix_616]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_617:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_617]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_617]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_618:
    lea rsi, [rip + .L__s3_failure_prefix_618]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_619:
    lea rsi, [rip + .L__s3_failure_prefix_619]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_620:
    lea rsi, [rip + .L__s3_failure_prefix_620]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_621:
    lea rsi, [rip + .L__s3_failure_prefix_621]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_622:
    lea rsi, [rip + .L__s3_failure_prefix_622]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_623:
    lea rsi, [rip + .L__s3_failure_prefix_623]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_624:
    lea rsi, [rip + .L__s3_failure_prefix_624]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_625:
    lea rsi, [rip + .L__s3_failure_prefix_625]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_626:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_626]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_626]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_627:
    lea rsi, [rip + .L__s3_failure_prefix_627]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_628:
    lea rsi, [rip + .L__s3_failure_prefix_628]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_629:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_629]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_629]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_630:
    lea rsi, [rip + .L__s3_failure_prefix_630]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_631:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_631]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_631]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_632:
    lea rsi, [rip + .L__s3_failure_prefix_632]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_633:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_633]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_633]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_634:
    lea rsi, [rip + .L__s3_failure_prefix_634]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_635:
    lea rsi, [rip + .L__s3_failure_prefix_635]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_636:
    lea rsi, [rip + .L__s3_failure_prefix_636]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_637:
    lea rsi, [rip + .L__s3_failure_prefix_637]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_638:
    lea rsi, [rip + .L__s3_failure_prefix_638]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_639:
    lea rsi, [rip + .L__s3_failure_prefix_639]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_640:
    lea rsi, [rip + .L__s3_failure_prefix_640]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_641:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_641]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_641]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_642:
    lea rsi, [rip + .L__s3_failure_prefix_642]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_643:
    lea rsi, [rip + .L__s3_failure_prefix_643]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_644:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_644]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_644]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_645:
    lea rsi, [rip + .L__s3_failure_prefix_645]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_646:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_646]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_646]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_647:
    lea rsi, [rip + .L__s3_failure_prefix_647]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_648:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_648]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_648]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_649:
    lea rsi, [rip + .L__s3_failure_prefix_649]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_650:
    lea rsi, [rip + .L__s3_failure_prefix_650]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_651:
    lea rsi, [rip + .L__s3_failure_prefix_651]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_652:
    lea rsi, [rip + .L__s3_failure_prefix_652]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_653:
    lea rsi, [rip + .L__s3_failure_prefix_653]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_654:
    lea rsi, [rip + .L__s3_failure_prefix_654]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_655:
    lea rsi, [rip + .L__s3_failure_prefix_655]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_656:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_656]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_656]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_657:
    lea rsi, [rip + .L__s3_failure_prefix_657]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_658:
    lea rsi, [rip + .L__s3_failure_prefix_658]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_659:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_659]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_659]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_660:
    lea rsi, [rip + .L__s3_failure_prefix_660]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_661:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_661]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_661]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_662:
    lea rsi, [rip + .L__s3_failure_prefix_662]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_663:
    lea rsi, [rip + .L__s3_failure_prefix_663]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_664:
    lea rsi, [rip + .L__s3_failure_prefix_664]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_665:
    lea rsi, [rip + .L__s3_failure_prefix_665]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_666:
    lea rsi, [rip + .L__s3_failure_prefix_666]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_667:
    lea rsi, [rip + .L__s3_failure_prefix_667]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_668:
    lea rsi, [rip + .L__s3_failure_prefix_668]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_669:
    lea rsi, [rip + .L__s3_failure_prefix_669]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_670:
    lea rsi, [rip + .L__s3_failure_prefix_670]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_671:
    lea rsi, [rip + .L__s3_failure_prefix_671]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_672:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_672]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_672]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_673:
    lea rsi, [rip + .L__s3_failure_prefix_673]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_674:
    lea rsi, [rip + .L__s3_failure_prefix_674]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_675:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_675]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_675]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_676:
    lea rsi, [rip + .L__s3_failure_prefix_676]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_677:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_677]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_677]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_678:
    lea rsi, [rip + .L__s3_failure_prefix_678]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_679:
    lea rsi, [rip + .L__s3_failure_prefix_679]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_680:
    lea rsi, [rip + .L__s3_failure_prefix_680]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_681:
    lea rsi, [rip + .L__s3_failure_prefix_681]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_682:
    lea rsi, [rip + .L__s3_failure_prefix_682]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_683:
    lea rsi, [rip + .L__s3_failure_prefix_683]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_684:
    lea rsi, [rip + .L__s3_failure_prefix_684]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_685:
    lea rsi, [rip + .L__s3_failure_prefix_685]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_686:
    lea rsi, [rip + .L__s3_failure_prefix_686]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_687:
    lea rsi, [rip + .L__s3_failure_prefix_687]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_688:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_688]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_688]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_689:
    lea rsi, [rip + .L__s3_failure_prefix_689]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_690:
    lea rsi, [rip + .L__s3_failure_prefix_690]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_691:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_691]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_691]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_692:
    lea rsi, [rip + .L__s3_failure_prefix_692]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_693:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_693]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_693]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_694:
    lea rsi, [rip + .L__s3_failure_prefix_694]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_695:
    lea rsi, [rip + .L__s3_failure_prefix_695]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_696:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_696]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_696]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_697:
    lea rsi, [rip + .L__s3_failure_prefix_697]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_698:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_698]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_698]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_699:
    lea rsi, [rip + .L__s3_failure_prefix_699]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_700:
    lea rsi, [rip + .L__s3_failure_prefix_700]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_701:
    lea rsi, [rip + .L__s3_failure_prefix_701]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_702:
    lea rsi, [rip + .L__s3_failure_prefix_702]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_703:
    lea rsi, [rip + .L__s3_failure_prefix_703]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_704:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_704]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_704]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_705:
    lea rsi, [rip + .L__s3_failure_prefix_705]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_706:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_706]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_706]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_707:
    lea rsi, [rip + .L__s3_failure_prefix_707]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_708:
    lea rsi, [rip + .L__s3_failure_prefix_708]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_709:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_709]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_709]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_710:
    lea rsi, [rip + .L__s3_failure_prefix_710]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_711:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_711]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_711]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_712:
    lea rsi, [rip + .L__s3_failure_prefix_712]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_713:
    lea rsi, [rip + .L__s3_failure_prefix_713]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_714:
    lea rsi, [rip + .L__s3_failure_prefix_714]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_715:
    lea rsi, [rip + .L__s3_failure_prefix_715]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_716:
    lea rsi, [rip + .L__s3_failure_prefix_716]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_717:
    lea rsi, [rip + .L__s3_failure_prefix_717]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_718:
    lea rsi, [rip + .L__s3_failure_prefix_718]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_719:
    lea rsi, [rip + .L__s3_failure_prefix_719]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_720:
    lea rsi, [rip + .L__s3_failure_prefix_720]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_721:
    lea rsi, [rip + .L__s3_failure_prefix_721]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_722:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_722]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_722]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_723:
    lea rsi, [rip + .L__s3_failure_prefix_723]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_724:
    lea rsi, [rip + .L__s3_failure_prefix_724]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_725:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_725]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_725]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_726:
    lea rsi, [rip + .L__s3_failure_prefix_726]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_727:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_727]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_727]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_728:
    lea rsi, [rip + .L__s3_failure_prefix_728]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_729:
    lea rsi, [rip + .L__s3_failure_prefix_729]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_730:
    lea rsi, [rip + .L__s3_failure_prefix_730]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_731:
    lea rsi, [rip + .L__s3_failure_prefix_731]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_732:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_732]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_732]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_733:
    lea rsi, [rip + .L__s3_failure_prefix_733]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_734:
    lea rsi, [rip + .L__s3_failure_prefix_734]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_735:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_735]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_735]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_736:
    lea rsi, [rip + .L__s3_failure_prefix_736]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_737:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_737]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_737]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_738:
    lea rsi, [rip + .L__s3_failure_prefix_738]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_739:
    lea rsi, [rip + .L__s3_failure_prefix_739]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_740:
    lea rsi, [rip + .L__s3_failure_prefix_740]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_741:
    lea rsi, [rip + .L__s3_failure_prefix_741]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_742:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_742]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_742]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_743:
    lea rsi, [rip + .L__s3_failure_prefix_743]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_744:
    lea rsi, [rip + .L__s3_failure_prefix_744]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_745:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_745]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_745]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_746:
    lea rsi, [rip + .L__s3_failure_prefix_746]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_747:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_747]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_747]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_748:
    lea rsi, [rip + .L__s3_failure_prefix_748]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_749:
    lea rsi, [rip + .L__s3_failure_prefix_749]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_750:
    lea rsi, [rip + .L__s3_failure_prefix_750]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_751:
    lea rsi, [rip + .L__s3_failure_prefix_751]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_752:
    lea rsi, [rip + .L__s3_failure_prefix_752]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_753:
    lea rsi, [rip + .L__s3_failure_prefix_753]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_754:
    lea rsi, [rip + .L__s3_failure_prefix_754]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_755:
    lea rsi, [rip + .L__s3_failure_prefix_755]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_756:
    lea rsi, [rip + .L__s3_failure_prefix_756]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_757:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_757]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_757]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_758:
    lea rsi, [rip + .L__s3_failure_prefix_758]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_759:
    lea rsi, [rip + .L__s3_failure_prefix_759]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_760:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_760]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_760]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_761:
    lea rsi, [rip + .L__s3_failure_prefix_761]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_762:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_762]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_762]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_763:
    lea rsi, [rip + .L__s3_failure_prefix_763]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_764:
    lea rsi, [rip + .L__s3_failure_prefix_764]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_765:
    lea rsi, [rip + .L__s3_failure_prefix_765]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_766:
    lea rsi, [rip + .L__s3_failure_prefix_766]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_767:
    lea rsi, [rip + .L__s3_failure_prefix_767]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_768:
    lea rsi, [rip + .L__s3_failure_prefix_768]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_769:
    lea rsi, [rip + .L__s3_failure_prefix_769]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_770:
    lea rsi, [rip + .L__s3_failure_prefix_770]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_771:
    lea rsi, [rip + .L__s3_failure_prefix_771]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_772:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_772]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_772]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_773:
    lea rsi, [rip + .L__s3_failure_prefix_773]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_774:
    lea rsi, [rip + .L__s3_failure_prefix_774]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_775:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_775]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_775]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_776:
    lea rsi, [rip + .L__s3_failure_prefix_776]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_777:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_777]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_777]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_778:
    lea rsi, [rip + .L__s3_failure_prefix_778]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_779:
    lea rsi, [rip + .L__s3_failure_prefix_779]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_780:
    lea rsi, [rip + .L__s3_failure_prefix_780]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_781:
    lea rsi, [rip + .L__s3_failure_prefix_781]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_782:
    lea rsi, [rip + .L__s3_failure_prefix_782]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_783:
    lea rsi, [rip + .L__s3_failure_prefix_783]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_784:
    lea rsi, [rip + .L__s3_failure_prefix_784]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_785:
    lea rsi, [rip + .L__s3_failure_prefix_785]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_786:
    lea rsi, [rip + .L__s3_failure_prefix_786]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_787:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_787]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_787]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_788:
    lea rsi, [rip + .L__s3_failure_prefix_788]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_789:
    lea rsi, [rip + .L__s3_failure_prefix_789]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_790:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_790]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_790]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_791:
    lea rsi, [rip + .L__s3_failure_prefix_791]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_792:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_792]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_792]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_793:
    lea rsi, [rip + .L__s3_failure_prefix_793]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_794:
    lea rsi, [rip + .L__s3_failure_prefix_794]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_795:
    lea rsi, [rip + .L__s3_failure_prefix_795]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_796:
    lea rsi, [rip + .L__s3_failure_prefix_796]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_797:
    lea rsi, [rip + .L__s3_failure_prefix_797]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_798:
    lea rsi, [rip + .L__s3_failure_prefix_798]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_799:
    lea rsi, [rip + .L__s3_failure_prefix_799]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_800:
    lea rsi, [rip + .L__s3_failure_prefix_800]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_801:
    lea rsi, [rip + .L__s3_failure_prefix_801]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_802:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_802]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_802]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_803:
    lea rsi, [rip + .L__s3_failure_prefix_803]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_804:
    lea rsi, [rip + .L__s3_failure_prefix_804]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_805:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_805]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_805]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_806:
    lea rsi, [rip + .L__s3_failure_prefix_806]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_807:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_807]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_807]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_808:
    lea rsi, [rip + .L__s3_failure_prefix_808]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_809:
    lea rsi, [rip + .L__s3_failure_prefix_809]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_810:
    lea rsi, [rip + .L__s3_failure_prefix_810]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_811:
    lea rsi, [rip + .L__s3_failure_prefix_811]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_812:
    lea rsi, [rip + .L__s3_failure_prefix_812]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_813:
    lea rsi, [rip + .L__s3_failure_prefix_813]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_814:
    lea rsi, [rip + .L__s3_failure_prefix_814]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_815:
    lea rsi, [rip + .L__s3_failure_prefix_815]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_816:
    lea rsi, [rip + .L__s3_failure_prefix_816]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_817:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_817]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_817]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_818:
    lea rsi, [rip + .L__s3_failure_prefix_818]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_819:
    lea rsi, [rip + .L__s3_failure_prefix_819]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_820:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_820]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_820]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_821:
    lea rsi, [rip + .L__s3_failure_prefix_821]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_822:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_822]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_822]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_823:
    lea rsi, [rip + .L__s3_failure_prefix_823]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_824:
    lea rsi, [rip + .L__s3_failure_prefix_824]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_825:
    lea rsi, [rip + .L__s3_failure_prefix_825]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_826:
    lea rsi, [rip + .L__s3_failure_prefix_826]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_827:
    lea rsi, [rip + .L__s3_failure_prefix_827]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_828:
    lea rsi, [rip + .L__s3_failure_prefix_828]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_829:
    lea rsi, [rip + .L__s3_failure_prefix_829]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_830:
    lea rsi, [rip + .L__s3_failure_prefix_830]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_831:
    lea rsi, [rip + .L__s3_failure_prefix_831]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_832:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_832]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_832]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_833:
    lea rsi, [rip + .L__s3_failure_prefix_833]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_834:
    lea rsi, [rip + .L__s3_failure_prefix_834]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_835:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_835]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_835]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_836:
    lea rsi, [rip + .L__s3_failure_prefix_836]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_837:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_837]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_837]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_838:
    lea rsi, [rip + .L__s3_failure_prefix_838]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_839:
    lea rsi, [rip + .L__s3_failure_prefix_839]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_840:
    lea rsi, [rip + .L__s3_failure_prefix_840]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_841:
    lea rsi, [rip + .L__s3_failure_prefix_841]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_842:
    lea rsi, [rip + .L__s3_failure_prefix_842]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_843:
    lea rsi, [rip + .L__s3_failure_prefix_843]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_844:
    lea rsi, [rip + .L__s3_failure_prefix_844]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_845:
    lea rsi, [rip + .L__s3_failure_prefix_845]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_846:
    lea rsi, [rip + .L__s3_failure_prefix_846]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_847:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_847]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_847]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_848:
    lea rsi, [rip + .L__s3_failure_prefix_848]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_849:
    lea rsi, [rip + .L__s3_failure_prefix_849]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_850:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_850]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_850]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_851:
    lea rsi, [rip + .L__s3_failure_prefix_851]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_852:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_852]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_852]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_853:
    lea rsi, [rip + .L__s3_failure_prefix_853]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_854:
    lea rsi, [rip + .L__s3_failure_prefix_854]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_855:
    lea rsi, [rip + .L__s3_failure_prefix_855]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_856:
    lea rsi, [rip + .L__s3_failure_prefix_856]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_857:
    lea rsi, [rip + .L__s3_failure_prefix_857]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_858:
    lea rsi, [rip + .L__s3_failure_prefix_858]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_859:
    lea rsi, [rip + .L__s3_failure_prefix_859]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_860:
    lea rsi, [rip + .L__s3_failure_prefix_860]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_861:
    lea rsi, [rip + .L__s3_failure_prefix_861]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_862:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_862]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_862]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_863:
    lea rsi, [rip + .L__s3_failure_prefix_863]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_864:
    lea rsi, [rip + .L__s3_failure_prefix_864]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_865:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_865]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_865]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_866:
    lea rsi, [rip + .L__s3_failure_prefix_866]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_867:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_867]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_867]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_868:
    lea rsi, [rip + .L__s3_failure_prefix_868]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_869:
    lea rsi, [rip + .L__s3_failure_prefix_869]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_870:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_870]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_870]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_871:
    lea rsi, [rip + .L__s3_failure_prefix_871]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_872:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_872]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_872]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_873:
    lea rsi, [rip + .L__s3_failure_prefix_873]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_874:
    lea rsi, [rip + .L__s3_failure_prefix_874]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_875:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_875]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_875]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_876:
    lea rsi, [rip + .L__s3_failure_prefix_876]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_877:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_877]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_877]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_878:
    lea rsi, [rip + .L__s3_failure_prefix_878]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_879:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_879]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_879]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_880:
    lea rsi, [rip + .L__s3_failure_prefix_880]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_881:
    lea rsi, [rip + .L__s3_failure_prefix_881]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_882:
    lea rsi, [rip + .L__s3_failure_prefix_882]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_883:
    lea rsi, [rip + .L__s3_failure_prefix_883]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_884:
    lea rsi, [rip + .L__s3_failure_prefix_884]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_885:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_885]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_885]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_886:
    lea rsi, [rip + .L__s3_failure_prefix_886]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_887:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_887]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_887]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_888:
    lea rsi, [rip + .L__s3_failure_prefix_888]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_889:
    lea rsi, [rip + .L__s3_failure_prefix_889]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_890:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_890]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_890]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_891:
    lea rsi, [rip + .L__s3_failure_prefix_891]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_892:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_892]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_892]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_893:
    lea rsi, [rip + .L__s3_failure_prefix_893]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_894:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_894]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_894]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_895:
    lea rsi, [rip + .L__s3_failure_prefix_895]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_896:
    lea rsi, [rip + .L__s3_failure_prefix_896]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_897:
    lea rsi, [rip + .L__s3_failure_prefix_897]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_898:
    lea rsi, [rip + .L__s3_failure_prefix_898]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_899:
    lea rsi, [rip + .L__s3_failure_prefix_899]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_900:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_900]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_900]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_901:
    lea rsi, [rip + .L__s3_failure_prefix_901]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_902:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_902]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_902]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_903:
    lea rsi, [rip + .L__s3_failure_prefix_903]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_904:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_904]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_904]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_905:
    lea rsi, [rip + .L__s3_failure_prefix_905]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_906:
    lea rsi, [rip + .L__s3_failure_prefix_906]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_907:
    lea rsi, [rip + .L__s3_failure_prefix_907]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_908:
    lea rsi, [rip + .L__s3_failure_prefix_908]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_909:
    lea rsi, [rip + .L__s3_failure_prefix_909]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_910:
    lea rsi, [rip + .L__s3_failure_prefix_910]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_911:
    lea rsi, [rip + .L__s3_failure_prefix_911]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_912:
    lea rsi, [rip + .L__s3_failure_prefix_912]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_913:
    lea rsi, [rip + .L__s3_failure_prefix_913]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_914:
    lea rsi, [rip + .L__s3_failure_prefix_914]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_915:
    lea rsi, [rip + .L__s3_failure_prefix_915]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_916:
    lea rsi, [rip + .L__s3_failure_prefix_916]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_917:
    lea rsi, [rip + .L__s3_failure_prefix_917]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_918:
    lea rsi, [rip + .L__s3_failure_prefix_918]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_919:
    lea rsi, [rip + .L__s3_failure_prefix_919]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_920:
    lea rsi, [rip + .L__s3_failure_prefix_920]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_921:
    lea rsi, [rip + .L__s3_failure_prefix_921]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_922:
    lea rsi, [rip + .L__s3_failure_prefix_922]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_923:
    lea rsi, [rip + .L__s3_failure_prefix_923]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_924:
    lea rsi, [rip + .L__s3_failure_prefix_924]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_925:
    lea rsi, [rip + .L__s3_failure_prefix_925]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_926:
    lea rsi, [rip + .L__s3_failure_prefix_926]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_927:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_927]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_927]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_928:
    lea rsi, [rip + .L__s3_failure_prefix_928]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_929:
    lea rsi, [rip + .L__s3_failure_prefix_929]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_930:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_930]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_930]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_931:
    lea rsi, [rip + .L__s3_failure_prefix_931]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_932:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_932]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_932]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_933:
    lea rsi, [rip + .L__s3_failure_prefix_933]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_934:
    lea rsi, [rip + .L__s3_failure_prefix_934]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_935:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_935]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_935]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_936:
    lea rsi, [rip + .L__s3_failure_prefix_936]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_937:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_937]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_937]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_938:
    lea rsi, [rip + .L__s3_failure_prefix_938]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_939:
    lea rsi, [rip + .L__s3_failure_prefix_939]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_940:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_940]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_940]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_941:
    lea rsi, [rip + .L__s3_failure_prefix_941]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_942:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_942]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_942]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_943:
    lea rsi, [rip + .L__s3_failure_prefix_943]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_944:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_944]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_944]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_945:
    lea rsi, [rip + .L__s3_failure_prefix_945]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_946:
    lea rsi, [rip + .L__s3_failure_prefix_946]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_947:
    lea rsi, [rip + .L__s3_failure_prefix_947]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_948:
    lea rsi, [rip + .L__s3_failure_prefix_948]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_949:
    lea rsi, [rip + .L__s3_failure_prefix_949]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_950:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_950]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_950]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_951:
    lea rsi, [rip + .L__s3_failure_prefix_951]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_952:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_952]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_952]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_953:
    lea rsi, [rip + .L__s3_failure_prefix_953]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_954:
    lea rsi, [rip + .L__s3_failure_prefix_954]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_955:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_955]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_955]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_956:
    lea rsi, [rip + .L__s3_failure_prefix_956]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_957:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_957]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_957]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_958:
    lea rsi, [rip + .L__s3_failure_prefix_958]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_959:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_959]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_959]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_960:
    lea rsi, [rip + .L__s3_failure_prefix_960]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_961:
    lea rsi, [rip + .L__s3_failure_prefix_961]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_962:
    lea rsi, [rip + .L__s3_failure_prefix_962]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_963:
    lea rsi, [rip + .L__s3_failure_prefix_963]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_964:
    lea rsi, [rip + .L__s3_failure_prefix_964]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_965:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_965]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_965]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_966:
    lea rsi, [rip + .L__s3_failure_prefix_966]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_967:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_967]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_967]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_968:
    lea rsi, [rip + .L__s3_failure_prefix_968]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_969:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_969]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_969]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_970:
    lea rsi, [rip + .L__s3_failure_prefix_970]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_971:
    lea rsi, [rip + .L__s3_failure_prefix_971]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_972:
    lea rsi, [rip + .L__s3_failure_prefix_972]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_973:
    lea rsi, [rip + .L__s3_failure_prefix_973]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_974:
    lea rsi, [rip + .L__s3_failure_prefix_974]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_975:
    lea rsi, [rip + .L__s3_failure_prefix_975]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_976:
    lea rsi, [rip + .L__s3_failure_prefix_976]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_977:
    lea rsi, [rip + .L__s3_failure_prefix_977]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_978:
    lea rsi, [rip + .L__s3_failure_prefix_978]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_979:
    lea rsi, [rip + .L__s3_failure_prefix_979]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_980:
    lea rsi, [rip + .L__s3_failure_prefix_980]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_981:
    lea rsi, [rip + .L__s3_failure_prefix_981]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_982:
    lea rsi, [rip + .L__s3_failure_prefix_982]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_983:
    lea rsi, [rip + .L__s3_failure_prefix_983]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_984:
    lea rsi, [rip + .L__s3_failure_prefix_984]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_985:
    lea rsi, [rip + .L__s3_failure_prefix_985]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_986:
    lea rsi, [rip + .L__s3_failure_prefix_986]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_987:
    lea rsi, [rip + .L__s3_failure_prefix_987]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_988:
    lea rsi, [rip + .L__s3_failure_prefix_988]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_989:
    lea rsi, [rip + .L__s3_failure_prefix_989]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_990:
    lea rsi, [rip + .L__s3_failure_prefix_990]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_991:
    lea rsi, [rip + .L__s3_failure_prefix_991]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_992:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_992]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_992]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_993:
    lea rsi, [rip + .L__s3_failure_prefix_993]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_994:
    lea rsi, [rip + .L__s3_failure_prefix_994]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_995:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_995]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_995]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_996:
    lea rsi, [rip + .L__s3_failure_prefix_996]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_997:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_997]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_997]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_998:
    lea rsi, [rip + .L__s3_failure_prefix_998]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_999:
    lea rsi, [rip + .L__s3_failure_prefix_999]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1000:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1000]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1000]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1001:
    lea rsi, [rip + .L__s3_failure_prefix_1001]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1002:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1002]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1002]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1003:
    lea rsi, [rip + .L__s3_failure_prefix_1003]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1004:
    lea rsi, [rip + .L__s3_failure_prefix_1004]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1005:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1005]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1005]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1006:
    lea rsi, [rip + .L__s3_failure_prefix_1006]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1007:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1007]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1007]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1008:
    lea rsi, [rip + .L__s3_failure_prefix_1008]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1009:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1009]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_1009]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1010:
    lea rsi, [rip + .L__s3_failure_prefix_1010]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1011:
    lea rsi, [rip + .L__s3_failure_prefix_1011]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1012:
    lea rsi, [rip + .L__s3_failure_prefix_1012]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1013:
    lea rsi, [rip + .L__s3_failure_prefix_1013]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1014:
    lea rsi, [rip + .L__s3_failure_prefix_1014]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1015:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1015]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1015]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1016:
    lea rsi, [rip + .L__s3_failure_prefix_1016]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1017:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1017]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1017]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1018:
    lea rsi, [rip + .L__s3_failure_prefix_1018]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1019:
    lea rsi, [rip + .L__s3_failure_prefix_1019]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1020:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1020]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_1020]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1021:
    lea rsi, [rip + .L__s3_failure_prefix_1021]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1022:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1022]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1022]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1023:
    lea rsi, [rip + .L__s3_failure_prefix_1023]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1024:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1024]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_1024]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1025:
    lea rsi, [rip + .L__s3_failure_prefix_1025]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1026:
    lea rsi, [rip + .L__s3_failure_prefix_1026]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1027:
    lea rsi, [rip + .L__s3_failure_prefix_1027]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1028:
    lea rsi, [rip + .L__s3_failure_prefix_1028]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1029:
    lea rsi, [rip + .L__s3_failure_prefix_1029]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1030:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1030]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_1030]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1031:
    lea rsi, [rip + .L__s3_failure_prefix_1031]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1032:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1032]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1032]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1033:
    lea rsi, [rip + .L__s3_failure_prefix_1033]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1034:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1034]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_1034]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1035:
    lea rsi, [rip + .L__s3_failure_prefix_1035]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1036:
    lea rsi, [rip + .L__s3_failure_prefix_1036]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1037:
    lea rsi, [rip + .L__s3_failure_prefix_1037]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1038:
    lea rsi, [rip + .L__s3_failure_prefix_1038]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1039:
    lea rsi, [rip + .L__s3_failure_prefix_1039]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1040:
    lea rsi, [rip + .L__s3_failure_prefix_1040]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1041:
    lea rsi, [rip + .L__s3_failure_prefix_1041]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1042:
    lea rsi, [rip + .L__s3_failure_prefix_1042]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1043:
    lea rsi, [rip + .L__s3_failure_prefix_1043]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1044:
    lea rsi, [rip + .L__s3_failure_prefix_1044]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1045:
    lea rsi, [rip + .L__s3_failure_prefix_1045]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1046:
    lea rsi, [rip + .L__s3_failure_prefix_1046]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1047:
    lea rsi, [rip + .L__s3_failure_prefix_1047]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1048:
    lea rsi, [rip + .L__s3_failure_prefix_1048]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1049:
    lea rsi, [rip + .L__s3_failure_prefix_1049]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1050:
    lea rsi, [rip + .L__s3_failure_prefix_1050]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1051:
    lea rsi, [rip + .L__s3_failure_prefix_1051]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1052:
    lea rsi, [rip + .L__s3_failure_prefix_1052]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1053:
    lea rsi, [rip + .L__s3_failure_prefix_1053]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1054:
    lea rsi, [rip + .L__s3_failure_prefix_1054]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1055:
    lea rsi, [rip + .L__s3_failure_prefix_1055]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1056:
    lea rsi, [rip + .L__s3_failure_prefix_1056]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1057:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1057]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1057]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1058:
    lea rsi, [rip + .L__s3_failure_prefix_1058]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1059:
    lea rsi, [rip + .L__s3_failure_prefix_1059]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1060:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1060]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1060]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1061:
    lea rsi, [rip + .L__s3_failure_prefix_1061]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1062:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1062]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1062]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1063:
    lea rsi, [rip + .L__s3_failure_prefix_1063]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1064:
    lea rsi, [rip + .L__s3_failure_prefix_1064]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1065:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1065]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1065]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1066:
    lea rsi, [rip + .L__s3_failure_prefix_1066]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1067:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1067]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1067]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1068:
    lea rsi, [rip + .L__s3_failure_prefix_1068]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1069:
    lea rsi, [rip + .L__s3_failure_prefix_1069]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1070:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1070]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1070]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1071:
    lea rsi, [rip + .L__s3_failure_prefix_1071]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1072:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1072]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1072]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1073:
    lea rsi, [rip + .L__s3_failure_prefix_1073]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1074:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1074]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_1074]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1075:
    lea rsi, [rip + .L__s3_failure_prefix_1075]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1076:
    lea rsi, [rip + .L__s3_failure_prefix_1076]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1077:
    lea rsi, [rip + .L__s3_failure_prefix_1077]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1078:
    lea rsi, [rip + .L__s3_failure_prefix_1078]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1079:
    lea rsi, [rip + .L__s3_failure_prefix_1079]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1080:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1080]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1080]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1081:
    lea rsi, [rip + .L__s3_failure_prefix_1081]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1082:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1082]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1082]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1083:
    lea rsi, [rip + .L__s3_failure_prefix_1083]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1084:
    lea rsi, [rip + .L__s3_failure_prefix_1084]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1085:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1085]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1085]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1086:
    lea rsi, [rip + .L__s3_failure_prefix_1086]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1087:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1087]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1087]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1088:
    lea rsi, [rip + .L__s3_failure_prefix_1088]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1089:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1089]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_1089]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1090:
    lea rsi, [rip + .L__s3_failure_prefix_1090]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1091:
    lea rsi, [rip + .L__s3_failure_prefix_1091]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1092:
    lea rsi, [rip + .L__s3_failure_prefix_1092]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1093:
    lea rsi, [rip + .L__s3_failure_prefix_1093]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1094:
    lea rsi, [rip + .L__s3_failure_prefix_1094]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1095:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1095]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_1095]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1096:
    lea rsi, [rip + .L__s3_failure_prefix_1096]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1097:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1097]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1097]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1098:
    lea rsi, [rip + .L__s3_failure_prefix_1098]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1099:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1099]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_1099]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1100:
    lea rsi, [rip + .L__s3_failure_prefix_1100]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1101:
    lea rsi, [rip + .L__s3_failure_prefix_1101]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1102:
    lea rsi, [rip + .L__s3_failure_prefix_1102]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1103:
    lea rsi, [rip + .L__s3_failure_prefix_1103]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1104:
    lea rsi, [rip + .L__s3_failure_prefix_1104]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1105:
    lea rsi, [rip + .L__s3_failure_prefix_1105]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1106:
    lea rsi, [rip + .L__s3_failure_prefix_1106]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1107:
    lea rsi, [rip + .L__s3_failure_prefix_1107]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1108:
    lea rsi, [rip + .L__s3_failure_prefix_1108]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1109:
    lea rsi, [rip + .L__s3_failure_prefix_1109]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1110:
    lea rsi, [rip + .L__s3_failure_prefix_1110]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1111:
    lea rsi, [rip + .L__s3_failure_prefix_1111]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1112:
    lea rsi, [rip + .L__s3_failure_prefix_1112]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1113:
    lea rsi, [rip + .L__s3_failure_prefix_1113]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1114:
    lea rsi, [rip + .L__s3_failure_prefix_1114]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1115:
    lea rsi, [rip + .L__s3_failure_prefix_1115]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1116:
    lea rsi, [rip + .L__s3_failure_prefix_1116]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1117:
    lea rsi, [rip + .L__s3_failure_prefix_1117]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1118:
    lea rsi, [rip + .L__s3_failure_prefix_1118]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1119:
    lea rsi, [rip + .L__s3_failure_prefix_1119]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1120:
    lea rsi, [rip + .L__s3_failure_prefix_1120]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1121:
    lea rsi, [rip + .L__s3_failure_prefix_1121]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1122:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1122]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1122]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1123:
    lea rsi, [rip + .L__s3_failure_prefix_1123]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1124:
    lea rsi, [rip + .L__s3_failure_prefix_1124]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1125:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1125]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1125]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1126:
    lea rsi, [rip + .L__s3_failure_prefix_1126]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1127:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1127]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1127]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1128:
    lea rsi, [rip + .L__s3_failure_prefix_1128]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1129:
    lea rsi, [rip + .L__s3_failure_prefix_1129]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1130:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1130]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1130]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1131:
    lea rsi, [rip + .L__s3_failure_prefix_1131]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1132:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1132]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1132]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1133:
    lea rsi, [rip + .L__s3_failure_prefix_1133]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1134:
    lea rsi, [rip + .L__s3_failure_prefix_1134]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1135:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1135]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1135]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1136:
    lea rsi, [rip + .L__s3_failure_prefix_1136]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1137:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1137]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1137]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1138:
    lea rsi, [rip + .L__s3_failure_prefix_1138]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1139:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1139]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_1139]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1140:
    lea rsi, [rip + .L__s3_failure_prefix_1140]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1141:
    lea rsi, [rip + .L__s3_failure_prefix_1141]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1142:
    lea rsi, [rip + .L__s3_failure_prefix_1142]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1143:
    lea rsi, [rip + .L__s3_failure_prefix_1143]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1144:
    lea rsi, [rip + .L__s3_failure_prefix_1144]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1145:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1145]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1145]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1146:
    lea rsi, [rip + .L__s3_failure_prefix_1146]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1147:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1147]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1147]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1148:
    lea rsi, [rip + .L__s3_failure_prefix_1148]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1149:
    lea rsi, [rip + .L__s3_failure_prefix_1149]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1150:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1150]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_1150]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1151:
    lea rsi, [rip + .L__s3_failure_prefix_1151]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1152:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1152]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1152]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1153:
    lea rsi, [rip + .L__s3_failure_prefix_1153]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1154:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1154]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_1154]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1155:
    lea rsi, [rip + .L__s3_failure_prefix_1155]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1156:
    lea rsi, [rip + .L__s3_failure_prefix_1156]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1157:
    lea rsi, [rip + .L__s3_failure_prefix_1157]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1158:
    lea rsi, [rip + .L__s3_failure_prefix_1158]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1159:
    lea rsi, [rip + .L__s3_failure_prefix_1159]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1160:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1160]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_1160]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1161:
    lea rsi, [rip + .L__s3_failure_prefix_1161]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1162:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1162]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1162]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1163:
    lea rsi, [rip + .L__s3_failure_prefix_1163]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1164:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1164]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_1164]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_1165:
    lea rsi, [rip + .L__s3_failure_prefix_1165]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1166:
    lea rsi, [rip + .L__s3_failure_prefix_1166]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1167:
    lea rsi, [rip + .L__s3_failure_prefix_1167]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1168:
    lea rsi, [rip + .L__s3_failure_prefix_1168]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1169:
    lea rsi, [rip + .L__s3_failure_prefix_1169]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1170:
    lea rsi, [rip + .L__s3_failure_prefix_1170]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1171:
    lea rsi, [rip + .L__s3_failure_prefix_1171]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1172:
    lea rsi, [rip + .L__s3_failure_prefix_1172]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1173:
    lea rsi, [rip + .L__s3_failure_prefix_1173]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1174:
    lea rsi, [rip + .L__s3_failure_prefix_1174]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1175:
    lea rsi, [rip + .L__s3_failure_prefix_1175]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1176:
    lea rsi, [rip + .L__s3_failure_prefix_1176]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1177:
    lea rsi, [rip + .L__s3_failure_prefix_1177]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1178:
    lea rsi, [rip + .L__s3_failure_prefix_1178]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1179:
    lea rsi, [rip + .L__s3_failure_prefix_1179]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1180:
    lea rsi, [rip + .L__s3_failure_prefix_1180]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1181:
    lea rsi, [rip + .L__s3_failure_prefix_1181]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1182:
    lea rsi, [rip + .L__s3_failure_prefix_1182]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1183:
    lea rsi, [rip + .L__s3_failure_prefix_1183]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1184:
    lea rsi, [rip + .L__s3_failure_prefix_1184]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1185:
    lea rsi, [rip + .L__s3_failure_prefix_1185]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1186:
    lea rsi, [rip + .L__s3_failure_prefix_1186]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1187:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1187]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1187]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1188:
    lea rsi, [rip + .L__s3_failure_prefix_1188]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1189:
    lea rsi, [rip + .L__s3_failure_prefix_1189]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1190:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1190]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1190]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_1191:
    lea rsi, [rip + .L__s3_failure_prefix_1191]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1192:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1192]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1192]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1193:
    lea rsi, [rip + .L__s3_failure_prefix_1193]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1194:
    lea rsi, [rip + .L__s3_failure_prefix_1194]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1195:
    lea rsi, [rip + .L__s3_failure_prefix_1195]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_1196:
    lea rsi, [rip + .L__s3_failure_prefix_1196]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1197:
    lea rsi, [rip + .L__s3_failure_prefix_1197]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1198:
    lea rsi, [rip + .L__s3_failure_prefix_1198]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1199:
    lea rsi, [rip + .L__s3_failure_prefix_1199]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1200:
    lea rsi, [rip + .L__s3_failure_prefix_1200]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1201:
    lea rsi, [rip + .L__s3_failure_prefix_1201]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1202:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1202]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1202]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1203:
    lea rsi, [rip + .L__s3_failure_prefix_1203]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1204:
    lea rsi, [rip + .L__s3_failure_prefix_1204]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1205:
    lea rsi, [rip + .L__s3_failure_prefix_1205]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1206:
    lea rsi, [rip + .L__s3_failure_prefix_1206]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1207:
    lea rsi, [rip + .L__s3_failure_prefix_1207]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1208:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1208]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1208]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_1209:
    lea rsi, [rip + .L__s3_failure_prefix_1209]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1210:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1210]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1210]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1211:
    lea rsi, [rip + .L__s3_failure_prefix_1211]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1212:
    lea rsi, [rip + .L__s3_failure_prefix_1212]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1213:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1213]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1213]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1214:
    lea rsi, [rip + .L__s3_failure_prefix_1214]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1215:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1215]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1215]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1216:
    lea rsi, [rip + .L__s3_failure_prefix_1216]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1217:
    lea rsi, [rip + .L__s3_failure_prefix_1217]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1218:
    lea rsi, [rip + .L__s3_failure_prefix_1218]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1219:
    lea rsi, [rip + .L__s3_failure_prefix_1219]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1220:
    lea rsi, [rip + .L__s3_failure_prefix_1220]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1221:
    lea rsi, [rip + .L__s3_failure_prefix_1221]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1222:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1222]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1222]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1223:
    lea rsi, [rip + .L__s3_failure_prefix_1223]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1224:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1224]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1224]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1225:
    lea rsi, [rip + .L__s3_failure_prefix_1225]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1226:
    lea rsi, [rip + .L__s3_failure_prefix_1226]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1227:
    lea rsi, [rip + .L__s3_failure_prefix_1227]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1228:
    lea rsi, [rip + .L__s3_failure_prefix_1228]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1229:
    lea rsi, [rip + .L__s3_failure_prefix_1229]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1230:
    lea rsi, [rip + .L__s3_failure_prefix_1230]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1231:
    lea rsi, [rip + .L__s3_failure_prefix_1231]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1232:
    lea rsi, [rip + .L__s3_failure_prefix_1232]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1233:
    lea rsi, [rip + .L__s3_failure_prefix_1233]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1234:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1234]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1234]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1235:
    lea rsi, [rip + .L__s3_failure_prefix_1235]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1236:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1236]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1236]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1237:
    lea rsi, [rip + .L__s3_failure_prefix_1237]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1238:
    lea rsi, [rip + .L__s3_failure_prefix_1238]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1239:
    lea rsi, [rip + .L__s3_failure_prefix_1239]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1240:
    lea rsi, [rip + .L__s3_failure_prefix_1240]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1241:
    lea rsi, [rip + .L__s3_failure_prefix_1241]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1242:
    lea rsi, [rip + .L__s3_failure_prefix_1242]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1243:
    lea rsi, [rip + .L__s3_failure_prefix_1243]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1244:
    lea rsi, [rip + .L__s3_failure_prefix_1244]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1245:
    lea rsi, [rip + .L__s3_failure_prefix_1245]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1246:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1246]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1246]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1247:
    lea rsi, [rip + .L__s3_failure_prefix_1247]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1248:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1248]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1248]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1249:
    lea rsi, [rip + .L__s3_failure_prefix_1249]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1250:
    lea rsi, [rip + .L__s3_failure_prefix_1250]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1251:
    lea rsi, [rip + .L__s3_failure_prefix_1251]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1252:
    lea rsi, [rip + .L__s3_failure_prefix_1252]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1253:
    lea rsi, [rip + .L__s3_failure_prefix_1253]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1254:
    lea rsi, [rip + .L__s3_failure_prefix_1254]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1255:
    lea rsi, [rip + .L__s3_failure_prefix_1255]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1256:
    lea rsi, [rip + .L__s3_failure_prefix_1256]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_1257:
    lea rsi, [rip + .L__s3_failure_prefix_1257]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1258:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1258]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_1258]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1259:
    lea rsi, [rip + .L__s3_failure_prefix_1259]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1260:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1260]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_1260]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1261:
    lea rsi, [rip + .L__s3_failure_prefix_1261]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1262:
    lea rsi, [rip + .L__s3_failure_prefix_1262]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1263:
    lea rsi, [rip + .L__s3_failure_prefix_1263]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1264:
    lea rsi, [rip + .L__s3_failure_prefix_1264]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1265:
    lea rsi, [rip + .L__s3_failure_prefix_1265]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1266:
    lea rsi, [rip + .L__s3_failure_prefix_1266]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1267:
    lea rsi, [rip + .L__s3_failure_prefix_1267]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1268:
    lea rsi, [rip + .L__s3_failure_prefix_1268]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1269:
    lea rsi, [rip + .L__s3_failure_prefix_1269]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1270:
    lea rsi, [rip + .L__s3_failure_prefix_1270]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1271:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1271]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1271]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1272:
    lea rsi, [rip + .L__s3_failure_prefix_1272]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1273:
    lea rsi, [rip + .L__s3_failure_prefix_1273]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1274:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1274]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_1274]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_1275:
    lea rsi, [rip + .L__s3_failure_prefix_1275]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1276:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1276]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1276]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1277:
    lea rsi, [rip + .L__s3_failure_prefix_1277]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_1278:
    lea rsi, [rip + .L__s3_failure_prefix_1278]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1279:
    lea rsi, [rip + .L__s3_failure_prefix_1279]
    mov edx, 122
    jmp __s3_fail_message
.L__s3_failure_site_1280:
    lea rsi, [rip + .L__s3_failure_prefix_1280]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1281:
    lea rsi, [rip + .L__s3_failure_prefix_1281]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1282:
    lea rsi, [rip + .L__s3_failure_prefix_1282]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1283:
    lea rsi, [rip + .L__s3_failure_prefix_1283]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_1284:
    lea rsi, [rip + .L__s3_failure_prefix_1284]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1285:
    lea rsi, [rip + .L__s3_failure_prefix_1285]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1286:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1286]
    mov edx, 105
    lea rcx, [rip + .L__s3_failure_suffix_1286]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1287:
    lea rsi, [rip + .L__s3_failure_prefix_1287]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1288:
    lea rsi, [rip + .L__s3_failure_prefix_1288]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1289:
    lea rsi, [rip + .L__s3_failure_prefix_1289]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1290:
    lea rsi, [rip + .L__s3_failure_prefix_1290]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1291:
    lea rsi, [rip + .L__s3_failure_prefix_1291]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_1292:
    lea rsi, [rip + .L__s3_failure_prefix_1292]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_1293:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1293]
    mov edx, 103
    lea rcx, [rip + .L__s3_failure_suffix_1293]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1294:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1294]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_1294]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_1295:
    lea rsi, [rip + .L__s3_failure_prefix_1295]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1296:
    lea rsi, [rip + .L__s3_failure_prefix_1296]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1297:
    lea rsi, [rip + .L__s3_failure_prefix_1297]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1298:
    lea rsi, [rip + .L__s3_failure_prefix_1298]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1299:
    lea rsi, [rip + .L__s3_failure_prefix_1299]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_1300:
    lea rsi, [rip + .L__s3_failure_prefix_1300]
    mov edx, 144
    jmp __s3_fail_message
.L__s3_failure_site_1301:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1301]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_1301]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1302:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1302]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_1302]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_1303:
    lea rsi, [rip + .L__s3_failure_prefix_1303]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_1304:
    lea rsi, [rip + .L__s3_failure_prefix_1304]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1305:
    lea rsi, [rip + .L__s3_failure_prefix_1305]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1306:
    lea rsi, [rip + .L__s3_failure_prefix_1306]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1307:
    lea rsi, [rip + .L__s3_failure_prefix_1307]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_1308:
    lea rsi, [rip + .L__s3_failure_prefix_1308]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_1309:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1309]
    mov edx, 103
    lea rcx, [rip + .L__s3_failure_suffix_1309]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1310:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1310]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_1310]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_1311:
    lea rsi, [rip + .L__s3_failure_prefix_1311]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1312:
    lea rsi, [rip + .L__s3_failure_prefix_1312]
    mov edx, 148
    jmp __s3_fail_message
.L__s3_failure_site_1313:
    lea rsi, [rip + .L__s3_failure_prefix_1313]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_1314:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1314]
    mov edx, 117
    lea rcx, [rip + .L__s3_failure_suffix_1314]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_1315:
    lea rsi, [rip + .L__s3_failure_prefix_1315]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_1316:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_1316]
    mov edx, 103
    lea rcx, [rip + .L__s3_failure_suffix_1316]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_1317:
    lea rsi, [rip + .L__s3_failure_prefix_1317]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_1318:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_1318]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_1318]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_1319:
    lea rsi, [rip + .L__s3_failure_prefix_1319]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_1320:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_1320]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_1320]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_1321:
    lea rsi, [rip + .L__s3_failure_prefix_1321]
    mov edx, 131
    jmp __s3_fail_message
.L__s3_failure_site_1322:
    lea rsi, [rip + .L__s3_failure_prefix_1322]
    mov edx, 128
    jmp __s3_fail_message

.section .rodata
.L__s3_failure_prefix_0:
    .ascii "runtime error [frame limit] in function 'xsbench_binary_search'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_0:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_1:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 2:20 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_2:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 2:5 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_3:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 2:5 (block entry, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_4:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 2:5 (block entry, TSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_5:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 2:5 (block entry, TSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_6:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 2:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_6:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_7:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 3:5 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_8:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 3:5 (block entry, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_9:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 3:5 (block entry, TSTORE): register r7 is uninitialized\n"
.L__s3_failure_prefix_10:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 3:5 (block entry, TSTORE): register r4 is uninitialized\n"
.L__s3_failure_prefix_11:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 3:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_11:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_12:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 13:23 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_13:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 13:17 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_14:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_15:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_16:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_17:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_18:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_19:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_20:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_21:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 10:24 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_22:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 10:17 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_23:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:27 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_24:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:34 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_25:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:41 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_26:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:48 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_27:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:9 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_28:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:33 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_29:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:47 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_30:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:51 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_31:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:9 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_32:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 7:49 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_33:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 7:9 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_34:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 8:15 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_35:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:11 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_36:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:18 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_37:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:24 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_38:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:5 (block entry, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_39:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:11 (block while_condition_0, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_40:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 4:11 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_40:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_41:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:11 (block while_condition_0, TLOAD): register r31 is uninitialized\n"
.L__s3_failure_prefix_42:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 4:11 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_42:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_43:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:18 (block while_condition_0, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_44:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 4:18 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_44:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_45:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:18 (block while_condition_0, TLOAD): register r32 is uninitialized\n"
.L__s3_failure_prefix_46:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 4:18 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_46:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_47:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:16 (block while_condition_0, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_48:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 4:16 (block while_condition_0, TNDIFF): i64 subtraction overflow\n"
.L__s3_failure_prefix_49:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:16 (block while_condition_0, TNDIFF): register r34 is uninitialized\n"
.L__s3_failure_prefix_50:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:16 (block while_condition_0, TNDIFF): register r35 is uninitialized\n"
.L__s3_failure_prefix_51:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block while_condition_0, TCMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_52:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block while_condition_0, TCMP): register r36 is uninitialized\n"
.L__s3_failure_prefix_53:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block while_condition_0, TCMP): register r33 is uninitialized\n"
.L__s3_failure_prefix_54:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block while_condition_0, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_55:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:27 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_56:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 5:27 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_56:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_57:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:27 (block while_body_1, TLOAD): register r19 is uninitialized\n"
.L__s3_failure_prefix_58:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 5:27 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_58:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_59:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:34 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_60:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 5:34 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_60:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_61:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:34 (block while_body_1, TLOAD): register r20 is uninitialized\n"
.L__s3_failure_prefix_62:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 5:34 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_62:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_63:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:41 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_64:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 5:41 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_64:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_65:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:41 (block while_body_1, TLOAD): register r21 is uninitialized\n"
.L__s3_failure_prefix_66:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 5:41 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_66:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_67:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:39 (block while_body_1, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_68:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 5:39 (block while_body_1, TNDIFF): i64 subtraction overflow\n"
.L__s3_failure_prefix_69:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:39 (block while_body_1, TNDIFF): register r39 is uninitialized\n"
.L__s3_failure_prefix_70:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:39 (block while_body_1, TNDIFF): register r40 is uninitialized\n"
.L__s3_failure_prefix_71:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:46 (block while_body_1, TDIV): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_72:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 5:46 (block while_body_1, TDIV): i64 division overflow\n"
.L__s3_failure_prefix_73:
    .ascii "runtime error [division by zero] in function 'xsbench_binary_search'\nat source 5:46 (block while_body_1, TDIV): i64 division by zero\n"
.L__s3_failure_prefix_74:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:46 (block while_body_1, TDIV): register r41 is uninitialized\n"
.L__s3_failure_prefix_75:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:46 (block while_body_1, TDIV): register r22 is uninitialized\n"
.L__s3_failure_prefix_76:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:31 (block while_body_1, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_77:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 5:31 (block while_body_1, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_78:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:31 (block while_body_1, TADD): register r38 is uninitialized\n"
.L__s3_failure_prefix_79:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:31 (block while_body_1, TADD): register r42 is uninitialized\n"
.L__s3_failure_prefix_80:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 5:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_81:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:9 (block while_body_1, TSTORE): register r23 is uninitialized\n"
.L__s3_failure_prefix_82:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 5:9 (block while_body_1, TSTORE): register r43 is uninitialized\n"
.L__s3_failure_prefix_83:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 5:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_83:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_84:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:45 (block while_body_1, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_85:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 6:45 (block while_body_1, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_86:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:45 (block while_body_1, TMUL): register r2 is uninitialized\n"
.L__s3_failure_prefix_87:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:45 (block while_body_1, TMUL): register r25 is uninitialized\n"
.L__s3_failure_prefix_88:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:35 (block while_body_1, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_89:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 6:35 (block while_body_1, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_90:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:35 (block while_body_1, TADD): register r24 is uninitialized\n"
.L__s3_failure_prefix_91:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:35 (block while_body_1, TADD): register r44 is uninitialized\n"
.L__s3_failure_prefix_92:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:51 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_93:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 6:51 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_93:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_94:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:51 (block while_body_1, TLOAD): register r26 is uninitialized\n"
.L__s3_failure_prefix_95:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 6:51 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_95:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_96:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:49 (block while_body_1, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_97:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 6:49 (block while_body_1, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_98:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:49 (block while_body_1, TADD): register r45 is uninitialized\n"
.L__s3_failure_prefix_99:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:49 (block while_body_1, TADD): register r46 is uninitialized\n"
.L__s3_failure_prefix_100:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 6:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_101:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:9 (block while_body_1, TSTORE): register r27 is uninitialized\n"
.L__s3_failure_prefix_102:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 6:9 (block while_body_1, TSTORE): register r47 is uninitialized\n"
.L__s3_failure_prefix_103:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 6:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_103:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_104:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 7:49 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_105:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 7:49 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_105:
    .ascii " is uninitialized in m4\n"
.L__s3_failure_prefix_106:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 7:49 (block while_body_1, TLOAD): register r28 is uninitialized\n"
.L__s3_failure_prefix_107:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 7:49 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_107:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_108:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 7:40 (block while_body_1, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_109:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 7:40 (block while_body_1, TSLOAD): slice index "
.L__s3_failure_suffix_109:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_110:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 7:40 (block while_body_1, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_111:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 7:40 (block while_body_1, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_112:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 7:40 (block while_body_1, TSLOAD): register r48 is uninitialized\n"
.L__s3_failure_prefix_113:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 7:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_114:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 7:9 (block while_body_1, TSTORE): register r29 is uninitialized\n"
.L__s3_failure_prefix_115:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 7:9 (block while_body_1, TSTORE): register r49 is uninitialized\n"
.L__s3_failure_prefix_116:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 7:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_116:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_117:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 8:15 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_118:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 8:15 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_118:
    .ascii " is uninitialized in m5\n"
.L__s3_failure_prefix_119:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 8:15 (block while_body_1, TLOAD): register r30 is uninitialized\n"
.L__s3_failure_prefix_120:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 8:15 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_120:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_121:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 8:35 (block while_body_1, TCMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_122:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 8:35 (block while_body_1, TCMP): register r50 is uninitialized\n"
.L__s3_failure_prefix_123:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 8:35 (block while_body_1, TCMP): register r3 is uninitialized\n"
.L__s3_failure_prefix_124:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 8:9 (block while_body_1, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_125:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:5 (block while_exit_0_2, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_126:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:5 (block while_exit_1_3, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_127:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 14:12 (block while_exit_4, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_128:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 14:12 (block while_exit_4, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_129:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 14:12 (block while_exit_4, TLOAD): index "
.L__s3_failure_suffix_129:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_130:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 14:12 (block while_exit_4, TLOAD): register r52 is uninitialized\n"
.L__s3_failure_prefix_131:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 14:12 (block while_exit_4, TLOAD): index "
.L__s3_failure_suffix_131:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_132:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 14:5 (block while_exit_4, TRET): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_133:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 14:5 (block while_exit_4, TRET): register r53 is uninitialized\n"
.L__s3_failure_prefix_134:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block rel_neg_5, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_135:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block rel_neg_5, TSTORE): register r11 is uninitialized\n"
.L__s3_failure_prefix_136:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block rel_neg_5, TSTORE): register r12 is uninitialized\n"
.L__s3_failure_prefix_137:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 4:22 (block rel_neg_5, TSTORE): index "
.L__s3_failure_suffix_137:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_138:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 4:22 (block rel_neg_5, TSTORE): trit result "
.L__s3_failure_suffix_138:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_139:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block rel_neg_5, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_140:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block rel_zero_6, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_141:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block rel_zero_6, TSTORE): register r15 is uninitialized\n"
.L__s3_failure_prefix_142:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block rel_zero_6, TSTORE): register r16 is uninitialized\n"
.L__s3_failure_prefix_143:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 4:22 (block rel_zero_6, TSTORE): index "
.L__s3_failure_suffix_143:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_144:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 4:22 (block rel_zero_6, TSTORE): trit result "
.L__s3_failure_suffix_144:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_145:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block rel_zero_6, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_146:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block rel_pos_7, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_147:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block rel_pos_7, TSTORE): register r13 is uninitialized\n"
.L__s3_failure_prefix_148:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block rel_pos_7, TSTORE): register r14 is uninitialized\n"
.L__s3_failure_prefix_149:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 4:22 (block rel_pos_7, TSTORE): index "
.L__s3_failure_suffix_149:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_150:
    .ascii "runtime error [overflow] in function 'xsbench_binary_search'\nat source 4:22 (block rel_pos_7, TSTORE): trit result "
.L__s3_failure_suffix_150:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_151:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block rel_pos_7, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_152:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:22 (block rel_cont_8, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_153:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 4:22 (block rel_cont_8, TLOAD): index "
.L__s3_failure_suffix_153:
    .ascii " is uninitialized in m2\n"
.L__s3_failure_prefix_154:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:22 (block rel_cont_8, TLOAD): register r10 is uninitialized\n"
.L__s3_failure_prefix_155:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 4:22 (block rel_cont_8, TLOAD): index "
.L__s3_failure_suffix_155:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_156:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 4:5 (block rel_cont_8, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_157:
    .ascii "runtime error [invalid trit state] in function 'xsbench_binary_search'\nat source 4:5 (block rel_cont_8, TBR3): value "
.L__s3_failure_suffix_157:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_158:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 4:5 (block rel_cont_8, TBR3): register r54 is uninitialized\n"
.L__s3_failure_prefix_159:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 13:23 (block switch_negative_9, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_160:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 13:23 (block switch_negative_9, TLOAD): index "
.L__s3_failure_suffix_160:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_161:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 13:23 (block switch_negative_9, TLOAD): register r8 is uninitialized\n"
.L__s3_failure_prefix_162:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 13:23 (block switch_negative_9, TLOAD): index "
.L__s3_failure_suffix_162:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_163:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 13:17 (block switch_negative_9, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_164:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 13:17 (block switch_negative_9, TSTORE): register r9 is uninitialized\n"
.L__s3_failure_prefix_165:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 13:17 (block switch_negative_9, TSTORE): register r55 is uninitialized\n"
.L__s3_failure_prefix_166:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 13:17 (block switch_negative_9, TSTORE): index "
.L__s3_failure_suffix_166:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_167:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 12:13 (block switch_negative_9, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_168:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 12:13 (block switch_neutral_10, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_169:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 10:24 (block switch_positive_11, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_170:
    .ascii "runtime error [uninitialized memory] in function 'xsbench_binary_search'\nat source 10:24 (block switch_positive_11, TLOAD): index "
.L__s3_failure_suffix_170:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_171:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 10:24 (block switch_positive_11, TLOAD): register r17 is uninitialized\n"
.L__s3_failure_prefix_172:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 10:24 (block switch_positive_11, TLOAD): index "
.L__s3_failure_suffix_172:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_173:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 10:17 (block switch_positive_11, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_174:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 10:17 (block switch_positive_11, TSTORE): register r18 is uninitialized\n"
.L__s3_failure_prefix_175:
    .ascii "runtime error [uninitialized register] in function 'xsbench_binary_search'\nat source 10:17 (block switch_positive_11, TSTORE): register r56 is uninitialized\n"
.L__s3_failure_prefix_176:
    .ascii "runtime error [bounds] in function 'xsbench_binary_search'\nat source 10:17 (block switch_positive_11, TSTORE): index "
.L__s3_failure_suffix_176:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_177:
    .ascii "runtime error [instruction limit] in function 'xsbench_binary_search'\nat source 9:13 (block switch_positive_11, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_178:
    .ascii "runtime error [frame limit] in function 'xs_lookup_batch'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_178:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_179:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 17:23 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_180:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 17:5 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_181:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 17:5 (block entry, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_182:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 17:5 (block entry, TSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_183:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 17:5 (block entry, TSTORE): register r4 is uninitialized\n"
.L__s3_failure_prefix_184:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 17:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_184:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_185:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 18:25 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_186:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 18:5 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_187:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 18:5 (block entry, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_188:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 18:5 (block entry, TSTORE): register r7 is uninitialized\n"
.L__s3_failure_prefix_189:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 18:5 (block entry, TSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_190:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 18:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_190:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_191:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 19:38 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_192:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 19:29 (block entry, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_193:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 19:29 (block entry, TSLOAD): slice index "
.L__s3_failure_suffix_193:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_194:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 19:29 (block entry, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_195:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 19:29 (block entry, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_196:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 19:29 (block entry, TSLOAD): register r8 is uninitialized\n"
.L__s3_failure_prefix_197:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 19:5 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_198:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 19:5 (block entry, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_199:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 19:5 (block entry, TSTORE): register r10 is uninitialized\n"
.L__s3_failure_prefix_200:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 19:5 (block entry, TSTORE): register r9 is uninitialized\n"
.L__s3_failure_prefix_201:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 19:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_201:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_202:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:5 (block entry, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_203:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:11 (block while_condition_0, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_204:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:11 (block while_condition_0, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_205:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 20:11 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_205:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_206:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:11 (block while_condition_0, TLOAD): register r11 is uninitialized\n"
.L__s3_failure_prefix_207:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 20:11 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_207:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_208:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:20 (block while_condition_0, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_209:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:20 (block while_condition_0, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_210:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 20:20 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_210:
    .ascii " is uninitialized in m2\n"
.L__s3_failure_prefix_211:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:20 (block while_condition_0, TLOAD): register r13 is uninitialized\n"
.L__s3_failure_prefix_212:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 20:20 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_212:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_213:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block while_condition_0, TCMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_214:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block while_condition_0, TCMP): register r12 is uninitialized\n"
.L__s3_failure_prefix_215:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block while_condition_0, TCMP): register r14 is uninitialized\n"
.L__s3_failure_prefix_216:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block while_condition_0, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_217:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 21:39 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_218:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 21:44 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_219:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 21:44 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_220:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 21:44 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_220:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_221:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 21:44 (block while_body_1, TLOAD): register r25 is uninitialized\n"
.L__s3_failure_prefix_222:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 21:44 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_222:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_223:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 21:42 (block while_body_1, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_224:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 21:42 (block while_body_1, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_225:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 21:42 (block while_body_1, TADD): register r24 is uninitialized\n"
.L__s3_failure_prefix_226:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 21:42 (block while_body_1, TADD): register r26 is uninitialized\n"
.L__s3_failure_prefix_227:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 21:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_228:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 21:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_229:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 21:9 (block while_body_1, TSTORE): register r28 is uninitialized\n"
.L__s3_failure_prefix_230:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 21:9 (block while_body_1, TSTORE): register r27 is uninitialized\n"
.L__s3_failure_prefix_231:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 21:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_231:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_232:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 22:41 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_233:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 22:46 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_234:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 22:46 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_235:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 22:46 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_235:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_236:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 22:46 (block while_body_1, TLOAD): register r30 is uninitialized\n"
.L__s3_failure_prefix_237:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 22:46 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_237:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_238:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 22:44 (block while_body_1, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_239:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 22:44 (block while_body_1, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_240:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 22:44 (block while_body_1, TADD): register r29 is uninitialized\n"
.L__s3_failure_prefix_241:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 22:44 (block while_body_1, TADD): register r31 is uninitialized\n"
.L__s3_failure_prefix_242:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 22:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_243:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 22:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_244:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 22:9 (block while_body_1, TSTORE): register r33 is uninitialized\n"
.L__s3_failure_prefix_245:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 22:9 (block while_body_1, TSTORE): register r32 is uninitialized\n"
.L__s3_failure_prefix_246:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 22:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_246:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_247:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 23:42 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_248:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 23:42 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_249:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 23:42 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_249:
    .ascii " is uninitialized in m4\n"
.L__s3_failure_prefix_250:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 23:42 (block while_body_1, TLOAD): register r34 is uninitialized\n"
.L__s3_failure_prefix_251:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 23:42 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_251:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_252:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 23:33 (block while_body_1, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_253:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 23:33 (block while_body_1, TSLOAD): slice index "
.L__s3_failure_suffix_253:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_254:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 23:33 (block while_body_1, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_255:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 23:33 (block while_body_1, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_256:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 23:33 (block while_body_1, TSLOAD): register r35 is uninitialized\n"
.L__s3_failure_prefix_257:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 23:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_258:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 23:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_259:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 23:9 (block while_body_1, TSTORE): register r37 is uninitialized\n"
.L__s3_failure_prefix_260:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 23:9 (block while_body_1, TSTORE): register r36 is uninitialized\n"
.L__s3_failure_prefix_261:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 23:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_261:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_262:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 24:34 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_263:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 24:34 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_264:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 24:34 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_264:
    .ascii " is uninitialized in m6\n"
.L__s3_failure_prefix_265:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 24:34 (block while_body_1, TLOAD): register r38 is uninitialized\n"
.L__s3_failure_prefix_266:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 24:34 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_266:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_267:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 24:27 (block while_body_1, TCVT): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_268:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 24:27 (block while_body_1, TCVT): register r39 is uninitialized\n"
.L__s3_failure_prefix_269:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 24:50 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_270:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 24:48 (block while_body_1, TDIV): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_271:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 24:48 (block while_body_1, TDIV): register r40 is uninitialized\n"
.L__s3_failure_prefix_272:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 24:48 (block while_body_1, TDIV): register r41 is uninitialized\n"
.L__s3_failure_prefix_273:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 24:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_274:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 24:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_275:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 24:9 (block while_body_1, TSTORE): register r43 is uninitialized\n"
.L__s3_failure_prefix_276:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 24:9 (block while_body_1, TSTORE): register r42 is uninitialized\n"
.L__s3_failure_prefix_277:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 24:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_277:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_278:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 25:38 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_279:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 25:38 (block while_body_1, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_280:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 25:38 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_280:
    .ascii " is uninitialized in m5\n"
.L__s3_failure_prefix_281:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 25:38 (block while_body_1, TLOAD): register r44 is uninitialized\n"
.L__s3_failure_prefix_282:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 25:38 (block while_body_1, TLOAD): index "
.L__s3_failure_suffix_282:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_283:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 25:29 (block while_body_1, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_284:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 25:29 (block while_body_1, TSLOAD): slice index "
.L__s3_failure_suffix_284:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_285:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 25:29 (block while_body_1, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_286:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 25:29 (block while_body_1, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_287:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 25:29 (block while_body_1, TSLOAD): register r45 is uninitialized\n"
.L__s3_failure_prefix_288:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 25:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_289:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 25:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_290:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 25:9 (block while_body_1, TSTORE): register r47 is uninitialized\n"
.L__s3_failure_prefix_291:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 25:9 (block while_body_1, TSTORE): register r46 is uninitialized\n"
.L__s3_failure_prefix_292:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 25:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_292:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_293:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 26:29 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_294:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 26:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_295:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 26:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_296:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 26:9 (block while_body_1, TSTORE): register r49 is uninitialized\n"
.L__s3_failure_prefix_297:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 26:9 (block while_body_1, TSTORE): register r48 is uninitialized\n"
.L__s3_failure_prefix_298:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 26:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_298:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_299:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 27:29 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_300:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 27:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_301:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 27:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_302:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 27:9 (block while_body_1, TSTORE): register r51 is uninitialized\n"
.L__s3_failure_prefix_303:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 27:9 (block while_body_1, TSTORE): register r50 is uninitialized\n"
.L__s3_failure_prefix_304:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 27:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_304:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_305:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 28:31 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_306:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 28:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_307:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 28:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_308:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 28:9 (block while_body_1, TSTORE): register r53 is uninitialized\n"
.L__s3_failure_prefix_309:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 28:9 (block while_body_1, TSTORE): register r52 is uninitialized\n"
.L__s3_failure_prefix_310:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 28:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_310:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_311:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 29:34 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_312:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 29:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_313:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 29:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_314:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 29:9 (block while_body_1, TSTORE): register r55 is uninitialized\n"
.L__s3_failure_prefix_315:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 29:9 (block while_body_1, TSTORE): register r54 is uninitialized\n"
.L__s3_failure_prefix_316:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 29:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_316:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_317:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 30:31 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_318:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 30:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_319:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 30:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_320:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 30:9 (block while_body_1, TSTORE): register r57 is uninitialized\n"
.L__s3_failure_prefix_321:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 30:9 (block while_body_1, TSTORE): register r56 is uninitialized\n"
.L__s3_failure_prefix_322:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 30:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_322:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_323:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 31:34 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_324:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 31:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_325:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 31:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_326:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 31:9 (block while_body_1, TSTORE): register r59 is uninitialized\n"
.L__s3_failure_prefix_327:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 31:9 (block while_body_1, TSTORE): register r58 is uninitialized\n"
.L__s3_failure_prefix_328:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 31:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_328:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_329:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:9 (block while_body_1, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_330:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:5 (block while_exit_0_2, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_331:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:5 (block while_exit_1_3, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_332:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 67:12 (block while_exit_4, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_333:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 67:12 (block while_exit_4, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_334:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 67:12 (block while_exit_4, TLOAD): index "
.L__s3_failure_suffix_334:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_335:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 67:12 (block while_exit_4, TLOAD): register r372 is uninitialized\n"
.L__s3_failure_prefix_336:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 67:12 (block while_exit_4, TLOAD): index "
.L__s3_failure_suffix_336:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_337:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 67:5 (block while_exit_4, TRET): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_338:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 67:5 (block while_exit_4, TRET): register r373 is uninitialized\n"
.L__s3_failure_prefix_339:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_340:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_341:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_342:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TSTORE): register r16 is uninitialized\n"
.L__s3_failure_prefix_343:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TSTORE): register r17 is uninitialized\n"
.L__s3_failure_prefix_344:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TSTORE): index "
.L__s3_failure_suffix_344:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_345:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TSTORE): trit result "
.L__s3_failure_suffix_345:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_346:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_neg_5, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_347:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_348:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_349:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_350:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TSTORE): register r18 is uninitialized\n"
.L__s3_failure_prefix_351:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TSTORE): register r19 is uninitialized\n"
.L__s3_failure_prefix_352:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TSTORE): index "
.L__s3_failure_suffix_352:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_353:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TSTORE): trit result "
.L__s3_failure_suffix_353:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_354:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_zero_6, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_355:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_356:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_357:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_358:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TSTORE): register r20 is uninitialized\n"
.L__s3_failure_prefix_359:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TSTORE): register r21 is uninitialized\n"
.L__s3_failure_prefix_360:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TSTORE): index "
.L__s3_failure_suffix_360:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_361:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TSTORE): trit result "
.L__s3_failure_suffix_361:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_362:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_pos_7, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_363:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_cont_8, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_364:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:18 (block rel_cont_8, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_365:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 20:18 (block rel_cont_8, TLOAD): index "
.L__s3_failure_suffix_365:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_366:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:18 (block rel_cont_8, TLOAD): register r22 is uninitialized\n"
.L__s3_failure_prefix_367:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 20:18 (block rel_cont_8, TLOAD): index "
.L__s3_failure_suffix_367:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_368:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:5 (block rel_cont_8, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_369:
    .ascii "runtime error [invalid trit state] in function 'xs_lookup_batch'\nat source 20:5 (block rel_cont_8, TBR3): value "
.L__s3_failure_suffix_369:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_370:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 20:5 (block rel_cont_8, TBR3): register r23 is uninitialized\n"
.L__s3_failure_prefix_371:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:15 (block while_condition_9, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_372:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:15 (block while_condition_9, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_373:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 32:15 (block while_condition_9, TLOAD): index "
.L__s3_failure_suffix_373:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_374:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:15 (block while_condition_9, TLOAD): register r60 is uninitialized\n"
.L__s3_failure_prefix_375:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 32:15 (block while_condition_9, TLOAD): index "
.L__s3_failure_suffix_375:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_376:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:26 (block while_condition_9, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_377:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block while_condition_9, TCMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_378:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block while_condition_9, TCMP): register r61 is uninitialized\n"
.L__s3_failure_prefix_379:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block while_condition_9, TCMP): register r62 is uninitialized\n"
.L__s3_failure_prefix_380:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block while_condition_9, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_381:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:42 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_382:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:42 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_383:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 33:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_383:
    .ascii " is uninitialized in m8\n"
.L__s3_failure_prefix_384:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:42 (block while_body_10, TLOAD): register r72 is uninitialized\n"
.L__s3_failure_prefix_385:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 33:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_385:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_386:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:53 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_387:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:51 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_388:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 33:51 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_389:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:51 (block while_body_10, TMUL): register r73 is uninitialized\n"
.L__s3_failure_prefix_390:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:51 (block while_body_10, TMUL): register r74 is uninitialized\n"
.L__s3_failure_prefix_391:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:57 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_392:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:57 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_393:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 33:57 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_393:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_394:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:57 (block while_body_10, TLOAD): register r76 is uninitialized\n"
.L__s3_failure_prefix_395:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 33:57 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_395:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_396:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:55 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_397:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 33:55 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_398:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:55 (block while_body_10, TADD): register r75 is uninitialized\n"
.L__s3_failure_prefix_399:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:55 (block while_body_10, TADD): register r77 is uninitialized\n"
.L__s3_failure_prefix_400:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_401:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 33:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_402:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:13 (block while_body_10, TSTORE): register r79 is uninitialized\n"
.L__s3_failure_prefix_403:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 33:13 (block while_body_10, TSTORE): register r78 is uninitialized\n"
.L__s3_failure_prefix_404:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 33:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_404:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_405:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 34:41 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_406:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 34:41 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_407:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 34:41 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_407:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_408:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 34:41 (block while_body_10, TLOAD): register r80 is uninitialized\n"
.L__s3_failure_prefix_409:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 34:41 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_409:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_410:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 34:32 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_411:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 34:32 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_411:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_412:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 34:32 (block while_body_10, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_413:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 34:32 (block while_body_10, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_414:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 34:32 (block while_body_10, TSLOAD): register r81 is uninitialized\n"
.L__s3_failure_prefix_415:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 34:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_416:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 34:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_417:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 34:13 (block while_body_10, TSTORE): register r83 is uninitialized\n"
.L__s3_failure_prefix_418:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 34:13 (block while_body_10, TSTORE): register r82 is uninitialized\n"
.L__s3_failure_prefix_419:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 34:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_419:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_420:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:44 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_421:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:48 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_422:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:48 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_423:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 35:48 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_423:
    .ascii " is uninitialized in m8\n"
.L__s3_failure_prefix_424:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:48 (block while_body_10, TLOAD): register r85 is uninitialized\n"
.L__s3_failure_prefix_425:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 35:48 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_425:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_426:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:59 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_427:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:57 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_428:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 35:57 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_429:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:57 (block while_body_10, TMUL): register r86 is uninitialized\n"
.L__s3_failure_prefix_430:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:57 (block while_body_10, TMUL): register r87 is uninitialized\n"
.L__s3_failure_prefix_431:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:46 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_432:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 35:46 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_433:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:46 (block while_body_10, TADD): register r84 is uninitialized\n"
.L__s3_failure_prefix_434:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:46 (block while_body_10, TADD): register r88 is uninitialized\n"
.L__s3_failure_prefix_435:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:63 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_436:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:63 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_437:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 35:63 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_437:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_438:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:63 (block while_body_10, TLOAD): register r90 is uninitialized\n"
.L__s3_failure_prefix_439:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 35:63 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_439:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_440:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:61 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_441:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 35:61 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_442:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:61 (block while_body_10, TADD): register r89 is uninitialized\n"
.L__s3_failure_prefix_443:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:61 (block while_body_10, TADD): register r91 is uninitialized\n"
.L__s3_failure_prefix_444:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_445:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 35:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_446:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:13 (block while_body_10, TSTORE): register r93 is uninitialized\n"
.L__s3_failure_prefix_447:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 35:13 (block while_body_10, TSTORE): register r92 is uninitialized\n"
.L__s3_failure_prefix_448:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 35:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_448:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_449:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 36:43 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_450:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 36:43 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_451:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 36:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_451:
    .ascii " is uninitialized in m18\n"
.L__s3_failure_prefix_452:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 36:43 (block while_body_10, TLOAD): register r94 is uninitialized\n"
.L__s3_failure_prefix_453:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 36:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_453:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_454:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 36:38 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_455:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 36:38 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_455:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_456:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 36:38 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_457:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 36:38 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_458:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 36:38 (block while_body_10, TSLOAD): register r95 is uninitialized\n"
.L__s3_failure_prefix_459:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 36:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_460:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 36:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_461:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 36:13 (block while_body_10, TSTORE): register r97 is uninitialized\n"
.L__s3_failure_prefix_462:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 36:13 (block while_body_10, TSTORE): register r96 is uninitialized\n"
.L__s3_failure_prefix_463:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 36:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_463:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_464:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:34 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_465:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:39 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_466:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:39 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_467:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 37:39 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_467:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_468:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 37:39 (block while_body_10, TLOAD): register r99 is uninitialized\n"
.L__s3_failure_prefix_469:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 37:39 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_469:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_470:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:49 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_471:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:47 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_472:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 37:47 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_473:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 37:47 (block while_body_10, TMUL): register r100 is uninitialized\n"
.L__s3_failure_prefix_474:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 37:47 (block while_body_10, TMUL): register r101 is uninitialized\n"
.L__s3_failure_prefix_475:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:37 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_476:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 37:37 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_477:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 37:37 (block while_body_10, TADD): register r98 is uninitialized\n"
.L__s3_failure_prefix_478:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 37:37 (block while_body_10, TADD): register r102 is uninitialized\n"
.L__s3_failure_prefix_479:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_480:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 37:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_481:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 37:13 (block while_body_10, TSTORE): register r104 is uninitialized\n"
.L__s3_failure_prefix_482:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 37:13 (block while_body_10, TSTORE): register r103 is uninitialized\n"
.L__s3_failure_prefix_483:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 37:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_483:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_484:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:60 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_485:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:60 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_486:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 38:60 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_486:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_487:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:60 (block while_body_10, TLOAD): register r105 is uninitialized\n"
.L__s3_failure_prefix_488:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 38:60 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_488:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_489:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:69 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_490:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:69 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_491:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 38:69 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_491:
    .ascii " is uninitialized in m6\n"
.L__s3_failure_prefix_492:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:69 (block while_body_10, TLOAD): register r107 is uninitialized\n"
.L__s3_failure_prefix_493:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 38:69 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_493:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_494:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:83 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_495:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:28 (block while_body_10, TCALL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_496:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:28 (block while_body_10, TCALL): register r2 is uninitialized\n"
.L__s3_failure_prefix_497:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:28 (block while_body_10, TCALL): register r3 is uninitialized\n"
.L__s3_failure_prefix_498:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:28 (block while_body_10, TCALL): register r106 is uninitialized\n"
.L__s3_failure_prefix_499:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:28 (block while_body_10, TCALL): register r108 is uninitialized\n"
.L__s3_failure_prefix_500:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:28 (block while_body_10, TCALL): register r109 is uninitialized\n"
.L__s3_failure_prefix_501:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_502:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 38:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_503:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:13 (block while_body_10, TSTORE): register r111 is uninitialized\n"
.L__s3_failure_prefix_504:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 38:13 (block while_body_10, TSTORE): register r110 is uninitialized\n"
.L__s3_failure_prefix_505:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 38:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_505:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_506:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 39:29 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_507:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 39:29 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_508:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 39:29 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_508:
    .ascii " is uninitialized in m21\n"
.L__s3_failure_prefix_509:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 39:29 (block while_body_10, TLOAD): register r112 is uninitialized\n"
.L__s3_failure_prefix_510:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 39:29 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_510:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_511:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 39:35 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_512:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 39:33 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_513:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 39:33 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_514:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 39:33 (block while_body_10, TADD): register r113 is uninitialized\n"
.L__s3_failure_prefix_515:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 39:33 (block while_body_10, TADD): register r114 is uninitialized\n"
.L__s3_failure_prefix_516:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 39:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_517:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 39:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_518:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 39:13 (block while_body_10, TSTORE): register r116 is uninitialized\n"
.L__s3_failure_prefix_519:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 39:13 (block while_body_10, TSTORE): register r115 is uninitialized\n"
.L__s3_failure_prefix_520:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 39:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_520:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_521:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:34 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_522:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:34 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_523:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 40:34 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_523:
    .ascii " is uninitialized in m20\n"
.L__s3_failure_prefix_524:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:34 (block while_body_10, TLOAD): register r117 is uninitialized\n"
.L__s3_failure_prefix_525:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 40:34 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_525:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_526:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:46 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_527:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:46 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_528:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 40:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_528:
    .ascii " is uninitialized in m21\n"
.L__s3_failure_prefix_529:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:46 (block while_body_10, TLOAD): register r119 is uninitialized\n"
.L__s3_failure_prefix_530:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 40:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_530:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_531:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:52 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_532:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:50 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_533:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 40:50 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_534:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:50 (block while_body_10, TMUL): register r120 is uninitialized\n"
.L__s3_failure_prefix_535:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:50 (block while_body_10, TMUL): register r121 is uninitialized\n"
.L__s3_failure_prefix_536:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:44 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_537:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 40:44 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_538:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:44 (block while_body_10, TADD): register r118 is uninitialized\n"
.L__s3_failure_prefix_539:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:44 (block while_body_10, TADD): register r122 is uninitialized\n"
.L__s3_failure_prefix_540:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_541:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 40:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_542:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:13 (block while_body_10, TSTORE): register r124 is uninitialized\n"
.L__s3_failure_prefix_543:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 40:13 (block while_body_10, TSTORE): register r123 is uninitialized\n"
.L__s3_failure_prefix_544:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 40:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_544:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_545:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:35 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_546:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:35 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_547:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 41:35 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_547:
    .ascii " is uninitialized in m20\n"
.L__s3_failure_prefix_548:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:35 (block while_body_10, TLOAD): register r125 is uninitialized\n"
.L__s3_failure_prefix_549:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 41:35 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_549:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_550:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:47 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_551:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:47 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_552:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 41:47 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_552:
    .ascii " is uninitialized in m22\n"
.L__s3_failure_prefix_553:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:47 (block while_body_10, TLOAD): register r127 is uninitialized\n"
.L__s3_failure_prefix_554:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 41:47 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_554:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_555:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:54 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_556:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:52 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_557:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 41:52 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_558:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:52 (block while_body_10, TMUL): register r128 is uninitialized\n"
.L__s3_failure_prefix_559:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:52 (block while_body_10, TMUL): register r129 is uninitialized\n"
.L__s3_failure_prefix_560:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:45 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_561:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 41:45 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_562:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:45 (block while_body_10, TADD): register r126 is uninitialized\n"
.L__s3_failure_prefix_563:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:45 (block while_body_10, TADD): register r130 is uninitialized\n"
.L__s3_failure_prefix_564:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_565:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 41:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_566:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:13 (block while_body_10, TSTORE): register r132 is uninitialized\n"
.L__s3_failure_prefix_567:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 41:13 (block while_body_10, TSTORE): register r131 is uninitialized\n"
.L__s3_failure_prefix_568:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 41:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_568:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_569:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:41 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_570:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:45 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_571:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:45 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_572:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 42:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_572:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_573:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:45 (block while_body_10, TLOAD): register r134 is uninitialized\n"
.L__s3_failure_prefix_574:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 42:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_574:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_575:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:55 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_576:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:53 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_577:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 42:53 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_578:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:53 (block while_body_10, TMUL): register r135 is uninitialized\n"
.L__s3_failure_prefix_579:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:53 (block while_body_10, TMUL): register r136 is uninitialized\n"
.L__s3_failure_prefix_580:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:43 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_581:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 42:43 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_582:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:43 (block while_body_10, TADD): register r133 is uninitialized\n"
.L__s3_failure_prefix_583:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:43 (block while_body_10, TADD): register r137 is uninitialized\n"
.L__s3_failure_prefix_584:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:59 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_585:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:59 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_586:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 42:59 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_586:
    .ascii " is uninitialized in m21\n"
.L__s3_failure_prefix_587:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:59 (block while_body_10, TLOAD): register r139 is uninitialized\n"
.L__s3_failure_prefix_588:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 42:59 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_588:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_589:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:57 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_590:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 42:57 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_591:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:57 (block while_body_10, TADD): register r138 is uninitialized\n"
.L__s3_failure_prefix_592:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:57 (block while_body_10, TADD): register r140 is uninitialized\n"
.L__s3_failure_prefix_593:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_594:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 42:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_595:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:13 (block while_body_10, TSTORE): register r142 is uninitialized\n"
.L__s3_failure_prefix_596:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 42:13 (block while_body_10, TSTORE): register r141 is uninitialized\n"
.L__s3_failure_prefix_597:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 42:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_597:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_598:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:42 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_599:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:46 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_600:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:46 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_601:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 43:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_601:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_602:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:46 (block while_body_10, TLOAD): register r144 is uninitialized\n"
.L__s3_failure_prefix_603:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 43:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_603:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_604:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:56 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_605:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:54 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_606:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 43:54 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_607:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:54 (block while_body_10, TMUL): register r145 is uninitialized\n"
.L__s3_failure_prefix_608:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:54 (block while_body_10, TMUL): register r146 is uninitialized\n"
.L__s3_failure_prefix_609:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:44 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_610:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 43:44 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_611:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:44 (block while_body_10, TADD): register r143 is uninitialized\n"
.L__s3_failure_prefix_612:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:44 (block while_body_10, TADD): register r147 is uninitialized\n"
.L__s3_failure_prefix_613:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:60 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_614:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:60 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_615:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 43:60 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_615:
    .ascii " is uninitialized in m22\n"
.L__s3_failure_prefix_616:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:60 (block while_body_10, TLOAD): register r149 is uninitialized\n"
.L__s3_failure_prefix_617:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 43:60 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_617:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_618:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:58 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_619:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 43:58 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_620:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:58 (block while_body_10, TADD): register r148 is uninitialized\n"
.L__s3_failure_prefix_621:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:58 (block while_body_10, TADD): register r150 is uninitialized\n"
.L__s3_failure_prefix_622:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_623:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 43:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_624:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:13 (block while_body_10, TSTORE): register r152 is uninitialized\n"
.L__s3_failure_prefix_625:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 43:13 (block while_body_10, TSTORE): register r151 is uninitialized\n"
.L__s3_failure_prefix_626:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 43:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_626:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_627:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 44:50 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_628:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 44:50 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_629:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 44:50 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_629:
    .ascii " is uninitialized in m25\n"
.L__s3_failure_prefix_630:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 44:50 (block while_body_10, TLOAD): register r153 is uninitialized\n"
.L__s3_failure_prefix_631:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 44:50 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_631:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_632:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 44:41 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_633:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 44:41 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_633:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_634:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 44:41 (block while_body_10, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_635:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 44:41 (block while_body_10, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_636:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 44:41 (block while_body_10, TSLOAD): register r154 is uninitialized\n"
.L__s3_failure_prefix_637:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 44:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_638:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 44:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_639:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 44:13 (block while_body_10, TSTORE): register r156 is uninitialized\n"
.L__s3_failure_prefix_640:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 44:13 (block while_body_10, TSTORE): register r155 is uninitialized\n"
.L__s3_failure_prefix_641:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 44:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_641:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_642:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 45:51 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_643:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 45:51 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_644:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 45:51 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_644:
    .ascii " is uninitialized in m26\n"
.L__s3_failure_prefix_645:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 45:51 (block while_body_10, TLOAD): register r157 is uninitialized\n"
.L__s3_failure_prefix_646:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 45:51 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_646:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_647:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 45:42 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_648:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 45:42 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_648:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_649:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 45:42 (block while_body_10, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_650:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 45:42 (block while_body_10, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_651:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 45:42 (block while_body_10, TSLOAD): register r158 is uninitialized\n"
.L__s3_failure_prefix_652:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 45:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_653:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 45:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_654:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 45:13 (block while_body_10, TSTORE): register r160 is uninitialized\n"
.L__s3_failure_prefix_655:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 45:13 (block while_body_10, TSTORE): register r159 is uninitialized\n"
.L__s3_failure_prefix_656:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 45:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_656:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_657:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 46:42 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_658:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 46:42 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_659:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 46:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_659:
    .ascii " is uninitialized in m27\n"
.L__s3_failure_prefix_660:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 46:42 (block while_body_10, TLOAD): register r161 is uninitialized\n"
.L__s3_failure_prefix_661:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 46:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_661:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_662:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 46:35 (block while_body_10, TCVT): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_663:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 46:35 (block while_body_10, TCVT): register r162 is uninitialized\n"
.L__s3_failure_prefix_664:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 46:62 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_665:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 46:60 (block while_body_10, TDIV): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_666:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 46:60 (block while_body_10, TDIV): register r163 is uninitialized\n"
.L__s3_failure_prefix_667:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 46:60 (block while_body_10, TDIV): register r164 is uninitialized\n"
.L__s3_failure_prefix_668:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 46:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_669:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 46:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_670:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 46:13 (block while_body_10, TSTORE): register r166 is uninitialized\n"
.L__s3_failure_prefix_671:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 46:13 (block while_body_10, TSTORE): register r165 is uninitialized\n"
.L__s3_failure_prefix_672:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 46:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_672:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_673:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 47:43 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_674:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 47:43 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_675:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 47:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_675:
    .ascii " is uninitialized in m28\n"
.L__s3_failure_prefix_676:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 47:43 (block while_body_10, TLOAD): register r167 is uninitialized\n"
.L__s3_failure_prefix_677:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 47:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_677:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_678:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 47:36 (block while_body_10, TCVT): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_679:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 47:36 (block while_body_10, TCVT): register r168 is uninitialized\n"
.L__s3_failure_prefix_680:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 47:64 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_681:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 47:62 (block while_body_10, TDIV): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_682:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 47:62 (block while_body_10, TDIV): register r169 is uninitialized\n"
.L__s3_failure_prefix_683:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 47:62 (block while_body_10, TDIV): register r170 is uninitialized\n"
.L__s3_failure_prefix_684:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 47:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_685:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 47:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_686:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 47:13 (block while_body_10, TSTORE): register r172 is uninitialized\n"
.L__s3_failure_prefix_687:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 47:13 (block while_body_10, TSTORE): register r171 is uninitialized\n"
.L__s3_failure_prefix_688:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 47:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_688:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_689:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:32 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_690:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:32 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_691:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 48:32 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_691:
    .ascii " is uninitialized in m30\n"
.L__s3_failure_prefix_692:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:32 (block while_body_10, TLOAD): register r173 is uninitialized\n"
.L__s3_failure_prefix_693:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 48:32 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_693:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_694:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:46 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_695:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:46 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_696:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 48:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_696:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_697:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:46 (block while_body_10, TLOAD): register r175 is uninitialized\n"
.L__s3_failure_prefix_698:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 48:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_698:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_699:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:44 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_700:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:44 (block while_body_10, TNDIFF): register r174 is uninitialized\n"
.L__s3_failure_prefix_701:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:44 (block while_body_10, TNDIFF): register r176 is uninitialized\n"
.L__s3_failure_prefix_702:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:57 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_703:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:57 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_704:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 48:57 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_704:
    .ascii " is uninitialized in m30\n"
.L__s3_failure_prefix_705:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:57 (block while_body_10, TLOAD): register r178 is uninitialized\n"
.L__s3_failure_prefix_706:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 48:57 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_706:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_707:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:71 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_708:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:71 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_709:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 48:71 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_709:
    .ascii " is uninitialized in m29\n"
.L__s3_failure_prefix_710:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:71 (block while_body_10, TLOAD): register r180 is uninitialized\n"
.L__s3_failure_prefix_711:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 48:71 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_711:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_712:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:69 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_713:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:69 (block while_body_10, TNDIFF): register r179 is uninitialized\n"
.L__s3_failure_prefix_714:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:69 (block while_body_10, TNDIFF): register r181 is uninitialized\n"
.L__s3_failure_prefix_715:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:54 (block while_body_10, TDIV): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_716:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:54 (block while_body_10, TDIV): register r177 is uninitialized\n"
.L__s3_failure_prefix_717:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:54 (block while_body_10, TDIV): register r182 is uninitialized\n"
.L__s3_failure_prefix_718:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_719:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 48:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_720:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:13 (block while_body_10, TSTORE): register r184 is uninitialized\n"
.L__s3_failure_prefix_721:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 48:13 (block while_body_10, TSTORE): register r183 is uninitialized\n"
.L__s3_failure_prefix_722:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 48:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_722:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_723:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 49:41 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_724:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 49:41 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_725:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 49:41 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_725:
    .ascii " is uninitialized in m24\n"
.L__s3_failure_prefix_726:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 49:41 (block while_body_10, TLOAD): register r185 is uninitialized\n"
.L__s3_failure_prefix_727:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 49:41 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_727:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_728:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 49:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_729:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 49:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_730:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 49:13 (block while_body_10, TSTORE): register r187 is uninitialized\n"
.L__s3_failure_prefix_731:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 49:13 (block while_body_10, TSTORE): register r186 is uninitialized\n"
.L__s3_failure_prefix_732:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 49:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_732:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_733:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 50:40 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_734:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 50:40 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_735:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 50:40 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_735:
    .ascii " is uninitialized in m23\n"
.L__s3_failure_prefix_736:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 50:40 (block while_body_10, TLOAD): register r188 is uninitialized\n"
.L__s3_failure_prefix_737:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 50:40 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_737:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_738:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 50:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_739:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 50:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_740:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 50:13 (block while_body_10, TSTORE): register r190 is uninitialized\n"
.L__s3_failure_prefix_741:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 50:13 (block while_body_10, TSTORE): register r189 is uninitialized\n"
.L__s3_failure_prefix_742:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 50:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_742:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_743:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 51:43 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_744:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 51:43 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_745:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 51:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_745:
    .ascii " is uninitialized in m24\n"
.L__s3_failure_prefix_746:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 51:43 (block while_body_10, TLOAD): register r191 is uninitialized\n"
.L__s3_failure_prefix_747:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 51:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_747:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_748:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 51:56 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_749:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 51:54 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_750:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 51:54 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_751:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 51:54 (block while_body_10, TADD): register r192 is uninitialized\n"
.L__s3_failure_prefix_752:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 51:54 (block while_body_10, TADD): register r193 is uninitialized\n"
.L__s3_failure_prefix_753:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 51:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_754:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 51:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_755:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 51:13 (block while_body_10, TSTORE): register r195 is uninitialized\n"
.L__s3_failure_prefix_756:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 51:13 (block while_body_10, TSTORE): register r194 is uninitialized\n"
.L__s3_failure_prefix_757:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 51:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_757:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_758:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 52:42 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_759:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 52:42 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_760:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 52:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_760:
    .ascii " is uninitialized in m23\n"
.L__s3_failure_prefix_761:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 52:42 (block while_body_10, TLOAD): register r196 is uninitialized\n"
.L__s3_failure_prefix_762:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 52:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_762:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_763:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 52:54 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_764:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 52:52 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_765:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 52:52 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_766:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 52:52 (block while_body_10, TADD): register r197 is uninitialized\n"
.L__s3_failure_prefix_767:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 52:52 (block while_body_10, TADD): register r198 is uninitialized\n"
.L__s3_failure_prefix_768:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 52:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_769:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 52:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_770:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 52:13 (block while_body_10, TSTORE): register r200 is uninitialized\n"
.L__s3_failure_prefix_771:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 52:13 (block while_body_10, TSTORE): register r199 is uninitialized\n"
.L__s3_failure_prefix_772:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 52:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_772:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_773:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 53:46 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_774:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 53:46 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_775:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 53:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_775:
    .ascii " is uninitialized in m24\n"
.L__s3_failure_prefix_776:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 53:46 (block while_body_10, TLOAD): register r201 is uninitialized\n"
.L__s3_failure_prefix_777:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 53:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_777:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_778:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 53:59 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_779:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 53:57 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_780:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 53:57 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_781:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 53:57 (block while_body_10, TADD): register r202 is uninitialized\n"
.L__s3_failure_prefix_782:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 53:57 (block while_body_10, TADD): register r203 is uninitialized\n"
.L__s3_failure_prefix_783:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 53:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_784:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 53:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_785:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 53:13 (block while_body_10, TSTORE): register r205 is uninitialized\n"
.L__s3_failure_prefix_786:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 53:13 (block while_body_10, TSTORE): register r204 is uninitialized\n"
.L__s3_failure_prefix_787:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 53:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_787:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_788:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 54:45 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_789:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 54:45 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_790:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 54:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_790:
    .ascii " is uninitialized in m23\n"
.L__s3_failure_prefix_791:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 54:45 (block while_body_10, TLOAD): register r206 is uninitialized\n"
.L__s3_failure_prefix_792:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 54:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_792:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_793:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 54:57 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_794:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 54:55 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_795:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 54:55 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_796:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 54:55 (block while_body_10, TADD): register r207 is uninitialized\n"
.L__s3_failure_prefix_797:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 54:55 (block while_body_10, TADD): register r208 is uninitialized\n"
.L__s3_failure_prefix_798:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 54:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_799:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 54:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_800:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 54:13 (block while_body_10, TSTORE): register r210 is uninitialized\n"
.L__s3_failure_prefix_801:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 54:13 (block while_body_10, TSTORE): register r209 is uninitialized\n"
.L__s3_failure_prefix_802:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 54:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_802:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_803:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 55:43 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_804:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 55:43 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_805:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 55:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_805:
    .ascii " is uninitialized in m24\n"
.L__s3_failure_prefix_806:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 55:43 (block while_body_10, TLOAD): register r211 is uninitialized\n"
.L__s3_failure_prefix_807:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 55:43 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_807:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_808:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 55:56 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_809:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 55:54 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_810:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 55:54 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_811:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 55:54 (block while_body_10, TADD): register r212 is uninitialized\n"
.L__s3_failure_prefix_812:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 55:54 (block while_body_10, TADD): register r213 is uninitialized\n"
.L__s3_failure_prefix_813:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 55:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_814:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 55:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_815:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 55:13 (block while_body_10, TSTORE): register r215 is uninitialized\n"
.L__s3_failure_prefix_816:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 55:13 (block while_body_10, TSTORE): register r214 is uninitialized\n"
.L__s3_failure_prefix_817:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 55:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_817:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_818:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 56:42 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_819:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 56:42 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_820:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 56:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_820:
    .ascii " is uninitialized in m23\n"
.L__s3_failure_prefix_821:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 56:42 (block while_body_10, TLOAD): register r216 is uninitialized\n"
.L__s3_failure_prefix_822:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 56:42 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_822:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_823:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 56:54 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_824:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 56:52 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_825:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 56:52 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_826:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 56:52 (block while_body_10, TADD): register r217 is uninitialized\n"
.L__s3_failure_prefix_827:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 56:52 (block while_body_10, TADD): register r218 is uninitialized\n"
.L__s3_failure_prefix_828:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 56:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_829:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 56:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_830:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 56:13 (block while_body_10, TSTORE): register r220 is uninitialized\n"
.L__s3_failure_prefix_831:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 56:13 (block while_body_10, TSTORE): register r219 is uninitialized\n"
.L__s3_failure_prefix_832:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 56:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_832:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_833:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 57:46 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_834:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 57:46 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_835:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 57:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_835:
    .ascii " is uninitialized in m24\n"
.L__s3_failure_prefix_836:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 57:46 (block while_body_10, TLOAD): register r221 is uninitialized\n"
.L__s3_failure_prefix_837:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 57:46 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_837:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_838:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 57:59 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_839:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 57:57 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_840:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 57:57 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_841:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 57:57 (block while_body_10, TADD): register r222 is uninitialized\n"
.L__s3_failure_prefix_842:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 57:57 (block while_body_10, TADD): register r223 is uninitialized\n"
.L__s3_failure_prefix_843:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 57:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_844:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 57:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_845:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 57:13 (block while_body_10, TSTORE): register r225 is uninitialized\n"
.L__s3_failure_prefix_846:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 57:13 (block while_body_10, TSTORE): register r224 is uninitialized\n"
.L__s3_failure_prefix_847:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 57:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_847:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_848:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 58:45 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_849:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 58:45 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_850:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 58:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_850:
    .ascii " is uninitialized in m23\n"
.L__s3_failure_prefix_851:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 58:45 (block while_body_10, TLOAD): register r226 is uninitialized\n"
.L__s3_failure_prefix_852:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 58:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_852:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_853:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 58:57 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_854:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 58:55 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_855:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 58:55 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_856:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 58:55 (block while_body_10, TADD): register r227 is uninitialized\n"
.L__s3_failure_prefix_857:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 58:55 (block while_body_10, TADD): register r228 is uninitialized\n"
.L__s3_failure_prefix_858:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 58:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_859:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 58:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_860:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 58:13 (block while_body_10, TSTORE): register r230 is uninitialized\n"
.L__s3_failure_prefix_861:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 58:13 (block while_body_10, TSTORE): register r229 is uninitialized\n"
.L__s3_failure_prefix_862:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 58:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_862:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_863:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:24 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_864:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:24 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_865:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 59:24 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_865:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_866:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:24 (block while_body_10, TLOAD): register r231 is uninitialized\n"
.L__s3_failure_prefix_867:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:24 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_867:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_868:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:35 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_869:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:35 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_870:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 59:35 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_870:
    .ascii " is uninitialized in m19\n"
.L__s3_failure_prefix_871:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:35 (block while_body_10, TLOAD): register r233 is uninitialized\n"
.L__s3_failure_prefix_872:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:35 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_872:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_873:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:57 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_874:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:57 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_875:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 59:57 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_875:
    .ascii " is uninitialized in m32\n"
.L__s3_failure_prefix_876:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:57 (block while_body_10, TLOAD): register r235 is uninitialized\n"
.L__s3_failure_prefix_877:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:57 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_877:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_878:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:52 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_879:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:52 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_879:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_880:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:52 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_881:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:52 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_882:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:52 (block while_body_10, TSLOAD): register r236 is uninitialized\n"
.L__s3_failure_prefix_883:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:77 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_884:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:77 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_885:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 59:77 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_885:
    .ascii " is uninitialized in m31\n"
.L__s3_failure_prefix_886:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:77 (block while_body_10, TLOAD): register r238 is uninitialized\n"
.L__s3_failure_prefix_887:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:77 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_887:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_888:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:92 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_889:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:92 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_890:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 59:92 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_890:
    .ascii " is uninitialized in m32\n"
.L__s3_failure_prefix_891:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:92 (block while_body_10, TLOAD): register r240 is uninitialized\n"
.L__s3_failure_prefix_892:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:92 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_892:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_893:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:87 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_894:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:87 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_894:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_895:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:87 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_896:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:87 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_897:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:87 (block while_body_10, TSLOAD): register r241 is uninitialized\n"
.L__s3_failure_prefix_898:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:117 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_899:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:117 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_900:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 59:117 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_900:
    .ascii " is uninitialized in m33\n"
.L__s3_failure_prefix_901:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:117 (block while_body_10, TLOAD): register r243 is uninitialized\n"
.L__s3_failure_prefix_902:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:117 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_902:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_903:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:112 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_904:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:112 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_904:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_905:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:112 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_906:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:112 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_907:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:112 (block while_body_10, TSLOAD): register r244 is uninitialized\n"
.L__s3_failure_prefix_908:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:110 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_909:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:110 (block while_body_10, TNDIFF): register r242 is uninitialized\n"
.L__s3_failure_prefix_910:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:110 (block while_body_10, TNDIFF): register r245 is uninitialized\n"
.L__s3_failure_prefix_911:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:84 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_912:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:84 (block while_body_10, TMUL): register r239 is uninitialized\n"
.L__s3_failure_prefix_913:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:84 (block while_body_10, TMUL): register r246 is uninitialized\n"
.L__s3_failure_prefix_914:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:75 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_915:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:75 (block while_body_10, TNDIFF): register r237 is uninitialized\n"
.L__s3_failure_prefix_916:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:75 (block while_body_10, TNDIFF): register r247 is uninitialized\n"
.L__s3_failure_prefix_917:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:49 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_918:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:49 (block while_body_10, TMUL): register r234 is uninitialized\n"
.L__s3_failure_prefix_919:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:49 (block while_body_10, TMUL): register r248 is uninitialized\n"
.L__s3_failure_prefix_920:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:33 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_921:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:33 (block while_body_10, TADD): register r232 is uninitialized\n"
.L__s3_failure_prefix_922:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:33 (block while_body_10, TADD): register r249 is uninitialized\n"
.L__s3_failure_prefix_923:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_924:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 59:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_925:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:13 (block while_body_10, TSTORE): register r251 is uninitialized\n"
.L__s3_failure_prefix_926:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 59:13 (block while_body_10, TSTORE): register r250 is uninitialized\n"
.L__s3_failure_prefix_927:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 59:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_927:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_928:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:26 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_929:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:26 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_930:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 60:26 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_930:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_931:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:26 (block while_body_10, TLOAD): register r252 is uninitialized\n"
.L__s3_failure_prefix_932:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:26 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_932:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_933:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:39 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_934:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:39 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_935:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 60:39 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_935:
    .ascii " is uninitialized in m19\n"
.L__s3_failure_prefix_936:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:39 (block while_body_10, TLOAD): register r254 is uninitialized\n"
.L__s3_failure_prefix_937:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:39 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_937:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_938:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:61 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_939:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:61 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_940:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 60:61 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_940:
    .ascii " is uninitialized in m34\n"
.L__s3_failure_prefix_941:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:61 (block while_body_10, TLOAD): register r256 is uninitialized\n"
.L__s3_failure_prefix_942:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:61 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_942:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_943:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:56 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_944:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:56 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_944:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_945:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:56 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_946:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:56 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_947:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:56 (block while_body_10, TSLOAD): register r257 is uninitialized\n"
.L__s3_failure_prefix_948:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:83 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_949:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:83 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_950:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 60:83 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_950:
    .ascii " is uninitialized in m31\n"
.L__s3_failure_prefix_951:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:83 (block while_body_10, TLOAD): register r259 is uninitialized\n"
.L__s3_failure_prefix_952:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:83 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_952:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_953:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:98 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_954:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:98 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_955:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 60:98 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_955:
    .ascii " is uninitialized in m34\n"
.L__s3_failure_prefix_956:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:98 (block while_body_10, TLOAD): register r261 is uninitialized\n"
.L__s3_failure_prefix_957:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:98 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_957:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_958:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:93 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_959:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:93 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_959:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_960:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:93 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_961:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:93 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_962:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:93 (block while_body_10, TSLOAD): register r262 is uninitialized\n"
.L__s3_failure_prefix_963:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:125 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_964:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:125 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_965:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 60:125 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_965:
    .ascii " is uninitialized in m35\n"
.L__s3_failure_prefix_966:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:125 (block while_body_10, TLOAD): register r264 is uninitialized\n"
.L__s3_failure_prefix_967:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:125 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_967:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_968:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:120 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_969:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:120 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_969:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_970:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:120 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_971:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:120 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_972:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:120 (block while_body_10, TSLOAD): register r265 is uninitialized\n"
.L__s3_failure_prefix_973:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:118 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_974:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:118 (block while_body_10, TNDIFF): register r263 is uninitialized\n"
.L__s3_failure_prefix_975:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:118 (block while_body_10, TNDIFF): register r266 is uninitialized\n"
.L__s3_failure_prefix_976:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:90 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_977:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:90 (block while_body_10, TMUL): register r260 is uninitialized\n"
.L__s3_failure_prefix_978:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:90 (block while_body_10, TMUL): register r267 is uninitialized\n"
.L__s3_failure_prefix_979:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:81 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_980:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:81 (block while_body_10, TNDIFF): register r258 is uninitialized\n"
.L__s3_failure_prefix_981:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:81 (block while_body_10, TNDIFF): register r268 is uninitialized\n"
.L__s3_failure_prefix_982:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:53 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_983:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:53 (block while_body_10, TMUL): register r255 is uninitialized\n"
.L__s3_failure_prefix_984:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:53 (block while_body_10, TMUL): register r269 is uninitialized\n"
.L__s3_failure_prefix_985:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:37 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_986:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:37 (block while_body_10, TADD): register r253 is uninitialized\n"
.L__s3_failure_prefix_987:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:37 (block while_body_10, TADD): register r270 is uninitialized\n"
.L__s3_failure_prefix_988:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_989:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 60:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_990:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:13 (block while_body_10, TSTORE): register r272 is uninitialized\n"
.L__s3_failure_prefix_991:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 60:13 (block while_body_10, TSTORE): register r271 is uninitialized\n"
.L__s3_failure_prefix_992:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 60:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_992:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_993:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:29 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_994:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:29 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_995:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 61:29 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_995:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_996:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:29 (block while_body_10, TLOAD): register r273 is uninitialized\n"
.L__s3_failure_prefix_997:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:29 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_997:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_998:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:45 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_999:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:45 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1000:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 61:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1000:
    .ascii " is uninitialized in m19\n"
.L__s3_failure_prefix_1001:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:45 (block while_body_10, TLOAD): register r275 is uninitialized\n"
.L__s3_failure_prefix_1002:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1002:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1003:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:67 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1004:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:67 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1005:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 61:67 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1005:
    .ascii " is uninitialized in m36\n"
.L__s3_failure_prefix_1006:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:67 (block while_body_10, TLOAD): register r277 is uninitialized\n"
.L__s3_failure_prefix_1007:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:67 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1007:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1008:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:62 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1009:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:62 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1009:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1010:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:62 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1011:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:62 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1012:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:62 (block while_body_10, TSLOAD): register r278 is uninitialized\n"
.L__s3_failure_prefix_1013:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:92 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1014:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:92 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1015:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 61:92 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1015:
    .ascii " is uninitialized in m31\n"
.L__s3_failure_prefix_1016:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:92 (block while_body_10, TLOAD): register r280 is uninitialized\n"
.L__s3_failure_prefix_1017:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:92 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1017:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1018:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:107 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1019:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:107 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1020:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 61:107 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1020:
    .ascii " is uninitialized in m36\n"
.L__s3_failure_prefix_1021:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:107 (block while_body_10, TLOAD): register r282 is uninitialized\n"
.L__s3_failure_prefix_1022:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:107 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1022:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1023:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:102 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1024:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:102 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1024:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1025:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:102 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1026:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:102 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1027:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:102 (block while_body_10, TSLOAD): register r283 is uninitialized\n"
.L__s3_failure_prefix_1028:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:137 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1029:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:137 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1030:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 61:137 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1030:
    .ascii " is uninitialized in m37\n"
.L__s3_failure_prefix_1031:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:137 (block while_body_10, TLOAD): register r285 is uninitialized\n"
.L__s3_failure_prefix_1032:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:137 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1032:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1033:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:132 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1034:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:132 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1034:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1035:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:132 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1036:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:132 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1037:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:132 (block while_body_10, TSLOAD): register r286 is uninitialized\n"
.L__s3_failure_prefix_1038:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:130 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1039:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:130 (block while_body_10, TNDIFF): register r284 is uninitialized\n"
.L__s3_failure_prefix_1040:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:130 (block while_body_10, TNDIFF): register r287 is uninitialized\n"
.L__s3_failure_prefix_1041:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:99 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1042:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:99 (block while_body_10, TMUL): register r281 is uninitialized\n"
.L__s3_failure_prefix_1043:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:99 (block while_body_10, TMUL): register r288 is uninitialized\n"
.L__s3_failure_prefix_1044:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:90 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1045:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:90 (block while_body_10, TNDIFF): register r279 is uninitialized\n"
.L__s3_failure_prefix_1046:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:90 (block while_body_10, TNDIFF): register r289 is uninitialized\n"
.L__s3_failure_prefix_1047:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:59 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1048:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:59 (block while_body_10, TMUL): register r276 is uninitialized\n"
.L__s3_failure_prefix_1049:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:59 (block while_body_10, TMUL): register r290 is uninitialized\n"
.L__s3_failure_prefix_1050:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:43 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1051:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:43 (block while_body_10, TADD): register r274 is uninitialized\n"
.L__s3_failure_prefix_1052:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:43 (block while_body_10, TADD): register r291 is uninitialized\n"
.L__s3_failure_prefix_1053:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1054:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 61:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1055:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:13 (block while_body_10, TSTORE): register r293 is uninitialized\n"
.L__s3_failure_prefix_1056:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 61:13 (block while_body_10, TSTORE): register r292 is uninitialized\n"
.L__s3_failure_prefix_1057:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 61:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_1057:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1058:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:26 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1059:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:26 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1060:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 62:26 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1060:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_1061:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:26 (block while_body_10, TLOAD): register r294 is uninitialized\n"
.L__s3_failure_prefix_1062:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:26 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1062:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1063:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:39 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1064:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:39 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1065:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 62:39 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1065:
    .ascii " is uninitialized in m19\n"
.L__s3_failure_prefix_1066:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:39 (block while_body_10, TLOAD): register r296 is uninitialized\n"
.L__s3_failure_prefix_1067:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:39 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1067:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1068:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:61 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1069:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:61 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1070:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 62:61 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1070:
    .ascii " is uninitialized in m38\n"
.L__s3_failure_prefix_1071:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:61 (block while_body_10, TLOAD): register r298 is uninitialized\n"
.L__s3_failure_prefix_1072:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:61 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1072:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1073:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:56 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1074:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:56 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1074:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1075:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:56 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1076:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:56 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1077:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:56 (block while_body_10, TSLOAD): register r299 is uninitialized\n"
.L__s3_failure_prefix_1078:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:83 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1079:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:83 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1080:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 62:83 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1080:
    .ascii " is uninitialized in m31\n"
.L__s3_failure_prefix_1081:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:83 (block while_body_10, TLOAD): register r301 is uninitialized\n"
.L__s3_failure_prefix_1082:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:83 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1082:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1083:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:98 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1084:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:98 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1085:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 62:98 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1085:
    .ascii " is uninitialized in m38\n"
.L__s3_failure_prefix_1086:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:98 (block while_body_10, TLOAD): register r303 is uninitialized\n"
.L__s3_failure_prefix_1087:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:98 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1087:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1088:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:93 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1089:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:93 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1089:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1090:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:93 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1091:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:93 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1092:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:93 (block while_body_10, TSLOAD): register r304 is uninitialized\n"
.L__s3_failure_prefix_1093:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:125 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1094:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:125 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1095:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 62:125 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1095:
    .ascii " is uninitialized in m39\n"
.L__s3_failure_prefix_1096:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:125 (block while_body_10, TLOAD): register r306 is uninitialized\n"
.L__s3_failure_prefix_1097:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:125 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1097:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1098:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:120 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1099:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:120 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1099:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1100:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:120 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1101:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:120 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1102:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:120 (block while_body_10, TSLOAD): register r307 is uninitialized\n"
.L__s3_failure_prefix_1103:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:118 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1104:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:118 (block while_body_10, TNDIFF): register r305 is uninitialized\n"
.L__s3_failure_prefix_1105:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:118 (block while_body_10, TNDIFF): register r308 is uninitialized\n"
.L__s3_failure_prefix_1106:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:90 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1107:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:90 (block while_body_10, TMUL): register r302 is uninitialized\n"
.L__s3_failure_prefix_1108:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:90 (block while_body_10, TMUL): register r309 is uninitialized\n"
.L__s3_failure_prefix_1109:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:81 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1110:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:81 (block while_body_10, TNDIFF): register r300 is uninitialized\n"
.L__s3_failure_prefix_1111:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:81 (block while_body_10, TNDIFF): register r310 is uninitialized\n"
.L__s3_failure_prefix_1112:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:53 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1113:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:53 (block while_body_10, TMUL): register r297 is uninitialized\n"
.L__s3_failure_prefix_1114:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:53 (block while_body_10, TMUL): register r311 is uninitialized\n"
.L__s3_failure_prefix_1115:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:37 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1116:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:37 (block while_body_10, TADD): register r295 is uninitialized\n"
.L__s3_failure_prefix_1117:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:37 (block while_body_10, TADD): register r312 is uninitialized\n"
.L__s3_failure_prefix_1118:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1119:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 62:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1120:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:13 (block while_body_10, TSTORE): register r314 is uninitialized\n"
.L__s3_failure_prefix_1121:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 62:13 (block while_body_10, TSTORE): register r313 is uninitialized\n"
.L__s3_failure_prefix_1122:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 62:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_1122:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1123:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:29 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1124:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:29 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1125:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 63:29 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1125:
    .ascii " is uninitialized in m14\n"
.L__s3_failure_prefix_1126:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:29 (block while_body_10, TLOAD): register r315 is uninitialized\n"
.L__s3_failure_prefix_1127:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:29 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1127:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1128:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:45 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1129:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:45 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1130:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 63:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1130:
    .ascii " is uninitialized in m19\n"
.L__s3_failure_prefix_1131:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:45 (block while_body_10, TLOAD): register r317 is uninitialized\n"
.L__s3_failure_prefix_1132:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:45 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1132:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1133:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:67 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1134:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:67 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1135:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 63:67 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1135:
    .ascii " is uninitialized in m40\n"
.L__s3_failure_prefix_1136:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:67 (block while_body_10, TLOAD): register r319 is uninitialized\n"
.L__s3_failure_prefix_1137:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:67 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1137:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1138:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:62 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1139:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:62 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1139:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1140:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:62 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1141:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:62 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1142:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:62 (block while_body_10, TSLOAD): register r320 is uninitialized\n"
.L__s3_failure_prefix_1143:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:92 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1144:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:92 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1145:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 63:92 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1145:
    .ascii " is uninitialized in m31\n"
.L__s3_failure_prefix_1146:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:92 (block while_body_10, TLOAD): register r322 is uninitialized\n"
.L__s3_failure_prefix_1147:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:92 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1147:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1148:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:107 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1149:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:107 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1150:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 63:107 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1150:
    .ascii " is uninitialized in m40\n"
.L__s3_failure_prefix_1151:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:107 (block while_body_10, TLOAD): register r324 is uninitialized\n"
.L__s3_failure_prefix_1152:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:107 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1152:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1153:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:102 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1154:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:102 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1154:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1155:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:102 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1156:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:102 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1157:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:102 (block while_body_10, TSLOAD): register r325 is uninitialized\n"
.L__s3_failure_prefix_1158:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:137 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1159:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:137 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1160:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 63:137 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1160:
    .ascii " is uninitialized in m41\n"
.L__s3_failure_prefix_1161:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:137 (block while_body_10, TLOAD): register r327 is uninitialized\n"
.L__s3_failure_prefix_1162:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:137 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1162:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1163:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:132 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1164:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:132 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_1164:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_1165:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:132 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_1166:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:132 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_1167:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:132 (block while_body_10, TSLOAD): register r328 is uninitialized\n"
.L__s3_failure_prefix_1168:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:130 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1169:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:130 (block while_body_10, TNDIFF): register r326 is uninitialized\n"
.L__s3_failure_prefix_1170:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:130 (block while_body_10, TNDIFF): register r329 is uninitialized\n"
.L__s3_failure_prefix_1171:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:99 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1172:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:99 (block while_body_10, TMUL): register r323 is uninitialized\n"
.L__s3_failure_prefix_1173:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:99 (block while_body_10, TMUL): register r330 is uninitialized\n"
.L__s3_failure_prefix_1174:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:90 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1175:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:90 (block while_body_10, TNDIFF): register r321 is uninitialized\n"
.L__s3_failure_prefix_1176:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:90 (block while_body_10, TNDIFF): register r331 is uninitialized\n"
.L__s3_failure_prefix_1177:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:59 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1178:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:59 (block while_body_10, TMUL): register r318 is uninitialized\n"
.L__s3_failure_prefix_1179:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:59 (block while_body_10, TMUL): register r332 is uninitialized\n"
.L__s3_failure_prefix_1180:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:43 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1181:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:43 (block while_body_10, TADD): register r316 is uninitialized\n"
.L__s3_failure_prefix_1182:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:43 (block while_body_10, TADD): register r333 is uninitialized\n"
.L__s3_failure_prefix_1183:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1184:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 63:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1185:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:13 (block while_body_10, TSTORE): register r335 is uninitialized\n"
.L__s3_failure_prefix_1186:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 63:13 (block while_body_10, TSTORE): register r334 is uninitialized\n"
.L__s3_failure_prefix_1187:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 63:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_1187:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1188:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 64:24 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1189:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 64:24 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1190:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 64:24 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1190:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_1191:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 64:24 (block while_body_10, TLOAD): register r336 is uninitialized\n"
.L__s3_failure_prefix_1192:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 64:24 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_1192:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1193:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 64:35 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1194:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 64:33 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1195:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 64:33 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_1196:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 64:33 (block while_body_10, TADD): register r337 is uninitialized\n"
.L__s3_failure_prefix_1197:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 64:33 (block while_body_10, TADD): register r338 is uninitialized\n"
.L__s3_failure_prefix_1198:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 64:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1199:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 64:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1200:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 64:13 (block while_body_10, TSTORE): register r340 is uninitialized\n"
.L__s3_failure_prefix_1201:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 64:13 (block while_body_10, TSTORE): register r339 is uninitialized\n"
.L__s3_failure_prefix_1202:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 64:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_1202:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1203:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:9 (block while_body_10, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1204:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:9 (block while_exit_0_11, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1205:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:9 (block while_exit_1_12, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1206:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:20 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1207:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:20 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1208:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 65:20 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1208:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_1209:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:20 (block while_exit_13, TLOAD): register r341 is uninitialized\n"
.L__s3_failure_prefix_1210:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 65:20 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1210:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1211:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:31 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1212:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:31 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1213:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 65:31 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1213:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_1214:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:31 (block while_exit_13, TLOAD): register r343 is uninitialized\n"
.L__s3_failure_prefix_1215:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 65:31 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1215:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1216:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:29 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1217:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:29 (block while_exit_13, TADD): register r342 is uninitialized\n"
.L__s3_failure_prefix_1218:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:29 (block while_exit_13, TADD): register r344 is uninitialized\n"
.L__s3_failure_prefix_1219:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:42 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1220:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:48 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1221:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:48 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1222:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 65:48 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1222:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_1223:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:48 (block while_exit_13, TLOAD): register r347 is uninitialized\n"
.L__s3_failure_prefix_1224:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 65:48 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1224:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1225:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:46 (block while_exit_13, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1226:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:46 (block while_exit_13, TMUL): register r346 is uninitialized\n"
.L__s3_failure_prefix_1227:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:46 (block while_exit_13, TMUL): register r348 is uninitialized\n"
.L__s3_failure_prefix_1228:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:40 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1229:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:40 (block while_exit_13, TADD): register r345 is uninitialized\n"
.L__s3_failure_prefix_1230:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:40 (block while_exit_13, TADD): register r349 is uninitialized\n"
.L__s3_failure_prefix_1231:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:61 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1232:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:67 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1233:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:67 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1234:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 65:67 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1234:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_1235:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:67 (block while_exit_13, TLOAD): register r352 is uninitialized\n"
.L__s3_failure_prefix_1236:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 65:67 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1236:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1237:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:65 (block while_exit_13, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1238:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:65 (block while_exit_13, TMUL): register r351 is uninitialized\n"
.L__s3_failure_prefix_1239:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:65 (block while_exit_13, TMUL): register r353 is uninitialized\n"
.L__s3_failure_prefix_1240:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:59 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1241:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:59 (block while_exit_13, TADD): register r350 is uninitialized\n"
.L__s3_failure_prefix_1242:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:59 (block while_exit_13, TADD): register r354 is uninitialized\n"
.L__s3_failure_prefix_1243:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:83 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1244:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:89 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1245:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:89 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1246:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 65:89 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1246:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_1247:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:89 (block while_exit_13, TLOAD): register r357 is uninitialized\n"
.L__s3_failure_prefix_1248:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 65:89 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1248:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1249:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:87 (block while_exit_13, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1250:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:87 (block while_exit_13, TMUL): register r356 is uninitialized\n"
.L__s3_failure_prefix_1251:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:87 (block while_exit_13, TMUL): register r358 is uninitialized\n"
.L__s3_failure_prefix_1252:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:81 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1253:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:81 (block while_exit_13, TADD): register r355 is uninitialized\n"
.L__s3_failure_prefix_1254:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:81 (block while_exit_13, TADD): register r359 is uninitialized\n"
.L__s3_failure_prefix_1255:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:102 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1256:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:109 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1257:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:109 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1258:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 65:109 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1258:
    .ascii " is uninitialized in m14\n"
.L__s3_failure_prefix_1259:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:109 (block while_exit_13, TLOAD): register r362 is uninitialized\n"
.L__s3_failure_prefix_1260:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 65:109 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1260:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1261:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:107 (block while_exit_13, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1262:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:107 (block while_exit_13, TMUL): register r361 is uninitialized\n"
.L__s3_failure_prefix_1263:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:107 (block while_exit_13, TMUL): register r363 is uninitialized\n"
.L__s3_failure_prefix_1264:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:100 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1265:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:100 (block while_exit_13, TADD): register r360 is uninitialized\n"
.L__s3_failure_prefix_1266:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:100 (block while_exit_13, TADD): register r364 is uninitialized\n"
.L__s3_failure_prefix_1267:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:9 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1268:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 65:9 (block while_exit_13, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1269:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:9 (block while_exit_13, TSTORE): register r366 is uninitialized\n"
.L__s3_failure_prefix_1270:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 65:9 (block while_exit_13, TSTORE): register r365 is uninitialized\n"
.L__s3_failure_prefix_1271:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 65:9 (block while_exit_13, TSTORE): index "
.L__s3_failure_suffix_1271:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1272:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 66:18 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1273:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 66:18 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1274:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 66:18 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1274:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_1275:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 66:18 (block while_exit_13, TLOAD): register r367 is uninitialized\n"
.L__s3_failure_prefix_1276:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 66:18 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_1276:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1277:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 66:27 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1278:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 66:25 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1279:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 66:25 (block while_exit_13, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_1280:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 66:25 (block while_exit_13, TADD): register r368 is uninitialized\n"
.L__s3_failure_prefix_1281:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 66:25 (block while_exit_13, TADD): register r369 is uninitialized\n"
.L__s3_failure_prefix_1282:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 66:9 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1283:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 66:9 (block while_exit_13, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1284:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 66:9 (block while_exit_13, TSTORE): register r371 is uninitialized\n"
.L__s3_failure_prefix_1285:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 66:9 (block while_exit_13, TSTORE): register r370 is uninitialized\n"
.L__s3_failure_prefix_1286:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 66:9 (block while_exit_13, TSTORE): index "
.L__s3_failure_suffix_1286:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1287:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 20:5 (block while_exit_13, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1288:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1289:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1290:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1291:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TSTORE): register r64 is uninitialized\n"
.L__s3_failure_prefix_1292:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TSTORE): register r65 is uninitialized\n"
.L__s3_failure_prefix_1293:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TSTORE): index "
.L__s3_failure_suffix_1293:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1294:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TSTORE): trit result "
.L__s3_failure_suffix_1294:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_1295:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_neg_14, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1296:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1297:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1298:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1299:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TSTORE): register r66 is uninitialized\n"
.L__s3_failure_prefix_1300:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TSTORE): register r67 is uninitialized\n"
.L__s3_failure_prefix_1301:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TSTORE): index "
.L__s3_failure_suffix_1301:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1302:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TSTORE): trit result "
.L__s3_failure_suffix_1302:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_1303:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_zero_15, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1304:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1305:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1306:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1307:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TSTORE): register r68 is uninitialized\n"
.L__s3_failure_prefix_1308:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TSTORE): register r69 is uninitialized\n"
.L__s3_failure_prefix_1309:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TSTORE): index "
.L__s3_failure_suffix_1309:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1310:
    .ascii "runtime error [overflow] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TSTORE): trit result "
.L__s3_failure_suffix_1310:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_1311:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_pos_16, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1312:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_cont_17, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1313:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:24 (block rel_cont_17, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1314:
    .ascii "runtime error [uninitialized memory] in function 'xs_lookup_batch'\nat source 32:24 (block rel_cont_17, TLOAD): index "
.L__s3_failure_suffix_1314:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_1315:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:24 (block rel_cont_17, TLOAD): register r70 is uninitialized\n"
.L__s3_failure_prefix_1316:
    .ascii "runtime error [bounds] in function 'xs_lookup_batch'\nat source 32:24 (block rel_cont_17, TLOAD): index "
.L__s3_failure_suffix_1316:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_1317:
    .ascii "runtime error [instruction limit] in function 'xs_lookup_batch'\nat source 32:9 (block rel_cont_17, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1318:
    .ascii "runtime error [invalid trit state] in function 'xs_lookup_batch'\nat source 32:9 (block rel_cont_17, TBR3): value "
.L__s3_failure_suffix_1318:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_1319:
    .ascii "runtime error [uninitialized register] in function 'xs_lookup_batch'\nat source 32:9 (block rel_cont_17, TBR3): register r71 is uninitialized\n"
.L__s3_failure_prefix_1320:
    .ascii "runtime error [frame limit] in function 'main'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_1320:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_1321:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 70:12 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_1322:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 70:5 (block entry, TRET): instruction limit 10000000000 exceeded\n"

.section .text
.globl _start
.type _start, @function
_start:
    and rsp, -16
    call s3_main
    mov r12, rax
    mov eax, 1
    mov edi, 1
    lea rsi, [rip + .L__s3_result_prefix]
    mov edx, 18
    syscall
    mov rdi, r12
    call __s3_print_i64
    mov eax, 60
    xor edi, edi
    syscall
    ud2
.size _start, .-_start

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
    mov eax,-1
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
    mov eax,-1
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
    mov eax,-1
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
