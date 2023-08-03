# QUE: Create Dictionary of HINDI words with values as their ENGLISH translation provide user with an oprtion to look it up!

mydict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item",
    "ladka": "Boy"
}
print("Options are:", list(mydict.keys()))
a = input("Enter the HINDI word\n")
# for not get error line we will use get method
print("Meaning of word is:", mydict.get(a))
# print("The meaning of your word is:", mydict[a])

# QUE: s of unique no by user input

a1 = int(input("Enter number 1:"))
a2 = int(input("Enter number 2:"))
a3 = int(input("Enter number 3:"))
a4 = int(input("Enter number 4:"))

s = {a1, a2, a3, a4}
print(type(s))
print(s)

# QUE: Dictionary with each has their fav language and set it by user

favlang = {}
a = input("Enter fav lang of Jay\n")
b = input("Enter fav lang of Dharmik\n")
c = input("Enter fav lang of Arun\n")
d = input("Enter fav lang of Deep\n")

favlang['Jay'] = a
favlang['Dharmik'] = b
favlang['Arun'] = c
favlang['Deep'] = d

print(favlang)