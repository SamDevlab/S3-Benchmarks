.intel_syntax noprefix
# Generated deterministically by the S3 Linux x86-64 backend.
.section .text
.globl identity_f64
.type identity_f64, @function
identity_f64:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_0
    push rbp
    mov rbp, rsp
    sub rsp, 32
    movq rax, xmm0
    mov qword ptr [rbp - 8], rax
    mov rdi, qword ptr [rbp - 8]
    mov byte ptr [rbp - 9], 0
    mov byte ptr [rbp - 9], 1
    jmp .L_s3_f12_identity_f64_b5_entry
.L_s3_f12_identity_f64_b5_entry:
    mov rax, rdi
    movq xmm0, rax
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.size identity_f64, .-identity_f64

.globl rmsd
.type rmsd, @function
rmsd:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_2
    push rbp
    mov rbp, rsp
    sub rsp, 880
    mov qword ptr [rbp - 816], rbx
    mov qword ptr [rbp - 824], r12
    mov qword ptr [rbp - 832], r13
    mov qword ptr [rbp - 840], r14
    mov qword ptr [rbp - 848], r15
    mov qword ptr [rbp - 8], rdi
    mov qword ptr [rbp - 16], rsi
    mov qword ptr [rbp - 24], rdx
    mov qword ptr [rbp - 32], rcx
    mov qword ptr [rbp - 40], r8
    mov qword ptr [rbp - 48], r9
    mov rbx, qword ptr [rbp - 8]
    mov r12, qword ptr [rbp - 16]
    mov r13, qword ptr [rbp - 24]
    mov r14, qword ptr [rbp - 32]
    mov r15, qword ptr [rbp - 40]
    mov rdi, qword ptr [rbp - 48]
    mov r10, rdi
    mov r11, rcx
    mov byte ptr [rbp - 649], 0
    mov byte ptr [rbp - 650], 0
    mov byte ptr [rbp - 651], 0
    mov byte ptr [rbp - 652], 0
    mov byte ptr [rbp - 653], 0
    mov byte ptr [rbp - 654], 0
    mov byte ptr [rbp - 655], 0
    mov byte ptr [rbp - 656], 0
    mov byte ptr [rbp - 657], 0
    mov byte ptr [rbp - 658], 0
    mov byte ptr [rbp - 659], 0
    mov byte ptr [rbp - 660], 0
    mov byte ptr [rbp - 661], 0
    mov byte ptr [rbp - 662], 0
    mov byte ptr [rbp - 663], 0
    mov byte ptr [rbp - 664], 0
    mov byte ptr [rbp - 665], 0
    mov byte ptr [rbp - 666], 0
    mov byte ptr [rbp - 667], 0
    mov byte ptr [rbp - 668], 0
    mov byte ptr [rbp - 669], 0
    mov byte ptr [rbp - 670], 0
    mov byte ptr [rbp - 671], 0
    mov byte ptr [rbp - 672], 0
    mov byte ptr [rbp - 673], 0
    mov byte ptr [rbp - 674], 0
    mov byte ptr [rbp - 675], 0
    mov byte ptr [rbp - 676], 0
    mov byte ptr [rbp - 677], 0
    mov byte ptr [rbp - 678], 0
    mov byte ptr [rbp - 679], 0
    mov byte ptr [rbp - 680], 0
    mov byte ptr [rbp - 681], 0
    mov byte ptr [rbp - 682], 0
    mov byte ptr [rbp - 683], 0
    mov byte ptr [rbp - 684], 0
    mov byte ptr [rbp - 685], 0
    mov byte ptr [rbp - 686], 0
    mov byte ptr [rbp - 687], 0
    mov byte ptr [rbp - 688], 0
    mov byte ptr [rbp - 689], 0
    mov byte ptr [rbp - 690], 0
    mov byte ptr [rbp - 691], 0
    mov byte ptr [rbp - 692], 0
    mov byte ptr [rbp - 693], 0
    mov byte ptr [rbp - 694], 0
    mov byte ptr [rbp - 695], 0
    mov byte ptr [rbp - 696], 0
    mov byte ptr [rbp - 697], 0
    mov byte ptr [rbp - 698], 0
    mov byte ptr [rbp - 699], 0
    mov byte ptr [rbp - 700], 0
    mov byte ptr [rbp - 701], 0
    mov byte ptr [rbp - 702], 0
    mov byte ptr [rbp - 703], 0
    mov byte ptr [rbp - 704], 0
    mov byte ptr [rbp - 705], 0
    mov byte ptr [rbp - 706], 0
    mov byte ptr [rbp - 707], 0
    mov byte ptr [rbp - 708], 0
    mov byte ptr [rbp - 709], 0
    mov byte ptr [rbp - 710], 0
    mov byte ptr [rbp - 711], 0
    mov byte ptr [rbp - 712], 0
    mov byte ptr [rbp - 713], 0
    mov byte ptr [rbp - 714], 0
    mov byte ptr [rbp - 715], 0
    mov byte ptr [rbp - 716], 0
    mov byte ptr [rbp - 717], 0
    mov byte ptr [rbp - 718], 0
    mov byte ptr [rbp - 719], 0
    mov byte ptr [rbp - 720], 0
    mov byte ptr [rbp - 721], 0
    mov byte ptr [rbp - 722], 0
    mov byte ptr [rbp - 723], 0
    mov byte ptr [rbp - 724], 0
    mov byte ptr [rbp - 725], 0
    mov byte ptr [rbp - 726], 0
    mov byte ptr [rbp - 727], 0
    mov byte ptr [rbp - 728], 0
    mov byte ptr [rbp - 729], 0
    lea rdi, [rbp - 801]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 802]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 803]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 804]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 805]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 806]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 807]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 808]
    mov ecx, 1
    xor eax, eax
    rep stosb
    mov rdi, r10
    mov rcx, r11
    mov byte ptr [rbp - 649], 1
    mov byte ptr [rbp - 650], 1
    mov byte ptr [rbp - 651], 1
    mov byte ptr [rbp - 652], 1
    mov byte ptr [rbp - 653], 1
    mov byte ptr [rbp - 654], 1
    jmp .L_s3_f4_rmsd_b5_entry
.L_s3_f4_rmsd_b5_entry:
    mov rsi, 0
    mov byte ptr [rbp - 655], 1
    mov rdx, 0
    mov byte ptr [rbp - 656], 1
    cmp byte ptr [rbp - 656], 0
    je .L__s3_failure_site_6
    mov rax, rdx
    cmp byte ptr [rbp - 655], 0
    je .L__s3_failure_site_7
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_8
    mov qword ptr [rbp + rax*8 - 744], r10
    mov byte ptr [rbp + rax - 801], 1
    movabs rax, 0
    mov rsi, rax
    mov byte ptr [rbp - 657], 1
    mov rdx, 0
    mov byte ptr [rbp - 658], 1
    cmp byte ptr [rbp - 658], 0
    je .L__s3_failure_site_12
    mov rax, rdx
    cmp byte ptr [rbp - 657], 0
    je .L__s3_failure_site_13
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_14
    mov qword ptr [rbp + rax*8 - 752], r10
    mov byte ptr [rbp + rax - 802], 1
    jmp .L_s3_f4_rmsd_b17_while_condition_0
.L_s3_f4_rmsd_b17_while_condition_0:
    mov rsi, 0
    mov byte ptr [rbp - 659], 1
    cmp byte ptr [rbp - 659], 0
    je .L__s3_failure_site_19
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_20
    cmp byte ptr [rbp + r10 - 801], 0
    je .L__s3_failure_site_18
    mov rax, qword ptr [rbp + r10*8 - 744]
    mov rsi, rax
    mov byte ptr [rbp - 660], 1
    cmp byte ptr [rbp - 660], 0
    je .L__s3_failure_site_22
    mov rax, rsi
    cmp byte ptr [rbp - 653], 0
    je .L__s3_failure_site_23
    mov r10, r15
    cmp rax, r10
    jl .L_s3_f4_rmsd_b9_rel_neg_5
    jg .L_s3_f4_rmsd_b9_rel_pos_7
    jmp .L_s3_f4_rmsd_b10_rel_zero_6
.L_s3_f4_rmsd_b12_while_body_1:
    mov rsi, 0
    mov byte ptr [rbp - 670], 1
    mov rdx, 0
    mov byte ptr [rbp - 671], 1
    cmp byte ptr [rbp - 671], 0
    je .L__s3_failure_site_28
    mov rax, rdx
    cmp byte ptr [rbp - 670], 0
    je .L__s3_failure_site_29
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_30
    mov qword ptr [rbp + rax*8 - 768], r10
    mov byte ptr [rbp + rax - 804], 1
    movabs rax, 0
    mov rsi, rax
    mov byte ptr [rbp - 672], 1
    mov rdx, 0
    mov byte ptr [rbp - 673], 1
    cmp byte ptr [rbp - 673], 0
    je .L__s3_failure_site_34
    mov rax, rdx
    cmp byte ptr [rbp - 672], 0
    je .L__s3_failure_site_35
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_36
    mov qword ptr [rbp + rax*8 - 776], r10
    mov byte ptr [rbp + rax - 805], 1
    jmp .L_s3_f4_rmsd_b17_while_condition_9
