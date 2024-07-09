def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fib_list(n):
    res = []
    for i in range(n):
        res.append(fibonacci(i))
    return res
print(fib_list(10))