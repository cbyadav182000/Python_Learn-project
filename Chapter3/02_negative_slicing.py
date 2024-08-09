name = "chandrabhan"

print(name)

print(name[2:7])  #positive slicing

print(name[-11:-7])  #Negative slicing    #  OR  name[0:4]
print(name[0:4])

#Escape sequence characters in Python are used to represent characters that 
# are difficultor impossible to include directly in a string. 
# Here are some common escape sequences:


#Newline (\n): Inserts a new line in the string.
print("Hello\nWorld")
# Output:
# Hello
# World

#Backslash (\\): Inserts a backslash character
print("This is a backslash: \\")
# Output: This is a backslash: \

#Single Quote (\'): Inserts a single quote character
print('It\'s a nice day')
# Output: It's a nice day

#Double Quote (\"): Inserts a double quote character
print("She said, \"Hello!\"")
# Output: She said, "Hello!"

#Tab (\t): Inserts a tab character
print("Hello\tWorld")
# Output: Hello   World

#Backspace (\b): Inserts a backspace character
print("Hello\bWorld")
# Output: HellWorld

#Carriage Return (\r): Moves the cursor to the beginning of the line
print("Hello\rWorld")
# Output: World

#Form Feed (\f): Inserts a form feed character
print("Hello\fWorld")
# Output: Hello
#        World

#Octal value (\ooo): Inserts a character based on its octal value
print("\101")  # A
# Output: A

#Hex value (\xhh): Inserts a character based on its hexadecimal value
print("\x41")  # A
# Output: A

#Unicode character (\uXXXX or \UXXXXXXXX): Inserts a Unicode character
print("\u03A9")  # Ω (Omega symbol)
# Output: Ω

#Raw strings (r"string" or r'string'): Treats backslashes as literal characters
print(r"C:\new_folder\test.txt")
# Output: C:\new_folder\test.txt