.L_s3_f4_rmsd_b14_while_exit_0_2:
    jmp .L_s3_f4_rmsd_b12_while_exit_4
.L_s3_f4_rmsd_b14_while_exit_1_3:
    jmp .L_s3_f4_rmsd_b12_while_exit_4
.L_s3_f4_rmsd_b12_while_exit_4:
    mov rdi, 0
    mov byte ptr [rbp - 728], 1
    cmp byte ptr [rbp - 728], 0
    je .L__s3_failure_site_43
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_44
    cmp byte ptr [rbp + r10 - 802], 0
    je .L__s3_failure_site_42
    mov rax, qword ptr [rbp + r10*8 - 752]
    mov rdi, rax
    mov byte ptr [rbp - 729], 1
    cmp byte ptr [rbp - 729], 0
    je .L__s3_failure_site_46
    mov rax, rdi
    movq xmm0, rax
    mov rbx, qword ptr [rbp - 816]
    mov r12, qword ptr [rbp - 824]
    mov r13, qword ptr [rbp - 832]
    mov r14, qword ptr [rbp - 840]
    mov r15, qword ptr [rbp - 848]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f4_rmsd_b9_rel_neg_5:
    mov rsi, 0
    mov byte ptr [rbp - 662], 1
    mov rdx, -1
    mov byte ptr [rbp - 663], 1
    cmp byte ptr [rbp - 662], 0
    je .L__s3_failure_site_50
    mov rax, rsi
    cmp byte ptr [rbp - 663], 0
    je .L__s3_failure_site_51
    mov r10, rdx
    cmp rax, 1
    jae .L__s3_failure_site_52
    cmp r10, -1
    jl .L__s3_failure_site_53
    cmp r10, 1
    jg .L__s3_failure_site_53
    mov byte ptr [rbp + rax - 753], r10b
    mov byte ptr [rbp + rax - 803], 1
    jmp .L_s3_f4_rmsd_b10_rel_cont_8
.L_s3_f4_rmsd_b10_rel_zero_6:
    mov rsi, 0
    mov byte ptr [rbp - 664], 1
    mov rdx, 0
    mov byte ptr [rbp - 665], 1
    cmp byte ptr [rbp - 664], 0
    je .L__s3_failure_site_58
    mov rax, rsi
    cmp byte ptr [rbp - 665], 0
    je .L__s3_failure_site_59
    mov r10, rdx
    cmp rax, 1
    jae .L__s3_failure_site_60
    cmp r10, -1
    jl .L__s3_failure_site_61
    cmp r10, 1
    jg .L__s3_failure_site_61
    mov byte ptr [rbp + rax - 753], r10b
    mov byte ptr [rbp + rax - 803], 1
    jmp .L_s3_f4_rmsd_b10_rel_cont_8
.L_s3_f4_rmsd_b9_rel_pos_7:
    mov rsi, 0
    mov byte ptr [rbp - 666], 1
    mov rdx, 0
    mov byte ptr [rbp - 667], 1
    cmp byte ptr [rbp - 666], 0
    je .L__s3_failure_site_66
    mov rax, rsi
    cmp byte ptr [rbp - 667], 0
    je .L__s3_failure_site_67
    mov r10, rdx
    cmp rax, 1
    jae .L__s3_failure_site_68
    cmp r10, -1
    jl .L__s3_failure_site_69
    cmp r10, 1
    jg .L__s3_failure_site_69
    mov byte ptr [rbp + rax - 753], r10b
    mov byte ptr [rbp + rax - 803], 1
    jmp .L_s3_f4_rmsd_b10_rel_cont_8
.L_s3_f4_rmsd_b10_rel_cont_8:
    mov rsi, 0
    mov byte ptr [rbp - 668], 1
    cmp byte ptr [rbp - 668], 0
    je .L__s3_failure_site_74
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_75
    cmp byte ptr [rbp + r10 - 803], 0
    je .L__s3_failure_site_73
    movsx rax, byte ptr [rbp + r10 - 753]
    mov rsi, rax
    mov byte ptr [rbp - 669], 1
    cmp byte ptr [rbp - 669], 0
    je .L__s3_failure_site_78
    mov rax, rsi
    cmp rax, -1
    je .L_s3_f4_rmsd_b12_while_body_1
    cmp rax, 0
    je .L_s3_f4_rmsd_b14_while_exit_0_2
    cmp rax, 1
    je .L_s3_f4_rmsd_b14_while_exit_1_3
    jmp .L__s3_failure_site_77
.L_s3_f4_rmsd_b17_while_condition_9:
    mov rsi, 0
    mov byte ptr [rbp - 674], 1
    cmp byte ptr [rbp - 674], 0
    je .L__s3_failure_site_82
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_83
    cmp byte ptr [rbp + r10 - 804], 0
    je .L__s3_failure_site_81
    mov rax, qword ptr [rbp + r10*8 - 768]
    mov rsi, rax
    mov byte ptr [rbp - 675], 1
    cmp byte ptr [rbp - 675], 0
    je .L__s3_failure_site_85
    mov rax, rsi
    cmp byte ptr [rbp - 654], 0
    je .L__s3_failure_site_86
    mov r10, rdi
    cmp rax, r10
    jl .L_s3_f4_rmsd_b10_rel_neg_14
    jg .L_s3_f4_rmsd_b10_rel_pos_16
    jmp .L_s3_f4_rmsd_b11_rel_zero_15
