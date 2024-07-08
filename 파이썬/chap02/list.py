x = [1, 2, 3,4]
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
y = [1, 2, 3, 4]
for i, num in enumerate(x, 1):
    print(f'x[{i}] = {num}')
    
print(y[::-1])