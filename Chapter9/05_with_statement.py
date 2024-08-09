f = open("file.txt")

print(f.read())

f.close()

#The same can be written using "with" statement like this:
with open("file.txt") as f:
    print(f.read())

#apko file close karne ki need nhi hai,'with' ke use se yah automatically ho jata hai