import sys


def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


# range_list = range(1000)
range_list = my_range(1000)
print(f"range_list is {sys.getsizeof(range_list)} bytes.")

list_list = [num for num in range_list]
print(f"list_list is {sys.getsizeof(list_list)} bytes.")
