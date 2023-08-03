# Dictionary is unordered, mutable, indexed, cannot contain duplicate keys
myDict = {
    "Opr": "This Operation must be done before due date",
    "James": "This is agent 7 James Bond",
    "Marks": [1, 2, 3],
    "childDict": {'Opr': 'James'},
    1: 7
}

# myDict["Marks"] = [45,56,89] --> mutable

print(myDict['Opr'])
print(myDict['James'])
print(myDict['Marks'])

print("ChildDict:", myDict["childDict"])
print("ChildDict:", myDict["childDict"]['Opr'])

# Dictionary Methods:

# print("Print the keys of Dictionary:",myDict.keys())
print("Print the keys of Dictionary:", list(myDict.keys()))
# prints key for all contents
print("Values of Dictionary:", list(myDict.values()))
# prints (key,value) for all contents
print("Tuples of Dictionary:", list(myDict.items()))

print(myDict)
#  updating myDict
updatemyDict = {
    "Music": "Perfect"
}
myDict.update(updatemyDict)
print(myDict)

print(myDict.get("James"))
print(myDict["James"])
# main use of get method is that if we change the key name then get method will show us NONE while [] will throws error
print(myDict.get("James2"))
print(myDict["James2"])