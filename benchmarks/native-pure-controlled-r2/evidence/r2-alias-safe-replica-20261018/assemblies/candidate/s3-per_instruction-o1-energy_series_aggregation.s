.intel_syntax noprefix
# Generated deterministically by the S3 Linux x86-64 backend.
.section .text
.globl s3_absolute_f64
.type s3_absolute_f64, @function
s3_absolute_f64:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_0
    push rbp
    mov rbp, rsp
    sub rsp, 80
    mov qword ptr [rbp - 56], r15
    movq rax, xmm0
    mov qword ptr [rbp - 8], rax
    mov rdi, qword ptr [rbp - 8]
    mov r15, qword ptr [rip + __s3_instruction_remaining]
    jmp .L_s3_f12_absolute_f64_b5_entry
.L_s3_f12_absolute_f64_b5_entry:
    dec r15
    js .L__s3_failure_site_1
    movabs rax, 0
    mov rsi, rax
    dec r15
    js .L__s3_failure_site_2
    mov rax, rdi
    mov r10, rsi
    movq xmm0, rax
    movq xmm1, r10
    ucomisd xmm0, xmm1
    setb al
    setnp r11b
    and al, r11b
    movzx r11, al
    neg r11
    mov rsi, r11
    dec r15
    js .L__s3_failure_site_3
    mov rax, rsi
    cmp rax, -1
    je .L_s3_f12_absolute_f64_b17_switch_negative_0
    cmp rax, 0
    je .L_s3_f12_absolute_f64_b16_switch_neutral_1
    cmp rax, 1
    je .L_s3_f12_absolute_f64_b17_switch_positive_2
    jmp .L__s3_failure_site_4
.L_s3_f12_absolute_f64_b17_switch_negative_0:
    dec r15
    js .L__s3_failure_site_5
    movabs rax, 0
    mov rsi, rax
    dec r15
    js .L__s3_failure_site_6
    mov rax, rsi
    mov r10, rdi
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rdi, rax
    dec r15
    js .L__s3_failure_site_7
    mov rax, rdi
    movq xmm0, rax
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov r15, qword ptr [rbp - 56]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f12_absolute_f64_b16_switch_neutral_1:
    dec r15
    js .L__s3_failure_site_8
    mov rax, rdi
    movq xmm0, rax
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov r15, qword ptr [rbp - 56]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f12_absolute_f64_b17_switch_positive_2:
    dec r15
    js .L__s3_failure_site_9
    mov rax, rdi
    movq xmm0, rax
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov r15, qword ptr [rbp - 56]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.size s3_absolute_f64, .-s3_absolute_f64

.globl energy_series_aggregation
.type energy_series_aggregation, @function
energy_series_aggregation:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_10
    push rbp
    mov rbp, rsp
    sub rsp, 2144
    mov qword ptr [rbp - 2056], rbx
    mov qword ptr [rbp - 2064], r12
    mov qword ptr [rbp - 2072], r13
    mov qword ptr [rbp - 2080], r14
    mov qword ptr [rbp - 2088], r15
    mov qword ptr [rbp - 8], rdi
    mov qword ptr [rbp - 16], rsi
    mov qword ptr [rbp - 24], rdx
    mov qword ptr [rbp - 32], rcx
    movq rax, xmm0
    mov qword ptr [rbp - 40], rax
    mov qword ptr [rbp - 48], r8
    mov qword ptr [rbp - 56], r9
    mov r14, qword ptr [rbp - 8]
    mov rdi, qword ptr [rbp - 16]
    mov rsi, qword ptr [rbp - 24]
    mov rdx, qword ptr [rbp - 32]
    mov r13, qword ptr [rbp - 40]
    mov rbx, qword ptr [rbp - 48]
    mov r12, qword ptr [rbp - 56]
    mov r10, rdi
    mov r11, rcx
    mov byte ptr [rbp - 1689], 0
    mov byte ptr [rbp - 1690], 0
    mov byte ptr [rbp - 1691], 0
    mov byte ptr [rbp - 1692], 0
    mov byte ptr [rbp - 1693], 0
    mov byte ptr [rbp - 1694], 0
    mov byte ptr [rbp - 1695], 0
    mov byte ptr [rbp - 1696], 0
    mov byte ptr [rbp - 1697], 0
    mov byte ptr [rbp - 1698], 0
    mov byte ptr [rbp - 1699], 0
    mov byte ptr [rbp - 1700], 0
    mov byte ptr [rbp - 1701], 0
    mov byte ptr [rbp - 1702], 0
    mov byte ptr [rbp - 1703], 0
    mov byte ptr [rbp - 1704], 0
    mov byte ptr [rbp - 1705], 0
    mov byte ptr [rbp - 1706], 0
    mov byte ptr [rbp - 1707], 0
    mov byte ptr [rbp - 1708], 0
    mov byte ptr [rbp - 1709], 0
    mov byte ptr [rbp - 1710], 0
    mov byte ptr [rbp - 1711], 0
    mov byte ptr [rbp - 1712], 0
    mov byte ptr [rbp - 1713], 0
    mov byte ptr [rbp - 1714], 0
    mov byte ptr [rbp - 1715], 0
    mov byte ptr [rbp - 1716], 0
    mov byte ptr [rbp - 1717], 0
    mov byte ptr [rbp - 1718], 0
    mov byte ptr [rbp - 1719], 0
    mov byte ptr [rbp - 1720], 0
    mov byte ptr [rbp - 1721], 0
    mov byte ptr [rbp - 1722], 0
    mov byte ptr [rbp - 1723], 0
    mov byte ptr [rbp - 1724], 0
    mov byte ptr [rbp - 1725], 0
    mov byte ptr [rbp - 1726], 0
    mov byte ptr [rbp - 1727], 0
    mov byte ptr [rbp - 1728], 0
    mov byte ptr [rbp - 1729], 0
    mov byte ptr [rbp - 1730], 0
    mov byte ptr [rbp - 1731], 0
    mov byte ptr [rbp - 1732], 0
    mov byte ptr [rbp - 1733], 0
    mov byte ptr [rbp - 1734], 0
    mov byte ptr [rbp - 1735], 0
    mov byte ptr [rbp - 1736], 0
    mov byte ptr [rbp - 1737], 0
    mov byte ptr [rbp - 1738], 0
    mov byte ptr [rbp - 1739], 0
    mov byte ptr [rbp - 1740], 0
    mov byte ptr [rbp - 1741], 0
    mov byte ptr [rbp - 1742], 0
    mov byte ptr [rbp - 1743], 0
    mov byte ptr [rbp - 1744], 0
    mov byte ptr [rbp - 1745], 0
    mov byte ptr [rbp - 1746], 0
    mov byte ptr [rbp - 1747], 0
    mov byte ptr [rbp - 1748], 0
    mov byte ptr [rbp - 1749], 0
    mov byte ptr [rbp - 1750], 0
    mov byte ptr [rbp - 1751], 0
    mov byte ptr [rbp - 1752], 0
    mov byte ptr [rbp - 1753], 0
    mov byte ptr [rbp - 1754], 0
    mov byte ptr [rbp - 1755], 0
    mov byte ptr [rbp - 1756], 0
    mov byte ptr [rbp - 1757], 0
    mov byte ptr [rbp - 1758], 0
    mov byte ptr [rbp - 1759], 0
    mov byte ptr [rbp - 1760], 0
    mov byte ptr [rbp - 1761], 0
    mov byte ptr [rbp - 1762], 0
    mov byte ptr [rbp - 1763], 0
    mov byte ptr [rbp - 1764], 0
    mov byte ptr [rbp - 1765], 0
    mov byte ptr [rbp - 1766], 0
    mov byte ptr [rbp - 1767], 0
    mov byte ptr [rbp - 1768], 0
    mov byte ptr [rbp - 1769], 0
    mov byte ptr [rbp - 1770], 0
    mov byte ptr [rbp - 1771], 0
    mov byte ptr [rbp - 1772], 0
    mov byte ptr [rbp - 1773], 0
    mov byte ptr [rbp - 1774], 0
    mov byte ptr [rbp - 1775], 0
    mov byte ptr [rbp - 1776], 0
    mov byte ptr [rbp - 1777], 0
    mov byte ptr [rbp - 1778], 0
    mov byte ptr [rbp - 1779], 0
    mov byte ptr [rbp - 1780], 0
    mov byte ptr [rbp - 1781], 0
    mov byte ptr [rbp - 1782], 0
    mov byte ptr [rbp - 1783], 0
    mov byte ptr [rbp - 1784], 0
    mov byte ptr [rbp - 1785], 0
    mov byte ptr [rbp - 1786], 0
    mov byte ptr [rbp - 1787], 0
    mov byte ptr [rbp - 1788], 0
    mov byte ptr [rbp - 1789], 0
    mov byte ptr [rbp - 1790], 0
    mov byte ptr [rbp - 1791], 0
    mov byte ptr [rbp - 1792], 0
    mov byte ptr [rbp - 1793], 0
    mov byte ptr [rbp - 1794], 0
    mov byte ptr [rbp - 1795], 0
    mov byte ptr [rbp - 1796], 0
    mov byte ptr [rbp - 1797], 0
    mov byte ptr [rbp - 1798], 0
    mov byte ptr [rbp - 1799], 0
    mov byte ptr [rbp - 1800], 0
    mov byte ptr [rbp - 1801], 0
    mov byte ptr [rbp - 1802], 0
    mov byte ptr [rbp - 1803], 0
    mov byte ptr [rbp - 1804], 0
    mov byte ptr [rbp - 1805], 0
    mov byte ptr [rbp - 1806], 0
    mov byte ptr [rbp - 1807], 0
    mov byte ptr [rbp - 1808], 0
    mov byte ptr [rbp - 1809], 0
    mov byte ptr [rbp - 1810], 0
    mov byte ptr [rbp - 1811], 0
    mov byte ptr [rbp - 1812], 0
    mov byte ptr [rbp - 1813], 0
    mov byte ptr [rbp - 1814], 0
    mov byte ptr [rbp - 1815], 0
    mov byte ptr [rbp - 1816], 0
    mov byte ptr [rbp - 1817], 0
    mov byte ptr [rbp - 1818], 0
    mov byte ptr [rbp - 1819], 0
    mov byte ptr [rbp - 1820], 0
    mov byte ptr [rbp - 1821], 0
    mov byte ptr [rbp - 1822], 0
    mov byte ptr [rbp - 1823], 0
    mov byte ptr [rbp - 1824], 0
    mov byte ptr [rbp - 1825], 0
    mov byte ptr [rbp - 1826], 0
    mov byte ptr [rbp - 1827], 0
    mov byte ptr [rbp - 1828], 0
    mov byte ptr [rbp - 1829], 0
    mov byte ptr [rbp - 1830], 0
    mov byte ptr [rbp - 1831], 0
    mov byte ptr [rbp - 1832], 0
    mov byte ptr [rbp - 1833], 0
    mov byte ptr [rbp - 1834], 0
    mov byte ptr [rbp - 1835], 0
    mov byte ptr [rbp - 1836], 0
    mov byte ptr [rbp - 1837], 0
    mov byte ptr [rbp - 1838], 0
    mov byte ptr [rbp - 1839], 0
    mov byte ptr [rbp - 1840], 0
    mov byte ptr [rbp - 1841], 0
    mov byte ptr [rbp - 1842], 0
    mov byte ptr [rbp - 1843], 0
    mov byte ptr [rbp - 1844], 0
    mov byte ptr [rbp - 1845], 0
    mov byte ptr [rbp - 1846], 0
    mov byte ptr [rbp - 1847], 0
    mov byte ptr [rbp - 1848], 0
    mov byte ptr [rbp - 1849], 0
    mov byte ptr [rbp - 1850], 0
    mov byte ptr [rbp - 1851], 0
    mov byte ptr [rbp - 1852], 0
    mov byte ptr [rbp - 1853], 0
    mov byte ptr [rbp - 1854], 0
    mov byte ptr [rbp - 1855], 0
    mov byte ptr [rbp - 1856], 0
    mov byte ptr [rbp - 1857], 0
    mov byte ptr [rbp - 1858], 0
    mov byte ptr [rbp - 1859], 0
    mov byte ptr [rbp - 1860], 0
    mov byte ptr [rbp - 1861], 0
    mov byte ptr [rbp - 1862], 0
    mov byte ptr [rbp - 1863], 0
    mov byte ptr [rbp - 1864], 0
    mov byte ptr [rbp - 1865], 0
    mov byte ptr [rbp - 1866], 0
    mov byte ptr [rbp - 1867], 0
    mov byte ptr [rbp - 1868], 0
    mov byte ptr [rbp - 1869], 0
    mov byte ptr [rbp - 1870], 0
    mov byte ptr [rbp - 1871], 0
    mov byte ptr [rbp - 1872], 0
    mov byte ptr [rbp - 1873], 0
    mov byte ptr [rbp - 1874], 0
    mov byte ptr [rbp - 1875], 0
    mov byte ptr [rbp - 1876], 0
    mov byte ptr [rbp - 1877], 0
    mov byte ptr [rbp - 1878], 0
    mov byte ptr [rbp - 1879], 0
    mov byte ptr [rbp - 1880], 0
    mov byte ptr [rbp - 1881], 0
    mov byte ptr [rbp - 1882], 0
    mov byte ptr [rbp - 1883], 0
    mov byte ptr [rbp - 1884], 0
    mov byte ptr [rbp - 1885], 0
    mov byte ptr [rbp - 1886], 0
    mov byte ptr [rbp - 1887], 0
    mov byte ptr [rbp - 1888], 0
    mov byte ptr [rbp - 1889], 0
    mov byte ptr [rbp - 1890], 0
    mov byte ptr [rbp - 1891], 0
    mov byte ptr [rbp - 1892], 0
    mov byte ptr [rbp - 1893], 0
    mov byte ptr [rbp - 1894], 0
    mov byte ptr [rbp - 1895], 0
    mov byte ptr [rbp - 1896], 0
    mov byte ptr [rbp - 1897], 0
    mov byte ptr [rbp - 1898], 0
    mov byte ptr [rbp - 1899], 0
    lea rdi, [rbp - 2025]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2026]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2027]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2028]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2029]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2030]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2031]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2032]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2033]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2034]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2035]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2036]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2037]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2038]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2039]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2040]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2041]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2042]
    mov ecx, 1
    xor eax, eax
    rep stosb
    lea rdi, [rbp - 2043]
    mov ecx, 1
    xor eax, eax
    rep stosb
    mov rdi, r10
    mov rcx, r11
    mov byte ptr [rbp - 1689], 1
    mov byte ptr [rbp - 1690], 1
    mov byte ptr [rbp - 1691], 1
    mov byte ptr [rbp - 1692], 1
    mov byte ptr [rbp - 1693], 1
    mov byte ptr [rbp - 1694], 1
    mov byte ptr [rbp - 1695], 1
    mov r15, qword ptr [rip + __s3_instruction_remaining]
    jmp .L_s3_f25_energy_series_aggregation_b5_entry
.L_s3_f25_energy_series_aggregation_b5_entry:
    dec r15
    js .L__s3_failure_site_11
    cmp byte ptr [rbp - 1690], 0
    je .L__s3_failure_site_12
    mov rax, rdi
    mov rcx, rax
    mov byte ptr [rbp - 1696], 1
    dec r15
    js .L__s3_failure_site_13
    mov r8, 0
    mov byte ptr [rbp - 1697], 1
    dec r15
    js .L__s3_failure_site_14
    cmp byte ptr [rbp - 1697], 0
    je .L__s3_failure_site_15
    mov rax, r8
    cmp byte ptr [rbp - 1696], 0
    je .L__s3_failure_site_16
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_17
    mov qword ptr [rbp + rax*8 - 1912], r10
    mov byte ptr [rbp + rax - 2025], 1
    dec r15
    js .L__s3_failure_site_18
    cmp byte ptr [rbp - 1692], 0
    je .L__s3_failure_site_19
    mov rax, rdx
    mov rcx, rax
    mov byte ptr [rbp - 1698], 1
    dec r15
    js .L__s3_failure_site_20
    mov r8, 0
    mov byte ptr [rbp - 1699], 1
    dec r15
    js .L__s3_failure_site_21
    cmp byte ptr [rbp - 1699], 0
    je .L__s3_failure_site_22
    mov rax, r8
    cmp byte ptr [rbp - 1698], 0
    je .L__s3_failure_site_23
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_24
    mov qword ptr [rbp + rax*8 - 1920], r10
    mov byte ptr [rbp + rax - 2026], 1
    dec r15
    js .L__s3_failure_site_25
    cmp byte ptr [rbp - 1695], 0
    je .L__s3_failure_site_26
    mov rax, r12
    mov rcx, rax
    mov byte ptr [rbp - 1700], 1
    dec r15
    js .L__s3_failure_site_27
    mov r8, 0
    mov byte ptr [rbp - 1701], 1
    dec r15
    js .L__s3_failure_site_28
    cmp byte ptr [rbp - 1701], 0
    je .L__s3_failure_site_29
    mov rax, r8
    cmp byte ptr [rbp - 1700], 0
    je .L__s3_failure_site_30
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_31
    mov qword ptr [rbp + rax*8 - 1928], r10
    mov byte ptr [rbp + rax - 2027], 1
    dec r15
    js .L__s3_failure_site_32
    mov rcx, 0
    mov byte ptr [rbp - 1702], 1
    dec r15
    js .L__s3_failure_site_33
    cmp byte ptr [rbp - 1702], 0
    je .L__s3_failure_site_35
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_36
    cmp byte ptr [rbp + r10 - 2025], 0
    je .L__s3_failure_site_34
    mov rax, qword ptr [rbp + r10*8 - 1912]
    mov rcx, rax
    mov byte ptr [rbp - 1703], 1
    dec r15
    js .L__s3_failure_site_37
    mov r8, 364
    mov byte ptr [rbp - 1704], 1
    dec r15
    js .L__s3_failure_site_38
    cmp byte ptr [rbp - 1703], 0
    je .L__s3_failure_site_39
    mov rax, rcx
    cmp byte ptr [rbp - 1704], 0
    je .L__s3_failure_site_40
    mov r10, r8
    dec r15
    js .L__s3_failure_site_41
    cmp rax, r10
    jl .L_s3_f25_energy_series_aggregation_b9_rel_neg_0
    jg .L_s3_f25_energy_series_aggregation_b9_rel_pos_2
    jmp .L_s3_f25_energy_series_aggregation_b10_rel_zero_1
.L_s3_f25_energy_series_aggregation_b9_rel_neg_0:
    dec r15
    js .L__s3_failure_site_42
    mov rcx, 0
    mov byte ptr [rbp - 1706], 1
    dec r15
    js .L__s3_failure_site_43
    mov r8, 0
    mov byte ptr [rbp - 1707], 1
    dec r15
    js .L__s3_failure_site_44
    cmp byte ptr [rbp - 1706], 0
    je .L__s3_failure_site_45
    mov rax, rcx
    cmp byte ptr [rbp - 1707], 0
    je .L__s3_failure_site_46
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_47
    cmp r10, -1
    jl .L__s3_failure_site_48
    cmp r10, 1
    jg .L__s3_failure_site_48
    mov byte ptr [rbp + rax - 1929], r10b
    mov byte ptr [rbp + rax - 2028], 1
    dec r15
    js .L__s3_failure_site_49
    jmp .L_s3_f25_energy_series_aggregation_b10_rel_cont_3
.L_s3_f25_energy_series_aggregation_b10_rel_zero_1:
    dec r15
    js .L__s3_failure_site_50
    mov rcx, 0
    mov byte ptr [rbp - 1708], 1
    dec r15
    js .L__s3_failure_site_51
    mov r8, 0
    mov byte ptr [rbp - 1709], 1
    dec r15
    js .L__s3_failure_site_52
    cmp byte ptr [rbp - 1708], 0
    je .L__s3_failure_site_53
    mov rax, rcx
    cmp byte ptr [rbp - 1709], 0
    je .L__s3_failure_site_54
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_55
    cmp r10, -1
    jl .L__s3_failure_site_56
    cmp r10, 1
    jg .L__s3_failure_site_56
    mov byte ptr [rbp + rax - 1929], r10b
    mov byte ptr [rbp + rax - 2028], 1
    dec r15
    js .L__s3_failure_site_57
    jmp .L_s3_f25_energy_series_aggregation_b10_rel_cont_3
.L_s3_f25_energy_series_aggregation_b9_rel_pos_2:
    dec r15
    js .L__s3_failure_site_58
    mov rcx, 0
    mov byte ptr [rbp - 1710], 1
    dec r15
    js .L__s3_failure_site_59
    mov r8, -1
    mov byte ptr [rbp - 1711], 1
    dec r15
    js .L__s3_failure_site_60
    cmp byte ptr [rbp - 1710], 0
    je .L__s3_failure_site_61
    mov rax, rcx
    cmp byte ptr [rbp - 1711], 0
    je .L__s3_failure_site_62
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_63
    cmp r10, -1
    jl .L__s3_failure_site_64
    cmp r10, 1
    jg .L__s3_failure_site_64
    mov byte ptr [rbp + rax - 1929], r10b
    mov byte ptr [rbp + rax - 2028], 1
    dec r15
    js .L__s3_failure_site_65
    jmp .L_s3_f25_energy_series_aggregation_b10_rel_cont_3
.L_s3_f25_energy_series_aggregation_b10_rel_cont_3:
    dec r15
    js .L__s3_failure_site_66
    mov rcx, 0
    mov byte ptr [rbp - 1712], 1
    dec r15
    js .L__s3_failure_site_67
    cmp byte ptr [rbp - 1712], 0
    je .L__s3_failure_site_69
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_70
    cmp byte ptr [rbp + r10 - 2028], 0
    je .L__s3_failure_site_68
    movsx rax, byte ptr [rbp + r10 - 1929]
    mov rcx, rax
    mov byte ptr [rbp - 1713], 1
    dec r15
    js .L__s3_failure_site_71
    cmp byte ptr [rbp - 1713], 0
    je .L__s3_failure_site_73
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b17_switch_negative_4
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b16_switch_neutral_5
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b17_switch_positive_6
    jmp .L__s3_failure_site_72
.L_s3_f25_energy_series_aggregation_b17_switch_negative_4:
    dec r15
    js .L__s3_failure_site_74
    mov rcx, 0
    mov byte ptr [rbp - 1714], 1
    dec r15
    js .L__s3_failure_site_75
    mov r8, 0
    mov byte ptr [rbp - 1715], 1
    dec r15
    js .L__s3_failure_site_76
    cmp byte ptr [rbp - 1715], 0
    je .L__s3_failure_site_77
    mov rax, r8
    cmp byte ptr [rbp - 1714], 0
    je .L__s3_failure_site_78
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_79
    mov qword ptr [rbp + rax*8 - 1912], r10
    mov byte ptr [rbp + rax - 2025], 1
    dec r15
    js .L__s3_failure_site_80
    jmp .L_s3_f25_energy_series_aggregation_b17_switch_continue_7
.L_s3_f25_energy_series_aggregation_b16_switch_neutral_5:
    dec r15
    js .L__s3_failure_site_81
    mov rcx, 0
    mov byte ptr [rbp - 1716], 1
    dec r15
    js .L__s3_failure_site_82
    cmp byte ptr [rbp - 1716], 0
    je .L__s3_failure_site_84
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_85
    cmp byte ptr [rbp + r10 - 2025], 0
    je .L__s3_failure_site_83
    mov rax, qword ptr [rbp + r10*8 - 1912]
    mov rcx, rax
    mov byte ptr [rbp - 1717], 1
    dec r15
    js .L__s3_failure_site_86
    mov r8, 0
    mov byte ptr [rbp - 1718], 1
    dec r15
    js .L__s3_failure_site_87
    cmp byte ptr [rbp - 1718], 0
    je .L__s3_failure_site_88
    mov rax, r8
    cmp byte ptr [rbp - 1717], 0
    je .L__s3_failure_site_89
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_90
    mov qword ptr [rbp + rax*8 - 1912], r10
    mov byte ptr [rbp + rax - 2025], 1
    dec r15
    js .L__s3_failure_site_91
    jmp .L_s3_f25_energy_series_aggregation_b17_switch_continue_7
