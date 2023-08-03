#  QUE: store 7 fruits in list entered by user:

f1 = input("Enter Fruit Number 1:")
f2 = input("Enter Fruit Number 2:")
f3 = input("Enter Fruit Number 3:")
f4 = input("Enter Fruit Number 4:")
f5 = input("Enter Fruit Number 5:")
f6 = input("Enter Fruit Number 6:")
f7 = input("Enter Fruit Number 7:")

list = [f1, f2, f3, f4, f5, f6, f7]
print(list)

# QUE: enter 6 students marks by user:

m1 = int(input("Enter Marks For Students 1: "))
m2 = int(input("Enter Marks For Students 2: "))
m3 = int(input("Enter Marks For Students 3: "))
m4 = int(input("Enter Marks For Students 4: "))
m5 = int(input("Enter Marks For Students 5: "))
m6 = int(input("Enter Marks For Students 6: "))

list1 = [m1, m2, m3, m4, m5, m6]
list1.sort()
print(list1)

# QUE :Number 0 in tuple
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))