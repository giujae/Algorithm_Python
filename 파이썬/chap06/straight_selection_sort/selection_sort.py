def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

if __name__ == "__main__":
    print('선택정렬 할거임')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    selection_sort(x)
    
    print('오름차순 정렬했으')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')