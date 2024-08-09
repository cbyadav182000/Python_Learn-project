# # suppose that a program to calculate avearge of 4 numbers
# a=12
# b=45
# c=56
# d=57

# average=(a+b+c+d)/4

# print(average)


'''
using function we solve problem of repeat.

"FUNCTION"

'''
def avg(): # Function Defination
    a=int(input("Enter your number:"))
    b=int(input("Enter your number:"))
    c=int(input("Enter your number:"))

    average=(a+b+c)/3
    print("Averag",average)

avg() # Function Call
print("Thanks")