.L_s3_f25_energy_series_aggregation_b17_switch_positive_6:
    dec r15
    js .L__s3_failure_site_92
    mov rcx, 0
    mov byte ptr [rbp - 1719], 1
    dec r15
    js .L__s3_failure_site_93
    cmp byte ptr [rbp - 1719], 0
    je .L__s3_failure_site_95
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_96
    cmp byte ptr [rbp + r10 - 2025], 0
    je .L__s3_failure_site_94
    mov rax, qword ptr [rbp + r10*8 - 1912]
    mov rcx, rax
    mov byte ptr [rbp - 1720], 1
    dec r15
    js .L__s3_failure_site_97
    mov r8, 0
    mov byte ptr [rbp - 1721], 1
    dec r15
    js .L__s3_failure_site_98
    cmp byte ptr [rbp - 1721], 0
    je .L__s3_failure_site_99
    mov rax, r8
    cmp byte ptr [rbp - 1720], 0
    je .L__s3_failure_site_100
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_101
    mov qword ptr [rbp + rax*8 - 1912], r10
    mov byte ptr [rbp + rax - 2025], 1
    dec r15
    js .L__s3_failure_site_102
    jmp .L_s3_f25_energy_series_aggregation_b17_switch_continue_7
.L_s3_f25_energy_series_aggregation_b17_switch_continue_7:
    dec r15
    js .L__s3_failure_site_103
    mov rcx, 0
    mov byte ptr [rbp - 1722], 1
    dec r15
    js .L__s3_failure_site_104
    cmp byte ptr [rbp - 1722], 0
    je .L__s3_failure_site_106
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_107
    cmp byte ptr [rbp + r10 - 2025], 0
    je .L__s3_failure_site_105
    mov rax, qword ptr [rbp + r10*8 - 1912]
    mov rcx, rax
    mov byte ptr [rbp - 1723], 1
    dec r15
    js .L__s3_failure_site_108
    mov r8, 0
    mov byte ptr [rbp - 1724], 1
    dec r15
    js .L__s3_failure_site_109
    cmp byte ptr [rbp - 1723], 0
    je .L__s3_failure_site_110
    mov rax, rcx
    cmp byte ptr [rbp - 1724], 0
    je .L__s3_failure_site_111
    mov r10, r8
    dec r15
    js .L__s3_failure_site_112
    cmp rax, r10
    jl .L_s3_f25_energy_series_aggregation_b9_rel_neg_8
    jg .L_s3_f25_energy_series_aggregation_b10_rel_pos_10
    jmp .L_s3_f25_energy_series_aggregation_b10_rel_zero_9
.L_s3_f25_energy_series_aggregation_b9_rel_neg_8:
    dec r15
    js .L__s3_failure_site_113
    mov rcx, 0
    mov byte ptr [rbp - 1726], 1
    dec r15
    js .L__s3_failure_site_114
    mov r8, -1
    mov byte ptr [rbp - 1727], 1
    dec r15
    js .L__s3_failure_site_115
    cmp byte ptr [rbp - 1726], 0
    je .L__s3_failure_site_116
    mov rax, rcx
    cmp byte ptr [rbp - 1727], 0
    je .L__s3_failure_site_117
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_118
    cmp r10, -1
    jl .L__s3_failure_site_119
    cmp r10, 1
    jg .L__s3_failure_site_119
    mov byte ptr [rbp + rax - 1930], r10b
    mov byte ptr [rbp + rax - 2029], 1
    dec r15
    js .L__s3_failure_site_120
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_11
.L_s3_f25_energy_series_aggregation_b10_rel_zero_9:
    dec r15
    js .L__s3_failure_site_121
    mov rcx, 0
    mov byte ptr [rbp - 1728], 1
    dec r15
    js .L__s3_failure_site_122
    mov r8, -1
    mov byte ptr [rbp - 1729], 1
    dec r15
    js .L__s3_failure_site_123
    cmp byte ptr [rbp - 1728], 0
    je .L__s3_failure_site_124
    mov rax, rcx
    cmp byte ptr [rbp - 1729], 0
    je .L__s3_failure_site_125
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_126
    cmp r10, -1
    jl .L__s3_failure_site_127
    cmp r10, 1
    jg .L__s3_failure_site_127
    mov byte ptr [rbp + rax - 1930], r10b
    mov byte ptr [rbp + rax - 2029], 1
    dec r15
    js .L__s3_failure_site_128
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_11
.L_s3_f25_energy_series_aggregation_b10_rel_pos_10:
    dec r15
    js .L__s3_failure_site_129
    mov rcx, 0
    mov byte ptr [rbp - 1730], 1
    dec r15
    js .L__s3_failure_site_130
    mov r8, 0
    mov byte ptr [rbp - 1731], 1
    dec r15
    js .L__s3_failure_site_131
    cmp byte ptr [rbp - 1730], 0
    je .L__s3_failure_site_132
    mov rax, rcx
    cmp byte ptr [rbp - 1731], 0
    je .L__s3_failure_site_133
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_134
    cmp r10, -1
    jl .L__s3_failure_site_135
    cmp r10, 1
    jg .L__s3_failure_site_135
    mov byte ptr [rbp + rax - 1930], r10b
    mov byte ptr [rbp + rax - 2029], 1
    dec r15
    js .L__s3_failure_site_136
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_11
.L_s3_f25_energy_series_aggregation_b11_rel_cont_11:
    dec r15
    js .L__s3_failure_site_137
    mov rcx, 0
    mov byte ptr [rbp - 1732], 1
    dec r15
    js .L__s3_failure_site_138
    cmp byte ptr [rbp - 1732], 0
    je .L__s3_failure_site_140
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_141
    cmp byte ptr [rbp + r10 - 2029], 0
    je .L__s3_failure_site_139
    movsx rax, byte ptr [rbp + r10 - 1930]
    mov rcx, rax
    mov byte ptr [rbp - 1733], 1
    dec r15
    js .L__s3_failure_site_142
    cmp byte ptr [rbp - 1733], 0
    je .L__s3_failure_site_144
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b18_switch_negative_12
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b17_switch_neutral_13
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b18_switch_positive_14
    jmp .L__s3_failure_site_143
.L_s3_f25_energy_series_aggregation_b18_switch_negative_12:
    dec r15
    js .L__s3_failure_site_145
    mov rdi, 1
    mov byte ptr [rbp - 1734], 1
    dec r15
    js .L__s3_failure_site_146
    cmp byte ptr [rbp - 1734], 0
    je .L__s3_failure_site_147
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b17_switch_neutral_13:
    dec r15
    js .L__s3_failure_site_148
    mov rcx, 0
    mov byte ptr [rbp - 1735], 1
    dec r15
    js .L__s3_failure_site_149
    cmp byte ptr [rbp - 1735], 0
    je .L__s3_failure_site_151
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_152
    cmp byte ptr [rbp + r10 - 2026], 0
    je .L__s3_failure_site_150
    mov rax, qword ptr [rbp + r10*8 - 1920]
    mov rcx, rax
    mov byte ptr [rbp - 1736], 1
    dec r15
    js .L__s3_failure_site_153
    mov r8, 0
    mov byte ptr [rbp - 1737], 1
    dec r15
    js .L__s3_failure_site_154
    cmp byte ptr [rbp - 1737], 0
    je .L__s3_failure_site_156
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_157
    cmp byte ptr [rbp + r10 - 2025], 0
    je .L__s3_failure_site_155
    mov rax, qword ptr [rbp + r10*8 - 1912]
    mov r8, rax
    mov byte ptr [rbp - 1738], 1
    dec r15
    js .L__s3_failure_site_158
    cmp byte ptr [rbp - 1736], 0
    je .L__s3_failure_site_159
    mov rax, rcx
    cmp byte ptr [rbp - 1738], 0
    je .L__s3_failure_site_160
    mov r10, r8
    dec r15
    js .L__s3_failure_site_161
    cmp rax, r10
    jl .L_s3_f25_energy_series_aggregation_b10_rel_neg_15
    jg .L_s3_f25_energy_series_aggregation_b10_rel_pos_17
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_zero_16
.L_s3_f25_energy_series_aggregation_b18_switch_positive_14:
    dec r15
    js .L__s3_failure_site_162
    mov rdi, 1
    mov byte ptr [rbp - 1899], 1
    dec r15
    js .L__s3_failure_site_163
    cmp byte ptr [rbp - 1899], 0
    je .L__s3_failure_site_164
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b10_rel_neg_15:
    dec r15
    js .L__s3_failure_site_165
    mov rcx, 0
    mov byte ptr [rbp - 1740], 1
    dec r15
    js .L__s3_failure_site_166
    mov r8, 0
    mov byte ptr [rbp - 1741], 1
    dec r15
    js .L__s3_failure_site_167
    cmp byte ptr [rbp - 1740], 0
    je .L__s3_failure_site_168
    mov rax, rcx
    cmp byte ptr [rbp - 1741], 0
    je .L__s3_failure_site_169
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_170
    cmp r10, -1
    jl .L__s3_failure_site_171
    cmp r10, 1
    jg .L__s3_failure_site_171
    mov byte ptr [rbp + rax - 1931], r10b
    mov byte ptr [rbp + rax - 2030], 1
    dec r15
    js .L__s3_failure_site_172
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_18
.L_s3_f25_energy_series_aggregation_b11_rel_zero_16:
    dec r15
    js .L__s3_failure_site_173
    mov rcx, 0
    mov byte ptr [rbp - 1742], 1
    dec r15
    js .L__s3_failure_site_174
    mov r8, -1
    mov byte ptr [rbp - 1743], 1
    dec r15
    js .L__s3_failure_site_175
    cmp byte ptr [rbp - 1742], 0
    je .L__s3_failure_site_176
    mov rax, rcx
    cmp byte ptr [rbp - 1743], 0
    je .L__s3_failure_site_177
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_178
    cmp r10, -1
    jl .L__s3_failure_site_179
    cmp r10, 1
    jg .L__s3_failure_site_179
    mov byte ptr [rbp + rax - 1931], r10b
    mov byte ptr [rbp + rax - 2030], 1
    dec r15
    js .L__s3_failure_site_180
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_18
.L_s3_f25_energy_series_aggregation_b10_rel_pos_17:
    dec r15
    js .L__s3_failure_site_181
    mov rcx, 0
    mov byte ptr [rbp - 1744], 1
    dec r15
    js .L__s3_failure_site_182
    mov r8, 0
    mov byte ptr [rbp - 1745], 1
    dec r15
    js .L__s3_failure_site_183
    cmp byte ptr [rbp - 1744], 0
    je .L__s3_failure_site_184
    mov rax, rcx
    cmp byte ptr [rbp - 1745], 0
    je .L__s3_failure_site_185
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_186
    cmp r10, -1
    jl .L__s3_failure_site_187
    cmp r10, 1
    jg .L__s3_failure_site_187
    mov byte ptr [rbp + rax - 1931], r10b
    mov byte ptr [rbp + rax - 2030], 1
    dec r15
    js .L__s3_failure_site_188
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_18
.L_s3_f25_energy_series_aggregation_b11_rel_cont_18:
    dec r15
    js .L__s3_failure_site_189
    mov rcx, 0
    mov byte ptr [rbp - 1746], 1
    dec r15
    js .L__s3_failure_site_190
    cmp byte ptr [rbp - 1746], 0
    je .L__s3_failure_site_192
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_193
    cmp byte ptr [rbp + r10 - 2030], 0
    je .L__s3_failure_site_191
    movsx rax, byte ptr [rbp + r10 - 1931]
    mov rcx, rax
    mov byte ptr [rbp - 1747], 1
    dec r15
    js .L__s3_failure_site_194
    cmp byte ptr [rbp - 1747], 0
    je .L__s3_failure_site_196
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b18_switch_negative_19
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b17_switch_neutral_20
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b18_switch_positive_21
    jmp .L__s3_failure_site_195
.L_s3_f25_energy_series_aggregation_b18_switch_negative_19:
    dec r15
    js .L__s3_failure_site_197
    mov rcx, 0
    mov byte ptr [rbp - 1748], 1
    dec r15
    js .L__s3_failure_site_198
    cmp byte ptr [rbp - 1748], 0
    je .L__s3_failure_site_200
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_201
    cmp byte ptr [rbp + r10 - 2027], 0
    je .L__s3_failure_site_199
    mov rax, qword ptr [rbp + r10*8 - 1928]
    mov rcx, rax
    mov byte ptr [rbp - 1749], 1
    dec r15
    js .L__s3_failure_site_202
    mov r8, 5
    mov byte ptr [rbp - 1750], 1
    dec r15
    js .L__s3_failure_site_203
    cmp byte ptr [rbp - 1749], 0
    je .L__s3_failure_site_204
    mov rax, rcx
    cmp byte ptr [rbp - 1750], 0
    je .L__s3_failure_site_205
    mov r10, r8
    dec r15
    js .L__s3_failure_site_206
    cmp rax, r10
    jl .L_s3_f25_energy_series_aggregation_b10_rel_neg_22
    jg .L_s3_f25_energy_series_aggregation_b10_rel_pos_24
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_zero_23
.L_s3_f25_energy_series_aggregation_b17_switch_neutral_20:
    dec r15
    js .L__s3_failure_site_207
    mov rdi, 2
    mov byte ptr [rbp - 1897], 1
    dec r15
    js .L__s3_failure_site_208
    cmp byte ptr [rbp - 1897], 0
    je .L__s3_failure_site_209
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b18_switch_positive_21:
    dec r15
    js .L__s3_failure_site_210
    mov rdi, 2
    mov byte ptr [rbp - 1898], 1
    dec r15
    js .L__s3_failure_site_211
    cmp byte ptr [rbp - 1898], 0
    je .L__s3_failure_site_212
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b10_rel_neg_22:
    dec r15
    js .L__s3_failure_site_213
    mov rcx, 0
    mov byte ptr [rbp - 1752], 1
    dec r15
    js .L__s3_failure_site_214
    mov r8, 0
    mov byte ptr [rbp - 1753], 1
    dec r15
    js .L__s3_failure_site_215
    cmp byte ptr [rbp - 1752], 0
    je .L__s3_failure_site_216
    mov rax, rcx
    cmp byte ptr [rbp - 1753], 0
    je .L__s3_failure_site_217
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_218
    cmp r10, -1
    jl .L__s3_failure_site_219
    cmp r10, 1
    jg .L__s3_failure_site_219
    mov byte ptr [rbp + rax - 1932], r10b
    mov byte ptr [rbp + rax - 2031], 1
    dec r15
    js .L__s3_failure_site_220
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_25
.L_s3_f25_energy_series_aggregation_b11_rel_zero_23:
    dec r15
    js .L__s3_failure_site_221
    mov rcx, 0
    mov byte ptr [rbp - 1754], 1
    dec r15
    js .L__s3_failure_site_222
    mov r8, -1
    mov byte ptr [rbp - 1755], 1
    dec r15
    js .L__s3_failure_site_223
    cmp byte ptr [rbp - 1754], 0
    je .L__s3_failure_site_224
    mov rax, rcx
    cmp byte ptr [rbp - 1755], 0
    je .L__s3_failure_site_225
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_226
    cmp r10, -1
    jl .L__s3_failure_site_227
    cmp r10, 1
    jg .L__s3_failure_site_227
    mov byte ptr [rbp + rax - 1932], r10b
    mov byte ptr [rbp + rax - 2031], 1
    dec r15
    js .L__s3_failure_site_228
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_25
.L_s3_f25_energy_series_aggregation_b10_rel_pos_24:
    dec r15
    js .L__s3_failure_site_229
    mov rcx, 0
    mov byte ptr [rbp - 1756], 1
    dec r15
    js .L__s3_failure_site_230
    mov r8, 0
    mov byte ptr [rbp - 1757], 1
    dec r15
    js .L__s3_failure_site_231
    cmp byte ptr [rbp - 1756], 0
    je .L__s3_failure_site_232
    mov rax, rcx
    cmp byte ptr [rbp - 1757], 0
    je .L__s3_failure_site_233
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_234
    cmp r10, -1
    jl .L__s3_failure_site_235
    cmp r10, 1
    jg .L__s3_failure_site_235
    mov byte ptr [rbp + rax - 1932], r10b
    mov byte ptr [rbp + rax - 2031], 1
    dec r15
    js .L__s3_failure_site_236
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_25
.L_s3_f25_energy_series_aggregation_b11_rel_cont_25:
    dec r15
    js .L__s3_failure_site_237
    mov rcx, 0
    mov byte ptr [rbp - 1758], 1
    dec r15
    js .L__s3_failure_site_238
    cmp byte ptr [rbp - 1758], 0
    je .L__s3_failure_site_240
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_241
    cmp byte ptr [rbp + r10 - 2031], 0
    je .L__s3_failure_site_239
    movsx rax, byte ptr [rbp + r10 - 1932]
    mov rcx, rax
    mov byte ptr [rbp - 1759], 1
    dec r15
    js .L__s3_failure_site_242
    cmp byte ptr [rbp - 1759], 0
    je .L__s3_failure_site_244
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b18_switch_negative_26
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b17_switch_neutral_27
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b18_switch_positive_28
    jmp .L__s3_failure_site_243
.L_s3_f25_energy_series_aggregation_b18_switch_negative_26:
    dec r15
    js .L__s3_failure_site_245
    movabs rax, 0
    mov rcx, rax
    mov byte ptr [rbp - 1760], 1
    dec r15
    js .L__s3_failure_site_246
    cmp byte ptr [rbp - 1693], 0
    je .L__s3_failure_site_247
    mov rax, r13
    cmp byte ptr [rbp - 1760], 0
    je .L__s3_failure_site_248
    mov r10, rcx
    movq xmm0, rax
    movq xmm1, r10
    ucomisd xmm0, xmm1
    setbe al
    setnp r11b
    and al, r11b
    movzx r11, al
    neg r11
    mov rcx, r11
    mov byte ptr [rbp - 1761], 1
    dec r15
    js .L__s3_failure_site_249
    cmp byte ptr [rbp - 1761], 0
    je .L__s3_failure_site_251
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b18_switch_negative_29
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b17_switch_neutral_30
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b18_switch_positive_31
    jmp .L__s3_failure_site_250
.L_s3_f25_energy_series_aggregation_b17_switch_neutral_27:
    dec r15
    js .L__s3_failure_site_252
    mov rdi, 2
    mov byte ptr [rbp - 1895], 1
    dec r15
    js .L__s3_failure_site_253
    cmp byte ptr [rbp - 1895], 0
    je .L__s3_failure_site_254
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b18_switch_positive_28:
    dec r15
    js .L__s3_failure_site_255
    mov rdi, 2
    mov byte ptr [rbp - 1896], 1
    dec r15
    js .L__s3_failure_site_256
    cmp byte ptr [rbp - 1896], 0
    je .L__s3_failure_site_257
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b18_switch_negative_29:
    dec r15
    js .L__s3_failure_site_258
    mov rdi, 1
    mov byte ptr [rbp - 1762], 1
    dec r15
    js .L__s3_failure_site_259
    cmp byte ptr [rbp - 1762], 0
    je .L__s3_failure_site_260
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b17_switch_neutral_30:
    dec r15
    js .L__s3_failure_site_261
    mov rcx, 0
    mov byte ptr [rbp - 1763], 1
    dec r15
    js .L__s3_failure_site_262
    mov r8, 0
    mov byte ptr [rbp - 1764], 1
    dec r15
    js .L__s3_failure_site_263
    cmp byte ptr [rbp - 1764], 0
    je .L__s3_failure_site_264
    mov rax, r8
    cmp byte ptr [rbp - 1763], 0
    je .L__s3_failure_site_265
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_266
    mov qword ptr [rbp + rax*8 - 1944], r10
    mov byte ptr [rbp + rax - 2032], 1
    dec r15
    js .L__s3_failure_site_267
    movabs rax, 0
    mov rcx, rax
    mov byte ptr [rbp - 1765], 1
    dec r15
    js .L__s3_failure_site_268
    mov r8, 0
    mov byte ptr [rbp - 1766], 1
    dec r15
    js .L__s3_failure_site_269
    cmp byte ptr [rbp - 1766], 0
    je .L__s3_failure_site_270
    mov rax, r8
    cmp byte ptr [rbp - 1765], 0
    je .L__s3_failure_site_271
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_272
    mov qword ptr [rbp + rax*8 - 1952], r10
    mov byte ptr [rbp + rax - 2033], 1
    dec r15
    js .L__s3_failure_site_273
    movabs rax, 0
    mov rcx, rax
    mov byte ptr [rbp - 1767], 1
    dec r15
    js .L__s3_failure_site_274
    mov r8, 0
    mov byte ptr [rbp - 1768], 1
    dec r15
    js .L__s3_failure_site_275
    cmp byte ptr [rbp - 1768], 0
    je .L__s3_failure_site_276
    mov rax, r8
    cmp byte ptr [rbp - 1767], 0
    je .L__s3_failure_site_277
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_278
    mov qword ptr [rbp + rax*8 - 1960], r10
    mov byte ptr [rbp + rax - 2034], 1
    dec r15
    js .L__s3_failure_site_279
    movabs rax, 0
    mov rcx, rax
    mov byte ptr [rbp - 1769], 1
    dec r15
    js .L__s3_failure_site_280
    mov r8, 0
    mov byte ptr [rbp - 1770], 1
    dec r15
    js .L__s3_failure_site_281
    cmp byte ptr [rbp - 1770], 0
    je .L__s3_failure_site_282
    mov rax, r8
    cmp byte ptr [rbp - 1769], 0
    je .L__s3_failure_site_283
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_284
    mov qword ptr [rbp + rax*8 - 1968], r10
    mov byte ptr [rbp + rax - 2035], 1
    dec r15
    js .L__s3_failure_site_285
    mov rcx, 1
    mov byte ptr [rbp - 1771], 1
    dec r15
    js .L__s3_failure_site_286
    mov r8, 0
    mov byte ptr [rbp - 1772], 1
    dec r15
    js .L__s3_failure_site_287
    cmp byte ptr [rbp - 1772], 0
    je .L__s3_failure_site_288
    mov rax, r8
    cmp byte ptr [rbp - 1771], 0
    je .L__s3_failure_site_289
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_290
    mov qword ptr [rbp + rax*8 - 1976], r10
    mov byte ptr [rbp + rax - 2036], 1
    dec r15
    js .L__s3_failure_site_291
    movabs rax, 0
    mov rcx, rax
    mov byte ptr [rbp - 1773], 1
    dec r15
    js .L__s3_failure_site_292
    mov r8, 0
    mov byte ptr [rbp - 1774], 1
    dec r15
    js .L__s3_failure_site_293
    cmp byte ptr [rbp - 1774], 0
    je .L__s3_failure_site_294
    mov rax, r8
    cmp byte ptr [rbp - 1773], 0
    je .L__s3_failure_site_295
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_296
    mov qword ptr [rbp + rax*8 - 1984], r10
    mov byte ptr [rbp + rax - 2037], 1
    dec r15
    js .L__s3_failure_site_297
    jmp .L_s3_f25_energy_series_aggregation_b18_while_condition_32
