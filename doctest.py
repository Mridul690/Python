import doctest

def average(values):
    '''Compute the arithmetic mean of a list of numbers'''

    print(average([1]))

    print(average([1,-2,4,4]))

    return sum(values,0.0)/ len(values)

if __name__ =='__main__':
    doctest.testmod()