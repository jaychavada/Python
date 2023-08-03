# Sets are unordered, not allows duplicate values

a = {1, 3, 4, 6, 7, 1}
print(type(a))
print(a)

# imp: below syntex will create an empty dictionary, not an empty set
b = {}
print(type(b))

# for an empty set:
c = set()
print(type(c))
# Adding values
c.add(4)
c.add(5)
c.add(6)

# we can add tuple in set but not list nor dictionary
c.add((4, 5, 6, 7, 8))  # this tuple will be added

print(c)

# Operation on sets
a = {1, 3, 4, 6, 7, 1}
a.add(2)
print(a)
print("No of items in set:",len(a))
a.remove(3)
print(a)

print(a.pop())
print(a)
print(a.union(c))
print(a.intersection(c))