.L_s3_f25_energy_series_aggregation_b18_switch_positive_31:
    dec r15
    js .L__s3_failure_site_298
    mov rdi, 1
    mov byte ptr [rbp - 1894], 1
    dec r15
    js .L__s3_failure_site_299
    cmp byte ptr [rbp - 1894], 0
    je .L__s3_failure_site_300
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b18_while_condition_32:
    dec r15
    js .L__s3_failure_site_301
    mov rcx, 0
    mov byte ptr [rbp - 1775], 1
    dec r15
    js .L__s3_failure_site_302
    cmp byte ptr [rbp - 1775], 0
    je .L__s3_failure_site_304
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_305
    cmp byte ptr [rbp + r10 - 2032], 0
    je .L__s3_failure_site_303
    mov rax, qword ptr [rbp + r10*8 - 1944]
    mov rcx, rax
    mov byte ptr [rbp - 1776], 1
    dec r15
    js .L__s3_failure_site_306
    mov r8, 0
    mov byte ptr [rbp - 1777], 1
    dec r15
    js .L__s3_failure_site_307
    cmp byte ptr [rbp - 1777], 0
    je .L__s3_failure_site_309
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_310
    cmp byte ptr [rbp + r10 - 2025], 0
    je .L__s3_failure_site_308
    mov rax, qword ptr [rbp + r10*8 - 1912]
    mov r8, rax
    mov byte ptr [rbp - 1778], 1
    dec r15
    js .L__s3_failure_site_311
    cmp byte ptr [rbp - 1776], 0
    je .L__s3_failure_site_312
    mov rax, rcx
    cmp byte ptr [rbp - 1778], 0
    je .L__s3_failure_site_313
    mov r10, r8
    dec r15
    js .L__s3_failure_site_314
    cmp rax, r10
    jl .L_s3_f25_energy_series_aggregation_b10_rel_neg_37
    jg .L_s3_f25_energy_series_aggregation_b10_rel_pos_39
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_zero_38
.L_s3_f25_energy_series_aggregation_b13_while_body_33:
    dec r15
    js .L__s3_failure_site_315
    mov rcx, 0
    mov byte ptr [rbp - 1788], 1
    dec r15
    js .L__s3_failure_site_316
    cmp byte ptr [rbp - 1788], 0
    je .L__s3_failure_site_318
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_319
    cmp byte ptr [rbp + r10 - 2032], 0
    je .L__s3_failure_site_317
    mov rax, qword ptr [rbp + r10*8 - 1944]
    mov rcx, rax
    mov byte ptr [rbp - 1789], 1
    dec r15
    js .L__s3_failure_site_320
    cmp byte ptr [rbp - 1789], 0
    je .L__s3_failure_site_322
    mov rax, rcx
    cmp rax, -364
    jl .L__s3_failure_site_321
    cmp rax, 364
    jg .L__s3_failure_site_321
    mov rcx, rax
    mov byte ptr [rbp - 1790], 1
    dec r15
    js .L__s3_failure_site_323
    mov r8, 0
    mov byte ptr [rbp - 1791], 1
    dec r15
    js .L__s3_failure_site_324
    cmp byte ptr [rbp - 1791], 0
    je .L__s3_failure_site_325
    mov rax, r8
    cmp byte ptr [rbp - 1790], 0
    je .L__s3_failure_site_326
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_327
    cmp r10, -364
    jl .L__s3_failure_site_328
    cmp r10, 364
    jg .L__s3_failure_site_328
    mov word ptr [rbp + rax*2 - 1988], r10w
    mov byte ptr [rbp + rax - 2039], 1
    dec r15
    js .L__s3_failure_site_329
    mov rcx, 0
    mov byte ptr [rbp - 1792], 1
    dec r15
    js .L__s3_failure_site_330
    cmp byte ptr [rbp - 1792], 0
    je .L__s3_failure_site_332
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_333
    cmp byte ptr [rbp + r10 - 2039], 0
    je .L__s3_failure_site_331
    movsx rax, word ptr [rbp + r10*2 - 1988]
    mov rcx, rax
    mov byte ptr [rbp - 1793], 1
    dec r15
    js .L__s3_failure_site_334
    cmp byte ptr [rbp - 1689], 0
    je .L__s3_failure_site_336
    cmp byte ptr [rbp - 1690], 0
    je .L__s3_failure_site_337
    cmp byte ptr [rbp - 1793], 0
    je .L__s3_failure_site_338
    mov rax, rcx
    cmp rax, rdi
    jae .L__s3_failure_site_335
    mov rcx, qword ptr [r14 + rax * 8]
    mov byte ptr [rbp - 1794], 1
    dec r15
    js .L__s3_failure_site_339
    mov r8, 0
    mov byte ptr [rbp - 1795], 1
    dec r15
    js .L__s3_failure_site_340
    cmp byte ptr [rbp - 1795], 0
    je .L__s3_failure_site_341
    mov rax, r8
    cmp byte ptr [rbp - 1794], 0
    je .L__s3_failure_site_342
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_343
    mov qword ptr [rbp + rax*8 - 2000], r10
    mov byte ptr [rbp + rax - 2040], 1
    dec r15
    js .L__s3_failure_site_344
    mov rcx, 0
    mov byte ptr [rbp - 1796], 1
    dec r15
    js .L__s3_failure_site_345
    cmp byte ptr [rbp - 1796], 0
    je .L__s3_failure_site_347
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_348
    cmp byte ptr [rbp + r10 - 2039], 0
    je .L__s3_failure_site_346
    movsx rax, word ptr [rbp + r10*2 - 1988]
    mov rcx, rax
    mov byte ptr [rbp - 1797], 1
    dec r15
    js .L__s3_failure_site_349
    cmp byte ptr [rbp - 1691], 0
    je .L__s3_failure_site_351
    cmp byte ptr [rbp - 1692], 0
    je .L__s3_failure_site_352
    cmp byte ptr [rbp - 1797], 0
    je .L__s3_failure_site_353
    mov rax, rcx
    cmp rax, rdx
    jae .L__s3_failure_site_350
    mov rcx, qword ptr [rsi + rax * 8]
    mov byte ptr [rbp - 1798], 1
    dec r15
    js .L__s3_failure_site_354
    mov r8, 0
    mov byte ptr [rbp - 1799], 1
    dec r15
    js .L__s3_failure_site_355
    cmp byte ptr [rbp - 1799], 0
    je .L__s3_failure_site_356
    mov rax, r8
    cmp byte ptr [rbp - 1798], 0
    je .L__s3_failure_site_357
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_358
    mov qword ptr [rbp + rax*8 - 2008], r10
    mov byte ptr [rbp + rax - 2041], 1
    dec r15
    js .L__s3_failure_site_359
    mov rcx, 0
    mov byte ptr [rbp - 1800], 1
    dec r15
    js .L__s3_failure_site_360
    cmp byte ptr [rbp - 1800], 0
    je .L__s3_failure_site_362
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_363
    cmp byte ptr [rbp + r10 - 2033], 0
    je .L__s3_failure_site_361
    mov rax, qword ptr [rbp + r10*8 - 1952]
    mov rcx, rax
    mov byte ptr [rbp - 1801], 1
    dec r15
    js .L__s3_failure_site_364
    mov r8, 0
    mov byte ptr [rbp - 1802], 1
    dec r15
    js .L__s3_failure_site_365
    cmp byte ptr [rbp - 1802], 0
    je .L__s3_failure_site_367
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_368
    cmp byte ptr [rbp + r10 - 2040], 0
    je .L__s3_failure_site_366
    mov rax, qword ptr [rbp + r10*8 - 2000]
    mov r8, rax
    mov byte ptr [rbp - 1803], 1
    dec r15
    js .L__s3_failure_site_369
    cmp byte ptr [rbp - 1801], 0
    je .L__s3_failure_site_370
    mov rax, rcx
    cmp byte ptr [rbp - 1803], 0
    je .L__s3_failure_site_371
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 1804], 1
    dec r15
    js .L__s3_failure_site_372
    mov r8, 0
    mov byte ptr [rbp - 1805], 1
    dec r15
    js .L__s3_failure_site_373
    cmp byte ptr [rbp - 1805], 0
    je .L__s3_failure_site_374
    mov rax, r8
    cmp byte ptr [rbp - 1804], 0
    je .L__s3_failure_site_375
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_376
    mov qword ptr [rbp + rax*8 - 1952], r10
    mov byte ptr [rbp + rax - 2033], 1
    dec r15
    js .L__s3_failure_site_377
    mov rcx, 0
    mov byte ptr [rbp - 1806], 1
    dec r15
    js .L__s3_failure_site_378
    cmp byte ptr [rbp - 1806], 0
    je .L__s3_failure_site_380
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_381
    cmp byte ptr [rbp + r10 - 2034], 0
    je .L__s3_failure_site_379
    mov rax, qword ptr [rbp + r10*8 - 1960]
    mov rcx, rax
    mov byte ptr [rbp - 1807], 1
    dec r15
    js .L__s3_failure_site_382
    mov r8, 0
    mov byte ptr [rbp - 1808], 1
    dec r15
    js .L__s3_failure_site_383
    cmp byte ptr [rbp - 1808], 0
    je .L__s3_failure_site_385
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_386
    cmp byte ptr [rbp + r10 - 2040], 0
    je .L__s3_failure_site_384
    mov rax, qword ptr [rbp + r10*8 - 2000]
    mov r8, rax
    mov byte ptr [rbp - 1809], 1
    dec r15
    js .L__s3_failure_site_387
    cmp byte ptr [rbp - 1807], 0
    je .L__s3_failure_site_388
    mov rax, rcx
    cmp byte ptr [rbp - 1809], 0
    je .L__s3_failure_site_389
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 1810], 1
    dec r15
    js .L__s3_failure_site_390
    mov r8, 0
    mov byte ptr [rbp - 1811], 1
    dec r15
    js .L__s3_failure_site_391
    cmp byte ptr [rbp - 1811], 0
    je .L__s3_failure_site_393
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_394
    cmp byte ptr [rbp + r10 - 2041], 0
    je .L__s3_failure_site_392
    mov rax, qword ptr [rbp + r10*8 - 2008]
    mov r8, rax
    mov byte ptr [rbp - 1812], 1
    dec r15
    js .L__s3_failure_site_395
    cmp byte ptr [rbp - 1810], 0
    je .L__s3_failure_site_396
    mov rax, rcx
    cmp byte ptr [rbp - 1812], 0
    je .L__s3_failure_site_397
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 1813], 1
    dec r15
    js .L__s3_failure_site_398
    mov r8, 0
    mov byte ptr [rbp - 1814], 1
    dec r15
    js .L__s3_failure_site_399
    cmp byte ptr [rbp - 1814], 0
    je .L__s3_failure_site_400
    mov rax, r8
    cmp byte ptr [rbp - 1813], 0
    je .L__s3_failure_site_401
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_402
    mov qword ptr [rbp + rax*8 - 1960], r10
    mov byte ptr [rbp + rax - 2034], 1
    dec r15
    js .L__s3_failure_site_403
    mov rcx, 0
    mov byte ptr [rbp - 1815], 1
    dec r15
    js .L__s3_failure_site_404
    cmp byte ptr [rbp - 1815], 0
    je .L__s3_failure_site_406
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_407
    cmp byte ptr [rbp + r10 - 2037], 0
    je .L__s3_failure_site_405
    mov rax, qword ptr [rbp + r10*8 - 1984]
    mov rcx, rax
    mov byte ptr [rbp - 1816], 1
    dec r15
    js .L__s3_failure_site_408
    mov r8, 0
    mov byte ptr [rbp - 1817], 1
    dec r15
    js .L__s3_failure_site_409
    cmp byte ptr [rbp - 1817], 0
    je .L__s3_failure_site_411
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_412
    cmp byte ptr [rbp + r10 - 2040], 0
    je .L__s3_failure_site_410
    mov rax, qword ptr [rbp + r10*8 - 2000]
    mov r8, rax
    mov byte ptr [rbp - 1818], 1
    dec r15
    js .L__s3_failure_site_413
    mov r9, 0
    mov byte ptr [rbp - 1819], 1
    dec r15
    js .L__s3_failure_site_414
    cmp byte ptr [rbp - 1819], 0
    je .L__s3_failure_site_416
    mov r10, r9
    cmp r10, 1
    jae .L__s3_failure_site_417
    cmp byte ptr [rbp + r10 - 2041], 0
    je .L__s3_failure_site_415
    mov rax, qword ptr [rbp + r10*8 - 2008]
    mov r9, rax
    mov byte ptr [rbp - 1820], 1
    dec r15
    js .L__s3_failure_site_418
    cmp byte ptr [rbp - 1818], 0
    je .L__s3_failure_site_419
    mov rax, r8
    cmp byte ptr [rbp - 1820], 0
    je .L__s3_failure_site_420
    mov r10, r9
    movq xmm0, rax
    movq xmm1, r10
    subsd xmm0, xmm1
    movq rax, xmm0
    mov r8, rax
    mov byte ptr [rbp - 1821], 1
    dec r15
    js .L__s3_failure_site_421
    mov qword ptr [rip + __s3_instruction_remaining], r15
    cmp byte ptr [rbp - 1821], 0
    je .L__s3_failure_site_422
    mov qword ptr [rbp - 1064], r8
    mov qword ptr [rbp - 2096], rdi
    mov qword ptr [rbp - 2104], rsi
    mov qword ptr [rbp - 2112], rdx
    mov qword ptr [rbp - 2120], rcx
    mov rax, qword ptr [rbp - 1064]
    movq xmm0, rax
    call s3_absolute_f64
    movq rax, xmm0
    mov rdi, qword ptr [rbp - 2096]
    mov rsi, qword ptr [rbp - 2104]
    mov rdx, qword ptr [rbp - 2112]
    mov rcx, qword ptr [rbp - 2120]
    mov r8, rax
    mov byte ptr [rbp - 1822], 1
    mov r15, qword ptr [rip + __s3_instruction_remaining]
    dec r15
    js .L__s3_failure_site_423
    cmp byte ptr [rbp - 1816], 0
    je .L__s3_failure_site_424
    mov rax, rcx
    cmp byte ptr [rbp - 1822], 0
    je .L__s3_failure_site_425
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    addsd xmm0, xmm1
    movq rax, xmm0
    mov rcx, rax
    mov byte ptr [rbp - 1823], 1
    dec r15
    js .L__s3_failure_site_426
    mov r8, 0
    mov byte ptr [rbp - 1824], 1
    dec r15
    js .L__s3_failure_site_427
    cmp byte ptr [rbp - 1824], 0
    je .L__s3_failure_site_428
    mov rax, r8
    cmp byte ptr [rbp - 1823], 0
    je .L__s3_failure_site_429
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_430
    mov qword ptr [rbp + rax*8 - 1984], r10
    mov byte ptr [rbp + rax - 2037], 1
    dec r15
    js .L__s3_failure_site_431
    mov rcx, 0
    mov byte ptr [rbp - 1825], 1
    dec r15
    js .L__s3_failure_site_432
    cmp byte ptr [rbp - 1825], 0
    je .L__s3_failure_site_434
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_435
    cmp byte ptr [rbp + r10 - 2036], 0
    je .L__s3_failure_site_433
    mov rax, qword ptr [rbp + r10*8 - 1976]
    mov rcx, rax
    mov byte ptr [rbp - 1826], 1
    dec r15
    js .L__s3_failure_site_436
    mov r8, 1
    mov byte ptr [rbp - 1827], 1
    dec r15
    js .L__s3_failure_site_437
    cmp byte ptr [rbp - 1826], 0
    je .L__s3_failure_site_438
    mov rax, rcx
    cmp byte ptr [rbp - 1827], 0
    je .L__s3_failure_site_439
    mov r10, r8
    dec r15
    js .L__s3_failure_site_440
    cmp rax, r10
    jl .L_s3_f25_energy_series_aggregation_b10_rel_neg_41
    jg .L_s3_f25_energy_series_aggregation_b10_rel_pos_43
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_zero_42
.L_s3_f25_energy_series_aggregation_b15_while_exit_0_34:
    dec r15
    js .L__s3_failure_site_441
    jmp .L_s3_f25_energy_series_aggregation_b13_while_exit_36
.L_s3_f25_energy_series_aggregation_b15_while_exit_1_35:
    dec r15
    js .L__s3_failure_site_442
    jmp .L_s3_f25_energy_series_aggregation_b13_while_exit_36
.L_s3_f25_energy_series_aggregation_b13_while_exit_36:
    dec r15
    js .L__s3_failure_site_443
    mov rdi, 0
    mov byte ptr [rbp - 1867], 1
    dec r15
    js .L__s3_failure_site_444
    cmp byte ptr [rbp - 1867], 0
    je .L__s3_failure_site_446
    mov r10, rdi
    cmp r10, 1
    jae .L__s3_failure_site_447
    cmp byte ptr [rbp + r10 - 2025], 0
    je .L__s3_failure_site_445
    mov rax, qword ptr [rbp + r10*8 - 1912]
    mov rdi, rax
    mov byte ptr [rbp - 1868], 1
    dec r15
    js .L__s3_failure_site_448
    cmp byte ptr [rbp - 1868], 0
    je .L__s3_failure_site_449
    mov rax, rdi
    pxor xmm0, xmm0
    cvtsi2sd xmm0, rax
    movq rax, xmm0
    mov rdi, rax
    mov byte ptr [rbp - 1869], 1
    dec r15
    js .L__s3_failure_site_450
    mov rsi, 0
    mov byte ptr [rbp - 1870], 1
    dec r15
    js .L__s3_failure_site_451
    cmp byte ptr [rbp - 1870], 0
    je .L__s3_failure_site_452
    mov rax, rsi
    cmp byte ptr [rbp - 1869], 0
    je .L__s3_failure_site_453
    mov r10, rdi
    cmp rax, 1
    jae .L__s3_failure_site_454
    mov qword ptr [rbp + rax*8 - 2024], r10
    mov byte ptr [rbp + rax - 2043], 1
    dec r15
    js .L__s3_failure_site_455
    mov rdi, 0
    mov byte ptr [rbp - 1871], 1
    dec r15
    js .L__s3_failure_site_456
    mov rsi, 0
    mov byte ptr [rbp - 1872], 1
    dec r15
    js .L__s3_failure_site_457
    cmp byte ptr [rbp - 1872], 0
    je .L__s3_failure_site_459
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_460
    cmp byte ptr [rbp + r10 - 2033], 0
    je .L__s3_failure_site_458
    mov rax, qword ptr [rbp + r10*8 - 1952]
    mov rsi, rax
    mov byte ptr [rbp - 1873], 1
    dec r15
    js .L__s3_failure_site_461
    cmp byte ptr [rbp - 1694], 0
    je .L__s3_failure_site_463
    mov r10, rbx
    cmp byte ptr [rbp - 1695], 0
    je .L__s3_failure_site_464
    mov r11, r12
    cmp byte ptr [rbp - 1871], 0
    je .L__s3_failure_site_465
    mov rax, rdi
    cmp byte ptr [rbp - 1873], 0
    je .L__s3_failure_site_466
    mov rcx, rsi
    cmp rax, r11
    jae .L__s3_failure_site_462
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_467
    mov rdi, 1
    mov byte ptr [rbp - 1874], 1
    dec r15
    js .L__s3_failure_site_468
    mov rsi, 0
    mov byte ptr [rbp - 1875], 1
    dec r15
    js .L__s3_failure_site_469
    cmp byte ptr [rbp - 1875], 0
    je .L__s3_failure_site_471
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_472
    cmp byte ptr [rbp + r10 - 2035], 0
    je .L__s3_failure_site_470
    mov rax, qword ptr [rbp + r10*8 - 1968]
    mov rsi, rax
    mov byte ptr [rbp - 1876], 1
    dec r15
    js .L__s3_failure_site_473
    cmp byte ptr [rbp - 1694], 0
    je .L__s3_failure_site_475
    mov r10, rbx
    cmp byte ptr [rbp - 1695], 0
    je .L__s3_failure_site_476
    mov r11, r12
    cmp byte ptr [rbp - 1874], 0
    je .L__s3_failure_site_477
    mov rax, rdi
    cmp byte ptr [rbp - 1876], 0
    je .L__s3_failure_site_478
    mov rcx, rsi
    cmp rax, r11
    jae .L__s3_failure_site_474
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_479
    mov rdi, 2
    mov byte ptr [rbp - 1877], 1
    dec r15
    js .L__s3_failure_site_480
    mov rsi, 0
    mov byte ptr [rbp - 1878], 1
    dec r15
    js .L__s3_failure_site_481
    cmp byte ptr [rbp - 1878], 0
    je .L__s3_failure_site_483
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_484
    cmp byte ptr [rbp + r10 - 2034], 0
    je .L__s3_failure_site_482
    mov rax, qword ptr [rbp + r10*8 - 1960]
    mov rsi, rax
    mov byte ptr [rbp - 1879], 1
    dec r15
    js .L__s3_failure_site_485
    cmp byte ptr [rbp - 1694], 0
    je .L__s3_failure_site_487
    mov r10, rbx
    cmp byte ptr [rbp - 1695], 0
    je .L__s3_failure_site_488
    mov r11, r12
    cmp byte ptr [rbp - 1877], 0
    je .L__s3_failure_site_489
    mov rax, rdi
    cmp byte ptr [rbp - 1879], 0
    je .L__s3_failure_site_490
    mov rcx, rsi
    cmp rax, r11
    jae .L__s3_failure_site_486
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_491
    mov rdi, 3
    mov byte ptr [rbp - 1880], 1
    dec r15
    js .L__s3_failure_site_492
    mov rsi, 0
    mov byte ptr [rbp - 1881], 1
    dec r15
    js .L__s3_failure_site_493
    cmp byte ptr [rbp - 1881], 0
    je .L__s3_failure_site_495
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_496
    cmp byte ptr [rbp + r10 - 2033], 0
    je .L__s3_failure_site_494
    mov rax, qword ptr [rbp + r10*8 - 1952]
    mov rsi, rax
    mov byte ptr [rbp - 1882], 1
    dec r15
    js .L__s3_failure_site_497
    mov rdx, 0
    mov byte ptr [rbp - 1883], 1
    dec r15
    js .L__s3_failure_site_498
    cmp byte ptr [rbp - 1883], 0
    je .L__s3_failure_site_500
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_501
    cmp byte ptr [rbp + r10 - 2043], 0
    je .L__s3_failure_site_499
    mov rax, qword ptr [rbp + r10*8 - 2024]
    mov rdx, rax
    mov byte ptr [rbp - 1884], 1
    dec r15
    js .L__s3_failure_site_502
    cmp byte ptr [rbp - 1693], 0
    je .L__s3_failure_site_503
    mov rax, r13
    cmp byte ptr [rbp - 1884], 0
    je .L__s3_failure_site_504
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    mulsd xmm0, xmm1
    movq rax, xmm0
    mov rdx, rax
    mov byte ptr [rbp - 1885], 1
    dec r15
    js .L__s3_failure_site_505
    cmp byte ptr [rbp - 1882], 0
    je .L__s3_failure_site_506
    mov rax, rsi
    cmp byte ptr [rbp - 1885], 0
    je .L__s3_failure_site_507
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 1886], 1
    dec r15
    js .L__s3_failure_site_508
    cmp byte ptr [rbp - 1694], 0
    je .L__s3_failure_site_510
    mov r10, rbx
    cmp byte ptr [rbp - 1695], 0
    je .L__s3_failure_site_511
    mov r11, r12
    cmp byte ptr [rbp - 1880], 0
    je .L__s3_failure_site_512
    mov rax, rdi
    cmp byte ptr [rbp - 1886], 0
    je .L__s3_failure_site_513
    mov rcx, rsi
    cmp rax, r11
    jae .L__s3_failure_site_509
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_514
    mov rdi, 4
    mov byte ptr [rbp - 1887], 1
    dec r15
    js .L__s3_failure_site_515
    mov rsi, 0
    mov byte ptr [rbp - 1888], 1
    dec r15
    js .L__s3_failure_site_516
    cmp byte ptr [rbp - 1888], 0
    je .L__s3_failure_site_518
    mov r10, rsi
    cmp r10, 1
    jae .L__s3_failure_site_519
    cmp byte ptr [rbp + r10 - 2037], 0
    je .L__s3_failure_site_517
    mov rax, qword ptr [rbp + r10*8 - 1984]
    mov rsi, rax
    mov byte ptr [rbp - 1889], 1
    dec r15
    js .L__s3_failure_site_520
    mov rdx, 0
    mov byte ptr [rbp - 1890], 1
    dec r15
    js .L__s3_failure_site_521
    cmp byte ptr [rbp - 1890], 0
    je .L__s3_failure_site_523
    mov r10, rdx
    cmp r10, 1
    jae .L__s3_failure_site_524
    cmp byte ptr [rbp + r10 - 2043], 0
    je .L__s3_failure_site_522
    mov rax, qword ptr [rbp + r10*8 - 2024]
    mov rdx, rax
    mov byte ptr [rbp - 1891], 1
    dec r15
    js .L__s3_failure_site_525
    cmp byte ptr [rbp - 1889], 0
    je .L__s3_failure_site_526
    mov rax, rsi
    cmp byte ptr [rbp - 1891], 0
    je .L__s3_failure_site_527
    mov r10, rdx
    movq xmm0, rax
    movq xmm1, r10
    divsd xmm0, xmm1
    movq rax, xmm0
    mov rsi, rax
    mov byte ptr [rbp - 1892], 1
    dec r15
    js .L__s3_failure_site_528
    cmp byte ptr [rbp - 1694], 0
    je .L__s3_failure_site_530
    mov r10, rbx
    cmp byte ptr [rbp - 1695], 0
    je .L__s3_failure_site_531
    mov r11, r12
    cmp byte ptr [rbp - 1887], 0
    je .L__s3_failure_site_532
    mov rax, rdi
    cmp byte ptr [rbp - 1892], 0
    je .L__s3_failure_site_533
    mov rcx, rsi
    cmp rax, r11
    jae .L__s3_failure_site_529
    mov qword ptr [r10 + rax * 8], rcx
    dec r15
    js .L__s3_failure_site_534
    mov rdi, 0
    mov byte ptr [rbp - 1893], 1
    dec r15
    js .L__s3_failure_site_535
    cmp byte ptr [rbp - 1893], 0
    je .L__s3_failure_site_536
    mov rax, rdi
    mov qword ptr [rip + __s3_instruction_remaining], r15
    mov rbx, qword ptr [rbp - 2056]
    mov r12, qword ptr [rbp - 2064]
    mov r13, qword ptr [rbp - 2072]
    mov r14, qword ptr [rbp - 2080]
    mov r15, qword ptr [rbp - 2088]
    dec qword ptr [rip + __s3_frame_count]
    leave
    ret
