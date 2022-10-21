
from numpy import partition


NUM_DIMS = 3
CARDINALITY = [3 for i in range(NUM_DIMS)]
MINSUP = 2

dataCount = []

def initDataCount():
    for i in range(NUM_DIMS): 
        dataCount.append([0 for i in range(CARDINALITY[i])])

 
#Sorts a list of tuples based on the ith index of value
def sortTupleList(input: list, i: int): 
    return sorted(input, key=lambda a: a[i])

#Takes sorted input on dim d and puts the counts of instances of each 
#value in its corresponding spot in the datacount array 
# "datacount contains the number of records for each distinct value of the d-th dimension."
def bucPartition(input: list, d: int, C: int): 
    dataCount[d] = [0 for i in range(C)]
    for i in range(len(input)):
        dataCount[d][input[i][d]] += 1

    
def buc(input: list, dim: int, prettyPrintLocation: list):
    # print('buc call made Params: ', input, ', ', dim)
    # print('\n', sorted(input, key=lambda a: a[dim]), '\n')
    # Here 5 is the max number of attributes
    # print('Region: ', len(input)) 
    print(prettyPrintLocation, ': ', len(input))
    for i in range(dim, NUM_DIMS):
        C = CARDINALITY[i]
        # print('i: ', i)
        # first sort by attribute index
        table = sortTupleList(input, i)
        bucPartition(input, i, C)
        # print('table: ', table)
        # print('dc: ', dataCount)
        # print('\n 
        # Table for input: ', input, '\n dim: ', dim, '\n Table: ', table)
        # Then scan the new list and check the attribute index 
        # oldVal = (0, table[0][dim])
        # print(oldVal, '\n\n')
        k = 0
        for j in range(C): 
            # Get the current val
            # print(j)
            c = dataCount[i][j]
            if (c >= MINSUP):
                # print('count of value: ', j, ' in dim: ', i, ' = ', c)
                
                # if(k < len(table)):
                    # print(table[k], ' ', c)
                # if(i+1 < NUM_DIMS and k+c < len(table)):
                newLocation = prettyPrintLocation
                newLocation[i] = j
                buc([table[idx] for idx in range(k, k+c)], i+1, newLocation)
            k+= c
        prettyPrintLocation[i] = '*'
    return
        # print('\n BIG ITERATION DONE - dim: ', i)
            # newVal = (j, table[j][dim])
            # Check if it is a new val 
            # if (newVal[1] != oldVal[1]):
            #     # print('\n miss: ', newVal[1], ' ', oldVal[1], '\n')
            #     # we also check our count to see if it is above the minsup 
            #     if (newVal[0]-oldVal[0] >= MINSUP): 
            #         if (i+1 < 5):
            #             newState = state
            #             newState[i] = oldVal[1]
            #             buc([table[idx] for idx in range(oldVal[0], j)], i+1, newState)
                        
            #     # When we reach a different value we update oldval 
            #     # print('miss')
            #     oldVal= (j, newVal)
        
        
def processData(filename): 
    file = open(filename)
    list = []
    tupleVal = []
    i = 0
    for t in file: 
        t = t.replace(']', '')
        t = t.replace('[', '')
        t = t.replace('\n', '')
        split = t.split(', ')
        j = 0
        for num in split: 
            tupleVal.insert(j, int(num))
            j += 1
        j = 0
        i += 1
        tup = tuple(tupleVal)
        list.insert(i,tup)  
        tupleVal = []
    return list 
        

def main():
    data = processData('data.txt')
    initDataCount()

    buc(data, 0, ['*' for i in range(NUM_DIMS)])
    return 0


if __name__ == "__main__": 
    main()