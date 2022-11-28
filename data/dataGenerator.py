import random


# The goal with this generated data is to ease the implementation of the cubing algorithms... 
# When we bring sqlite data in instead of this randomly generated data the transition should 
# be easy. We want to keep the structure of this data as realistic as possible. 
# Fetching from sqlite will return tuples with different kinds of data. By mocking some of these 
# tuples with integer data, we can ensure the algorithms are working without having to worry 
# about different data types until later. 



def genData(numTuples: int, numDims: int, card: int):
    fName = str(numTuples) + 'tuples' + str(numDims) + 'dims' + str(card) + 'card.txt'
    f = open(fName, 'w')
    for i in range (numTuples): 
        listVal = []
        random.seed(i)
        for j in range(numDims):
            listVal.insert(j, random.randint(0, card-1))
        f.write(str(listVal))
        f.write('\n')
    

def main(): 
    #create data of 10000 tuples of length 5 with int values for each entry that are randomly chosen from 0-9
    
    genData(100, 5, 2)
    genData(100, 5, 5)
    genData(500, 3, 5)
    genData(500, 6, 8)
    genData(1000, 7, 9)
    genData(1000, 3, 6)    
    genData(1000, 5, 4)
    genData(10000, 10, 3)
    genData(10000, 8, 5)
    genData(10000, 6, 2)
    genData(10000, 3, 6)

if __name__ == "__main__": 
    main()