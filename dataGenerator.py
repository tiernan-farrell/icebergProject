import random


# The goal with this generated data is to ease the implementation of the cubing algorithms... 
# When we bring sqlite data in instead of this randomly generated data the transition should 
# be easy. We want to keep the structure of this data as realistic as possible. 
# Fetching from sqlite will return tuples with different kinds of data. By mocking some of these 
# tuples with integer data, we can ensure the algorithms are working without having to worry 
# about different data types until later. 

def main(): 
    #create data of 10000 tuples of length 5 with int values for each entry that are randomly chosen from 0-9
    
    for i in range (10000): 
        listVal = []
        random.seed(i)
        for j in range(5):
            listVal.insert(j, random.randint(0, 6))
        print(tuple(listVal))
    

if __name__ == "__main__": 
    main()