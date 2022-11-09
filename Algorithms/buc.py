    
import time


NUM_DIMS = 4
CARDINALITY = [7 for i in range(NUM_DIMS)]
MINSUP = 1

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



class BUC:
    def __init__(self, card, dims, minsup): 
        self.cardinality = card
        self.dims = dims
        self.minsup = minsup 
        self.dc = [[0 for _ in range(card[i])]for i in range(dims)]
        self.outList = []
    #Sorts a list of tuples based on the ith index of value
    def sortTupleList(self, input: list, i: int): 
        return sorted(input, key=lambda a: a[i])

    #Takes sorted input on dim d and puts the counts of instances of each 
    #value in its corresponding spot in the datacount array 
    # "datacount contains the number of records for each distinct value of the d-th dimension."
    def bucPartition(self, input: list, d: int, C: int): 
        self.dc[d] = [0 for i in range(C)]
        for i in range(len(input)):
            self.dc[d][input[i][d]] += 1

    def buc(self, input: list, dim: int, prettyPrintLocation: list):
        #self.outList.append(str(prettyPrintLocation) + ': ' + str(len(input)))
        outLoc = prettyPrintLocation.copy()
        outLoc.append(len(input))
        self.outList.append(outLoc)
        
        for i in range(dim, self.dims):
            C = self.cardinality[i]
            table = self.sortTupleList(input, i)
            self.bucPartition(input, i, C)
            k = 0
            for j in range(C): 
                c = self.dc[i][j]
                if (c >= self.minsup):
                    newLocation = prettyPrintLocation
                    newLocation[i] = j
                    self.buc([table[idx] for idx in range(k, k+c)], i+1, newLocation)
                k+= c
            prettyPrintLocation[i] = '*'
        return
    
    def getResults(self):
        return self.outList
    

def main(): 
    data = processData('data/testData.txt') 
    start = time.time()
    buc = BUC(CARDINALITY, NUM_DIMS, MINSUP)
    buc.buc(data, 0, ['*' for i in range(NUM_DIMS)])
    end = time.time()
    print('Tuples in datase: ', len(data), '\nTotal buc() time: ', end-start, '\nTotal iceberg cube size: ', len(buc.outList))
    for e in buc.getResults():
        print(str(e))
    return buc.getResults()

if __name__ == '__main__':
    main()