.L_s3_f4_rmsd_b13_while_body_10:
    mov rsi, 0
    mov byte ptr [rbp - 685], 1
    cmp byte ptr [rbp - 685], 0
    je .L__s3_failure_site_91
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_92
    cmp byte ptr [rbp + r10 - 801], 0
    je .L__s3_failure_site_90
    mov rax, qword ptr [rbp + r10*8 - 744]
    mov rsi, rax
    mov byte ptr [rbp - 686], 1
    cmp byte ptr [rbp - 686], 0
    je .L__s3_failure_site_95
    mov rax, rsi
    cmp byte ptr [rbp - 654], 0
    je .L__s3_failure_site_96
    mov r10, rdi
    imul rax, r10
    jo .L__s3_failure_site_94
    mov rsi, rax
    mov byte ptr [rbp - 687], 1
    mov rdx, 0
    mov byte ptr [rbp - 688], 1
    cmp byte ptr [rbp - 688], 0
    je .L__s3_failure_site_100
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_101
    cmp byte ptr [rbp + r10 - 804], 0
    je .L__s3_failure_site_99
    mov rax, qword ptr [rbp + r10*8 - 768]
    mov rdx, rax
    mov byte ptr [rbp - 689], 1
    cmp byte ptr [rbp - 687], 0
    je .L__s3_failure_site_104
    mov rax, rsi
    cmp byte ptr [rbp - 689], 0
    je .L__s3_failure_site_105
    mov r10, rdx
    add rax, r10
    jo .L__s3_failure_site_103
    mov rsi, rax
    mov byte ptr [rbp - 690], 1
    mov rdx, 0
    mov byte ptr [rbp - 691], 1
    cmp byte ptr [rbp - 691], 0
    je .L__s3_failure_site_108
    mov rax, rdx
    cmp byte ptr [rbp - 690], 0
    je .L__s3_failure_site_109
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_110
    mov qword ptr [rbp + rax*8 - 792], r10
    mov byte ptr [rbp + rax - 807], 1
    mov rsi, 0
    mov byte ptr [rbp - 692], 1
    cmp byte ptr [rbp - 692], 0
    je .L__s3_failure_site_114
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_115
    cmp byte ptr [rbp + r10 - 807], 0
    je .L__s3_failure_site_113
    mov rax, qword ptr [rbp + r10*8 - 792]
    mov rsi, rax
    mov byte ptr [rbp - 693], 1
    cmp byte ptr [rbp - 649], 0
    je .L__s3_failure_site_118
    mov r10, rbx
    cmp byte ptr [rbp - 650], 0
    je .L__s3_failure_site_119
    mov r11, r12
    cmp byte ptr [rbp - 693], 0
    je .L__s3_failure_site_120
    mov rax, rsi
    cmp rax, r11
    jae .L__s3_failure_site_117
    mov r11, qword ptr [r10 + rax * 8]
    mov rsi, r11
    mov byte ptr [rbp - 694], 1
    mov rdx, 0
    mov byte ptr [rbp - 695], 1
    cmp byte ptr [rbp - 695], 0
    je .L__s3_failure_site_124
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_125
    cmp byte ptr [rbp + r10 - 807], 0
    je .L__s3_failure_site_123
    mov rax, qword ptr [rbp + r10*8 - 792]
    mov rdx, rax
    mov byte ptr [rbp - 696], 1
    cmp byte ptr [rbp - 651], 0
    je .L__s3_failure_site_128
    mov r10, r13
    cmp byte ptr [rbp - 652], 0
    je .L__s3_failure_site_129
    mov r11, r14
    cmp byte ptr [rbp - 696], 0
    je .L__s3_failure_site_130
    mov rax, rdx
    cmp rax, r11
    jae .L__s3_failure_site_127
    mov r11, qword ptr [r10 + rax * 8]
    mov rdx, r11
    mov byte ptr [rbp - 697], 1
    cmp byte ptr [rbp - 694], 0
    je .L__s3_failure_site_132
    mov rax, rsi
    cmp byte ptr [rbp - 697], 0
    je .L__s3_failure_site_133
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 698], 1
    mov rdx, 0
    mov byte ptr [rbp - 699], 1
    cmp byte ptr [rbp - 699], 0
    je .L__s3_failure_site_136
    mov rax, rdx
    cmp byte ptr [rbp - 698], 0
    je .L__s3_failure_site_137
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_138
    mov qword ptr [rbp + rax*8 - 800], r10
    mov byte ptr [rbp + rax - 808], 1
    mov rsi, 0
    mov byte ptr [rbp - 700], 1
    cmp byte ptr [rbp - 700], 0
    je .L__s3_failure_site_142
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_143
    cmp byte ptr [rbp + r10 - 805], 0
    je .L__s3_failure_site_141
    mov rax, qword ptr [rbp + r10*8 - 776]
    mov rsi, rax
    mov byte ptr [rbp - 701], 1
    mov rdx, 0
    mov byte ptr [rbp - 702], 1
    cmp byte ptr [rbp - 702], 0
    je .L__s3_failure_site_147
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_148
    cmp byte ptr [rbp + r10 - 808], 0
    je .L__s3_failure_site_146
    mov rax, qword ptr [rbp + r10*8 - 800]
    mov rdx, rax
    mov byte ptr [rbp - 703], 1
    mov rcx, 0
    mov byte ptr [rbp - 704], 1
    cmp byte ptr [rbp - 704], 0
    je .L__s3_failure_site_152
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_153
    cmp byte ptr [rbp + r10 - 808], 0
    je .L__s3_failure_site_151
    mov rax, qword ptr [rbp + r10*8 - 800]
    mov rcx, rax
    mov byte ptr [rbp - 705], 1
    cmp byte ptr [rbp - 703], 0
    je .L__s3_failure_site_155
    mov rax, rdx
    cmp byte ptr [rbp - 705], 0
    je .L__s3_failure_site_156
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 706], 1
    cmp byte ptr [rbp - 701], 0
    je .L__s3_failure_site_158
    mov rax, rsi
    cmp byte ptr [rbp - 706], 0
    je .L__s3_failure_site_159
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 707], 1
    mov rdx, 0
    mov byte ptr [rbp - 708], 1
    cmp byte ptr [rbp - 708], 0
    je .L__s3_failure_site_162
    mov rax, rdx
    cmp byte ptr [rbp - 707], 0
    je .L__s3_failure_site_163
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_164
    mov qword ptr [rbp + rax*8 - 776], r10
    mov byte ptr [rbp + rax - 805], 1
    mov rsi, 0
    mov byte ptr [rbp - 709], 1
    cmp byte ptr [rbp - 709], 0
    je .L__s3_failure_site_168
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_169
    cmp byte ptr [rbp + r10 - 804], 0
    je .L__s3_failure_site_167
    mov rax, qword ptr [rbp + r10*8 - 768]
    mov rsi, rax
    mov byte ptr [rbp - 710], 1
    mov rdx, 1
    mov byte ptr [rbp - 711], 1
    cmp byte ptr [rbp - 710], 0
    je .L__s3_failure_site_173
    mov rax, rsi
    cmp byte ptr [rbp - 711], 0
    je .L__s3_failure_site_174
    mov r10, rdx
    add rax, r10
    jo .L__s3_failure_site_172
    mov rsi, rax
    mov byte ptr [rbp - 712], 1
    mov rdx, 0
    mov byte ptr [rbp - 713], 1
    cmp byte ptr [rbp - 713], 0
    je .L__s3_failure_site_177
    mov rax, rdx
    cmp byte ptr [rbp - 712], 0
    je .L__s3_failure_site_178
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_179
    mov qword ptr [rbp + rax*8 - 768], r10
    mov byte ptr [rbp + rax - 804], 1
    jmp .L_s3_f4_rmsd_b17_while_condition_9
.L_s3_f4_rmsd_b15_while_exit_0_11:
    jmp .L_s3_f4_rmsd_b13_while_exit_13
.L_s3_f4_rmsd_b15_while_exit_1_12:
    jmp .L_s3_f4_rmsd_b13_while_exit_13
.L_s3_f4_rmsd_b13_while_exit_13:
    mov rsi, 0
    mov byte ptr [rbp - 714], 1
    cmp byte ptr [rbp - 714], 0
    je .L__s3_failure_site_186
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_187
    cmp byte ptr [rbp + r10 - 802], 0
    je .L__s3_failure_site_185
    mov rax, qword ptr [rbp + r10*8 - 752]
    mov rsi, rax
    mov byte ptr [rbp - 715], 1
    mov rdx, 0
    mov byte ptr [rbp - 716], 1
    cmp byte ptr [rbp - 716], 0
    je .L__s3_failure_site_191
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_192
    cmp byte ptr [rbp + r10 - 805], 0
    je .L__s3_failure_site_190
    mov rax, qword ptr [rbp + r10*8 - 776]
    mov rdx, rax
    mov byte ptr [rbp - 717], 1
    cmp byte ptr [rbp - 654], 0
    je .L__s3_failure_site_194
    mov rax, rdi
    pxor xmm0, xmm0
    cvtsi2sd xmm0, rax
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 718], 1
    cmp byte ptr [rbp - 717], 0
    je .L__s3_failure_site_196
    mov rax, rdx
    cmp byte ptr [rbp - 718], 0
    je .L__s3_failure_site_197
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 719], 1
    cmp byte ptr [rbp - 719], 0
    je .L__s3_failure_site_199
    mov qword ptr [rbp - 568], rdx
    mov qword ptr [rbp - 856], rdi
    mov qword ptr [rbp - 864], rsi
    mov rdi, qword ptr [rbp - 568]
    call __s3_builtin_sqrt
    mov rdi, qword ptr [rbp - 856]
    mov rsi, qword ptr [rbp - 864]
    mov rdx, rax
    mov byte ptr [rbp - 720], 1
    cmp byte ptr [rbp - 715], 0
    je .L__s3_failure_site_201
    mov rax, rsi
    cmp byte ptr [rbp - 720], 0
    je .L__s3_failure_site_202
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 721], 1
    mov rdx, 0
    mov byte ptr [rbp - 722], 1
    cmp byte ptr [rbp - 722], 0
    je .L__s3_failure_site_205
    mov rax, rdx
    cmp byte ptr [rbp - 721], 0
    je .L__s3_failure_site_206
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_207
    mov qword ptr [rbp + rax*8 - 752], r10
    mov byte ptr [rbp + rax - 802], 1
    mov rsi, 0
    mov byte ptr [rbp - 723], 1
    cmp byte ptr [rbp - 723], 0
    je .L__s3_failure_site_211
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_212
    cmp byte ptr [rbp + r10 - 801], 0
    je .L__s3_failure_site_210
    mov rax, qword ptr [rbp + r10*8 - 744]
    mov rsi, rax
    mov byte ptr [rbp - 724], 1
    mov rdx, 1
    mov byte ptr [rbp - 725], 1
    cmp byte ptr [rbp - 724], 0
    je .L__s3_failure_site_216
    mov rax, rsi
    cmp byte ptr [rbp - 725], 0
    je .L__s3_failure_site_217
    mov r10, rdx
    add rax, r10
    jo .L__s3_failure_site_215
    mov rsi, rax
    mov byte ptr [rbp - 726], 1
    mov rdx, 0
    mov byte ptr [rbp - 727], 1
    cmp byte ptr [rbp - 727], 0
    je .L__s3_failure_site_220
    mov rax, rdx
    cmp byte ptr [rbp - 726], 0
    je .L__s3_failure_site_221
    mov r10, rsi
    cmp rax, 1
    jae .L__s3_failure_site_222
    mov qword ptr [rbp + rax*8 - 744], r10
    mov byte ptr [rbp + rax - 801], 1
    jmp .L_s3_f4_rmsd_b17_while_condition_0
