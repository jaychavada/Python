print("loop 1")
for i in range(10):
    print(i)
    if i == 5:
        break
print("loop 2")
for k in range(10):
    if k == 5:
        continue    
    print(k)
    
print("loop 3")
for j in range(4):
    print("Running")
    if j == 2:
        continue
    print(j)