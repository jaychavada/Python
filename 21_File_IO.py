f = open("one.txt","r")
# data = f.read()

#  reads first line
data = f.readline()
print(data)

#  reads second line
data = f.readline()
print(data)

# data = f.read(5)
f.close() 

f=open('another.txt','w')
f.write("Second file using write operation ")
f.close()

f=open('another.txt','a')
f.write("Appending")
f.close()