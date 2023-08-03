str = "hmm, Hello, World!"
str0 = " glad to here that"

# To join two string
print("After joining two strings:",str + str0)

# Concate or slicing in string
print("Slicing of String or concate:",str[1:5])

# Slicing with skip value
print("Slicing After skiping elements:",str0[1:5:2])

# .....................FUNCTION OF STRING....................

# Length of the string
print("Length of the string:", len(str))

# Count character 
print("Count any character:",str.count("m"))

# Convert the string to uppercase
print("Uppercase:", str.upper())

# Convert the string to lowercase
print("Lowercase:", str.lower())

# Capitalize the first character of the string
print("Capitalized:", str.capitalize())
 
# Check if the string starts with a specific substring
print("Starts with 'Hello':", str.startswith("Hello"))

# Check if the string ends with a specific substring
print("Ends with 'World!':", str.endswith("World!"))

# Find the index of a specific substring within the string
print("Index of 'World':", str.index("World"))

# Replace a substring within the string
new_string = str.replace("World", "Python")
print("Replaced string:", new_string)

# Split the string into a list of substrings
split_string = str.split(", ")
print("Split string:", split_string)

# Join a list of strings into a single string using a specific delimitere
joined_string = ", ".join(split_string)
print("Joined string:", joined_string)

# Remove leading and trailing whitespace from the string
whitespace_string = "   Example string with whitespace   "
print("Stripped string:", whitespace_string.strip())

# Print the following string by using escape characters : We are "VIKINGS" of the north.
str1 = "We are \"VIKINGS\" of the north in python"
print(str1)