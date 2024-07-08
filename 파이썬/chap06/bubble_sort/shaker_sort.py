def shaker_sort(a):
    left = 0
    right = len(a) - 1
    last = right
    ccnt = 0
    scnt = 0
    
    while left < right:
        for j in range(right, left, -1):
            ccnt += 1
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
                scnt += 1
        left = last

        for j in range(left, right):
            ccnt += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
                scnt += 1
        right = last
        
    return (ccnt, scnt)
if __name__ == "__main__":
    print('쉐이커정렬 할거임')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    print(shaker_sort(x))
    
    print('오름차순 정렬했으')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')