.L_s3_f4_rmsd_b10_rel_neg_14:
    mov rsi, 0
    mov byte ptr [rbp - 677], 1
    mov rdx, -1
    mov byte ptr [rbp - 678], 1
    cmp byte ptr [rbp - 677], 0
    je .L__s3_failure_site_227
    mov rax, rsi
    cmp byte ptr [rbp - 678], 0
    je .L__s3_failure_site_228
    mov r10, rdx
    cmp rax, 1
    jae .L__s3_failure_site_229
    cmp r10, -1
    jl .L__s3_failure_site_230
    cmp r10, 1
    jg .L__s3_failure_site_230
    mov byte ptr [rbp + rax - 777], r10b
    mov byte ptr [rbp + rax - 806], 1
    jmp .L_s3_f4_rmsd_b11_rel_cont_17
.L_s3_f4_rmsd_b11_rel_zero_15:
    mov rsi, 0
    mov byte ptr [rbp - 679], 1
    mov rdx, 0
    mov byte ptr [rbp - 680], 1
    cmp byte ptr [rbp - 679], 0
    je .L__s3_failure_site_235
    mov rax, rsi
    cmp byte ptr [rbp - 680], 0
    je .L__s3_failure_site_236
    mov r10, rdx
    cmp rax, 1
    jae .L__s3_failure_site_237
    cmp r10, -1
    jl .L__s3_failure_site_238
    cmp r10, 1
    jg .L__s3_failure_site_238
    mov byte ptr [rbp + rax - 777], r10b
    mov byte ptr [rbp + rax - 806], 1
    jmp .L_s3_f4_rmsd_b11_rel_cont_17
.L_s3_f4_rmsd_b10_rel_pos_16:
    mov rsi, 0
    mov byte ptr [rbp - 681], 1
    mov rdx, 0
    mov byte ptr [rbp - 682], 1
    cmp byte ptr [rbp - 681], 0
    je .L__s3_failure_site_243
    mov rax, rsi
    cmp byte ptr [rbp - 682], 0
    je .L__s3_failure_site_244
    mov r10, rdx
    cmp rax, 1
    jae .L__s3_failure_site_245
    cmp r10, -1
    jl .L__s3_failure_site_246
    cmp r10, 1
    jg .L__s3_failure_site_246
    mov byte ptr [rbp + rax - 777], r10b
    mov byte ptr [rbp + rax - 806], 1
    jmp .L_s3_f4_rmsd_b11_rel_cont_17
.L_s3_f4_rmsd_b11_rel_cont_17:
    mov rsi, 0
    mov byte ptr [rbp - 683], 1
    cmp byte ptr [rbp - 683], 0
    je .L__s3_failure_site_251
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_252
    cmp byte ptr [rbp + r10 - 806], 0
    je .L__s3_failure_site_250
    movsx rax, byte ptr [rbp + r10 - 777]
    mov rsi, rax
    mov byte ptr [rbp - 684], 1
    cmp byte ptr [rbp - 684], 0
    je .L__s3_failure_site_255
    mov rax, rsi
    cmp rax, -1
    je .L_s3_f4_rmsd_b13_while_body_10
    cmp rax, 0
    je .L_s3_f4_rmsd_b15_while_exit_0_11
    cmp rax, 1
    je .L_s3_f4_rmsd_b15_while_exit_1_12
    jmp .L__s3_failure_site_254
.size rmsd, .-rmsd

.globl s3_main
.type s3_main, @function
s3_main:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_256
    push rbp
    mov rbp, rsp
    sub rsp, 32
    mov byte ptr [rbp - 9], 0
    jmp .L_s3_f4_main_b5_entry
.L_s3_f4_main_b5_entry:
    mov rdi, 0
    mov byte ptr [rbp - 9], 1
    mov rax, rdi
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.size s3_main, .-s3_main

.section .text
.L__s3_failure_site_0:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_0]
    mov edx, 101
    lea rcx, [rip + .L__s3_failure_suffix_0]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_1:
    lea rsi, [rip + .L__s3_failure_prefix_1]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_2:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_2]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_2]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_3:
    lea rsi, [rip + .L__s3_failure_prefix_3]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_4:
    lea rsi, [rip + .L__s3_failure_prefix_4]
    mov edx, 129
    jmp __s3_fail_message
.L__s3_failure_site_5:
    lea rsi, [rip + .L__s3_failure_prefix_5]
    mov edx, 129
    jmp __s3_fail_message
.L__s3_failure_site_6:
    lea rsi, [rip + .L__s3_failure_prefix_6]
    mov edx, 124
    jmp __s3_fail_message
.L__s3_failure_site_7:
    lea rsi, [rip + .L__s3_failure_prefix_7]
    mov edx, 124
    jmp __s3_fail_message
.L__s3_failure_site_8:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_8]
    mov edx, 85
    lea rcx, [rip + .L__s3_failure_suffix_8]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_9:
    lea rsi, [rip + .L__s3_failure_prefix_9]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_10:
    lea rsi, [rip + .L__s3_failure_prefix_10]
    mov edx, 129
    jmp __s3_fail_message
.L__s3_failure_site_11:
    lea rsi, [rip + .L__s3_failure_prefix_11]
    mov edx, 129
    jmp __s3_fail_message
.L__s3_failure_site_12:
    lea rsi, [rip + .L__s3_failure_prefix_12]
    mov edx, 124
    jmp __s3_fail_message
.L__s3_failure_site_13:
    lea rsi, [rip + .L__s3_failure_prefix_13]
    mov edx, 124
    jmp __s3_fail_message
.L__s3_failure_site_14:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_14]
    mov edx, 85
    lea rcx, [rip + .L__s3_failure_suffix_14]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_15:
    lea rsi, [rip + .L__s3_failure_prefix_15]
    mov edx, 127
    jmp __s3_fail_message
.L__s3_failure_site_16:
    lea rsi, [rip + .L__s3_failure_prefix_16]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_17:
    lea rsi, [rip + .L__s3_failure_prefix_17]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_18:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_18]
    mov edx, 111
    lea rcx, [rip + .L__s3_failure_suffix_18]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_19:
    lea rsi, [rip + .L__s3_failure_prefix_19]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_20:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_20]
    mov edx, 97
    lea rcx, [rip + .L__s3_failure_suffix_20]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_21:
    lea rsi, [rip + .L__s3_failure_prefix_21]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_22:
    lea rsi, [rip + .L__s3_failure_prefix_22]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_23:
    lea rsi, [rip + .L__s3_failure_prefix_23]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_24:
    lea rsi, [rip + .L__s3_failure_prefix_24]
    mov edx, 140
    jmp __s3_fail_message
.L__s3_failure_site_25:
    lea rsi, [rip + .L__s3_failure_prefix_25]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_26:
    lea rsi, [rip + .L__s3_failure_prefix_26]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_27:
    lea rsi, [rip + .L__s3_failure_prefix_27]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_28:
    lea rsi, [rip + .L__s3_failure_prefix_28]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_29:
    lea rsi, [rip + .L__s3_failure_prefix_29]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_30:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_30]
    mov edx, 92
    lea rcx, [rip + .L__s3_failure_suffix_30]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_31:
    lea rsi, [rip + .L__s3_failure_prefix_31]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_32:
    lea rsi, [rip + .L__s3_failure_prefix_32]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_33:
    lea rsi, [rip + .L__s3_failure_prefix_33]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_34:
    lea rsi, [rip + .L__s3_failure_prefix_34]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_35:
    lea rsi, [rip + .L__s3_failure_prefix_35]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_36:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_36]
    mov edx, 92
    lea rcx, [rip + .L__s3_failure_suffix_36]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_37:
    lea rsi, [rip + .L__s3_failure_prefix_37]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_38:
    lea rsi, [rip + .L__s3_failure_prefix_38]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_39:
    lea rsi, [rip + .L__s3_failure_prefix_39]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_40:
    lea rsi, [rip + .L__s3_failure_prefix_40]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_41:
    lea rsi, [rip + .L__s3_failure_prefix_41]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_42:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_42]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_42]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_43:
    lea rsi, [rip + .L__s3_failure_prefix_43]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_44:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_44]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_44]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_45:
    lea rsi, [rip + .L__s3_failure_prefix_45]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_46:
    lea rsi, [rip + .L__s3_failure_prefix_46]
    mov edx, 131
    jmp __s3_fail_message
