f = open("file.txt","r")

# # lines = f.readlines()

# # print(lines, type(lines))
# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))
# f.close()

# #RESULT
# '''
# PS C:\Users\hpdeo\OneDrive\Desktop\Chapter9> python -u "c:\Users\hpdeo\OneDrive\Desktop\Chapter9\03_morefile.py"
# chandrabhan is  good boy. 
#  <class 'str'>
# he is a very brave man
#  <class 'str'>
# what is this
#  <class 'str'>
# PS C:\Users\hpdeo\OneDrive\Desktop\Chapter9> 
# '''
line = f.readline()
while(line!= ""):
    print(line)
    line = f.readline()

f.close()