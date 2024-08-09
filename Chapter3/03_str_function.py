name ="Chandrabhan"
print(len(name))
print(name.endswith("bhan"))

#print(name.endswith("bhana"))

print(name.startswith("chand")) #  it is case sensitive
print(name.startswith("Chand"))

print(name.capitalize())


#most using string function in python
#  1-> len():
s = "hello"
print(len(s))  # Output: 5


#  2--> str():  Converts a value to a string.
num = 123
print(str(num))  # Output: "123"

#  3-->lower():Converts all characters in the string to lowercase
p = "HELLO"
print(p.lower())  # Output: "hello"

#---> upper() s = "hello"  Converts all characters in the string to uppercase
print(s.upper())  # Output: "HELLO"

#Removes leading and trailing whitespace from the string.
s = "  hello  "
print(s.strip())  # Output: "hello"

#Splits the string into a list based on a specified delimiter
s = "hello world"
print(s.split())  # Output: ["hello", "world"]

#Joins a list of strings into a single string with a specified delimiter.
words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"

#Replaces all occurrences of a specified substring with another substring
s = "hello world"
print(s.replace("world", "Python"))  # Output: "hello Python"


#Returns the index of the first occurrence of a specified substring. Returns -1 if the substring is not found.
s = "hello world"
print(s.find("world"))  # Output: 6

s = "hello world"
print(s.startswith("hello"))  # Output: True


#Formats a string using placeholders.
s = "Hello, {}!"
print(s.format("world"))  # Output: "Hello, world!"

#Checks if all characters in the string are digits.
s = "12345"
print(s.isdigit())  # Output: True

#checks if all characters in the string are alphabetic.
s = "hello"
print(s.isalpha())  # Output: True


#Checks if all characters in the string are alphanumeric.
s = "hello123"
print(s.isalnum())  # Output: True
