
f =open('sample.txt','r') 
#By default 'r' is there in python file handling 
data = f.read()
print(data)
f.close 

g = open('another.txt','a')
g.write('pls write thsi')
g.close()


with open('another.txt') as f:
    a = f.read()
with open('another.txt','w') as f:
  a = f.write("me")
print(a)

