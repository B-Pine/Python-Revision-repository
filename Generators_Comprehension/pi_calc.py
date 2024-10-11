def odd():
    current = 1
    while True:
        yield current
        current += 2


def pi_series():
    approximation = 0
    odds = odd()
    while True:
        approximation += 4 / next(odds)
        yield approximation
        approximation -= 4 / next(odds)
        yield approximation


pi = pi_series()
for i in range(1000000):
    print(next(pi))

