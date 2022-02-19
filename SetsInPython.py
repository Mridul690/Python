'''
Sets does not prints repetative elements.
Thus, Sets is a collection of non-repetative elemenets
In python, elements in sets can be as unique values
Sets values can not be accessed using index
Unordered
'''
a = {1,2,3,1}
print(a)

'''An empty set can be created using below syntax'''
b  = set()
print(type(b))

# Set Methods

b.add(5) # Adds the given element in the set at random index
b.add(4) 
b.add(12)
b.add(2)
b.add(5) # Adding a value repatatively does not causes any change in it,
# any particular value can be added only once in a set

#b.add([1,2,3]) 
# list cannot be added in the set as it is unhashable type
# Hashable = UnChanged during the entire process = immutable type 

b.add((1,2,3))
# tuple can be added 

#Similarly, Dictionary cannot be added as it is unhashable type

print(b)

b.remove(4) # Removes the given element from the set
# b.remove(14) # throwS an error if element is not present in set
print(b)

print(b.pop()) # Returns an random(mostly first element in set) element from set and updates the set
print(b)

# b.clear() --> Empties the set b

print(b.union({9,7})) # returns a set which is the union of the both sets

print(b.intersection({5,6})) # Returns a set which contains elements present in both of the set 

s = {20,20.0,'20'}
print(len(s)) # Length of s will be 2
# This happens because python considers 20 and 20.0 equal values 
print(s)