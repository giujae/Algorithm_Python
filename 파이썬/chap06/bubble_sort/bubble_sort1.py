def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == "__main__":
    print('버블정렬 할거임')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    bubble_sort(x)
    
    print('오름차순 정렬했으')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')