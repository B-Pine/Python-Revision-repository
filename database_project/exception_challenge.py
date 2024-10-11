import sys


def getint(prompt):
    while True:
        try:
            receiver = int(input(prompt))
            return receiver
        except ValueError:
            print("Enter only numerical integers")
        except EOFError:  # should 've been EOFError
            sys.exit(0)
        finally:
            print("Finally statement always execute")


x = getint("Please enter the first number: ")
y = getint("Please enter the second number: ")

try:
    result = x / y
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Denominator can not be zero.")
else:
    print("Division executed successful")
