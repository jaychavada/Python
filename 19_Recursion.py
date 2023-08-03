n=int(input("Enter number:\n"))

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


print(f"Factorial is {factorial_iter(n)}")

# using recursion
def factorial_recursive(n):
    if (n == 0 or n == 1):
        return n
    else:
        return n * factorial_recursive(n-1)


print(f"Factorial is {factorial_recursive(n)}")