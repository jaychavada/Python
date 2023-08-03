# list is ordered and allow to duplicates
# we can create a list using []

a=["car","bike",10,10.5,True]
print(type(a))

print("Length of list is:",len(a))

print("list is:",a)

print("Access or print data using index at a[0]:",a[0])

# change the value in list 
a[2]= 20
print("After change the value of List:",a)

# ...............List slicing............

frnds=["Steven","Tom","Tony","Natasha",11]

print("Slicing of List:",frnds[0:4])
print("Slicing of in negative index List:",frnds[-4:])

# LIST METHODS:
c=[1,5,85,56,9,3]

print("Before sort of list",c)
c.sort()
print("After sort of list",c)

c.reverse()
print("Reverse list:",c)

c.append(45)
print("Append in list:",c)

c.insert(0,456)
print("Inserting at Index:",c)

c.pop(2)
print("Popping at specified index:",c)

c.remove(456)
print("Remove element:",c)