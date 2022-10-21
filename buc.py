
from numpy import partition


NUM_DIMS = 5
CARDINALITY = [7 for i in range(NUM_DIMS)]
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
    print(prettyPrintLocation, ': ', len(input))
    for i in range(dim, NUM_DIMS):
        C = CARDINALITY[i]
        table = sortTupleList(input, i)
        bucPartition(input, i, C)
        k = 0
        for j in range(C): 
            c = dataCount[i][j]
            if (c >= MINSUP):
                newLocation = prettyPrintLocation
                newLocation[i] = j
                buc([table[idx] for idx in range(k, k+c)], i+1, newLocation)
            k+= c
        prettyPrintLocation[i] = '*'
    return
        
        
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