.L_s3_f25_energy_series_aggregation_b10_rel_neg_37:
    dec r15
    js .L__s3_failure_site_537
    mov rcx, 0
    mov byte ptr [rbp - 1780], 1
    dec r15
    js .L__s3_failure_site_538
    mov r8, -1
    mov byte ptr [rbp - 1781], 1
    dec r15
    js .L__s3_failure_site_539
    cmp byte ptr [rbp - 1780], 0
    je .L__s3_failure_site_540
    mov rax, rcx
    cmp byte ptr [rbp - 1781], 0
    je .L__s3_failure_site_541
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_542
    cmp r10, -1
    jl .L__s3_failure_site_543
    cmp r10, 1
    jg .L__s3_failure_site_543
    mov byte ptr [rbp + rax - 1985], r10b
    mov byte ptr [rbp + rax - 2038], 1
    dec r15
    js .L__s3_failure_site_544
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_40
.L_s3_f25_energy_series_aggregation_b11_rel_zero_38:
    dec r15
    js .L__s3_failure_site_545
    mov rcx, 0
    mov byte ptr [rbp - 1782], 1
    dec r15
    js .L__s3_failure_site_546
    mov r8, 0
    mov byte ptr [rbp - 1783], 1
    dec r15
    js .L__s3_failure_site_547
    cmp byte ptr [rbp - 1782], 0
    je .L__s3_failure_site_548
    mov rax, rcx
    cmp byte ptr [rbp - 1783], 0
    je .L__s3_failure_site_549
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_550
    cmp r10, -1
    jl .L__s3_failure_site_551
    cmp r10, 1
    jg .L__s3_failure_site_551
    mov byte ptr [rbp + rax - 1985], r10b
    mov byte ptr [rbp + rax - 2038], 1
    dec r15
    js .L__s3_failure_site_552
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_40
.L_s3_f25_energy_series_aggregation_b10_rel_pos_39:
    dec r15
    js .L__s3_failure_site_553
    mov rcx, 0
    mov byte ptr [rbp - 1784], 1
    dec r15
    js .L__s3_failure_site_554
    mov r8, 0
    mov byte ptr [rbp - 1785], 1
    dec r15
    js .L__s3_failure_site_555
    cmp byte ptr [rbp - 1784], 0
    je .L__s3_failure_site_556
    mov rax, rcx
    cmp byte ptr [rbp - 1785], 0
    je .L__s3_failure_site_557
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_558
    cmp r10, -1
    jl .L__s3_failure_site_559
    cmp r10, 1
    jg .L__s3_failure_site_559
    mov byte ptr [rbp + rax - 1985], r10b
    mov byte ptr [rbp + rax - 2038], 1
    dec r15
    js .L__s3_failure_site_560
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_40
.L_s3_f25_energy_series_aggregation_b11_rel_cont_40:
    dec r15
    js .L__s3_failure_site_561
    mov rcx, 0
    mov byte ptr [rbp - 1786], 1
    dec r15
    js .L__s3_failure_site_562
    cmp byte ptr [rbp - 1786], 0
    je .L__s3_failure_site_564
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_565
    cmp byte ptr [rbp + r10 - 2038], 0
    je .L__s3_failure_site_563
    movsx rax, byte ptr [rbp + r10 - 1985]
    mov rcx, rax
    mov byte ptr [rbp - 1787], 1
    dec r15
    js .L__s3_failure_site_566
    cmp byte ptr [rbp - 1787], 0
    je .L__s3_failure_site_568
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b13_while_body_33
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b15_while_exit_0_34
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b15_while_exit_1_35
    jmp .L__s3_failure_site_567
.L_s3_f25_energy_series_aggregation_b10_rel_neg_41:
    dec r15
    js .L__s3_failure_site_569
    mov rcx, 0
    mov byte ptr [rbp - 1829], 1
    dec r15
    js .L__s3_failure_site_570
    mov r8, 0
    mov byte ptr [rbp - 1830], 1
    dec r15
    js .L__s3_failure_site_571
    cmp byte ptr [rbp - 1829], 0
    je .L__s3_failure_site_572
    mov rax, rcx
    cmp byte ptr [rbp - 1830], 0
    je .L__s3_failure_site_573
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_574
    cmp r10, -1
    jl .L__s3_failure_site_575
    cmp r10, 1
    jg .L__s3_failure_site_575
    mov byte ptr [rbp + rax - 2009], r10b
    mov byte ptr [rbp + rax - 2042], 1
    dec r15
    js .L__s3_failure_site_576
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_44
.L_s3_f25_energy_series_aggregation_b11_rel_zero_42:
    dec r15
    js .L__s3_failure_site_577
    mov rcx, 0
    mov byte ptr [rbp - 1831], 1
    dec r15
    js .L__s3_failure_site_578
    mov r8, -1
    mov byte ptr [rbp - 1832], 1
    dec r15
    js .L__s3_failure_site_579
    cmp byte ptr [rbp - 1831], 0
    je .L__s3_failure_site_580
    mov rax, rcx
    cmp byte ptr [rbp - 1832], 0
    je .L__s3_failure_site_581
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_582
    cmp r10, -1
    jl .L__s3_failure_site_583
    cmp r10, 1
    jg .L__s3_failure_site_583
    mov byte ptr [rbp + rax - 2009], r10b
    mov byte ptr [rbp + rax - 2042], 1
    dec r15
    js .L__s3_failure_site_584
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_44
.L_s3_f25_energy_series_aggregation_b10_rel_pos_43:
    dec r15
    js .L__s3_failure_site_585
    mov rcx, 0
    mov byte ptr [rbp - 1833], 1
    dec r15
    js .L__s3_failure_site_586
    mov r8, 0
    mov byte ptr [rbp - 1834], 1
    dec r15
    js .L__s3_failure_site_587
    cmp byte ptr [rbp - 1833], 0
    je .L__s3_failure_site_588
    mov rax, rcx
    cmp byte ptr [rbp - 1834], 0
    je .L__s3_failure_site_589
    mov r10, r8
    cmp rax, 1
    jae .L__s3_failure_site_590
    cmp r10, -1
    jl .L__s3_failure_site_591
    cmp r10, 1
    jg .L__s3_failure_site_591
    mov byte ptr [rbp + rax - 2009], r10b
    mov byte ptr [rbp + rax - 2042], 1
    dec r15
    js .L__s3_failure_site_592
    jmp .L_s3_f25_energy_series_aggregation_b11_rel_cont_44
.L_s3_f25_energy_series_aggregation_b11_rel_cont_44:
    dec r15
    js .L__s3_failure_site_593
    mov rcx, 0
    mov byte ptr [rbp - 1835], 1
    dec r15
    js .L__s3_failure_site_594
    cmp byte ptr [rbp - 1835], 0
    je .L__s3_failure_site_596
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_597
    cmp byte ptr [rbp + r10 - 2042], 0
    je .L__s3_failure_site_595
    movsx rax, byte ptr [rbp + r10 - 2009]
    mov rcx, rax
    mov byte ptr [rbp - 1836], 1
    dec r15
    js .L__s3_failure_site_598
    cmp byte ptr [rbp - 1836], 0
    je .L__s3_failure_site_600
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b18_switch_negative_45
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b17_switch_neutral_46
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b18_switch_positive_47
    jmp .L__s3_failure_site_599
.L_s3_f25_energy_series_aggregation_b18_switch_negative_45:
    dec r15
    js .L__s3_failure_site_601
    mov rcx, 0
    mov byte ptr [rbp - 1837], 1
    dec r15
    js .L__s3_failure_site_602
    cmp byte ptr [rbp - 1837], 0
    je .L__s3_failure_site_604
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_605
    cmp byte ptr [rbp + r10 - 2040], 0
    je .L__s3_failure_site_603
    mov rax, qword ptr [rbp + r10*8 - 2000]
    mov rcx, rax
    mov byte ptr [rbp - 1838], 1
    dec r15
    js .L__s3_failure_site_606
    mov r8, 0
    mov byte ptr [rbp - 1839], 1
    dec r15
    js .L__s3_failure_site_607
    cmp byte ptr [rbp - 1839], 0
    je .L__s3_failure_site_608
    mov rax, r8
    cmp byte ptr [rbp - 1838], 0
    je .L__s3_failure_site_609
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_610
    mov qword ptr [rbp + rax*8 - 1968], r10
    mov byte ptr [rbp + rax - 2035], 1
    dec r15
    js .L__s3_failure_site_611
    mov rcx, 0
    mov byte ptr [rbp - 1840], 1
    dec r15
    js .L__s3_failure_site_612
    mov r8, 0
    mov byte ptr [rbp - 1841], 1
    dec r15
    js .L__s3_failure_site_613
    cmp byte ptr [rbp - 1841], 0
    je .L__s3_failure_site_614
    mov rax, r8
    cmp byte ptr [rbp - 1840], 0
    je .L__s3_failure_site_615
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_616
    mov qword ptr [rbp + rax*8 - 1976], r10
    mov byte ptr [rbp + rax - 2036], 1
    dec r15
    js .L__s3_failure_site_617
    jmp .L_s3_f25_energy_series_aggregation_b18_switch_continue_48
.L_s3_f25_energy_series_aggregation_b17_switch_neutral_46:
    dec r15
    js .L__s3_failure_site_618
    mov rcx, 0
    mov byte ptr [rbp - 1842], 1
    dec r15
    js .L__s3_failure_site_619
    cmp byte ptr [rbp - 1842], 0
    je .L__s3_failure_site_621
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_622
    cmp byte ptr [rbp + r10 - 2036], 0
    je .L__s3_failure_site_620
    mov rax, qword ptr [rbp + r10*8 - 1976]
    mov rcx, rax
    mov byte ptr [rbp - 1843], 1
    dec r15
    js .L__s3_failure_site_623
    mov r8, 0
    mov byte ptr [rbp - 1844], 1
    dec r15
    js .L__s3_failure_site_624
    cmp byte ptr [rbp - 1844], 0
    je .L__s3_failure_site_625
    mov rax, r8
    cmp byte ptr [rbp - 1843], 0
    je .L__s3_failure_site_626
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_627
    mov qword ptr [rbp + rax*8 - 1976], r10
    mov byte ptr [rbp + rax - 2036], 1
    dec r15
    js .L__s3_failure_site_628
    jmp .L_s3_f25_energy_series_aggregation_b18_switch_continue_48
.L_s3_f25_energy_series_aggregation_b18_switch_positive_47:
    dec r15
    js .L__s3_failure_site_629
    mov rcx, 0
    mov byte ptr [rbp - 1845], 1
    dec r15
    js .L__s3_failure_site_630
    cmp byte ptr [rbp - 1845], 0
    je .L__s3_failure_site_632
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_633
    cmp byte ptr [rbp + r10 - 2036], 0
    je .L__s3_failure_site_631
    mov rax, qword ptr [rbp + r10*8 - 1976]
    mov rcx, rax
    mov byte ptr [rbp - 1846], 1
    dec r15
    js .L__s3_failure_site_634
    mov r8, 0
    mov byte ptr [rbp - 1847], 1
    dec r15
    js .L__s3_failure_site_635
    cmp byte ptr [rbp - 1847], 0
    je .L__s3_failure_site_636
    mov rax, r8
    cmp byte ptr [rbp - 1846], 0
    je .L__s3_failure_site_637
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_638
    mov qword ptr [rbp + rax*8 - 1976], r10
    mov byte ptr [rbp + rax - 2036], 1
    dec r15
    js .L__s3_failure_site_639
    jmp .L_s3_f25_energy_series_aggregation_b18_switch_continue_48
.L_s3_f25_energy_series_aggregation_b18_switch_continue_48:
    dec r15
    js .L__s3_failure_site_640
    mov rcx, 0
    mov byte ptr [rbp - 1848], 1
    dec r15
    js .L__s3_failure_site_641
    cmp byte ptr [rbp - 1848], 0
    je .L__s3_failure_site_643
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_644
    cmp byte ptr [rbp + r10 - 2035], 0
    je .L__s3_failure_site_642
    mov rax, qword ptr [rbp + r10*8 - 1968]
    mov rcx, rax
    mov byte ptr [rbp - 1849], 1
    dec r15
    js .L__s3_failure_site_645
    mov r8, 0
    mov byte ptr [rbp - 1850], 1
    dec r15
    js .L__s3_failure_site_646
    cmp byte ptr [rbp - 1850], 0
    je .L__s3_failure_site_648
    mov r10, r8
    cmp r10, 1
    jae .L__s3_failure_site_649
    cmp byte ptr [rbp + r10 - 2040], 0
    je .L__s3_failure_site_647
    mov rax, qword ptr [rbp + r10*8 - 2000]
    mov r8, rax
    mov byte ptr [rbp - 1851], 1
    dec r15
    js .L__s3_failure_site_650
    cmp byte ptr [rbp - 1849], 0
    je .L__s3_failure_site_651
    mov rax, rcx
    cmp byte ptr [rbp - 1851], 0
    je .L__s3_failure_site_652
    mov r10, r8
    movq xmm0, rax
    movq xmm1, r10
    ucomisd xmm0, xmm1
    setb al
    setnp r11b
    and al, r11b
    movzx r11, al
    neg r11
    mov rcx, r11
    mov byte ptr [rbp - 1852], 1
    dec r15
    js .L__s3_failure_site_653
    cmp byte ptr [rbp - 1852], 0
    je .L__s3_failure_site_655
    mov rax, rcx
    cmp rax, -1
    je .L_s3_f25_energy_series_aggregation_b18_switch_negative_49
    cmp rax, 0
    je .L_s3_f25_energy_series_aggregation_b17_switch_neutral_50
    cmp rax, 1
    je .L_s3_f25_energy_series_aggregation_b18_switch_positive_51
    jmp .L__s3_failure_site_654
.L_s3_f25_energy_series_aggregation_b18_switch_negative_49:
    dec r15
    js .L__s3_failure_site_656
    mov rcx, 0
    mov byte ptr [rbp - 1853], 1
    dec r15
    js .L__s3_failure_site_657
    cmp byte ptr [rbp - 1853], 0
    je .L__s3_failure_site_659
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_660
    cmp byte ptr [rbp + r10 - 2040], 0
    je .L__s3_failure_site_658
    mov rax, qword ptr [rbp + r10*8 - 2000]
    mov rcx, rax
    mov byte ptr [rbp - 1854], 1
    dec r15
    js .L__s3_failure_site_661
    mov r8, 0
    mov byte ptr [rbp - 1855], 1
    dec r15
    js .L__s3_failure_site_662
    cmp byte ptr [rbp - 1855], 0
    je .L__s3_failure_site_663
    mov rax, r8
    cmp byte ptr [rbp - 1854], 0
    je .L__s3_failure_site_664
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_665
    mov qword ptr [rbp + rax*8 - 1968], r10
    mov byte ptr [rbp + rax - 2035], 1
    dec r15
    js .L__s3_failure_site_666
    jmp .L_s3_f25_energy_series_aggregation_b18_switch_continue_52
.L_s3_f25_energy_series_aggregation_b17_switch_neutral_50:
    dec r15
    js .L__s3_failure_site_667
    mov rcx, 0
    mov byte ptr [rbp - 1856], 1
    dec r15
    js .L__s3_failure_site_668
    cmp byte ptr [rbp - 1856], 0
    je .L__s3_failure_site_670
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_671
    cmp byte ptr [rbp + r10 - 2035], 0
    je .L__s3_failure_site_669
    mov rax, qword ptr [rbp + r10*8 - 1968]
    mov rcx, rax
    mov byte ptr [rbp - 1857], 1
    dec r15
    js .L__s3_failure_site_672
    mov r8, 0
    mov byte ptr [rbp - 1858], 1
    dec r15
    js .L__s3_failure_site_673
    cmp byte ptr [rbp - 1858], 0
    je .L__s3_failure_site_674
    mov rax, r8
    cmp byte ptr [rbp - 1857], 0
    je .L__s3_failure_site_675
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_676
    mov qword ptr [rbp + rax*8 - 1968], r10
    mov byte ptr [rbp + rax - 2035], 1
    dec r15
    js .L__s3_failure_site_677
    jmp .L_s3_f25_energy_series_aggregation_b18_switch_continue_52
.L_s3_f25_energy_series_aggregation_b18_switch_positive_51:
    dec r15
    js .L__s3_failure_site_678
    mov rcx, 0
    mov byte ptr [rbp - 1859], 1
    dec r15
    js .L__s3_failure_site_679
    cmp byte ptr [rbp - 1859], 0
    je .L__s3_failure_site_681
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_682
    cmp byte ptr [rbp + r10 - 2035], 0
    je .L__s3_failure_site_680
    mov rax, qword ptr [rbp + r10*8 - 1968]
    mov rcx, rax
    mov byte ptr [rbp - 1860], 1
    dec r15
    js .L__s3_failure_site_683
    mov r8, 0
    mov byte ptr [rbp - 1861], 1
    dec r15
    js .L__s3_failure_site_684
    cmp byte ptr [rbp - 1861], 0
    je .L__s3_failure_site_685
    mov rax, r8
    cmp byte ptr [rbp - 1860], 0
    je .L__s3_failure_site_686
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_687
    mov qword ptr [rbp + rax*8 - 1968], r10
    mov byte ptr [rbp + rax - 2035], 1
    dec r15
    js .L__s3_failure_site_688
    jmp .L_s3_f25_energy_series_aggregation_b18_switch_continue_52
.L_s3_f25_energy_series_aggregation_b18_switch_continue_52:
    dec r15
    js .L__s3_failure_site_689
    mov rcx, 0
    mov byte ptr [rbp - 1862], 1
    dec r15
    js .L__s3_failure_site_690
    cmp byte ptr [rbp - 1862], 0
    je .L__s3_failure_site_692
    mov r10, rcx
    cmp r10, 1
    jae .L__s3_failure_site_693
    cmp byte ptr [rbp + r10 - 2032], 0
    je .L__s3_failure_site_691
    mov rax, qword ptr [rbp + r10*8 - 1944]
    mov rcx, rax
    mov byte ptr [rbp - 1863], 1
    dec r15
    js .L__s3_failure_site_694
    mov r8, 1
    mov byte ptr [rbp - 1864], 1
    dec r15
    js .L__s3_failure_site_695
    cmp byte ptr [rbp - 1863], 0
    je .L__s3_failure_site_697
    mov rax, rcx
    cmp byte ptr [rbp - 1864], 0
    je .L__s3_failure_site_698
    mov r10, r8
    add rax, r10
    jo .L__s3_failure_site_696
    mov rcx, rax
    mov byte ptr [rbp - 1865], 1
    dec r15
    js .L__s3_failure_site_699
    mov r8, 0
    mov byte ptr [rbp - 1866], 1
    dec r15
    js .L__s3_failure_site_700
    cmp byte ptr [rbp - 1866], 0
    je .L__s3_failure_site_701
    mov rax, r8
    cmp byte ptr [rbp - 1865], 0
    je .L__s3_failure_site_702
    mov r10, rcx
    cmp rax, 1
    jae .L__s3_failure_site_703
    mov qword ptr [rbp + rax*8 - 1944], r10
    mov byte ptr [rbp + rax - 2032], 1
    dec r15
    js .L__s3_failure_site_704
    jmp .L_s3_f25_energy_series_aggregation_b18_while_condition_32
.size energy_series_aggregation, .-energy_series_aggregation

.globl s3_main
.type s3_main, @function
s3_main:
    inc qword ptr [rip + __s3_frame_count]
    cmp qword ptr [rip + __s3_frame_count], 1024
    jg .L__s3_failure_site_705
    push rbp
    mov rbp, rsp
    sub rsp, 32
    mov qword ptr [rbp - 24], r15
    mov r15, qword ptr [rip + __s3_instruction_remaining]
    jmp .L_s3_f4_main_b5_entry
.L_s3_f4_main_b5_entry:
    dec r15
    js .L__s3_failure_site_706
    mov rdi, 0
    dec r15
    js .L__s3_failure_site_707
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
    mov edx, 101
    lea rcx, [rip + .L__s3_failure_suffix_0]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_1:
    lea rsi, [rip + .L__s3_failure_prefix_1]
    mov edx, 133
    jmp __s3_fail_message
.L__s3_failure_site_2:
    lea rsi, [rip + .L__s3_failure_prefix_2]
    mov edx, 131
    jmp __s3_fail_message
.L__s3_failure_site_3:
    lea rsi, [rip + .L__s3_failure_prefix_3]
    mov edx, 130
    jmp __s3_fail_message
.L__s3_failure_site_4:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_4]
    mov edx, 103
    lea rcx, [rip + .L__s3_failure_suffix_4]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_5:
    lea rsi, [rip + .L__s3_failure_prefix_5]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_6:
    lea rsi, [rip + .L__s3_failure_prefix_6]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_7:
    lea rsi, [rip + .L__s3_failure_prefix_7]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_8:
    lea rsi, [rip + .L__s3_failure_prefix_8]
    mov edx, 142
    jmp __s3_fail_message
.L__s3_failure_site_9:
    lea rsi, [rip + .L__s3_failure_prefix_9]
    mov edx, 143
    jmp __s3_fail_message
.L__s3_failure_site_10:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_10]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_10]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_11:
    lea rsi, [rip + .L__s3_failure_prefix_11]
    mov edx, 146
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
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_16:
    lea rsi, [rip + .L__s3_failure_prefix_16]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_17:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_17]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_17]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_18:
    lea rsi, [rip + .L__s3_failure_prefix_18]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_19:
    lea rsi, [rip + .L__s3_failure_prefix_19]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_20:
    lea rsi, [rip + .L__s3_failure_prefix_20]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_21:
    lea rsi, [rip + .L__s3_failure_prefix_21]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_22:
    lea rsi, [rip + .L__s3_failure_prefix_22]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_23:
    lea rsi, [rip + .L__s3_failure_prefix_23]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_24:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_24]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_24]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_25:
    lea rsi, [rip + .L__s3_failure_prefix_25]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_26:
    lea rsi, [rip + .L__s3_failure_prefix_26]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_27:
    lea rsi, [rip + .L__s3_failure_prefix_27]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_28:
    lea rsi, [rip + .L__s3_failure_prefix_28]
    mov edx, 146
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
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_31]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_31]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_32:
    lea rsi, [rip + .L__s3_failure_prefix_32]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_33:
    lea rsi, [rip + .L__s3_failure_prefix_33]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_34:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_34]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_34]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_35:
    lea rsi, [rip + .L__s3_failure_prefix_35]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_36:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_36]
    mov edx, 107
    lea rcx, [rip + .L__s3_failure_suffix_36]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_37:
    lea rsi, [rip + .L__s3_failure_prefix_37]
    mov edx, 147
    jmp __s3_fail_message
.L__s3_failure_site_38:
    lea rsi, [rip + .L__s3_failure_prefix_38]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_39:
    lea rsi, [rip + .L__s3_failure_prefix_39]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_40:
    lea rsi, [rip + .L__s3_failure_prefix_40]
    mov edx, 146
    jmp __s3_fail_message
.L__s3_failure_site_41:
    lea rsi, [rip + .L__s3_failure_prefix_41]
    mov edx, 145
    jmp __s3_fail_message
