def bubble_sort(a):
    n = len(a)
    k = 0
    ccnt = 0
    scnt = 0
    while k < n - 1:
        ccnt += 1

        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

                last = j
                scnt += 1
        k = last

    return(ccnt, scnt)

if __name__ == "__main__":
    print('버블정렬 할거임')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    print(bubble_sort(x))
    
    print('오름차순 정렬했으')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')