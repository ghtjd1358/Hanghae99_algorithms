# =============================== 1번 문제 ===========================
n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def fibonacci(n):
    return n - 2 

print(fib(n), fibonacci(n))