.L__s3_failure_site_42:
    lea rsi, [rip + .L__s3_failure_prefix_42]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_43:
    lea rsi, [rip + .L__s3_failure_prefix_43]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_44:
    lea rsi, [rip + .L__s3_failure_prefix_44]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_45:
    lea rsi, [rip + .L__s3_failure_prefix_45]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_46:
    lea rsi, [rip + .L__s3_failure_prefix_46]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_47:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_47]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_47]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_48:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_48]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_48]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_49:
    lea rsi, [rip + .L__s3_failure_prefix_49]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_50:
    lea rsi, [rip + .L__s3_failure_prefix_50]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_51:
    lea rsi, [rip + .L__s3_failure_prefix_51]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_52:
    lea rsi, [rip + .L__s3_failure_prefix_52]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_53:
    lea rsi, [rip + .L__s3_failure_prefix_53]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_54:
    lea rsi, [rip + .L__s3_failure_prefix_54]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_55:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_55]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_55]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_56:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_56]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_56]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_57:
    lea rsi, [rip + .L__s3_failure_prefix_57]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_58:
    lea rsi, [rip + .L__s3_failure_prefix_58]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_59:
    lea rsi, [rip + .L__s3_failure_prefix_59]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_60:
    lea rsi, [rip + .L__s3_failure_prefix_60]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_61:
    lea rsi, [rip + .L__s3_failure_prefix_61]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_62:
    lea rsi, [rip + .L__s3_failure_prefix_62]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_63:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_63]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_63]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_64:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_64]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_64]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_65:
    lea rsi, [rip + .L__s3_failure_prefix_65]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_66:
    lea rsi, [rip + .L__s3_failure_prefix_66]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_67:
    lea rsi, [rip + .L__s3_failure_prefix_67]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_68:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_68]
    mov edx, 126
    lea rcx, [rip + .L__s3_failure_suffix_68]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_69:
    lea rsi, [rip + .L__s3_failure_prefix_69]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_70:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_70]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_70]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_71:
    lea rsi, [rip + .L__s3_failure_prefix_71]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_72:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_72]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_72]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_73:
    lea rsi, [rip + .L__s3_failure_prefix_73]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_74:
    lea rsi, [rip + .L__s3_failure_prefix_74]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_75:
    lea rsi, [rip + .L__s3_failure_prefix_75]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_76:
    lea rsi, [rip + .L__s3_failure_prefix_76]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_77:
    lea rsi, [rip + .L__s3_failure_prefix_77]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_78:
    lea rsi, [rip + .L__s3_failure_prefix_78]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_79:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_79]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_79]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_80:
    lea rsi, [rip + .L__s3_failure_prefix_80]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_81:
    lea rsi, [rip + .L__s3_failure_prefix_81]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_82:
    lea rsi, [rip + .L__s3_failure_prefix_82]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_83:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_83]
    mov edx, 132
    lea rcx, [rip + .L__s3_failure_suffix_83]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_84:
    lea rsi, [rip + .L__s3_failure_prefix_84]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_85:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_85]
    mov edx, 118
    lea rcx, [rip + .L__s3_failure_suffix_85]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_86:
    lea rsi, [rip + .L__s3_failure_prefix_86]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_87:
    lea rsi, [rip + .L__s3_failure_prefix_87]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_88:
    lea rsi, [rip + .L__s3_failure_prefix_88]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_89:
    lea rsi, [rip + .L__s3_failure_prefix_89]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_90:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_90]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_90]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_91:
    lea rsi, [rip + .L__s3_failure_prefix_91]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_92:
    lea rsi, [rip + .L__s3_failure_prefix_92]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_93:
    lea rsi, [rip + .L__s3_failure_prefix_93]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_94:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_94]
    mov edx, 133
    lea rcx, [rip + .L__s3_failure_suffix_94]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_95:
    lea rsi, [rip + .L__s3_failure_prefix_95]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_96:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_96]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_96]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_97:
    lea rsi, [rip + .L__s3_failure_prefix_97]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_98:
    lea rsi, [rip + .L__s3_failure_prefix_98]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_99:
    lea rsi, [rip + .L__s3_failure_prefix_99]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_100:
    lea rsi, [rip + .L__s3_failure_prefix_100]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_101:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_101]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_101]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_102:
    lea rsi, [rip + .L__s3_failure_prefix_102]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_103:
    lea rsi, [rip + .L__s3_failure_prefix_103]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_104:
    lea rsi, [rip + .L__s3_failure_prefix_104]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_105:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_105]
    mov edx, 133
    lea rcx, [rip + .L__s3_failure_suffix_105]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_106:
    lea rsi, [rip + .L__s3_failure_prefix_106]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_107:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_107]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_107]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_108:
    lea rsi, [rip + .L__s3_failure_prefix_108]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_109:
    lea rsi, [rip + .L__s3_failure_prefix_109]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_110:
    lea rsi, [rip + .L__s3_failure_prefix_110]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_111:
    lea rsi, [rip + .L__s3_failure_prefix_111]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_112:
    lea rsi, [rip + .L__s3_failure_prefix_112]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_113:
    lea rsi, [rip + .L__s3_failure_prefix_113]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_114:
    lea rsi, [rip + .L__s3_failure_prefix_114]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_115:
    lea rsi, [rip + .L__s3_failure_prefix_115]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_116:
    lea rsi, [rip + .L__s3_failure_prefix_116]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_117:
    lea rsi, [rip + .L__s3_failure_prefix_117]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_118:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_118]
    mov edx, 112
    lea rcx, [rip + .L__s3_failure_suffix_118]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_119:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_119]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_119]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_120:
    lea rsi, [rip + .L__s3_failure_prefix_120]
    mov edx, 149
    jmp __s3_fail_message
.L__s3_failure_site_121:
    lea rsi, [rip + .L__s3_failure_prefix_121]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_122:
    lea rsi, [rip + .L__s3_failure_prefix_122]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_123:
    lea rsi, [rip + .L__s3_failure_prefix_123]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_124:
    lea rsi, [rip + .L__s3_failure_prefix_124]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_125:
    lea rsi, [rip + .L__s3_failure_prefix_125]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_126:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_126]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_126]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_127:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_127]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_127]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_128:
    lea rsi, [rip + .L__s3_failure_prefix_128]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_129:
    lea rsi, [rip + .L__s3_failure_prefix_129]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_130:
    lea rsi, [rip + .L__s3_failure_prefix_130]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_131:
    lea rsi, [rip + .L__s3_failure_prefix_131]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_132:
    lea rsi, [rip + .L__s3_failure_prefix_132]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_133:
    lea rsi, [rip + .L__s3_failure_prefix_133]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_134:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_134]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_134]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_135:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_135]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_135]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_136:
    lea rsi, [rip + .L__s3_failure_prefix_136]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_137:
    lea rsi, [rip + .L__s3_failure_prefix_137]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_138:
    lea rsi, [rip + .L__s3_failure_prefix_138]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_139:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_139]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_139]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_140:
    lea rsi, [rip + .L__s3_failure_prefix_140]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_141:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_141]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_141]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_142:
    lea rsi, [rip + .L__s3_failure_prefix_142]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_143:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_143]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_143]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_144:
    lea rsi, [rip + .L__s3_failure_prefix_144]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_145:
    lea rsi, [rip + .L__s3_failure_prefix_145]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_146:
    lea rsi, [rip + .L__s3_failure_prefix_146]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_147:
    lea rsi, [rip + .L__s3_failure_prefix_147]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_148:
    lea rsi, [rip + .L__s3_failure_prefix_148]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_149:
    lea rsi, [rip + .L__s3_failure_prefix_149]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_150:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_150]
    mov edx, 133
    lea rcx, [rip + .L__s3_failure_suffix_150]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_151:
    lea rsi, [rip + .L__s3_failure_prefix_151]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_152:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_152]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_152]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_153:
    lea rsi, [rip + .L__s3_failure_prefix_153]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_154:
    lea rsi, [rip + .L__s3_failure_prefix_154]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_155:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_155]
    mov edx, 133
    lea rcx, [rip + .L__s3_failure_suffix_155]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_156:
    lea rsi, [rip + .L__s3_failure_prefix_156]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_157:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_157]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_157]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_158:
    lea rsi, [rip + .L__s3_failure_prefix_158]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_159:
    lea rsi, [rip + .L__s3_failure_prefix_159]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_160:
    lea rsi, [rip + .L__s3_failure_prefix_160]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_161:
    lea rsi, [rip + .L__s3_failure_prefix_161]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_162:
    lea rsi, [rip + .L__s3_failure_prefix_162]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_163:
    lea rsi, [rip + .L__s3_failure_prefix_163]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_164:
    lea rsi, [rip + .L__s3_failure_prefix_164]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_165:
    lea rsi, [rip + .L__s3_failure_prefix_165]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_166:
    lea rsi, [rip + .L__s3_failure_prefix_166]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_167:
    lea rsi, [rip + .L__s3_failure_prefix_167]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_168:
    lea rsi, [rip + .L__s3_failure_prefix_168]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_169:
    lea rsi, [rip + .L__s3_failure_prefix_169]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_170:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_170]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_170]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_171:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_171]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_171]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_172:
    lea rsi, [rip + .L__s3_failure_prefix_172]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_173:
    lea rsi, [rip + .L__s3_failure_prefix_173]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_174:
    lea rsi, [rip + .L__s3_failure_prefix_174]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_175:
    lea rsi, [rip + .L__s3_failure_prefix_175]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_176:
    lea rsi, [rip + .L__s3_failure_prefix_176]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_177:
    lea rsi, [rip + .L__s3_failure_prefix_177]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_178:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_178]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_178]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_179:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_179]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_179]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_180:
    lea rsi, [rip + .L__s3_failure_prefix_180]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_181:
    lea rsi, [rip + .L__s3_failure_prefix_181]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_182:
    lea rsi, [rip + .L__s3_failure_prefix_182]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_183:
    lea rsi, [rip + .L__s3_failure_prefix_183]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_184:
    lea rsi, [rip + .L__s3_failure_prefix_184]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_185:
    lea rsi, [rip + .L__s3_failure_prefix_185]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_186:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_186]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_186]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_187:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_187]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_187]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_188:
    lea rsi, [rip + .L__s3_failure_prefix_188]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_189:
    lea rsi, [rip + .L__s3_failure_prefix_189]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_190:
    lea rsi, [rip + .L__s3_failure_prefix_190]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_191:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_191]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_191]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_192:
    lea rsi, [rip + .L__s3_failure_prefix_192]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_193:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_193]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_193]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_194:
    lea rsi, [rip + .L__s3_failure_prefix_194]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_195:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_195]
    mov edx, 124
    lea rcx, [rip + .L__s3_failure_suffix_195]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_196:
    lea rsi, [rip + .L__s3_failure_prefix_196]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_197:
    lea rsi, [rip + .L__s3_failure_prefix_197]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_198:
    lea rsi, [rip + .L__s3_failure_prefix_198]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_199:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_199]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_199]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_200:
    lea rsi, [rip + .L__s3_failure_prefix_200]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_201:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_201]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_201]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_202:
    lea rsi, [rip + .L__s3_failure_prefix_202]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_203:
    lea rsi, [rip + .L__s3_failure_prefix_203]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_204:
    lea rsi, [rip + .L__s3_failure_prefix_204]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_205:
    lea rsi, [rip + .L__s3_failure_prefix_205]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_206:
    lea rsi, [rip + .L__s3_failure_prefix_206]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_207:
    lea rsi, [rip + .L__s3_failure_prefix_207]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_208:
    lea rsi, [rip + .L__s3_failure_prefix_208]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_209:
    lea rsi, [rip + .L__s3_failure_prefix_209]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_210:
    lea rsi, [rip + .L__s3_failure_prefix_210]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_211:
    lea rsi, [rip + .L__s3_failure_prefix_211]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_212:
    lea rsi, [rip + .L__s3_failure_prefix_212]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_213:
    lea rsi, [rip + .L__s3_failure_prefix_213]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_214:
    lea rsi, [rip + .L__s3_failure_prefix_214]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_215:
    lea rsi, [rip + .L__s3_failure_prefix_215]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_216:
    lea rsi, [rip + .L__s3_failure_prefix_216]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_217:
    lea rsi, [rip + .L__s3_failure_prefix_217]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_218:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_218]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_218]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_219:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_219]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_219]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_220:
    lea rsi, [rip + .L__s3_failure_prefix_220]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_221:
    lea rsi, [rip + .L__s3_failure_prefix_221]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_222:
    lea rsi, [rip + .L__s3_failure_prefix_222]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_223:
    lea rsi, [rip + .L__s3_failure_prefix_223]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_224:
    lea rsi, [rip + .L__s3_failure_prefix_224]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_225:
    lea rsi, [rip + .L__s3_failure_prefix_225]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_226:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_226]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_226]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_227:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_227]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_227]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_228:
    lea rsi, [rip + .L__s3_failure_prefix_228]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_229:
    lea rsi, [rip + .L__s3_failure_prefix_229]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_230:
    lea rsi, [rip + .L__s3_failure_prefix_230]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_231:
    lea rsi, [rip + .L__s3_failure_prefix_231]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_232:
    lea rsi, [rip + .L__s3_failure_prefix_232]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_233:
    lea rsi, [rip + .L__s3_failure_prefix_233]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_234:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_234]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_234]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_235:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_235]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_235]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_236:
    lea rsi, [rip + .L__s3_failure_prefix_236]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_237:
    lea rsi, [rip + .L__s3_failure_prefix_237]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_238:
    lea rsi, [rip + .L__s3_failure_prefix_238]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_239:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_239]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_239]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_240:
    lea rsi, [rip + .L__s3_failure_prefix_240]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_241:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_241]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_241]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_242:
    lea rsi, [rip + .L__s3_failure_prefix_242]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_243:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_243]
    mov edx, 124
    lea rcx, [rip + .L__s3_failure_suffix_243]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_244:
    lea rsi, [rip + .L__s3_failure_prefix_244]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_245:
    lea rsi, [rip + .L__s3_failure_prefix_245]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_246:
    lea rsi, [rip + .L__s3_failure_prefix_246]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_247:
    lea rsi, [rip + .L__s3_failure_prefix_247]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_248:
    lea rsi, [rip + .L__s3_failure_prefix_248]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_249:
    lea rsi, [rip + .L__s3_failure_prefix_249]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_250:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_250]
    mov edx, 131
    lea rcx, [rip + .L__s3_failure_suffix_250]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_251:
    lea rsi, [rip + .L__s3_failure_prefix_251]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_252:
    lea rsi, [rip + .L__s3_failure_prefix_252]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_253:
    lea rsi, [rip + .L__s3_failure_prefix_253]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_254:
    lea rsi, [rip + .L__s3_failure_prefix_254]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_255:
    lea rsi, [rip + .L__s3_failure_prefix_255]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_256:
    lea rsi, [rip + .L__s3_failure_prefix_256]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_257:
    lea rsi, [rip + .L__s3_failure_prefix_257]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_258:
    lea rsi, [rip + .L__s3_failure_prefix_258]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_259:
    lea rsi, [rip + .L__s3_failure_prefix_259]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_260:
    lea rsi, [rip + .L__s3_failure_prefix_260]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_261:
    lea rsi, [rip + .L__s3_failure_prefix_261]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_262:
    lea rsi, [rip + .L__s3_failure_prefix_262]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_263:
    lea rsi, [rip + .L__s3_failure_prefix_263]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_264:
    lea rsi, [rip + .L__s3_failure_prefix_264]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_265:
    lea rsi, [rip + .L__s3_failure_prefix_265]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_266:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_266]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_266]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_267:
    lea rsi, [rip + .L__s3_failure_prefix_267]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_268:
    lea rsi, [rip + .L__s3_failure_prefix_268]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_269:
    lea rsi, [rip + .L__s3_failure_prefix_269]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_270:
    lea rsi, [rip + .L__s3_failure_prefix_270]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_271:
    lea rsi, [rip + .L__s3_failure_prefix_271]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_272:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_272]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_272]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_273:
    lea rsi, [rip + .L__s3_failure_prefix_273]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_274:
    lea rsi, [rip + .L__s3_failure_prefix_274]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_275:
    lea rsi, [rip + .L__s3_failure_prefix_275]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_276:
    lea rsi, [rip + .L__s3_failure_prefix_276]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_277:
    lea rsi, [rip + .L__s3_failure_prefix_277]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_278:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_278]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_278]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_279:
    lea rsi, [rip + .L__s3_failure_prefix_279]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_280:
    lea rsi, [rip + .L__s3_failure_prefix_280]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_281:
    lea rsi, [rip + .L__s3_failure_prefix_281]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_282:
    lea rsi, [rip + .L__s3_failure_prefix_282]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_283:
    lea rsi, [rip + .L__s3_failure_prefix_283]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_284:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_284]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_284]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_285:
    lea rsi, [rip + .L__s3_failure_prefix_285]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_286:
    lea rsi, [rip + .L__s3_failure_prefix_286]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_287:
    lea rsi, [rip + .L__s3_failure_prefix_287]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_288:
    lea rsi, [rip + .L__s3_failure_prefix_288]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_289:
    lea rsi, [rip + .L__s3_failure_prefix_289]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_290:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_290]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_290]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_291:
    lea rsi, [rip + .L__s3_failure_prefix_291]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_292:
    lea rsi, [rip + .L__s3_failure_prefix_292]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_293:
    lea rsi, [rip + .L__s3_failure_prefix_293]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_294:
    lea rsi, [rip + .L__s3_failure_prefix_294]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_295:
    lea rsi, [rip + .L__s3_failure_prefix_295]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_296:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_296]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_296]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_297:
    lea rsi, [rip + .L__s3_failure_prefix_297]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_298:
    lea rsi, [rip + .L__s3_failure_prefix_298]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_299:
    lea rsi, [rip + .L__s3_failure_prefix_299]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_300:
    lea rsi, [rip + .L__s3_failure_prefix_300]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_301:
    lea rsi, [rip + .L__s3_failure_prefix_301]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_302:
    lea rsi, [rip + .L__s3_failure_prefix_302]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_303:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_303]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_303]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_304:
    lea rsi, [rip + .L__s3_failure_prefix_304]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_305:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_305]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_305]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_306:
    lea rsi, [rip + .L__s3_failure_prefix_306]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_307:
    lea rsi, [rip + .L__s3_failure_prefix_307]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_308:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_308]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_308]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_309:
    lea rsi, [rip + .L__s3_failure_prefix_309]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_310:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_310]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_310]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_311:
    lea rsi, [rip + .L__s3_failure_prefix_311]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_312:
    lea rsi, [rip + .L__s3_failure_prefix_312]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_313:
    lea rsi, [rip + .L__s3_failure_prefix_313]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_314:
    lea rsi, [rip + .L__s3_failure_prefix_314]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_315:
    lea rsi, [rip + .L__s3_failure_prefix_315]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_316:
    lea rsi, [rip + .L__s3_failure_prefix_316]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_317:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_317]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_317]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_318:
    lea rsi, [rip + .L__s3_failure_prefix_318]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_319:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_319]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_319]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_320:
    lea rsi, [rip + .L__s3_failure_prefix_320]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_321:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_321]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_321]
    mov r8d, 21
    jmp __s3_fail_value
.L__s3_failure_site_322:
    lea rsi, [rip + .L__s3_failure_prefix_322]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_323:
    lea rsi, [rip + .L__s3_failure_prefix_323]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_324:
    lea rsi, [rip + .L__s3_failure_prefix_324]
    mov edx, 155
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
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_327]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_328:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_328]
    mov edx, 125
    lea rcx, [rip + .L__s3_failure_suffix_328]
    mov r8d, 21
    jmp __s3_fail_value
