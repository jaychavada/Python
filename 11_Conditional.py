a = int(input("Enter your Age\n"))

if (a >= 19):
    print("You can vote")
elif (a == 18):
    print("You can also vote")
else:
    print("You are minor so you can not vote")

# logical and relational operators
if(a>34 and a<56):
    print("You can work with us")
else:
    print("You can not work with us")

if(a>34 or a<56):
    print("You can work with us")
else:
    print("You can not work with us")
