def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p


marks1 = [95, 93, 86, 88]
percentage1 = percent(marks1)
print(percentage1)

#  DEFAULT ARGUMENTS


def greet(name="Stranger"):
    print("Good Day,"+name)

greet("Jay")
# here no arguments passed so it will consider default arguments as Stranger
greet()