.L__s3_failure_site_47:
    lea rsi, [rip + .L__s3_failure_prefix_47]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_48:
    lea rsi, [rip + .L__s3_failure_prefix_48]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_49:
    lea rsi, [rip + .L__s3_failure_prefix_49]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_50:
    lea rsi, [rip + .L__s3_failure_prefix_50]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_51:
    lea rsi, [rip + .L__s3_failure_prefix_51]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_52:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_52]
    mov edx, 90
    lea rcx, [rip + .L__s3_failure_suffix_52]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_53:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_53]
    mov edx, 98
    lea rcx, [rip + .L__s3_failure_suffix_53]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_54:
    lea rsi, [rip + .L__s3_failure_prefix_54]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_55:
    lea rsi, [rip + .L__s3_failure_prefix_55]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_56:
    lea rsi, [rip + .L__s3_failure_prefix_56]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_57:
    lea rsi, [rip + .L__s3_failure_prefix_57]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_58:
    lea rsi, [rip + .L__s3_failure_prefix_58]
    mov edx, 131
    jmp __s3_fail_message
.L__s3_failure_site_59:
    lea rsi, [rip + .L__s3_failure_prefix_59]
    mov edx, 131
    jmp __s3_fail_message
.L__s3_failure_site_60:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_60]
    mov edx, 91
    lea rcx, [rip + .L__s3_failure_suffix_60]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_61:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_61]
    mov edx, 99
    lea rcx, [rip + .L__s3_failure_suffix_61]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_62:
    lea rsi, [rip + .L__s3_failure_prefix_62]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_63:
    lea rsi, [rip + .L__s3_failure_prefix_63]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_64:
    lea rsi, [rip + .L__s3_failure_prefix_64]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_65:
    lea rsi, [rip + .L__s3_failure_prefix_65]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_66:
    lea rsi, [rip + .L__s3_failure_prefix_66]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_67:
    lea rsi, [rip + .L__s3_failure_prefix_67]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_68:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_68]
    mov edx, 90
    lea rcx, [rip + .L__s3_failure_suffix_68]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_69:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_69]
    mov edx, 98
    lea rcx, [rip + .L__s3_failure_suffix_69]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_70:
    lea rsi, [rip + .L__s3_failure_prefix_70]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_71:
    lea rsi, [rip + .L__s3_failure_prefix_71]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_72:
    lea rsi, [rip + .L__s3_failure_prefix_72]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_73:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_73]
    mov edx, 104
    lea rcx, [rip + .L__s3_failure_suffix_73]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_74:
    lea rsi, [rip + .L__s3_failure_prefix_74]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_75:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_75]
    mov edx, 90
    lea rcx, [rip + .L__s3_failure_suffix_75]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_76:
    lea rsi, [rip + .L__s3_failure_prefix_76]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_77:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_77]
    mov edx, 100
    lea rcx, [rip + .L__s3_failure_suffix_77]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_78:
    lea rsi, [rip + .L__s3_failure_prefix_78]
    mov edx, 128
    jmp __s3_fail_message
.L__s3_failure_site_79:
    lea rsi, [rip + .L__s3_failure_prefix_79]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_80:
    lea rsi, [rip + .L__s3_failure_prefix_80]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_81:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_81]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_81]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_82:
    lea rsi, [rip + .L__s3_failure_prefix_82]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_83:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_83]
    mov edx, 98
    lea rcx, [rip + .L__s3_failure_suffix_83]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_84:
    lea rsi, [rip + .L__s3_failure_prefix_84]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_85:
    lea rsi, [rip + .L__s3_failure_prefix_85]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_86:
    lea rsi, [rip + .L__s3_failure_prefix_86]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_87:
    lea rsi, [rip + .L__s3_failure_prefix_87]
    mov edx, 141
    jmp __s3_fail_message
.L__s3_failure_site_88:
    lea rsi, [rip + .L__s3_failure_prefix_88]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_89:
    lea rsi, [rip + .L__s3_failure_prefix_89]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_90:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_90]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_90]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_91:
    lea rsi, [rip + .L__s3_failure_prefix_91]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_92:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_92]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_92]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_93:
    lea rsi, [rip + .L__s3_failure_prefix_93]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_94:
    lea rsi, [rip + .L__s3_failure_prefix_94]
    mov edx, 117
    jmp __s3_fail_message
.L__s3_failure_site_95:
    lea rsi, [rip + .L__s3_failure_prefix_95]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_96:
    lea rsi, [rip + .L__s3_failure_prefix_96]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_97:
    lea rsi, [rip + .L__s3_failure_prefix_97]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_98:
    lea rsi, [rip + .L__s3_failure_prefix_98]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_99:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_99]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_99]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_100:
    lea rsi, [rip + .L__s3_failure_prefix_100]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_101:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_101]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_101]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_102:
    lea rsi, [rip + .L__s3_failure_prefix_102]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_103:
    lea rsi, [rip + .L__s3_failure_prefix_103]
    mov edx, 111
    jmp __s3_fail_message
.L__s3_failure_site_104:
    lea rsi, [rip + .L__s3_failure_prefix_104]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_105:
    lea rsi, [rip + .L__s3_failure_prefix_105]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_106:
    lea rsi, [rip + .L__s3_failure_prefix_106]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_107:
    lea rsi, [rip + .L__s3_failure_prefix_107]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_108:
    lea rsi, [rip + .L__s3_failure_prefix_108]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_109:
    lea rsi, [rip + .L__s3_failure_prefix_109]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_110:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_110]
    mov edx, 95
    lea rcx, [rip + .L__s3_failure_suffix_110]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_111:
    lea rsi, [rip + .L__s3_failure_prefix_111]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_112:
    lea rsi, [rip + .L__s3_failure_prefix_112]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_113:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_113]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_113]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_114:
    lea rsi, [rip + .L__s3_failure_prefix_114]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_115:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_115]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_115]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_116:
    lea rsi, [rip + .L__s3_failure_prefix_116]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_117:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_117]
    mov edx, 101
    lea rcx, [rip + .L__s3_failure_suffix_117]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_118:
    lea rsi, [rip + .L__s3_failure_prefix_118]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_119:
    lea rsi, [rip + .L__s3_failure_prefix_119]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_120:
    lea rsi, [rip + .L__s3_failure_prefix_120]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_121:
    lea rsi, [rip + .L__s3_failure_prefix_121]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_122:
    lea rsi, [rip + .L__s3_failure_prefix_122]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_123:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_123]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_123]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_124:
    lea rsi, [rip + .L__s3_failure_prefix_124]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_125:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_125]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_125]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_126:
    lea rsi, [rip + .L__s3_failure_prefix_126]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_127:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_127]
    mov edx, 101
    lea rcx, [rip + .L__s3_failure_suffix_127]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_128:
    lea rsi, [rip + .L__s3_failure_prefix_128]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_129:
    lea rsi, [rip + .L__s3_failure_prefix_129]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_130:
    lea rsi, [rip + .L__s3_failure_prefix_130]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_131:
    lea rsi, [rip + .L__s3_failure_prefix_131]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_132:
    lea rsi, [rip + .L__s3_failure_prefix_132]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_133:
    lea rsi, [rip + .L__s3_failure_prefix_133]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_134:
    lea rsi, [rip + .L__s3_failure_prefix_134]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_135:
    lea rsi, [rip + .L__s3_failure_prefix_135]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_136:
    lea rsi, [rip + .L__s3_failure_prefix_136]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_137:
    lea rsi, [rip + .L__s3_failure_prefix_137]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_138:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_138]
    mov edx, 95
    lea rcx, [rip + .L__s3_failure_suffix_138]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_139:
    lea rsi, [rip + .L__s3_failure_prefix_139]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_140:
    lea rsi, [rip + .L__s3_failure_prefix_140]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_141:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_141]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_141]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_142:
    lea rsi, [rip + .L__s3_failure_prefix_142]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_143:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_143]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_143]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_144:
    lea rsi, [rip + .L__s3_failure_prefix_144]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_145:
    lea rsi, [rip + .L__s3_failure_prefix_145]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_146:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_146]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_146]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_147:
    lea rsi, [rip + .L__s3_failure_prefix_147]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_148:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_148]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_148]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_149:
    lea rsi, [rip + .L__s3_failure_prefix_149]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_150:
    lea rsi, [rip + .L__s3_failure_prefix_150]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_151:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_151]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_151]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_152:
    lea rsi, [rip + .L__s3_failure_prefix_152]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_153:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_153]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_153]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_154:
    lea rsi, [rip + .L__s3_failure_prefix_154]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_155:
    lea rsi, [rip + .L__s3_failure_prefix_155]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_156:
    lea rsi, [rip + .L__s3_failure_prefix_156]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_157:
    lea rsi, [rip + .L__s3_failure_prefix_157]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_158:
    lea rsi, [rip + .L__s3_failure_prefix_158]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_159:
    lea rsi, [rip + .L__s3_failure_prefix_159]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_160:
    lea rsi, [rip + .L__s3_failure_prefix_160]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_161:
    lea rsi, [rip + .L__s3_failure_prefix_161]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_162:
    lea rsi, [rip + .L__s3_failure_prefix_162]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_163:
    lea rsi, [rip + .L__s3_failure_prefix_163]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_164:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_164]
    mov edx, 95
    lea rcx, [rip + .L__s3_failure_suffix_164]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_165:
    lea rsi, [rip + .L__s3_failure_prefix_165]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_166:
    lea rsi, [rip + .L__s3_failure_prefix_166]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_167:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_167]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_167]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_168:
    lea rsi, [rip + .L__s3_failure_prefix_168]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_169:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_169]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_169]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_170:
    lea rsi, [rip + .L__s3_failure_prefix_170]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_171:
    lea rsi, [rip + .L__s3_failure_prefix_171]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_172:
    lea rsi, [rip + .L__s3_failure_prefix_172]
    mov edx, 111
    jmp __s3_fail_message
