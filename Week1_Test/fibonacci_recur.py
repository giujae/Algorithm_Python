def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_list(n):
    result = []
    for i in range(n):
        result.append(fibonacci(i))
    return result

print(fibonacci_list(10))