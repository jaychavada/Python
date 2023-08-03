# QUE: find greatest out of 4 numbers entered by user

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
num3 = int(input("Enter Number 3:"))
num4 = int(input("Enter Number 4:"))

if (num1 > num4):
    f1 = num1
else:
    f1 = num4

if (num2 > num3):
    f2 = num2
else:
    f2 = num3

if (f1 > f2):
    print(str(f1) + " is maximum")
else:
    print(str(f2) + " is maximum")

# QUE: convert marks into greads
m = int(input("Enter Marks\n"))

if m>=90:
    grade ="Excellent"
elif m>=80:
    grade = "A"
elif m>=70:
    grade = "B"
elif m>=60:
    grade = "C"
elif m>=50:
    grade = "D"
else:
    grade = "FAIL"
print("You Grade is:",grade)