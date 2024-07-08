def qsort (a, left, right):
    pl = left
    pr = right
    x = a[(left + right) // 2]
    
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)
    
def quick_sort(a):
    qsort(a, 0, len(a) - 1)

if __name__ == "__main__":
    print('두 그룹으로 나눌거임')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    quick_sort(x)
        
    for i in range(num):
        print(f'x[{i}] = {x[i]}')