.L__s3_failure_site_173:
    lea rsi, [rip + .L__s3_failure_prefix_173]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_174:
    lea rsi, [rip + .L__s3_failure_prefix_174]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_175:
    lea rsi, [rip + .L__s3_failure_prefix_175]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_176:
    lea rsi, [rip + .L__s3_failure_prefix_176]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_177:
    lea rsi, [rip + .L__s3_failure_prefix_177]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_178:
    lea rsi, [rip + .L__s3_failure_prefix_178]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_179:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_179]
    mov edx, 95
    lea rcx, [rip + .L__s3_failure_suffix_179]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_180:
    lea rsi, [rip + .L__s3_failure_prefix_180]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_181:
    lea rsi, [rip + .L__s3_failure_prefix_181]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_182:
    lea rsi, [rip + .L__s3_failure_prefix_182]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_183:
    lea rsi, [rip + .L__s3_failure_prefix_183]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_184:
    lea rsi, [rip + .L__s3_failure_prefix_184]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_185:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_185]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_185]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_186:
    lea rsi, [rip + .L__s3_failure_prefix_186]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_187:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_187]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_187]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_188:
    lea rsi, [rip + .L__s3_failure_prefix_188]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_189:
    lea rsi, [rip + .L__s3_failure_prefix_189]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_190:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_190]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_190]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_191:
    lea rsi, [rip + .L__s3_failure_prefix_191]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_192:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_192]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_192]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_193:
    lea rsi, [rip + .L__s3_failure_prefix_193]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_194:
    lea rsi, [rip + .L__s3_failure_prefix_194]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_195:
    lea rsi, [rip + .L__s3_failure_prefix_195]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_196:
    lea rsi, [rip + .L__s3_failure_prefix_196]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_197:
    lea rsi, [rip + .L__s3_failure_prefix_197]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_198:
    lea rsi, [rip + .L__s3_failure_prefix_198]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_199:
    lea rsi, [rip + .L__s3_failure_prefix_199]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_200:
    lea rsi, [rip + .L__s3_failure_prefix_200]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_201:
    lea rsi, [rip + .L__s3_failure_prefix_201]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_202:
    lea rsi, [rip + .L__s3_failure_prefix_202]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_203:
    lea rsi, [rip + .L__s3_failure_prefix_203]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_204:
    lea rsi, [rip + .L__s3_failure_prefix_204]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_205:
    lea rsi, [rip + .L__s3_failure_prefix_205]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_206:
    lea rsi, [rip + .L__s3_failure_prefix_206]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_207:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_207]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_207]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_208:
    lea rsi, [rip + .L__s3_failure_prefix_208]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_209:
    lea rsi, [rip + .L__s3_failure_prefix_209]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_210:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_210]
    mov edx, 108
    lea rcx, [rip + .L__s3_failure_suffix_210]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_211:
    lea rsi, [rip + .L__s3_failure_prefix_211]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_212:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_212]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_212]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_213:
    lea rsi, [rip + .L__s3_failure_prefix_213]
    mov edx, 139
    jmp __s3_fail_message
.L__s3_failure_site_214:
    lea rsi, [rip + .L__s3_failure_prefix_214]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_215:
    lea rsi, [rip + .L__s3_failure_prefix_215]
    mov edx, 111
    jmp __s3_fail_message
.L__s3_failure_site_216:
    lea rsi, [rip + .L__s3_failure_prefix_216]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_217:
    lea rsi, [rip + .L__s3_failure_prefix_217]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_218:
    lea rsi, [rip + .L__s3_failure_prefix_218]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_219:
    lea rsi, [rip + .L__s3_failure_prefix_219]
    mov edx, 138
    jmp __s3_fail_message
.L__s3_failure_site_220:
    lea rsi, [rip + .L__s3_failure_prefix_220]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_221:
    lea rsi, [rip + .L__s3_failure_prefix_221]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_222:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_222]
    mov edx, 94
    lea rcx, [rip + .L__s3_failure_suffix_222]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_223:
    lea rsi, [rip + .L__s3_failure_prefix_223]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_224:
    lea rsi, [rip + .L__s3_failure_prefix_224]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_225:
    lea rsi, [rip + .L__s3_failure_prefix_225]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_226:
    lea rsi, [rip + .L__s3_failure_prefix_226]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_227:
    lea rsi, [rip + .L__s3_failure_prefix_227]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_228:
    lea rsi, [rip + .L__s3_failure_prefix_228]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_229:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_229]
    mov edx, 92
    lea rcx, [rip + .L__s3_failure_suffix_229]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_230:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_230]
    mov edx, 100
    lea rcx, [rip + .L__s3_failure_suffix_230]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_231:
    lea rsi, [rip + .L__s3_failure_prefix_231]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_232:
    lea rsi, [rip + .L__s3_failure_prefix_232]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_233:
    lea rsi, [rip + .L__s3_failure_prefix_233]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_234:
    lea rsi, [rip + .L__s3_failure_prefix_234]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_235:
    lea rsi, [rip + .L__s3_failure_prefix_235]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_236:
    lea rsi, [rip + .L__s3_failure_prefix_236]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_237:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_237]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_237]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_238:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_238]
    mov edx, 101
    lea rcx, [rip + .L__s3_failure_suffix_238]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_239:
    lea rsi, [rip + .L__s3_failure_prefix_239]
    mov edx, 135
    jmp __s3_fail_message
.L__s3_failure_site_240:
    lea rsi, [rip + .L__s3_failure_prefix_240]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_241:
    lea rsi, [rip + .L__s3_failure_prefix_241]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_242:
    lea rsi, [rip + .L__s3_failure_prefix_242]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_243:
    lea rsi, [rip + .L__s3_failure_prefix_243]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_244:
    lea rsi, [rip + .L__s3_failure_prefix_244]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_245:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_245]
    mov edx, 92
    lea rcx, [rip + .L__s3_failure_suffix_245]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_246:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_246]
    mov edx, 100
    lea rcx, [rip + .L__s3_failure_suffix_246]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_247:
    lea rsi, [rip + .L__s3_failure_prefix_247]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_248:
    lea rsi, [rip + .L__s3_failure_prefix_248]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_249:
    lea rsi, [rip + .L__s3_failure_prefix_249]
    mov edx, 136
    jmp __s3_fail_message
.L__s3_failure_site_250:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_250]
    mov edx, 106
    lea rcx, [rip + .L__s3_failure_suffix_250]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_251:
    lea rsi, [rip + .L__s3_failure_prefix_251]
    mov edx, 132
    jmp __s3_fail_message
.L__s3_failure_site_252:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_252]
    mov edx, 92
    lea rcx, [rip + .L__s3_failure_suffix_252]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_253:
    lea rsi, [rip + .L__s3_failure_prefix_253]
    mov edx, 134
    jmp __s3_fail_message
.L__s3_failure_site_254:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_254]
    mov edx, 102
    lea rcx, [rip + .L__s3_failure_suffix_254]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_255:
    lea rsi, [rip + .L__s3_failure_prefix_255]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_256:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_256]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_256]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_257:
    lea rsi, [rip + .L__s3_failure_prefix_257]
    mov edx, 131
    jmp __s3_fail_message
.L__s3_failure_site_258:
    lea rsi, [rip + .L__s3_failure_prefix_258]
    mov edx, 128
    jmp __s3_fail_message