.L__s3_failure_site_329:
    lea rsi, [rip + .L__s3_failure_prefix_329]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_330:
    lea rsi, [rip + .L__s3_failure_prefix_330]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_331:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_331]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_331]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_332:
    lea rsi, [rip + .L__s3_failure_prefix_332]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_333:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_333]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_333]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_334:
    lea rsi, [rip + .L__s3_failure_prefix_334]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_335:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_335]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_335]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_336:
    lea rsi, [rip + .L__s3_failure_prefix_336]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_337:
    lea rsi, [rip + .L__s3_failure_prefix_337]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_338:
    lea rsi, [rip + .L__s3_failure_prefix_338]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_339:
    lea rsi, [rip + .L__s3_failure_prefix_339]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_340:
    lea rsi, [rip + .L__s3_failure_prefix_340]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_341:
    lea rsi, [rip + .L__s3_failure_prefix_341]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_342:
    lea rsi, [rip + .L__s3_failure_prefix_342]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_343:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_343]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_343]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_344:
    lea rsi, [rip + .L__s3_failure_prefix_344]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_345:
    lea rsi, [rip + .L__s3_failure_prefix_345]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_346:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_346]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_346]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_347:
    lea rsi, [rip + .L__s3_failure_prefix_347]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_348:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_348]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_348]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_349:
    lea rsi, [rip + .L__s3_failure_prefix_349]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_350:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_350]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_350]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_351:
    lea rsi, [rip + .L__s3_failure_prefix_351]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_352:
    lea rsi, [rip + .L__s3_failure_prefix_352]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_353:
    lea rsi, [rip + .L__s3_failure_prefix_353]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_354:
    lea rsi, [rip + .L__s3_failure_prefix_354]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_355:
    lea rsi, [rip + .L__s3_failure_prefix_355]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_356:
    lea rsi, [rip + .L__s3_failure_prefix_356]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_357:
    lea rsi, [rip + .L__s3_failure_prefix_357]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_358:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_358]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_358]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_359:
    lea rsi, [rip + .L__s3_failure_prefix_359]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_360:
    lea rsi, [rip + .L__s3_failure_prefix_360]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_361:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_361]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_361]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_362:
    lea rsi, [rip + .L__s3_failure_prefix_362]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_363:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_363]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_363]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_364:
    lea rsi, [rip + .L__s3_failure_prefix_364]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_365:
    lea rsi, [rip + .L__s3_failure_prefix_365]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_366:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_366]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_366]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_367:
    lea rsi, [rip + .L__s3_failure_prefix_367]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_368:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_368]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_368]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_369:
    lea rsi, [rip + .L__s3_failure_prefix_369]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_370:
    lea rsi, [rip + .L__s3_failure_prefix_370]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_371:
    lea rsi, [rip + .L__s3_failure_prefix_371]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_372:
    lea rsi, [rip + .L__s3_failure_prefix_372]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_373:
    lea rsi, [rip + .L__s3_failure_prefix_373]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_374:
    lea rsi, [rip + .L__s3_failure_prefix_374]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_375:
    lea rsi, [rip + .L__s3_failure_prefix_375]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_376:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_376]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_376]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_377:
    lea rsi, [rip + .L__s3_failure_prefix_377]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_378:
    lea rsi, [rip + .L__s3_failure_prefix_378]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_379:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_379]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_379]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_380:
    lea rsi, [rip + .L__s3_failure_prefix_380]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_381:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_381]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_381]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_382:
    lea rsi, [rip + .L__s3_failure_prefix_382]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_383:
    lea rsi, [rip + .L__s3_failure_prefix_383]
    mov edx, 154
    jmp __s3_fail_message
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
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_388:
    lea rsi, [rip + .L__s3_failure_prefix_388]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_389:
    lea rsi, [rip + .L__s3_failure_prefix_389]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_390:
    lea rsi, [rip + .L__s3_failure_prefix_390]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_391:
    lea rsi, [rip + .L__s3_failure_prefix_391]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_392:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_392]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_392]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_393:
    lea rsi, [rip + .L__s3_failure_prefix_393]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_394:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_394]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_394]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_395:
    lea rsi, [rip + .L__s3_failure_prefix_395]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_396:
    lea rsi, [rip + .L__s3_failure_prefix_396]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_397:
    lea rsi, [rip + .L__s3_failure_prefix_397]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_398:
    lea rsi, [rip + .L__s3_failure_prefix_398]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_399:
    lea rsi, [rip + .L__s3_failure_prefix_399]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_400:
    lea rsi, [rip + .L__s3_failure_prefix_400]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_401:
    lea rsi, [rip + .L__s3_failure_prefix_401]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_402:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_402]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_402]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_403:
    lea rsi, [rip + .L__s3_failure_prefix_403]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_404:
    lea rsi, [rip + .L__s3_failure_prefix_404]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_405:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_405]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_405]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_406:
    lea rsi, [rip + .L__s3_failure_prefix_406]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_407:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_407]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_407]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_408:
    lea rsi, [rip + .L__s3_failure_prefix_408]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_409:
    lea rsi, [rip + .L__s3_failure_prefix_409]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_410:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_410]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_410]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_411:
    lea rsi, [rip + .L__s3_failure_prefix_411]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_412:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_412]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_412]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_413:
    lea rsi, [rip + .L__s3_failure_prefix_413]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_414:
    lea rsi, [rip + .L__s3_failure_prefix_414]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_415:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_415]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_415]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_416:
    lea rsi, [rip + .L__s3_failure_prefix_416]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_417:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_417]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_417]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_418:
    lea rsi, [rip + .L__s3_failure_prefix_418]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_419:
    lea rsi, [rip + .L__s3_failure_prefix_419]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_420:
    lea rsi, [rip + .L__s3_failure_prefix_420]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_421:
    lea rsi, [rip + .L__s3_failure_prefix_421]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_422:
    lea rsi, [rip + .L__s3_failure_prefix_422]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_423:
    lea rsi, [rip + .L__s3_failure_prefix_423]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_424:
    lea rsi, [rip + .L__s3_failure_prefix_424]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_425:
    lea rsi, [rip + .L__s3_failure_prefix_425]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_426:
    lea rsi, [rip + .L__s3_failure_prefix_426]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_427:
    lea rsi, [rip + .L__s3_failure_prefix_427]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_428:
    lea rsi, [rip + .L__s3_failure_prefix_428]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_429:
    lea rsi, [rip + .L__s3_failure_prefix_429]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_430:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_430]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_430]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_431:
    lea rsi, [rip + .L__s3_failure_prefix_431]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_432:
    lea rsi, [rip + .L__s3_failure_prefix_432]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_433:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_433]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_433]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_434:
    lea rsi, [rip + .L__s3_failure_prefix_434]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_435:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_435]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_435]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_436:
    lea rsi, [rip + .L__s3_failure_prefix_436]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_437:
    lea rsi, [rip + .L__s3_failure_prefix_437]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_438:
    lea rsi, [rip + .L__s3_failure_prefix_438]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_439:
    lea rsi, [rip + .L__s3_failure_prefix_439]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_440:
    lea rsi, [rip + .L__s3_failure_prefix_440]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_441:
    lea rsi, [rip + .L__s3_failure_prefix_441]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_442:
    lea rsi, [rip + .L__s3_failure_prefix_442]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_443:
    lea rsi, [rip + .L__s3_failure_prefix_443]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_444:
    lea rsi, [rip + .L__s3_failure_prefix_444]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_445:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_445]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_445]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_446:
    lea rsi, [rip + .L__s3_failure_prefix_446]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_447:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_447]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_447]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_448:
    lea rsi, [rip + .L__s3_failure_prefix_448]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_449:
    lea rsi, [rip + .L__s3_failure_prefix_449]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_450:
    lea rsi, [rip + .L__s3_failure_prefix_450]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_451:
    lea rsi, [rip + .L__s3_failure_prefix_451]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_452:
    lea rsi, [rip + .L__s3_failure_prefix_452]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_453:
    lea rsi, [rip + .L__s3_failure_prefix_453]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_454:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_454]
    mov edx, 116
    lea rcx, [rip + .L__s3_failure_suffix_454]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_455:
    lea rsi, [rip + .L__s3_failure_prefix_455]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_456:
    lea rsi, [rip + .L__s3_failure_prefix_456]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_457:
    lea rsi, [rip + .L__s3_failure_prefix_457]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_458:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_458]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_458]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_459:
    lea rsi, [rip + .L__s3_failure_prefix_459]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_460:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_460]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_460]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_461:
    lea rsi, [rip + .L__s3_failure_prefix_461]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_462:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_462]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_462]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_463:
    lea rsi, [rip + .L__s3_failure_prefix_463]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_464:
    lea rsi, [rip + .L__s3_failure_prefix_464]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_465:
    lea rsi, [rip + .L__s3_failure_prefix_465]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_466:
    lea rsi, [rip + .L__s3_failure_prefix_466]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_467:
    lea rsi, [rip + .L__s3_failure_prefix_467]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_468:
    lea rsi, [rip + .L__s3_failure_prefix_468]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_469:
    lea rsi, [rip + .L__s3_failure_prefix_469]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_470:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_470]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_470]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_471:
    lea rsi, [rip + .L__s3_failure_prefix_471]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_472:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_472]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_472]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_473:
    lea rsi, [rip + .L__s3_failure_prefix_473]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_474:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_474]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_474]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_475:
    lea rsi, [rip + .L__s3_failure_prefix_475]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_476:
    lea rsi, [rip + .L__s3_failure_prefix_476]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_477:
    lea rsi, [rip + .L__s3_failure_prefix_477]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_478:
    lea rsi, [rip + .L__s3_failure_prefix_478]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_479:
    lea rsi, [rip + .L__s3_failure_prefix_479]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_480:
    lea rsi, [rip + .L__s3_failure_prefix_480]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_481:
    lea rsi, [rip + .L__s3_failure_prefix_481]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_482:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_482]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_482]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_483:
    lea rsi, [rip + .L__s3_failure_prefix_483]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_484:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_484]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_484]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_485:
    lea rsi, [rip + .L__s3_failure_prefix_485]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_486:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_486]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_486]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_487:
    lea rsi, [rip + .L__s3_failure_prefix_487]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_488:
    lea rsi, [rip + .L__s3_failure_prefix_488]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_489:
    lea rsi, [rip + .L__s3_failure_prefix_489]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_490:
    lea rsi, [rip + .L__s3_failure_prefix_490]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_491:
    lea rsi, [rip + .L__s3_failure_prefix_491]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_492:
    lea rsi, [rip + .L__s3_failure_prefix_492]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_493:
    lea rsi, [rip + .L__s3_failure_prefix_493]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_494:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_494]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_494]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_495:
    lea rsi, [rip + .L__s3_failure_prefix_495]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_496:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_496]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_496]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_497:
    lea rsi, [rip + .L__s3_failure_prefix_497]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_498:
    lea rsi, [rip + .L__s3_failure_prefix_498]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_499:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_499]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_499]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_500:
    lea rsi, [rip + .L__s3_failure_prefix_500]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_501:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_501]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_501]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_502:
    lea rsi, [rip + .L__s3_failure_prefix_502]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_503:
    lea rsi, [rip + .L__s3_failure_prefix_503]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_504:
    lea rsi, [rip + .L__s3_failure_prefix_504]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_505:
    lea rsi, [rip + .L__s3_failure_prefix_505]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_506:
    lea rsi, [rip + .L__s3_failure_prefix_506]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_507:
    lea rsi, [rip + .L__s3_failure_prefix_507]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_508:
    lea rsi, [rip + .L__s3_failure_prefix_508]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_509:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_509]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_509]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_510:
    lea rsi, [rip + .L__s3_failure_prefix_510]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_511:
    lea rsi, [rip + .L__s3_failure_prefix_511]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_512:
    lea rsi, [rip + .L__s3_failure_prefix_512]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_513:
    lea rsi, [rip + .L__s3_failure_prefix_513]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_514:
    lea rsi, [rip + .L__s3_failure_prefix_514]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_515:
    lea rsi, [rip + .L__s3_failure_prefix_515]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_516:
    lea rsi, [rip + .L__s3_failure_prefix_516]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_517:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_517]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_517]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_518:
    lea rsi, [rip + .L__s3_failure_prefix_518]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_519:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_519]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_519]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_520:
    lea rsi, [rip + .L__s3_failure_prefix_520]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_521:
    lea rsi, [rip + .L__s3_failure_prefix_521]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_522:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_522]
    mov edx, 129
    lea rcx, [rip + .L__s3_failure_suffix_522]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_523:
    lea rsi, [rip + .L__s3_failure_prefix_523]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_524:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_524]
    mov edx, 115
    lea rcx, [rip + .L__s3_failure_suffix_524]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_525:
    lea rsi, [rip + .L__s3_failure_prefix_525]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_526:
    lea rsi, [rip + .L__s3_failure_prefix_526]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_527:
    lea rsi, [rip + .L__s3_failure_prefix_527]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_528:
    lea rsi, [rip + .L__s3_failure_prefix_528]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_529:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_529]
    mov edx, 123
    lea rcx, [rip + .L__s3_failure_suffix_529]
    mov r8d, 15
    jmp __s3_fail_value
.L__s3_failure_site_530:
    lea rsi, [rip + .L__s3_failure_prefix_530]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_531:
    lea rsi, [rip + .L__s3_failure_prefix_531]
    mov edx, 156
    jmp __s3_fail_message
.L__s3_failure_site_532:
    lea rsi, [rip + .L__s3_failure_prefix_532]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_533:
    lea rsi, [rip + .L__s3_failure_prefix_533]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_534:
    lea rsi, [rip + .L__s3_failure_prefix_534]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_535:
    lea rsi, [rip + .L__s3_failure_prefix_535]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_536:
    lea rsi, [rip + .L__s3_failure_prefix_536]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_537:
    lea rsi, [rip + .L__s3_failure_prefix_537]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_538:
    lea rsi, [rip + .L__s3_failure_prefix_538]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_539:
    lea rsi, [rip + .L__s3_failure_prefix_539]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_540:
    lea rsi, [rip + .L__s3_failure_prefix_540]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_541:
    lea rsi, [rip + .L__s3_failure_prefix_541]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_542:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_542]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_542]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_543:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_543]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_543]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_544:
    lea rsi, [rip + .L__s3_failure_prefix_544]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_545:
    lea rsi, [rip + .L__s3_failure_prefix_545]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_546:
    lea rsi, [rip + .L__s3_failure_prefix_546]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_547:
    lea rsi, [rip + .L__s3_failure_prefix_547]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_548:
    lea rsi, [rip + .L__s3_failure_prefix_548]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_549:
    lea rsi, [rip + .L__s3_failure_prefix_549]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_550:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_550]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_550]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_551:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_551]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_551]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_552:
    lea rsi, [rip + .L__s3_failure_prefix_552]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_553:
    lea rsi, [rip + .L__s3_failure_prefix_553]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_554:
    lea rsi, [rip + .L__s3_failure_prefix_554]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_555:
    lea rsi, [rip + .L__s3_failure_prefix_555]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_556:
    lea rsi, [rip + .L__s3_failure_prefix_556]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_557:
    lea rsi, [rip + .L__s3_failure_prefix_557]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_558:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_558]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_558]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_559:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_559]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_559]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_560:
    lea rsi, [rip + .L__s3_failure_prefix_560]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_561:
    lea rsi, [rip + .L__s3_failure_prefix_561]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_562:
    lea rsi, [rip + .L__s3_failure_prefix_562]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_563:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_563]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_563]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_564:
    lea rsi, [rip + .L__s3_failure_prefix_564]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_565:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_565]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_565]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_566:
    lea rsi, [rip + .L__s3_failure_prefix_566]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_567:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_567]
    mov edx, 124
    lea rcx, [rip + .L__s3_failure_suffix_567]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_568:
    lea rsi, [rip + .L__s3_failure_prefix_568]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_569:
    lea rsi, [rip + .L__s3_failure_prefix_569]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_570:
    lea rsi, [rip + .L__s3_failure_prefix_570]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_571:
    lea rsi, [rip + .L__s3_failure_prefix_571]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_572:
    lea rsi, [rip + .L__s3_failure_prefix_572]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_573:
    lea rsi, [rip + .L__s3_failure_prefix_573]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_574:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_574]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_574]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_575:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_575]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_575]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_576:
    lea rsi, [rip + .L__s3_failure_prefix_576]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_577:
    lea rsi, [rip + .L__s3_failure_prefix_577]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_578:
    lea rsi, [rip + .L__s3_failure_prefix_578]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_579:
    lea rsi, [rip + .L__s3_failure_prefix_579]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_580:
    lea rsi, [rip + .L__s3_failure_prefix_580]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_581:
    lea rsi, [rip + .L__s3_failure_prefix_581]
    mov edx, 155
    jmp __s3_fail_message
.L__s3_failure_site_582:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_582]
    mov edx, 114
    lea rcx, [rip + .L__s3_failure_suffix_582]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_583:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_583]
    mov edx, 122
    lea rcx, [rip + .L__s3_failure_suffix_583]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_584:
    lea rsi, [rip + .L__s3_failure_prefix_584]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_585:
    lea rsi, [rip + .L__s3_failure_prefix_585]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_586:
    lea rsi, [rip + .L__s3_failure_prefix_586]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_587:
    lea rsi, [rip + .L__s3_failure_prefix_587]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_588:
    lea rsi, [rip + .L__s3_failure_prefix_588]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_589:
    lea rsi, [rip + .L__s3_failure_prefix_589]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_590:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_590]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_590]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_591:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_591]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_591]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_592:
    lea rsi, [rip + .L__s3_failure_prefix_592]
    mov edx, 150
    jmp __s3_fail_message
.L__s3_failure_site_593:
    lea rsi, [rip + .L__s3_failure_prefix_593]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_594:
    lea rsi, [rip + .L__s3_failure_prefix_594]
    mov edx, 152
    jmp __s3_fail_message
.L__s3_failure_site_595:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_595]
    mov edx, 127
    lea rcx, [rip + .L__s3_failure_suffix_595]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_596:
    lea rsi, [rip + .L__s3_failure_prefix_596]
    mov edx, 154
    jmp __s3_fail_message
.L__s3_failure_site_597:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_597]
    mov edx, 113
    lea rcx, [rip + .L__s3_failure_suffix_597]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_598:
    lea rsi, [rip + .L__s3_failure_prefix_598]
    mov edx, 151
    jmp __s3_fail_message
.L__s3_failure_site_599:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_599]
    mov edx, 124
    lea rcx, [rip + .L__s3_failure_suffix_599]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_600:
    lea rsi, [rip + .L__s3_failure_prefix_600]
    mov edx, 153
    jmp __s3_fail_message
.L__s3_failure_site_601:
    lea rsi, [rip + .L__s3_failure_prefix_601]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_602:
    lea rsi, [rip + .L__s3_failure_prefix_602]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_603:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_603]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_603]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_604:
    lea rsi, [rip + .L__s3_failure_prefix_604]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_605:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_605]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_605]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_606:
    lea rsi, [rip + .L__s3_failure_prefix_606]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_607:
    lea rsi, [rip + .L__s3_failure_prefix_607]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_608:
    lea rsi, [rip + .L__s3_failure_prefix_608]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_609:
    lea rsi, [rip + .L__s3_failure_prefix_609]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_610:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_610]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_610]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_611:
    lea rsi, [rip + .L__s3_failure_prefix_611]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_612:
    lea rsi, [rip + .L__s3_failure_prefix_612]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_613:
    lea rsi, [rip + .L__s3_failure_prefix_613]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_614:
    lea rsi, [rip + .L__s3_failure_prefix_614]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_615:
    lea rsi, [rip + .L__s3_failure_prefix_615]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_616:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_616]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_616]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_617:
    lea rsi, [rip + .L__s3_failure_prefix_617]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_618:
    lea rsi, [rip + .L__s3_failure_prefix_618]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_619:
    lea rsi, [rip + .L__s3_failure_prefix_619]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_620:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_620]
    mov edx, 133
    lea rcx, [rip + .L__s3_failure_suffix_620]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_621:
    lea rsi, [rip + .L__s3_failure_prefix_621]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_622:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_622]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_622]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_623:
    lea rsi, [rip + .L__s3_failure_prefix_623]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_624:
    lea rsi, [rip + .L__s3_failure_prefix_624]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_625:
    lea rsi, [rip + .L__s3_failure_prefix_625]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_626:
    lea rsi, [rip + .L__s3_failure_prefix_626]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_627:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_627]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_627]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_628:
    lea rsi, [rip + .L__s3_failure_prefix_628]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_629:
    lea rsi, [rip + .L__s3_failure_prefix_629]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_630:
    lea rsi, [rip + .L__s3_failure_prefix_630]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_631:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_631]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_631]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_632:
    lea rsi, [rip + .L__s3_failure_prefix_632]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_633:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_633]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_633]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_634:
    lea rsi, [rip + .L__s3_failure_prefix_634]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_635:
    lea rsi, [rip + .L__s3_failure_prefix_635]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_636:
    lea rsi, [rip + .L__s3_failure_prefix_636]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_637:
    lea rsi, [rip + .L__s3_failure_prefix_637]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_638:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_638]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_638]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_639:
    lea rsi, [rip + .L__s3_failure_prefix_639]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_640:
    lea rsi, [rip + .L__s3_failure_prefix_640]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_641:
    lea rsi, [rip + .L__s3_failure_prefix_641]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_642:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_642]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_642]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_643:
    lea rsi, [rip + .L__s3_failure_prefix_643]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_644:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_644]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_644]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_645:
    lea rsi, [rip + .L__s3_failure_prefix_645]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_646:
    lea rsi, [rip + .L__s3_failure_prefix_646]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_647:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_647]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_647]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_648:
    lea rsi, [rip + .L__s3_failure_prefix_648]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_649:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_649]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_649]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_650:
    lea rsi, [rip + .L__s3_failure_prefix_650]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_651:
    lea rsi, [rip + .L__s3_failure_prefix_651]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_652:
    lea rsi, [rip + .L__s3_failure_prefix_652]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_653:
    lea rsi, [rip + .L__s3_failure_prefix_653]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_654:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_654]
    mov edx, 131
    lea rcx, [rip + .L__s3_failure_suffix_654]
    mov r8d, 17
    jmp __s3_fail_value
.L__s3_failure_site_655:
    lea rsi, [rip + .L__s3_failure_prefix_655]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_656:
    lea rsi, [rip + .L__s3_failure_prefix_656]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_657:
    lea rsi, [rip + .L__s3_failure_prefix_657]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_658:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_658]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_658]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_659:
    lea rsi, [rip + .L__s3_failure_prefix_659]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_660:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_660]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_660]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_661:
    lea rsi, [rip + .L__s3_failure_prefix_661]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_662:
    lea rsi, [rip + .L__s3_failure_prefix_662]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_663:
    lea rsi, [rip + .L__s3_failure_prefix_663]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_664:
    lea rsi, [rip + .L__s3_failure_prefix_664]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_665:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_665]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_665]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_666:
    lea rsi, [rip + .L__s3_failure_prefix_666]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_667:
    lea rsi, [rip + .L__s3_failure_prefix_667]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_668:
    lea rsi, [rip + .L__s3_failure_prefix_668]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_669:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_669]
    mov edx, 133
    lea rcx, [rip + .L__s3_failure_suffix_669]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_670:
    lea rsi, [rip + .L__s3_failure_prefix_670]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_671:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_671]
    mov edx, 119
    lea rcx, [rip + .L__s3_failure_suffix_671]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_672:
    lea rsi, [rip + .L__s3_failure_prefix_672]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_673:
    lea rsi, [rip + .L__s3_failure_prefix_673]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_674:
    lea rsi, [rip + .L__s3_failure_prefix_674]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_675:
    lea rsi, [rip + .L__s3_failure_prefix_675]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_676:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_676]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_676]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_677:
    lea rsi, [rip + .L__s3_failure_prefix_677]
    mov edx, 157
    jmp __s3_fail_message
.L__s3_failure_site_678:
    lea rsi, [rip + .L__s3_failure_prefix_678]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_679:
    lea rsi, [rip + .L__s3_failure_prefix_679]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_680:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_680]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_680]
    mov r8d, 25
    jmp __s3_fail_value
.L__s3_failure_site_681:
    lea rsi, [rip + .L__s3_failure_prefix_681]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_682:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_682]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_682]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_683:
    lea rsi, [rip + .L__s3_failure_prefix_683]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_684:
    lea rsi, [rip + .L__s3_failure_prefix_684]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_685:
    lea rsi, [rip + .L__s3_failure_prefix_685]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_686:
    lea rsi, [rip + .L__s3_failure_prefix_686]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_687:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_687]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_687]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_688:
    lea rsi, [rip + .L__s3_failure_prefix_688]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_689:
    lea rsi, [rip + .L__s3_failure_prefix_689]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_690:
    lea rsi, [rip + .L__s3_failure_prefix_690]
    mov edx, 159
    jmp __s3_fail_message
.L__s3_failure_site_691:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_691]
    mov edx, 134
    lea rcx, [rip + .L__s3_failure_suffix_691]
    mov r8d, 24
    jmp __s3_fail_value
.L__s3_failure_site_692:
    lea rsi, [rip + .L__s3_failure_prefix_692]
    mov edx, 161
    jmp __s3_fail_message
.L__s3_failure_site_693:
    mov rdi, r10
    lea rsi, [rip + .L__s3_failure_prefix_693]
    mov edx, 120
    lea rcx, [rip + .L__s3_failure_suffix_693]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_694:
    lea rsi, [rip + .L__s3_failure_prefix_694]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_695:
    lea rsi, [rip + .L__s3_failure_prefix_695]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_696:
    lea rsi, [rip + .L__s3_failure_prefix_696]
    mov edx, 137
    jmp __s3_fail_message
.L__s3_failure_site_697:
    lea rsi, [rip + .L__s3_failure_prefix_697]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_698:
    lea rsi, [rip + .L__s3_failure_prefix_698]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_699:
    lea rsi, [rip + .L__s3_failure_prefix_699]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_700:
    lea rsi, [rip + .L__s3_failure_prefix_700]
    mov edx, 160
    jmp __s3_fail_message
.L__s3_failure_site_701:
    lea rsi, [rip + .L__s3_failure_prefix_701]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_702:
    lea rsi, [rip + .L__s3_failure_prefix_702]
    mov edx, 162
    jmp __s3_fail_message
.L__s3_failure_site_703:
    mov rdi, rax
    lea rsi, [rip + .L__s3_failure_prefix_703]
    mov edx, 121
    lea rcx, [rip + .L__s3_failure_suffix_703]
    mov r8d, 16
    jmp __s3_fail_value
.L__s3_failure_site_704:
    lea rsi, [rip + .L__s3_failure_prefix_704]
    mov edx, 158
    jmp __s3_fail_message
.L__s3_failure_site_705:
    mov rdi, qword ptr [rip + __s3_frame_count]
    lea rsi, [rip + .L__s3_failure_prefix_705]
    mov edx, 93
    lea rcx, [rip + .L__s3_failure_suffix_705]
    mov r8d, 20
    jmp __s3_fail_value
.L__s3_failure_site_706:
    lea rsi, [rip + .L__s3_failure_prefix_706]
    mov edx, 126
    jmp __s3_fail_message
.L__s3_failure_site_707:
    lea rsi, [rip + .L__s3_failure_prefix_707]
    mov edx, 123
    jmp __s3_fail_message

.section .rodata
.L__s3_failure_prefix_0:
    .ascii "runtime error [frame limit] in function 'absolute_f64'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_0:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_1:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 2:19 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_2:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 2:17 (block entry, TREL): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_3:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 2:5 (block entry, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_4:
    .ascii "runtime error [invalid trit state] in function 'absolute_f64'\nat source 2:5 (block entry, TBR3): value "
