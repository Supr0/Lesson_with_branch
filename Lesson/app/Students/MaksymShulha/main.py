def factorial(x):
    i = x
    j = x
    while i > 1:
        i -= 1
        j *= i
    return j

if __name__ == '__main__':
    print(factorial(int(input())))