name = '''Mridul
kant 
Kaushik'''
an = 'amazing'
d = an[0::2]
print(d)
print(name)
a=5
def Ad():
    print('Defining a function \n')
    a=5
    for i in range(1,6):
        a = a*i
        print (a)
    print(type(a),"\n",type(name))
    print(name[0]+"\n"+name[5])
    sl1 = name[0 : ] # In this case, name[0,last element] is taken
    #otherwise the end number is not included
    s12 = name[::-1] #Reversing the elements
    print(sl1 +"\n"+ s12)
    print(len(name))


Ad()

# name[3] = d -->Not allowed
     