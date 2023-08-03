# QUE : MULTIPLICATION TABLE OF GIVEN NUMBER
num = int(input("Enter number\n"))

for i in range(1, 11):
    # print(str(num)+" X "+str(i)+" = "+str(i*num))
    # using fstring
    print(f"{num} x {i} = {num*i}")

# QUE : PRIME NUMBER
n = int(input("Enter the number\n"))
prime = True
for i in range(2, n):
    if (n % i == 0):
        prime = False
        break
if prime:
    print("Number is Prime.")
else:
    print("Number is not Prime.")

# QUE: sum of n natural number
n = int(input("Enter Natural number\n"))
sum = 0
for i in range(1, n + 1):

    sum += i

print(sum)

# QUE: factorial
num = int(input("Enter number\n"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print(f"The factorial of number {num} is {factorial}")

# QUE: PATTERN 1
n = 4
for i in range(4):
    print("*" * (i+1))

# QUE: PATTERN 2
n = 3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