.L__s3_failure_suffix_4:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_5:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 4:20 (block switch_negative_0, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_6:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 4:24 (block switch_negative_0, TNDIFF): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_7:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 4:13 (block switch_negative_0, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_8:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 6:13 (block switch_neutral_1, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_9:
    .ascii "runtime error [instruction limit] in function 'absolute_f64'\nat source 8:13 (block switch_positive_2, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_10:
    .ascii "runtime error [frame limit] in function 'energy_series_aggregation'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_10:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_11:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 16:29 (block entry, TSLEN): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_12:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 16:29 (block entry, TSLEN): register r1 is uninitialized\n"
.L__s3_failure_prefix_13:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 16:5 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_14:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 16:5 (block entry, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_15:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 16:5 (block entry, TSTORE): register r8 is uninitialized\n"
.L__s3_failure_prefix_16:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 16:5 (block entry, TSTORE): register r7 is uninitialized\n"
.L__s3_failure_prefix_17:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 16:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_17:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_18:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 17:27 (block entry, TSLEN): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_19:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 17:27 (block entry, TSLEN): register r3 is uninitialized\n"
.L__s3_failure_prefix_20:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 17:5 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_21:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 17:5 (block entry, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_22:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 17:5 (block entry, TSTORE): register r10 is uninitialized\n"
.L__s3_failure_prefix_23:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 17:5 (block entry, TSTORE): register r9 is uninitialized\n"
.L__s3_failure_prefix_24:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 17:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_24:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_25:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 18:29 (block entry, TSLEN): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_26:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 18:29 (block entry, TSLEN): register r6 is uninitialized\n"
.L__s3_failure_prefix_27:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 18:5 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_28:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 18:5 (block entry, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_29:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 18:5 (block entry, TSTORE): register r12 is uninitialized\n"
.L__s3_failure_prefix_30:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 18:5 (block entry, TSTORE): register r11 is uninitialized\n"
.L__s3_failure_prefix_31:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 18:5 (block entry, TSTORE): index "
.L__s3_failure_suffix_31:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_32:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:11 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_33:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:11 (block entry, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_34:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 19:11 (block entry, TLOAD): index "
.L__s3_failure_suffix_34:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_35:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:11 (block entry, TLOAD): register r13 is uninitialized\n"
.L__s3_failure_prefix_36:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 19:11 (block entry, TLOAD): index "
.L__s3_failure_suffix_36:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_37:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:26 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_38:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block entry, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_39:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block entry, TCMP): register r14 is uninitialized\n"
.L__s3_failure_prefix_40:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block entry, TCMP): register r15 is uninitialized\n"
.L__s3_failure_prefix_41:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block entry, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_42:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_43:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_44:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_45:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TSTORE): register r17 is uninitialized\n"
.L__s3_failure_prefix_46:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TSTORE): register r18 is uninitialized\n"
.L__s3_failure_prefix_47:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TSTORE): index "
.L__s3_failure_suffix_47:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_48:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TSTORE): trit result "
.L__s3_failure_suffix_48:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_49:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_neg_0, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_50:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_51:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_52:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_53:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TSTORE): register r19 is uninitialized\n"
.L__s3_failure_prefix_54:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TSTORE): register r20 is uninitialized\n"
.L__s3_failure_prefix_55:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TSTORE): index "
.L__s3_failure_suffix_55:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_56:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TSTORE): trit result "
.L__s3_failure_suffix_56:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_57:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_zero_1, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_58:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_59:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_60:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_61:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TSTORE): register r21 is uninitialized\n"
.L__s3_failure_prefix_62:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TSTORE): register r22 is uninitialized\n"
.L__s3_failure_prefix_63:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TSTORE): index "
.L__s3_failure_suffix_63:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_64:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TSTORE): trit result "
.L__s3_failure_suffix_64:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_65:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_pos_2, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_66:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_cont_3, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_67:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:24 (block rel_cont_3, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_68:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 19:24 (block rel_cont_3, TLOAD): index "
.L__s3_failure_suffix_68:
    .ascii " is uninitialized in m3\n"
.L__s3_failure_prefix_69:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:24 (block rel_cont_3, TLOAD): register r23 is uninitialized\n"
.L__s3_failure_prefix_70:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 19:24 (block rel_cont_3, TLOAD): index "
.L__s3_failure_suffix_70:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_71:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 19:5 (block rel_cont_3, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_72:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 19:5 (block rel_cont_3, TBR3): value "
.L__s3_failure_suffix_72:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_73:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 19:5 (block rel_cont_3, TBR3): register r24 is uninitialized\n"
.L__s3_failure_prefix_74:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 21:28 (block switch_negative_4, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_75:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 21:13 (block switch_negative_4, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_76:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 21:13 (block switch_negative_4, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_77:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 21:13 (block switch_negative_4, TSTORE): register r26 is uninitialized\n"
.L__s3_failure_prefix_78:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 21:13 (block switch_negative_4, TSTORE): register r25 is uninitialized\n"
.L__s3_failure_prefix_79:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 21:13 (block switch_negative_4, TSTORE): index "
.L__s3_failure_suffix_79:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_80:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 20:9 (block switch_negative_4, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_81:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 23:28 (block switch_neutral_5, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_82:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 23:28 (block switch_neutral_5, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_83:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 23:28 (block switch_neutral_5, TLOAD): index "
.L__s3_failure_suffix_83:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_84:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 23:28 (block switch_neutral_5, TLOAD): register r27 is uninitialized\n"
.L__s3_failure_prefix_85:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 23:28 (block switch_neutral_5, TLOAD): index "
.L__s3_failure_suffix_85:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_86:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 23:13 (block switch_neutral_5, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_87:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 23:13 (block switch_neutral_5, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_88:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 23:13 (block switch_neutral_5, TSTORE): register r29 is uninitialized\n"
.L__s3_failure_prefix_89:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 23:13 (block switch_neutral_5, TSTORE): register r28 is uninitialized\n"
.L__s3_failure_prefix_90:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 23:13 (block switch_neutral_5, TSTORE): index "
.L__s3_failure_suffix_90:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_91:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 22:9 (block switch_neutral_5, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_92:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 25:28 (block switch_positive_6, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_93:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 25:28 (block switch_positive_6, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_94:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 25:28 (block switch_positive_6, TLOAD): index "
.L__s3_failure_suffix_94:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_95:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 25:28 (block switch_positive_6, TLOAD): register r30 is uninitialized\n"
.L__s3_failure_prefix_96:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 25:28 (block switch_positive_6, TLOAD): index "
.L__s3_failure_suffix_96:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_97:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 25:13 (block switch_positive_6, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_98:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 25:13 (block switch_positive_6, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_99:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 25:13 (block switch_positive_6, TSTORE): register r32 is uninitialized\n"
.L__s3_failure_prefix_100:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 25:13 (block switch_positive_6, TSTORE): register r31 is uninitialized\n"
.L__s3_failure_prefix_101:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 25:13 (block switch_positive_6, TSTORE): index "
.L__s3_failure_suffix_101:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_102:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 24:9 (block switch_positive_6, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_103:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:11 (block switch_continue_7, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_104:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:11 (block switch_continue_7, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_105:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 26:11 (block switch_continue_7, TLOAD): index "
.L__s3_failure_suffix_105:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_106:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:11 (block switch_continue_7, TLOAD): register r33 is uninitialized\n"
.L__s3_failure_prefix_107:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 26:11 (block switch_continue_7, TLOAD): index "
.L__s3_failure_suffix_107:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_108:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:27 (block switch_continue_7, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_109:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block switch_continue_7, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_110:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block switch_continue_7, TCMP): register r34 is uninitialized\n"
.L__s3_failure_prefix_111:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block switch_continue_7, TCMP): register r35 is uninitialized\n"
.L__s3_failure_prefix_112:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block switch_continue_7, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_113:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_114:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_115:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_116:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TSTORE): register r37 is uninitialized\n"
.L__s3_failure_prefix_117:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TSTORE): register r38 is uninitialized\n"
.L__s3_failure_prefix_118:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TSTORE): index "
.L__s3_failure_suffix_118:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_119:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TSTORE): trit result "
.L__s3_failure_suffix_119:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_120:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_neg_8, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_121:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_122:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_123:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_124:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TSTORE): register r39 is uninitialized\n"
.L__s3_failure_prefix_125:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TSTORE): register r40 is uninitialized\n"
.L__s3_failure_prefix_126:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TSTORE): index "
.L__s3_failure_suffix_126:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_127:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TSTORE): trit result "
.L__s3_failure_suffix_127:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_128:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_zero_9, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_129:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_130:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_131:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_132:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TSTORE): register r41 is uninitialized\n"
.L__s3_failure_prefix_133:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TSTORE): register r42 is uninitialized\n"
.L__s3_failure_prefix_134:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TSTORE): index "
.L__s3_failure_suffix_134:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_135:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TSTORE): trit result "
.L__s3_failure_suffix_135:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_136:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_pos_10, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_137:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_cont_11, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_138:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:24 (block rel_cont_11, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_139:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 26:24 (block rel_cont_11, TLOAD): index "
.L__s3_failure_suffix_139:
    .ascii " is uninitialized in m4\n"
.L__s3_failure_prefix_140:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:24 (block rel_cont_11, TLOAD): register r43 is uninitialized\n"
.L__s3_failure_prefix_141:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 26:24 (block rel_cont_11, TLOAD): index "
.L__s3_failure_suffix_141:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_142:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 26:5 (block rel_cont_11, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_143:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 26:5 (block rel_cont_11, TBR3): value "
.L__s3_failure_suffix_143:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_144:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 26:5 (block rel_cont_11, TBR3): register r44 is uninitialized\n"
.L__s3_failure_prefix_145:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 28:20 (block switch_negative_12, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_146:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 28:13 (block switch_negative_12, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_147:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 28:13 (block switch_negative_12, TRET): register r45 is uninitialized\n"
.L__s3_failure_prefix_148:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:19 (block switch_neutral_13, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_149:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:19 (block switch_neutral_13, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_150:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 30:19 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_150:
    .ascii " is uninitialized in m1\n"
.L__s3_failure_prefix_151:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:19 (block switch_neutral_13, TLOAD): register r46 is uninitialized\n"
.L__s3_failure_prefix_152:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 30:19 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_152:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_153:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:33 (block switch_neutral_13, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_154:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:33 (block switch_neutral_13, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_155:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 30:33 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_155:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_156:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:33 (block switch_neutral_13, TLOAD): register r48 is uninitialized\n"
.L__s3_failure_prefix_157:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 30:33 (block switch_neutral_13, TLOAD): index "
.L__s3_failure_suffix_157:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_158:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block switch_neutral_13, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_159:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block switch_neutral_13, TCMP): register r47 is uninitialized\n"
.L__s3_failure_prefix_160:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block switch_neutral_13, TCMP): register r49 is uninitialized\n"
.L__s3_failure_prefix_161:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block switch_neutral_13, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_162:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 85:20 (block switch_positive_14, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_163:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 85:13 (block switch_positive_14, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_164:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 85:13 (block switch_positive_14, TRET): register r210 is uninitialized\n"
.L__s3_failure_prefix_165:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_166:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_167:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_168:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TSTORE): register r51 is uninitialized\n"
.L__s3_failure_prefix_169:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TSTORE): register r52 is uninitialized\n"
.L__s3_failure_prefix_170:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TSTORE): index "
.L__s3_failure_suffix_170:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_171:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TSTORE): trit result "
.L__s3_failure_suffix_171:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_172:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_neg_15, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_173:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_174:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_175:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_176:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TSTORE): register r53 is uninitialized\n"
.L__s3_failure_prefix_177:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TSTORE): register r54 is uninitialized\n"
.L__s3_failure_prefix_178:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TSTORE): index "
.L__s3_failure_suffix_178:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_179:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TSTORE): trit result "
.L__s3_failure_suffix_179:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_180:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_zero_16, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_181:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_182:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_183:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_184:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TSTORE): register r55 is uninitialized\n"
.L__s3_failure_prefix_185:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TSTORE): register r56 is uninitialized\n"
.L__s3_failure_prefix_186:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TSTORE): index "
.L__s3_failure_suffix_186:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_187:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TSTORE): trit result "
.L__s3_failure_suffix_187:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_188:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_pos_17, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_189:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_cont_18, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_190:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:30 (block rel_cont_18, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_191:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 30:30 (block rel_cont_18, TLOAD): index "
.L__s3_failure_suffix_191:
    .ascii " is uninitialized in m5\n"
.L__s3_failure_prefix_192:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:30 (block rel_cont_18, TLOAD): register r57 is uninitialized\n"
.L__s3_failure_prefix_193:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 30:30 (block rel_cont_18, TLOAD): index "
.L__s3_failure_suffix_193:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_194:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 30:13 (block rel_cont_18, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_195:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 30:13 (block rel_cont_18, TBR3): value "
.L__s3_failure_suffix_195:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_196:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 30:13 (block rel_cont_18, TBR3): register r58 is uninitialized\n"
.L__s3_failure_prefix_197:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:27 (block switch_negative_19, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_198:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:27 (block switch_negative_19, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_199:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 32:27 (block switch_negative_19, TLOAD): index "
.L__s3_failure_suffix_199:
    .ascii " is uninitialized in m2\n"
.L__s3_failure_prefix_200:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:27 (block switch_negative_19, TLOAD): register r59 is uninitialized\n"
.L__s3_failure_prefix_201:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 32:27 (block switch_negative_19, TLOAD): index "
.L__s3_failure_suffix_201:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_202:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:43 (block switch_negative_19, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_203:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block switch_negative_19, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_204:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block switch_negative_19, TCMP): register r60 is uninitialized\n"
.L__s3_failure_prefix_205:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block switch_negative_19, TCMP): register r61 is uninitialized\n"
.L__s3_failure_prefix_206:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block switch_negative_19, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_207:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 81:28 (block switch_neutral_20, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_208:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 81:21 (block switch_neutral_20, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_209:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 81:21 (block switch_neutral_20, TRET): register r208 is uninitialized\n"
.L__s3_failure_prefix_210:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 83:28 (block switch_positive_21, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_211:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 83:21 (block switch_positive_21, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_212:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 83:21 (block switch_positive_21, TRET): register r209 is uninitialized\n"
.L__s3_failure_prefix_213:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_214:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_215:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_216:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TSTORE): register r63 is uninitialized\n"
.L__s3_failure_prefix_217:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TSTORE): register r64 is uninitialized\n"
.L__s3_failure_prefix_218:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TSTORE): index "
.L__s3_failure_suffix_218:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_219:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TSTORE): trit result "
.L__s3_failure_suffix_219:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_220:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_neg_22, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_221:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_222:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_223:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_224:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TSTORE): register r65 is uninitialized\n"
.L__s3_failure_prefix_225:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TSTORE): register r66 is uninitialized\n"
.L__s3_failure_prefix_226:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TSTORE): index "
.L__s3_failure_suffix_226:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_227:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TSTORE): trit result "
.L__s3_failure_suffix_227:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_228:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_zero_23, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_229:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_230:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_231:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_232:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TSTORE): register r67 is uninitialized\n"
.L__s3_failure_prefix_233:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TSTORE): register r68 is uninitialized\n"
.L__s3_failure_prefix_234:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TSTORE): index "
.L__s3_failure_suffix_234:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_235:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TSTORE): trit result "
.L__s3_failure_suffix_235:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_236:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_pos_24, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_237:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_cont_25, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_238:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:40 (block rel_cont_25, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_239:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 32:40 (block rel_cont_25, TLOAD): index "
.L__s3_failure_suffix_239:
    .ascii " is uninitialized in m6\n"
.L__s3_failure_prefix_240:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:40 (block rel_cont_25, TLOAD): register r69 is uninitialized\n"
.L__s3_failure_prefix_241:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 32:40 (block rel_cont_25, TLOAD): index "
.L__s3_failure_suffix_241:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_242:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 32:21 (block rel_cont_25, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_243:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 32:21 (block rel_cont_25, TBR3): value "
.L__s3_failure_suffix_243:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_244:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 32:21 (block rel_cont_25, TBR3): register r70 is uninitialized\n"
.L__s3_failure_prefix_245:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 34:49 (block switch_negative_26, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_246:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 34:46 (block switch_negative_26, TREL): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_247:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 34:46 (block switch_negative_26, TREL): register r4 is uninitialized\n"
.L__s3_failure_prefix_248:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 34:46 (block switch_negative_26, TREL): register r71 is uninitialized\n"
.L__s3_failure_prefix_249:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 34:29 (block switch_negative_26, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_250:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 34:29 (block switch_negative_26, TBR3): value "
.L__s3_failure_suffix_250:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_251:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 34:29 (block switch_negative_26, TBR3): register r72 is uninitialized\n"
.L__s3_failure_prefix_252:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 77:36 (block switch_neutral_27, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_253:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 77:29 (block switch_neutral_27, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_254:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 77:29 (block switch_neutral_27, TRET): register r206 is uninitialized\n"
.L__s3_failure_prefix_255:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 79:36 (block switch_positive_28, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_256:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 79:29 (block switch_positive_28, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_257:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 79:29 (block switch_positive_28, TRET): register r207 is uninitialized\n"
.L__s3_failure_prefix_258:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 36:44 (block switch_negative_29, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_259:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 36:37 (block switch_negative_29, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_260:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 36:37 (block switch_negative_29, TRET): register r73 is uninitialized\n"
.L__s3_failure_prefix_261:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 38:55 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_262:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 38:37 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_263:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 38:37 (block switch_neutral_30, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_264:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 38:37 (block switch_neutral_30, TSTORE): register r75 is uninitialized\n"
.L__s3_failure_prefix_265:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 38:37 (block switch_neutral_30, TSTORE): register r74 is uninitialized\n"
.L__s3_failure_prefix_266:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 38:37 (block switch_neutral_30, TSTORE): index "
.L__s3_failure_suffix_266:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_267:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 39:58 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_268:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 39:37 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_269:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 39:37 (block switch_neutral_30, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_270:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 39:37 (block switch_neutral_30, TSTORE): register r77 is uninitialized\n"
.L__s3_failure_prefix_271:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 39:37 (block switch_neutral_30, TSTORE): register r76 is uninitialized\n"
.L__s3_failure_prefix_272:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 39:37 (block switch_neutral_30, TSTORE): index "
.L__s3_failure_suffix_272:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_273:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 40:59 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_274:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 40:37 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_275:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 40:37 (block switch_neutral_30, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_276:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 40:37 (block switch_neutral_30, TSTORE): register r79 is uninitialized\n"
.L__s3_failure_prefix_277:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 40:37 (block switch_neutral_30, TSTORE): register r78 is uninitialized\n"
.L__s3_failure_prefix_278:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 40:37 (block switch_neutral_30, TSTORE): index "
.L__s3_failure_suffix_278:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_279:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 41:53 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_280:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 41:37 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_281:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 41:37 (block switch_neutral_30, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_282:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 41:37 (block switch_neutral_30, TSTORE): register r81 is uninitialized\n"
.L__s3_failure_prefix_283:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 41:37 (block switch_neutral_30, TSTORE): register r80 is uninitialized\n"
.L__s3_failure_prefix_284:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 41:37 (block switch_neutral_30, TSTORE): index "
.L__s3_failure_suffix_284:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_285:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 42:61 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_286:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 42:37 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_287:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 42:37 (block switch_neutral_30, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_288:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 42:37 (block switch_neutral_30, TSTORE): register r83 is uninitialized\n"
.L__s3_failure_prefix_289:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 42:37 (block switch_neutral_30, TSTORE): register r82 is uninitialized\n"
.L__s3_failure_prefix_290:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 42:37 (block switch_neutral_30, TSTORE): index "
.L__s3_failure_suffix_290:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_291:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 43:65 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_292:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 43:37 (block switch_neutral_30, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_293:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 43:37 (block switch_neutral_30, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_294:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 43:37 (block switch_neutral_30, TSTORE): register r85 is uninitialized\n"
.L__s3_failure_prefix_295:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 43:37 (block switch_neutral_30, TSTORE): register r84 is uninitialized\n"
.L__s3_failure_prefix_296:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 43:37 (block switch_neutral_30, TSTORE): index "
.L__s3_failure_suffix_296:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_297:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:37 (block switch_neutral_30, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_298:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 75:44 (block switch_positive_31, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_299:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 75:37 (block switch_positive_31, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_300:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 75:37 (block switch_positive_31, TRET): register r205 is uninitialized\n"
.L__s3_failure_prefix_301:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:43 (block while_condition_32, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_302:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:43 (block while_condition_32, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_303:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 44:43 (block while_condition_32, TLOAD): index "
.L__s3_failure_suffix_303:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_304:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:43 (block while_condition_32, TLOAD): register r86 is uninitialized\n"
.L__s3_failure_prefix_305:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 44:43 (block while_condition_32, TLOAD): index "
.L__s3_failure_suffix_305:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_306:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:52 (block while_condition_32, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_307:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:52 (block while_condition_32, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_308:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 44:52 (block while_condition_32, TLOAD): index "
.L__s3_failure_suffix_308:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_309:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:52 (block while_condition_32, TLOAD): register r88 is uninitialized\n"
.L__s3_failure_prefix_310:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 44:52 (block while_condition_32, TLOAD): index "
.L__s3_failure_suffix_310:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_311:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block while_condition_32, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_312:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block while_condition_32, TCMP): register r87 is uninitialized\n"
.L__s3_failure_prefix_313:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block while_condition_32, TCMP): register r89 is uninitialized\n"
.L__s3_failure_prefix_314:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block while_condition_32, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_315:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 45:76 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_316:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 45:76 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_317:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 45:76 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_317:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_318:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 45:76 (block while_body_33, TLOAD): register r99 is uninitialized\n"
.L__s3_failure_prefix_319:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 45:76 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_319:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_320:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 45:67 (block while_body_33, TCVT): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_321:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 45:67 (block while_body_33, TCVT): tryte result "
.L__s3_failure_suffix_321:
    .ascii " outside [-364, 364]\n"
.L__s3_failure_prefix_322:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 45:67 (block while_body_33, TCVT): register r100 is uninitialized\n"
.L__s3_failure_prefix_323:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 45:41 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_324:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 45:41 (block while_body_33, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_325:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 45:41 (block while_body_33, TSTORE): register r102 is uninitialized\n"
.L__s3_failure_prefix_326:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 45:41 (block while_body_33, TSTORE): register r101 is uninitialized\n"
.L__s3_failure_prefix_327:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 45:41 (block while_body_33, TSTORE): index "
.L__s3_failure_suffix_327:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_328:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 45:41 (block while_body_33, TSTORE): tryte result "
.L__s3_failure_suffix_328:
    .ascii " outside [-364, 364]\n"
.L__s3_failure_prefix_329:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 46:66 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_330:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 46:66 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_331:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 46:66 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_331:
    .ascii " is uninitialized in m14\n"
.L__s3_failure_prefix_332:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 46:66 (block while_body_33, TLOAD): register r103 is uninitialized\n"
.L__s3_failure_prefix_333:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 46:66 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_333:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_334:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 46:55 (block while_body_33, TSLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_335:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 46:55 (block while_body_33, TSLOAD): slice index "
.L__s3_failure_suffix_335:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_336:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 46:55 (block while_body_33, TSLOAD): register r0 is uninitialized\n"
.L__s3_failure_prefix_337:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 46:55 (block while_body_33, TSLOAD): register r1 is uninitialized\n"
.L__s3_failure_prefix_338:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 46:55 (block while_body_33, TSLOAD): register r104 is uninitialized\n"
.L__s3_failure_prefix_339:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 46:41 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_340:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 46:41 (block while_body_33, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_341:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 46:41 (block while_body_33, TSTORE): register r106 is uninitialized\n"
.L__s3_failure_prefix_342:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 46:41 (block while_body_33, TSTORE): register r105 is uninitialized\n"
.L__s3_failure_prefix_343:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 46:41 (block while_body_33, TSTORE): index "
.L__s3_failure_suffix_343:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_344:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 47:64 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_345:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 47:64 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_346:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 47:64 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_346:
    .ascii " is uninitialized in m14\n"
.L__s3_failure_prefix_347:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 47:64 (block while_body_33, TLOAD): register r107 is uninitialized\n"
.L__s3_failure_prefix_348:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 47:64 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_348:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_349:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 47:57 (block while_body_33, TSLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_350:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 47:57 (block while_body_33, TSLOAD): slice index "
.L__s3_failure_suffix_350:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_351:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 47:57 (block while_body_33, TSLOAD): register r2 is uninitialized\n"
.L__s3_failure_prefix_352:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 47:57 (block while_body_33, TSLOAD): register r3 is uninitialized\n"
.L__s3_failure_prefix_353:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 47:57 (block while_body_33, TSLOAD): register r108 is uninitialized\n"
.L__s3_failure_prefix_354:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 47:41 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_355:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 47:41 (block while_body_33, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_356:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 47:41 (block while_body_33, TSTORE): register r110 is uninitialized\n"
.L__s3_failure_prefix_357:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 47:41 (block while_body_33, TSTORE): register r109 is uninitialized\n"
.L__s3_failure_prefix_358:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 47:41 (block while_body_33, TSTORE): index "
.L__s3_failure_suffix_358:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_359:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 48:53 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_360:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 48:53 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_361:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 48:53 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_361:
    .ascii " is uninitialized in m8\n"
.L__s3_failure_prefix_362:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 48:53 (block while_body_33, TLOAD): register r111 is uninitialized\n"
.L__s3_failure_prefix_363:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 48:53 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_363:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_364:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 48:65 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_365:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 48:65 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_366:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 48:65 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_366:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_367:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 48:65 (block while_body_33, TLOAD): register r113 is uninitialized\n"
.L__s3_failure_prefix_368:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 48:65 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_368:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_369:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 48:63 (block while_body_33, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_370:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 48:63 (block while_body_33, TADD): register r112 is uninitialized\n"
.L__s3_failure_prefix_371:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 48:63 (block while_body_33, TADD): register r114 is uninitialized\n"
.L__s3_failure_prefix_372:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 48:41 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_373:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 48:41 (block while_body_33, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_374:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 48:41 (block while_body_33, TSTORE): register r116 is uninitialized\n"
.L__s3_failure_prefix_375:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 48:41 (block while_body_33, TSTORE): register r115 is uninitialized\n"
.L__s3_failure_prefix_376:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 48:41 (block while_body_33, TSTORE): index "
.L__s3_failure_suffix_376:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_377:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:54 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_378:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:54 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_379:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 49:54 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_379:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_380:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:54 (block while_body_33, TLOAD): register r117 is uninitialized\n"
.L__s3_failure_prefix_381:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 49:54 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_381:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_382:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:67 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_383:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:67 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_384:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 49:67 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_384:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_385:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:67 (block while_body_33, TLOAD): register r119 is uninitialized\n"
.L__s3_failure_prefix_386:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 49:67 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_386:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_387:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:65 (block while_body_33, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_388:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:65 (block while_body_33, TADD): register r118 is uninitialized\n"
.L__s3_failure_prefix_389:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:65 (block while_body_33, TADD): register r120 is uninitialized\n"
.L__s3_failure_prefix_390:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:72 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_391:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:72 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_392:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 49:72 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_392:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_393:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:72 (block while_body_33, TLOAD): register r122 is uninitialized\n"
.L__s3_failure_prefix_394:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 49:72 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_394:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_395:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:70 (block while_body_33, TNDIFF): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_396:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:70 (block while_body_33, TNDIFF): register r121 is uninitialized\n"
.L__s3_failure_prefix_397:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:70 (block while_body_33, TNDIFF): register r123 is uninitialized\n"
.L__s3_failure_prefix_398:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:41 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_399:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 49:41 (block while_body_33, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_400:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:41 (block while_body_33, TSTORE): register r125 is uninitialized\n"
.L__s3_failure_prefix_401:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 49:41 (block while_body_33, TSTORE): register r124 is uninitialized\n"
.L__s3_failure_prefix_402:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 49:41 (block while_body_33, TSTORE): index "
.L__s3_failure_suffix_402:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_403:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:60 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_404:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:60 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_405:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 50:60 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_405:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_406:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:60 (block while_body_33, TLOAD): register r126 is uninitialized\n"
.L__s3_failure_prefix_407:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 50:60 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_407:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_408:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:92 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_409:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:92 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_410:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 50:92 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_410:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_411:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:92 (block while_body_33, TLOAD): register r128 is uninitialized\n"
.L__s3_failure_prefix_412:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 50:92 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_412:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_413:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:97 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_414:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:97 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_415:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 50:97 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_415:
    .ascii " is uninitialized in m16\n"
.L__s3_failure_prefix_416:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:97 (block while_body_33, TLOAD): register r130 is uninitialized\n"
.L__s3_failure_prefix_417:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 50:97 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_417:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_418:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:95 (block while_body_33, TNDIFF): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_419:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:95 (block while_body_33, TNDIFF): register r129 is uninitialized\n"
.L__s3_failure_prefix_420:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:95 (block while_body_33, TNDIFF): register r131 is uninitialized\n"
.L__s3_failure_prefix_421:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:79 (block while_body_33, TCALL): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_422:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:79 (block while_body_33, TCALL): register r132 is uninitialized\n"
.L__s3_failure_prefix_423:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:77 (block while_body_33, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_424:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:77 (block while_body_33, TADD): register r127 is uninitialized\n"
.L__s3_failure_prefix_425:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:77 (block while_body_33, TADD): register r133 is uninitialized\n"
.L__s3_failure_prefix_426:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:41 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_427:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 50:41 (block while_body_33, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_428:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:41 (block while_body_33, TSTORE): register r135 is uninitialized\n"
.L__s3_failure_prefix_429:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 50:41 (block while_body_33, TSTORE): register r134 is uninitialized\n"
.L__s3_failure_prefix_430:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 50:41 (block while_body_33, TSTORE): index "
.L__s3_failure_suffix_430:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_431:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:47 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_432:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:47 (block while_body_33, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_433:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 51:47 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_433:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_434:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:47 (block while_body_33, TLOAD): register r136 is uninitialized\n"
.L__s3_failure_prefix_435:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 51:47 (block while_body_33, TLOAD): index "
.L__s3_failure_suffix_435:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_436:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:63 (block while_body_33, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_437:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block while_body_33, TCMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_438:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block while_body_33, TCMP): register r137 is uninitialized\n"
.L__s3_failure_prefix_439:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block while_body_33, TCMP): register r138 is uninitialized\n"
.L__s3_failure_prefix_440:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block while_body_33, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_441:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:37 (block while_exit_0_34, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_442:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:37 (block while_exit_1_35, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_443:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 67:67 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_444:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 67:67 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_445:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 67:67 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_445:
    .ascii " is uninitialized in m0\n"
.L__s3_failure_prefix_446:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 67:67 (block while_exit_36, TLOAD): register r178 is uninitialized\n"
.L__s3_failure_prefix_447:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 67:67 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_447:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_448:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 67:60 (block while_exit_36, TCVT): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_449:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 67:60 (block while_exit_36, TCVT): register r179 is uninitialized\n"
.L__s3_failure_prefix_450:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 67:37 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_451:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 67:37 (block while_exit_36, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_452:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 67:37 (block while_exit_36, TSTORE): register r181 is uninitialized\n"
.L__s3_failure_prefix_453:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 67:37 (block while_exit_36, TSTORE): register r180 is uninitialized\n"
.L__s3_failure_prefix_454:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 67:37 (block while_exit_36, TSTORE): index "
.L__s3_failure_suffix_454:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_455:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 68:44 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_456:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 68:49 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_457:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 68:49 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_458:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 68:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_458:
    .ascii " is uninitialized in m8\n"
.L__s3_failure_prefix_459:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 68:49 (block while_exit_36, TLOAD): register r183 is uninitialized\n"
.L__s3_failure_prefix_460:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 68:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_460:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_461:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 68:37 (block while_exit_36, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_462:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 68:37 (block while_exit_36, TSSTORE): slice index "
.L__s3_failure_suffix_462:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_463:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 68:37 (block while_exit_36, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_464:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 68:37 (block while_exit_36, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_465:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 68:37 (block while_exit_36, TSSTORE): register r182 is uninitialized\n"
.L__s3_failure_prefix_466:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 68:37 (block while_exit_36, TSSTORE): register r184 is uninitialized\n"
.L__s3_failure_prefix_467:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 69:44 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_468:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 69:49 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_469:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 69:49 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_470:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 69:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_470:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_471:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 69:49 (block while_exit_36, TLOAD): register r186 is uninitialized\n"
.L__s3_failure_prefix_472:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 69:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_472:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_473:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 69:37 (block while_exit_36, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_474:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 69:37 (block while_exit_36, TSSTORE): slice index "
.L__s3_failure_suffix_474:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_475:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 69:37 (block while_exit_36, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_476:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 69:37 (block while_exit_36, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_477:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 69:37 (block while_exit_36, TSSTORE): register r185 is uninitialized\n"
.L__s3_failure_prefix_478:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 69:37 (block while_exit_36, TSSTORE): register r187 is uninitialized\n"
.L__s3_failure_prefix_479:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 70:44 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_480:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 70:49 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_481:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 70:49 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_482:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 70:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_482:
    .ascii " is uninitialized in m9\n"
.L__s3_failure_prefix_483:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 70:49 (block while_exit_36, TLOAD): register r189 is uninitialized\n"
.L__s3_failure_prefix_484:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 70:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_484:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_485:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 70:37 (block while_exit_36, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_486:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 70:37 (block while_exit_36, TSSTORE): slice index "
.L__s3_failure_suffix_486:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_487:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 70:37 (block while_exit_36, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_488:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 70:37 (block while_exit_36, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_489:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 70:37 (block while_exit_36, TSSTORE): register r188 is uninitialized\n"
.L__s3_failure_prefix_490:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 70:37 (block while_exit_36, TSSTORE): register r190 is uninitialized\n"
.L__s3_failure_prefix_491:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:44 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_492:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:49 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_493:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:49 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_494:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 71:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_494:
    .ascii " is uninitialized in m8\n"
.L__s3_failure_prefix_495:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:49 (block while_exit_36, TLOAD): register r192 is uninitialized\n"
.L__s3_failure_prefix_496:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 71:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_496:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_497:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:75 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_498:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:75 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_499:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 71:75 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_499:
    .ascii " is uninitialized in m18\n"
.L__s3_failure_prefix_500:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:75 (block while_exit_36, TLOAD): register r194 is uninitialized\n"
.L__s3_failure_prefix_501:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 71:75 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_501:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_502:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:73 (block while_exit_36, TMUL): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_503:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:73 (block while_exit_36, TMUL): register r4 is uninitialized\n"
.L__s3_failure_prefix_504:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:73 (block while_exit_36, TMUL): register r195 is uninitialized\n"
.L__s3_failure_prefix_505:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:59 (block while_exit_36, TDIV): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_506:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:59 (block while_exit_36, TDIV): register r193 is uninitialized\n"
.L__s3_failure_prefix_507:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:59 (block while_exit_36, TDIV): register r196 is uninitialized\n"
.L__s3_failure_prefix_508:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 71:37 (block while_exit_36, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_509:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 71:37 (block while_exit_36, TSSTORE): slice index "
.L__s3_failure_suffix_509:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_510:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:37 (block while_exit_36, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_511:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:37 (block while_exit_36, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_512:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:37 (block while_exit_36, TSSTORE): register r191 is uninitialized\n"
.L__s3_failure_prefix_513:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 71:37 (block while_exit_36, TSSTORE): register r197 is uninitialized\n"
.L__s3_failure_prefix_514:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 72:44 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_515:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 72:49 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_516:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 72:49 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_517:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 72:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_517:
    .ascii " is uninitialized in m12\n"
.L__s3_failure_prefix_518:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:49 (block while_exit_36, TLOAD): register r199 is uninitialized\n"
.L__s3_failure_prefix_519:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 72:49 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_519:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_520:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 72:68 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_521:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 72:68 (block while_exit_36, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_522:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 72:68 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_522:
    .ascii " is uninitialized in m18\n"
.L__s3_failure_prefix_523:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:68 (block while_exit_36, TLOAD): register r201 is uninitialized\n"
.L__s3_failure_prefix_524:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 72:68 (block while_exit_36, TLOAD): index "
.L__s3_failure_suffix_524:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_525:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 72:66 (block while_exit_36, TDIV): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_526:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:66 (block while_exit_36, TDIV): register r200 is uninitialized\n"
.L__s3_failure_prefix_527:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:66 (block while_exit_36, TDIV): register r202 is uninitialized\n"
.L__s3_failure_prefix_528:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 72:37 (block while_exit_36, TSSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_529:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 72:37 (block while_exit_36, TSSTORE): slice index "
.L__s3_failure_suffix_529:
    .ascii " out of bounds\n"
.L__s3_failure_prefix_530:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:37 (block while_exit_36, TSSTORE): register r5 is uninitialized\n"
.L__s3_failure_prefix_531:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:37 (block while_exit_36, TSSTORE): register r6 is uninitialized\n"
.L__s3_failure_prefix_532:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:37 (block while_exit_36, TSSTORE): register r198 is uninitialized\n"
.L__s3_failure_prefix_533:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 72:37 (block while_exit_36, TSSTORE): register r203 is uninitialized\n"
.L__s3_failure_prefix_534:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 73:44 (block while_exit_36, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_535:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 73:37 (block while_exit_36, TRET): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_536:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 73:37 (block while_exit_36, TRET): register r204 is uninitialized\n"
.L__s3_failure_prefix_537:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_538:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_539:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_540:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TSTORE): register r91 is uninitialized\n"
.L__s3_failure_prefix_541:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TSTORE): register r92 is uninitialized\n"
.L__s3_failure_prefix_542:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TSTORE): index "
.L__s3_failure_suffix_542:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_543:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TSTORE): trit result "
.L__s3_failure_suffix_543:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_544:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_neg_37, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_545:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_546:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_547:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_548:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TSTORE): register r93 is uninitialized\n"
.L__s3_failure_prefix_549:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TSTORE): register r94 is uninitialized\n"
.L__s3_failure_prefix_550:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TSTORE): index "
.L__s3_failure_suffix_550:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_551:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TSTORE): trit result "
.L__s3_failure_suffix_551:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_552:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_zero_38, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_553:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_554:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_555:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_556:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TSTORE): register r95 is uninitialized\n"
.L__s3_failure_prefix_557:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TSTORE): register r96 is uninitialized\n"
.L__s3_failure_prefix_558:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TSTORE): index "
.L__s3_failure_suffix_558:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_559:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TSTORE): trit result "
.L__s3_failure_suffix_559:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_560:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_pos_39, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_561:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_cont_40, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_562:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:50 (block rel_cont_40, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_563:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 44:50 (block rel_cont_40, TLOAD): index "
.L__s3_failure_suffix_563:
    .ascii " is uninitialized in m13\n"
.L__s3_failure_prefix_564:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:50 (block rel_cont_40, TLOAD): register r97 is uninitialized\n"
.L__s3_failure_prefix_565:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 44:50 (block rel_cont_40, TLOAD): index "
.L__s3_failure_suffix_565:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_566:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:37 (block rel_cont_40, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_567:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 44:37 (block rel_cont_40, TBR3): value "
.L__s3_failure_suffix_567:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_568:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 44:37 (block rel_cont_40, TBR3): register r98 is uninitialized\n"
.L__s3_failure_prefix_569:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_570:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_571:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_572:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TSTORE): register r140 is uninitialized\n"
.L__s3_failure_prefix_573:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TSTORE): register r141 is uninitialized\n"
.L__s3_failure_prefix_574:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TSTORE): index "
.L__s3_failure_suffix_574:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_575:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TSTORE): trit result "
.L__s3_failure_suffix_575:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_576:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_neg_41, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_577:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_578:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_579:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_580:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TSTORE): register r142 is uninitialized\n"
.L__s3_failure_prefix_581:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TSTORE): register r143 is uninitialized\n"
.L__s3_failure_prefix_582:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TSTORE): index "
.L__s3_failure_suffix_582:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_583:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TSTORE): trit result "
.L__s3_failure_suffix_583:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_584:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_zero_42, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_585:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_586:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_587:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_588:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TSTORE): register r144 is uninitialized\n"
.L__s3_failure_prefix_589:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TSTORE): register r145 is uninitialized\n"
.L__s3_failure_prefix_590:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TSTORE): index "
.L__s3_failure_suffix_590:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_591:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TSTORE): trit result "
.L__s3_failure_suffix_591:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_592:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_pos_43, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_593:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_cont_44, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_594:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:60 (block rel_cont_44, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_595:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 51:60 (block rel_cont_44, TLOAD): index "
.L__s3_failure_suffix_595:
    .ascii " is uninitialized in m17\n"
.L__s3_failure_prefix_596:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:60 (block rel_cont_44, TLOAD): register r146 is uninitialized\n"
.L__s3_failure_prefix_597:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 51:60 (block rel_cont_44, TLOAD): index "
.L__s3_failure_suffix_597:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_598:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 51:41 (block rel_cont_44, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_599:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 51:41 (block rel_cont_44, TBR3): value "
.L__s3_failure_suffix_599:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_600:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 51:41 (block rel_cont_44, TBR3): register r147 is uninitialized\n"
.L__s3_failure_prefix_601:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 53:56 (block switch_negative_45, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_602:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 53:56 (block switch_negative_45, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_603:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 53:56 (block switch_negative_45, TLOAD): index "
.L__s3_failure_suffix_603:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_604:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 53:56 (block switch_negative_45, TLOAD): register r148 is uninitialized\n"
.L__s3_failure_prefix_605:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 53:56 (block switch_negative_45, TLOAD): index "
.L__s3_failure_suffix_605:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_606:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 53:49 (block switch_negative_45, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_607:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 53:49 (block switch_negative_45, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_608:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 53:49 (block switch_negative_45, TSTORE): register r150 is uninitialized\n"
.L__s3_failure_prefix_609:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 53:49 (block switch_negative_45, TSTORE): register r149 is uninitialized\n"
.L__s3_failure_prefix_610:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 53:49 (block switch_negative_45, TSTORE): index "
.L__s3_failure_suffix_610:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_611:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 54:64 (block switch_negative_45, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_612:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 54:49 (block switch_negative_45, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_613:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 54:49 (block switch_negative_45, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_614:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 54:49 (block switch_negative_45, TSTORE): register r152 is uninitialized\n"
.L__s3_failure_prefix_615:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 54:49 (block switch_negative_45, TSTORE): register r151 is uninitialized\n"
.L__s3_failure_prefix_616:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 54:49 (block switch_negative_45, TSTORE): index "
.L__s3_failure_suffix_616:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_617:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 52:45 (block switch_negative_45, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_618:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 56:64 (block switch_neutral_46, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_619:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 56:64 (block switch_neutral_46, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_620:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 56:64 (block switch_neutral_46, TLOAD): index "
.L__s3_failure_suffix_620:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_621:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 56:64 (block switch_neutral_46, TLOAD): register r153 is uninitialized\n"
.L__s3_failure_prefix_622:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 56:64 (block switch_neutral_46, TLOAD): index "
.L__s3_failure_suffix_622:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_623:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 56:49 (block switch_neutral_46, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_624:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 56:49 (block switch_neutral_46, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_625:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 56:49 (block switch_neutral_46, TSTORE): register r155 is uninitialized\n"
.L__s3_failure_prefix_626:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 56:49 (block switch_neutral_46, TSTORE): register r154 is uninitialized\n"
.L__s3_failure_prefix_627:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 56:49 (block switch_neutral_46, TSTORE): index "
.L__s3_failure_suffix_627:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_628:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 55:45 (block switch_neutral_46, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_629:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 58:64 (block switch_positive_47, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_630:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 58:64 (block switch_positive_47, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_631:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 58:64 (block switch_positive_47, TLOAD): index "
.L__s3_failure_suffix_631:
    .ascii " is uninitialized in m11\n"
.L__s3_failure_prefix_632:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 58:64 (block switch_positive_47, TLOAD): register r156 is uninitialized\n"
.L__s3_failure_prefix_633:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 58:64 (block switch_positive_47, TLOAD): index "
.L__s3_failure_suffix_633:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_634:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 58:49 (block switch_positive_47, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_635:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 58:49 (block switch_positive_47, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_636:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 58:49 (block switch_positive_47, TSTORE): register r158 is uninitialized\n"
.L__s3_failure_prefix_637:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 58:49 (block switch_positive_47, TSTORE): register r157 is uninitialized\n"
.L__s3_failure_prefix_638:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 58:49 (block switch_positive_47, TSTORE): index "
.L__s3_failure_suffix_638:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_639:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 57:45 (block switch_positive_47, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_640:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 59:47 (block switch_continue_48, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_641:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 59:47 (block switch_continue_48, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_642:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 59:47 (block switch_continue_48, TLOAD): index "
.L__s3_failure_suffix_642:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_643:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 59:47 (block switch_continue_48, TLOAD): register r159 is uninitialized\n"
.L__s3_failure_prefix_644:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 59:47 (block switch_continue_48, TLOAD): index "
.L__s3_failure_suffix_644:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_645:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 59:54 (block switch_continue_48, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_646:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 59:54 (block switch_continue_48, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_647:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 59:54 (block switch_continue_48, TLOAD): index "
.L__s3_failure_suffix_647:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_648:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 59:54 (block switch_continue_48, TLOAD): register r161 is uninitialized\n"
.L__s3_failure_prefix_649:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 59:54 (block switch_continue_48, TLOAD): index "
.L__s3_failure_suffix_649:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_650:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 59:52 (block switch_continue_48, TREL): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_651:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 59:52 (block switch_continue_48, TREL): register r160 is uninitialized\n"
.L__s3_failure_prefix_652:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 59:52 (block switch_continue_48, TREL): register r162 is uninitialized\n"
.L__s3_failure_prefix_653:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 59:41 (block switch_continue_48, TBR3): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_654:
    .ascii "runtime error [invalid trit state] in function 'energy_series_aggregation'\nat source 59:41 (block switch_continue_48, TBR3): value "
.L__s3_failure_suffix_654:
    .ascii " outside [-1, 1]\n"
.L__s3_failure_prefix_655:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 59:41 (block switch_continue_48, TBR3): register r163 is uninitialized\n"
.L__s3_failure_prefix_656:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 61:56 (block switch_negative_49, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_657:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 61:56 (block switch_negative_49, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_658:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 61:56 (block switch_negative_49, TLOAD): index "
.L__s3_failure_suffix_658:
    .ascii " is uninitialized in m15\n"
.L__s3_failure_prefix_659:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 61:56 (block switch_negative_49, TLOAD): register r164 is uninitialized\n"
.L__s3_failure_prefix_660:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 61:56 (block switch_negative_49, TLOAD): index "
.L__s3_failure_suffix_660:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_661:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 61:49 (block switch_negative_49, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_662:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 61:49 (block switch_negative_49, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_663:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 61:49 (block switch_negative_49, TSTORE): register r166 is uninitialized\n"
.L__s3_failure_prefix_664:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 61:49 (block switch_negative_49, TSTORE): register r165 is uninitialized\n"
.L__s3_failure_prefix_665:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 61:49 (block switch_negative_49, TSTORE): index "
.L__s3_failure_suffix_665:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_666:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 60:45 (block switch_negative_49, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_667:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 63:56 (block switch_neutral_50, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_668:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 63:56 (block switch_neutral_50, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_669:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 63:56 (block switch_neutral_50, TLOAD): index "
.L__s3_failure_suffix_669:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_670:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 63:56 (block switch_neutral_50, TLOAD): register r167 is uninitialized\n"
.L__s3_failure_prefix_671:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 63:56 (block switch_neutral_50, TLOAD): index "
.L__s3_failure_suffix_671:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_672:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 63:49 (block switch_neutral_50, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_673:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 63:49 (block switch_neutral_50, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_674:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 63:49 (block switch_neutral_50, TSTORE): register r169 is uninitialized\n"
.L__s3_failure_prefix_675:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 63:49 (block switch_neutral_50, TSTORE): register r168 is uninitialized\n"
.L__s3_failure_prefix_676:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 63:49 (block switch_neutral_50, TSTORE): index "
.L__s3_failure_suffix_676:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_677:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 62:45 (block switch_neutral_50, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_678:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 65:56 (block switch_positive_51, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_679:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 65:56 (block switch_positive_51, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_680:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 65:56 (block switch_positive_51, TLOAD): index "
.L__s3_failure_suffix_680:
    .ascii " is uninitialized in m10\n"
.L__s3_failure_prefix_681:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 65:56 (block switch_positive_51, TLOAD): register r170 is uninitialized\n"
.L__s3_failure_prefix_682:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 65:56 (block switch_positive_51, TLOAD): index "
.L__s3_failure_suffix_682:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_683:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 65:49 (block switch_positive_51, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_684:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 65:49 (block switch_positive_51, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_685:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 65:49 (block switch_positive_51, TSTORE): register r172 is uninitialized\n"
.L__s3_failure_prefix_686:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 65:49 (block switch_positive_51, TSTORE): register r171 is uninitialized\n"
.L__s3_failure_prefix_687:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 65:49 (block switch_positive_51, TSTORE): index "
.L__s3_failure_suffix_687:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_688:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 64:45 (block switch_positive_51, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_689:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 66:50 (block switch_continue_52, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_690:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 66:50 (block switch_continue_52, TLOAD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_691:
    .ascii "runtime error [uninitialized memory] in function 'energy_series_aggregation'\nat source 66:50 (block switch_continue_52, TLOAD): index "
.L__s3_failure_suffix_691:
    .ascii " is uninitialized in m7\n"
.L__s3_failure_prefix_692:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 66:50 (block switch_continue_52, TLOAD): register r173 is uninitialized\n"
.L__s3_failure_prefix_693:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 66:50 (block switch_continue_52, TLOAD): index "
.L__s3_failure_suffix_693:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_694:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 66:59 (block switch_continue_52, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_695:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 66:57 (block switch_continue_52, TADD): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_696:
    .ascii "runtime error [overflow] in function 'energy_series_aggregation'\nat source 66:57 (block switch_continue_52, TADD): i64 addition overflow\n"
.L__s3_failure_prefix_697:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 66:57 (block switch_continue_52, TADD): register r174 is uninitialized\n"
.L__s3_failure_prefix_698:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 66:57 (block switch_continue_52, TADD): register r175 is uninitialized\n"
.L__s3_failure_prefix_699:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 66:41 (block switch_continue_52, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_700:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 66:41 (block switch_continue_52, TSTORE): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_701:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 66:41 (block switch_continue_52, TSTORE): register r177 is uninitialized\n"
.L__s3_failure_prefix_702:
    .ascii "runtime error [uninitialized register] in function 'energy_series_aggregation'\nat source 66:41 (block switch_continue_52, TSTORE): register r176 is uninitialized\n"
.L__s3_failure_prefix_703:
    .ascii "runtime error [bounds] in function 'energy_series_aggregation'\nat source 66:41 (block switch_continue_52, TSTORE): index "
.L__s3_failure_suffix_703:
    .ascii " outside [0, 1)\n"
.L__s3_failure_prefix_704:
    .ascii "runtime error [instruction limit] in function 'energy_series_aggregation'\nat source 44:37 (block switch_continue_52, TJMP): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_705:
    .ascii "runtime error [frame limit] in function 'main'\nat source unknown (block entry, ENTER): depth "
.L__s3_failure_suffix_705:
    .ascii " exceeds limit 1024\n"
.L__s3_failure_prefix_706:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 88:12 (block entry, TCONST): instruction limit 100000 exceeded\n"
.L__s3_failure_prefix_707:
    .ascii "runtime error [instruction limit] in function 'main'\nat source 88:5 (block entry, TRET): instruction limit 100000 exceeded\n"

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
