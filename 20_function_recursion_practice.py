# QUE: MAX OUT OF 3 NUMBERS

def max(a, b, c):
    if (a > b):
        if (a > c):
            return a
        else:
            return c
    else:
        if (b > c):
            return b
        else:
            return c


m = max(3, 4, 56)
print("Maximum number is", str(m))

# QUE : CELSIUS TO FAHRENHEIT


def far(cel):
    return (cel * (9/5)) + 32


c = int(input("Enter celsius tempetature:\n"))
f = (far(c))
print("Fahrenheit is:", f)

# QUE: SUM OF N NATURAL NUMBER

n = int(input("Enter Number\n"))
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

print(f"The sum of {n} natural number is {sum_of_natural_numbers(n)}")

# QUE: PATTERN

n=6
for i in range(n):
    print("*" * (n-i))