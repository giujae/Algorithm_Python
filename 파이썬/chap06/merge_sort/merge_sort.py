def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    return merged_arr
    
if __name__ == "__main__":
    print('병합 정렬 할거임')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    merged_arr = merge_sort(x)
    
    print('오름차순 정렬했으')
    for i in range(num):
        print(f'merged_arr[{i}] = {merged_arr[i]}')