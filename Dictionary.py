# Syntax : Dict_name = { key : value }
# Mutable,Unordered 

# Cannot put duplicate keys

from turtle import update


myDic = {
    "Fast": "In a quick manner",
    "harryd": "CodeDi",
    "Marks": [2,3,5],
    "anotherDic":{'harry': 8}
}

print(myDic['Fast'])
print(myDic['Marks'])
print(myDic['anotherDic']['harry'])

myDic['Marks'] = [23,34,45]
print(myDic['Marks'])

# Dictionary Methods

print(type(myDic))
print(myDic.keys())
print(myDic.values())
print(myDic.items()) # Print (keys,values) of dictionary

updateDic = {
    "lovish":'Friend',
    'Div':'run',
    'Fast': '24 km/hr'
}
myDic.update(updateDic) # Updates the dictionary
print(myDic)
# update() func also updates the existing key if the passed dic contains the similar key

print(myDic.get("harryd")) 

#print(myDic.get(["harryw"]))# Returns 'NONE' if key is not present in dictionary
#print(myDic["harryw"]) #Throws error if key is not present 
# The get() func never throws error in case the given key is absent in dictionay while through the normal way of accessing key, it throws an error
# that's the basic difference between both the ways of printing the values of the given key 

#Empty Dictionary
a = {}
print(type(a))

favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)

'''
If two or more vlaues have same keys then the key will be assigned the latest value
However, if two or more keys have same value, it will not create any problem instead different keys can have same values
'''