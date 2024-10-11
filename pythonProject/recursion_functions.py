# factorial function

def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1


def fibo(n):
    if n <= 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


# print(fact(5))
print(fibo(5))
