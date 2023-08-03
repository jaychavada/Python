#  While loop
i = 0
while i <= 10:
    print(i)
    i = i+1
print("Done")

fruits = ['Banana', 'watermelon', 'Grapes', 'Mangoes']
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i+1

# For loop
list = ['Banana', 'watermelon', 'Grapes', 'Mangoes']
print("Using for loop:")

for item in list:
    print(item)

# range function 
for i in range(5,10):
    print(i)
    
# for with else
for i in range(10):
    print(i)
else:
    print("This is inside else of for") # Optional else