.section .rodata
.L__s3_failure_prefix_0:
    .ascii "runtime error [frame limit] in function 'identity_f64'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_0:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_1:
    .ascii "runtime error [instruction limit] in function 'identity_f64'\nat source 2:5 (block entry, TRET): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_2:
    .ascii "runtime error [frame limit] in function 'rmsd'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_2:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_3:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 5:21 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_4:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 5:5 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_5:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 5:5 (block entry, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_6:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 5:5 (block entry, TSTORE): register r7 is uninitialized\n"
.L__s3_failure_prefix_7:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 5:5 (block entry, TSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_8:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 5:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_8:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_9:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 6:22 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_10:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 6:5 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_11:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 6:5 (block entry, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_12:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 6:5 (block entry, TSTORE): register r9 is uninitialized\n"
.L__s3_failure_prefix_13:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 6:5 (block entry, TSTORE): register r8 is uninitialized\n"
.L__s3_failure_prefix_14:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 6:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_14:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_15:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:5 (block entry, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_16:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:11 (block while_condition_0, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_17:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:11 (block while_condition_0, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_18:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 7:11 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_18:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_19:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:11 (block while_condition_0, TLOAD): register r10 is uninitialized\n"
.L__s3_failure_prefix_20:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 7:11 (block while_condition_0, TLOAD): index "
.L__s3_failure_suffix_20:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_21:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block while_condition_0, TCMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_22:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block while_condition_0, TCMP): register r11 is uninitialized\n"
.L__s3_failure_prefix_23:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block while_condition_0, TCMP): register r4 is uninitialized\n"
.L__s3_failure_prefix_24:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block while_condition_0, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_25:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 8:31 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_26:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 8:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_27:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 8:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_28:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 8:9 (block while_body_1, TSTORE): register r22 is uninitialized\n"
.L__s3_failure_prefix_29:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 8:9 (block while_body_1, TSTORE): register r21 is uninitialized\n"
.L__s3_failure_prefix_30:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 8:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_30:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_31:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 9:24 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_32:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 9:9 (block while_body_1, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_33:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 9:9 (block while_body_1, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_34:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 9:9 (block while_body_1, TSTORE): register r24 is uninitialized\n"
.L__s3_failure_prefix_35:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 9:9 (block while_body_1, TSTORE): register r23 is uninitialized\n"
.L__s3_failure_prefix_36:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 9:9 (block while_body_1, TSTORE): index "
.L__s3_failure_suffix_36:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_37:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:9 (block while_body_1, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_38:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:5 (block while_exit_0_2, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_39:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:5 (block while_exit_1_3, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_40:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 17:12 (block while_exit_4, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_41:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 17:12 (block while_exit_4, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_42:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 17:12 (block while_exit_4, TLOAD): index "
.L__s3_failure_suffix_42:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_43:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 17:12 (block while_exit_4, TLOAD): register r79 is uninitialized\n"
.L__s3_failure_prefix_44:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 17:12 (block while_exit_4, TLOAD): index "
.L__s3_failure_suffix_44:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_45:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 17:5 (block while_exit_4, TRET): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_46:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 17:5 (block while_exit_4, TRET): register r80 is uninitialized\n"
.L__s3_failure_prefix_47:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_48:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_49:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_50:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TSTORE): register r13 is uninitialized\n"
.L__s3_failure_prefix_51:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TSTORE): register r14 is uninitialized\n"
.L__s3_failure_prefix_52:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TSTORE): index "
.L__s3_failure_suffix_52:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_53:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TSTORE): trit result "
.L__s3_failure_suffix_53:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_54:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_neg_5, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_55:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_56:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_57:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_58:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TSTORE): register r15 is uninitialized\n"
.L__s3_failure_prefix_59:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TSTORE): register r16 is uninitialized\n"
.L__s3_failure_prefix_60:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TSTORE): index "
.L__s3_failure_suffix_60:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_61:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TSTORE): trit result "
.L__s3_failure_suffix_61:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_62:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_zero_6, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_63:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_64:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_65:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_66:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TSTORE): register r17 is uninitialized\n"
.L__s3_failure_prefix_67:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TSTORE): register r18 is uninitialized\n"
.L__s3_failure_prefix_68:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TSTORE): index "
.L__s3_failure_suffix_68:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_69:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TSTORE): trit result "
.L__s3_failure_suffix_69:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_70:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_pos_7, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_71:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_cont_8, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_72:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:16 (block rel_cont_8, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_73:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 7:16 (block rel_cont_8, TLOAD): index "
.L__s3_failure_suffix_73:
    .ascii " is uninitialized in m2\n"
.L__s3_failure_prefix_74:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:16 (block rel_cont_8, TLOAD): register r19 is uninitialized\n"
.L__s3_failure_prefix_75:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 7:16 (block rel_cont_8, TLOAD): index "
.L__s3_failure_suffix_75:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_76:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:5 (block rel_cont_8, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_77:
    .ascii "runtime error [invalid trit state] in function 'rmsd'\nat source 7:5 (block rel_cont_8, TBR3): value "
.L__s3_failure_suffix_77:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_78:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 7:5 (block rel_cont_8, TBR3): register r20 is uninitialized\n"
.L__s3_failure_prefix_79:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:15 (block while_condition_9, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_80:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:15 (block while_condition_9, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_81:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 10:15 (block while_condition_9, TLOAD): index "
.L__s3_failure_suffix_81:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_82:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:15 (block while_condition_9, TLOAD): register r25 is uninitialized\n"
.L__s3_failure_prefix_83:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 10:15 (block while_condition_9, TLOAD): index "
.L__s3_failure_suffix_83:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_84:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block while_condition_9, TCMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_85:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block while_condition_9, TCMP): register r26 is uninitialized\n"
.L__s3_failure_prefix_86:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block while_condition_9, TCMP): register r5 is uninitialized\n"
.L__s3_failure_prefix_87:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block while_condition_9, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_88:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:31 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_89:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:31 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_90:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 11:31 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_90:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_91:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:31 (block while_body_10, TLOAD): register r36 is uninitialized\n"
.L__s3_failure_prefix_92:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 11:31 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_92:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_93:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:36 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_94:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 11:36 (block while_body_10, TMUL): i64 multiplication overflow\n"
.L__s3_failure_prefix_95:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:36 (block while_body_10, TMUL): register r37 is uninitialized\n"
.L__s3_failure_prefix_96:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:36 (block while_body_10, TMUL): register r5 is uninitialized\n"
.L__s3_failure_prefix_97:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:52 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_98:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:52 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_99:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 11:52 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_99:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_100:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:52 (block while_body_10, TLOAD): register r39 is uninitialized\n"
.L__s3_failure_prefix_101:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 11:52 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_101:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_102:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:50 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_103:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 11:50 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_104:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:50 (block while_body_10, TADD): register r38 is uninitialized\n"
.L__s3_failure_prefix_105:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:50 (block while_body_10, TADD): register r40 is uninitialized\n"
.L__s3_failure_prefix_106:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_107:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 11:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_108:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:13 (block while_body_10, TSTORE): register r42 is uninitialized\n"
.L__s3_failure_prefix_109:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 11:13 (block while_body_10, TSTORE): register r41 is uninitialized\n"
.L__s3_failure_prefix_110:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 11:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_110:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_111:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:35 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_112:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:35 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_113:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 12:35 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_113:
    .ascii " is uninitialized in m6\n"
.L__s3_failure_prefix_114:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:35 (block while_body_10, TLOAD): register r43 is uninitialized\n"
.L__s3_failure_prefix_115:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 12:35 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_115:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_116:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:30 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_117:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 12:30 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_117:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_118:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:30 (block while_body_10, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_119:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:30 (block while_body_10, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_120:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:30 (block while_body_10, TSLOAD): register r44 is uninitialized\n"
.L__s3_failure_prefix_121:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:51 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_122:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:51 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_123:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 12:51 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_123:
    .ascii " is uninitialized in m6\n"
.L__s3_failure_prefix_124:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:51 (block while_body_10, TLOAD): register r46 is uninitialized\n"
.L__s3_failure_prefix_125:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 12:51 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_125:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_126:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:45 (block while_body_10, TSLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_127:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 12:45 (block while_body_10, TSLOAD): slice index "
.L__s3_failure_suffix_127:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_128:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:45 (block while_body_10, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_129:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:45 (block while_body_10, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_130:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:45 (block while_body_10, TSLOAD): register r47 is uninitialized\n"
.L__s3_failure_prefix_131:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:43 (block while_body_10, TNDIFF): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_132:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:43 (block while_body_10, TNDIFF): register r45 is uninitialized\n"
.L__s3_failure_prefix_133:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:43 (block while_body_10, TNDIFF): register r48 is uninitialized\n"
.L__s3_failure_prefix_134:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_135:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 12:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_136:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:13 (block while_body_10, TSTORE): register r50 is uninitialized\n"
.L__s3_failure_prefix_137:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 12:13 (block while_body_10, TSTORE): register r49 is uninitialized\n"
.L__s3_failure_prefix_138:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 12:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_138:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_139:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:19 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_140:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:19 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_141:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 13:19 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_141:
    .ascii " is uninitialized in m4\n"
.L__s3_failure_prefix_142:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:19 (block while_body_10, TLOAD): register r51 is uninitialized\n"
.L__s3_failure_prefix_143:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 13:19 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_143:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_144:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:25 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_145:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:25 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_146:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 13:25 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_146:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_147:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:25 (block while_body_10, TLOAD): register r53 is uninitialized\n"
.L__s3_failure_prefix_148:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 13:25 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_148:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_149:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:33 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_150:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:33 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_151:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 13:33 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_151:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_152:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:33 (block while_body_10, TLOAD): register r55 is uninitialized\n"
.L__s3_failure_prefix_153:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 13:33 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_153:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_154:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:31 (block while_body_10, TMUL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_155:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:31 (block while_body_10, TMUL): register r54 is uninitialized\n"
.L__s3_failure_prefix_156:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:31 (block while_body_10, TMUL): register r56 is uninitialized\n"
.L__s3_failure_prefix_157:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:23 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_158:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:23 (block while_body_10, TADD): register r52 is uninitialized\n"
.L__s3_failure_prefix_159:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:23 (block while_body_10, TADD): register r57 is uninitialized\n"
.L__s3_failure_prefix_160:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_161:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 13:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_162:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:13 (block while_body_10, TSTORE): register r59 is uninitialized\n"
.L__s3_failure_prefix_163:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 13:13 (block while_body_10, TSTORE): register r58 is uninitialized\n"
.L__s3_failure_prefix_164:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 13:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_164:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_165:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 14:26 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_166:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 14:26 (block while_body_10, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_167:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 14:26 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_167:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_168:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 14:26 (block while_body_10, TLOAD): register r60 is uninitialized\n"
.L__s3_failure_prefix_169:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 14:26 (block while_body_10, TLOAD): index "
.L__s3_failure_suffix_169:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_170:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 14:39 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_171:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 14:37 (block while_body_10, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_172:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 14:37 (block while_body_10, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_173:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 14:37 (block while_body_10, TADD): register r61 is uninitialized\n"
.L__s3_failure_prefix_174:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 14:37 (block while_body_10, TADD): register r62 is uninitialized\n"
.L__s3_failure_prefix_175:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 14:13 (block while_body_10, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_176:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 14:13 (block while_body_10, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_177:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 14:13 (block while_body_10, TSTORE): register r64 is uninitialized\n"
.L__s3_failure_prefix_178:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 14:13 (block while_body_10, TSTORE): register r63 is uninitialized\n"
.L__s3_failure_prefix_179:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 14:13 (block while_body_10, TSTORE): index "
.L__s3_failure_suffix_179:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_180:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:9 (block while_body_10, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_181:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:9 (block while_exit_0_11, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_182:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:9 (block while_exit_1_12, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_183:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:17 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_184:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:17 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_185:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 15:17 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_185:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_186:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:17 (block while_exit_13, TLOAD): register r65 is uninitialized\n"
.L__s3_failure_prefix_187:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 15:17 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_187:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_188:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:30 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_189:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:30 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_190:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 15:30 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_190:
    .ascii " is uninitialized in m4\n"
.L__s3_failure_prefix_191:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:30 (block while_exit_13, TLOAD): register r67 is uninitialized\n"
.L__s3_failure_prefix_192:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 15:30 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_192:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_193:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:36 (block while_exit_13, TCVT): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_194:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:36 (block while_exit_13, TCVT): register r5 is uninitialized\n"
.L__s3_failure_prefix_195:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:34 (block while_exit_13, TDIV): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_196:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:34 (block while_exit_13, TDIV): register r68 is uninitialized\n"
.L__s3_failure_prefix_197:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:34 (block while_exit_13, TDIV): register r69 is uninitialized\n"
.L__s3_failure_prefix_198:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:25 (block while_exit_13, TCALL): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_199:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:25 (block while_exit_13, TCALL): register r70 is uninitialized\n"
.L__s3_failure_prefix_200:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:23 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_201:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:23 (block while_exit_13, TADD): register r66 is uninitialized\n"
.L__s3_failure_prefix_202:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:23 (block while_exit_13, TADD): register r71 is uninitialized\n"
.L__s3_failure_prefix_203:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:9 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_204:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 15:9 (block while_exit_13, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_205:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:9 (block while_exit_13, TSTORE): register r73 is uninitialized\n"
.L__s3_failure_prefix_206:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 15:9 (block while_exit_13, TSTORE): register r72 is uninitialized\n"
.L__s3_failure_prefix_207:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 15:9 (block while_exit_13, TSTORE): index "
.L__s3_failure_suffix_207:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_208:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 16:16 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_209:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 16:16 (block while_exit_13, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_210:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 16:16 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_210:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_211:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 16:16 (block while_exit_13, TLOAD): register r74 is uninitialized\n"
.L__s3_failure_prefix_212:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 16:16 (block while_exit_13, TLOAD): index "
.L__s3_failure_suffix_212:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_213:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 16:23 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_214:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 16:21 (block while_exit_13, TADD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_215:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 16:21 (block while_exit_13, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_216:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 16:21 (block while_exit_13, TADD): register r75 is uninitialized\n"
.L__s3_failure_prefix_217:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 16:21 (block while_exit_13, TADD): register r76 is uninitialized\n"
.L__s3_failure_prefix_218:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 16:9 (block while_exit_13, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_219:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 16:9 (block while_exit_13, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_220:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 16:9 (block while_exit_13, TSTORE): register r78 is uninitialized\n"
.L__s3_failure_prefix_221:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 16:9 (block while_exit_13, TSTORE): register r77 is uninitialized\n"
.L__s3_failure_prefix_222:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 16:9 (block while_exit_13, TSTORE): index "
.L__s3_failure_suffix_222:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_223:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 7:5 (block while_exit_13, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_224:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_225:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_226:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_227:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TSTORE): register r28 is uninitialized\n"
.L__s3_failure_prefix_228:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TSTORE): register r29 is uninitialized\n"
.L__s3_failure_prefix_229:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TSTORE): index "
.L__s3_failure_suffix_229:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_230:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TSTORE): trit result "
.L__s3_failure_suffix_230:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_231:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_neg_14, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_232:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_233:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_234:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_235:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TSTORE): register r30 is uninitialized\n"
.L__s3_failure_prefix_236:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TSTORE): register r31 is uninitialized\n"
.L__s3_failure_prefix_237:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TSTORE): index "
.L__s3_failure_suffix_237:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_238:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TSTORE): trit result "
.L__s3_failure_suffix_238:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_239:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_zero_15, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_240:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_241:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_242:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TSTORE): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_243:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TSTORE): register r32 is uninitialized\n"
.L__s3_failure_prefix_244:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TSTORE): register r33 is uninitialized\n"
.L__s3_failure_prefix_245:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TSTORE): index "
.L__s3_failure_suffix_245:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_246:
    .ascii "runtime error [overflow] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TSTORE): trit result "
.L__s3_failure_suffix_246:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_247:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_pos_16, TJMP): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_248:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_cont_17, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_249:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:26 (block rel_cont_17, TLOAD): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_250:
    .ascii "runtime error [uninitialized memory] in function 'rmsd'\nat source 10:26 (block rel_cont_17, TLOAD): index "
.L__s3_failure_suffix_250:
    .ascii " is uninitialized in m5\n"
.L__s3_failure_prefix_251:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:26 (block rel_cont_17, TLOAD): register r34 is uninitialized\n"
.L__s3_failure_prefix_252:
    .ascii "runtime error [bounds] in function 'rmsd'\nat source 10:26 (block rel_cont_17, TLOAD): index "
.L__s3_failure_suffix_252:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_253:
    .ascii "runtime error [instruction limit] in function 'rmsd'\nat source 10:9 (block rel_cont_17, TBR3): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_254:
    .ascii "runtime error [invalid trit state] in function 'rmsd'\nat source 10:9 (block rel_cont_17, TBR3): value "
.L__s3_failure_suffix_254:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_255:
    .ascii "runtime error [uninitialized register] in function 'rmsd'\nat source 10:9 (block rel_cont_17, TBR3): register r35 is uninitialized\n"
.L__s3_failure_prefix_256:
    .ascii "runtime error [frame limit] in function 'main'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_256:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_257:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 20:12 (block entry, TCONST): instruction limit 10000000000 exceeded\n"
.L__s3_failure_prefix_258:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 20:5 (block entry, TRET): instruction limit 10000000000 exceeded\n"

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
