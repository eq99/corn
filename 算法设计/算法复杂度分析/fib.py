import time

# 0, 1, 1, 2, 3, 5, 8, ...


def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    pre = 1
    ppre = 0
    curr = 0

    # fix fib2(1) == 1
    if n == 1:
        return 1

    while n > 1:
        curr = ppre + pre
        ppre = pre
        pre = curr
        n = n-1

    return curr


def time_cal(n, func):
    start = time.time()
    result = func(n)
    print(f'Get {result} use {time.time()-start}')


time_cal(30, fib1)
time_cal(30, fib2)
