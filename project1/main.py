import random
'''
1 for snake
-1 for water
0 for gun
'''
# Generate a random number from the list [-1, 0, 1]
computer= random.choice([-1, 0, 1])
youstr = input("Enter your choice:")
youDict = {"s":1, "w":-1, "g": 0}
reversedDict = {1:"Snake", -1:"Water", 0:"Gun"}


you = youDict[youstr]

print(f"You Chose{reversedDict[you]}\nComputer chose {reversedDict[computer]}")

if(computer== you):
    print("Draw")
elif(computer==-1 and you==1):
    print("You win")

elif(computer==-1 and you==0):
    print("You loose")

elif(computer==1 and you==-1):
    print("You loose")

elif(computer==0 and you==-1):
    print("You win")\

elif(computer==0 and you==1):
    print("You win")

else:
    print("something wrong")

