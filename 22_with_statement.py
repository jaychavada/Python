with open('another.txt', 'r') as f:
    a = f.read()
print(a)

with open('another.txt', 'w') as f:
    b = f.write("This is file used by WITH statement")
    print(b)