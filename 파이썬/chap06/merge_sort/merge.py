def merge_sorted_list(a, b, c):
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)
    
    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
        
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1

