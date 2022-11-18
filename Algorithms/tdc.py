import time

NUM_DIMS = 4
CARDINALITY = [7 for i in range(NUM_DIMS)]
MINSUP = 2

class TDC:
    def __init__(self, card, dims, minsup): 
        self.cardinality = card
        self.dims = dims
        self.minsup = minsup 
        self.dc = [[0 for _ in range(card[i])]for i in range(dims)]
        self.outList = []
        self.checkedDims = []
        self.cube = {}
    #Sorts a list of tuples based on the ith index of value
    def sortTupleList(self, input: list, i: int): 
        return sorted(input, key=lambda a: a[i])

    def starKey(self, row: tuple, dims: list): 
        elements = []
        for i in range(len(row)):
            if i in dims: 
                elements.append(row[i])
            else:
                elements.append('*')
        return tuple(elements)


    def needsTrimmed(self, l: list): 
        trimList = [self.dims - i-1 for i in range(len(l))]
        trimList.reverse()

        if l == trimList:
            # print('list to be trimmed: ', l)
            return True
        
        return False

    def trim(self, lis: list): 
        if len(lis) == 2: 
            newList = lis
            newList.pop()
        else: 
            newList = [i for i in range(len(lis)-1)]

        return newList
        
    def inc(self, lis: list): 
        if len(lis) == 1: 
            if (lis[0] < self.dims-1):
                return [lis[0] + 1]
        newList = lis
        end = len(lis) - 1
        flag = True
        while flag and len(lis) > 1 and end >= 0:
            if lis[end] < self.dims - 1 - (len(lis)-1 - end):
                newList[end] = lis[end] + 1
                if end == 0:
                    return [i for i in range(newList[end], len(lis)+newList[end])]
                flag = False
            else: 
                end -= 1
        return newList
    
    
    
    def tdc(self, input: list, dimensionList: list):
        for i in range(len(dimensionList)):
            if [dimensionList[j] for j in range(i+1)] not in self.checkedDims:
                self.checkedDims.append([dimensionList[j] for j in range(i+1)])
        # print(self.checkedDims)
        sortedInput = sorted(input, key=lambda x: tuple([x[dimensionList[i]]] for i in range(len(dimensionList))))
        d = {}
        #keeps track of which dimension combinations need to be pruned
        prune = []
        pruneD = {}
        # Loop through input sorted on dimension order and insert counts into cube
        for row in sortedInput: 
            
            for i in range(len(dimensionList)):
                key = [dimensionList[j] for j in range(i+1)]
                if(tuple(key) not in pruneD):
                    pruneD[tuple(key)] = True
                # print('Row: ', row, '   key: ', key, '  ')
                # With the dimensions we are checking on we check the sorted table and update the cube 
                starredKey = self.starKey(row, key)
                if starredKey in d:
                    d[starredKey] += 1
                    # sets flag of dimension combination to false if found to be "frequent" for some combination
                    if(d[starredKey] >= self.minsup):
                        pruneD[tuple(key)] = False
                else: 
                    d[starredKey] = 1 
        # print("pruneD", pruneD)
        # sets dimension combination to be pruned as smallest flagged dimension combo to maximize amount of pruning
        for key in pruneD:
            if pruneD[key] and not prune:
                prune = list(key)
        # print("Prune list", prune)
        for key in d: 
            if key not in self.cube:
                if d[key] >= self.minsup:
                    self.cube[key] = d[key]
                    outElem = list(key)
                    outElem.append(d[key])
                    self.outList.append(outElem)
        # Recursive calls happen dimension list is not empty 
        f = True
        while len(dimensionList) > 0 and f:
            # print(dimensionList)
            # if dimension list needs to be trimmed
            if self.needsTrimmed(dimensionList):
                dimensionList = self.trim(dimensionList)
            else: 
                dimensionList = self.inc(dimensionList)
            #if prune dims are subset of current dimensionList, skip to the next dimensionList
            if(prune and set(prune).issubset(set(dimensionList))):
                    print("pruning", dimensionList)
                    for i in range(len(dimensionList)):
                        if [dimensionList[j] for j in range(i+1)] not in self.checkedDims:
                            self.checkedDims.append([dimensionList[j] for j in range(i+1)])
            if dimensionList not in self.checkedDims: 
                f = False 
                # print('Recursive call: ', dimensionList)
                self.tdc(input, dimensionList)            
                    
            
        if len(dimensionList) == 0: 
            if tuple(['*' for i in range(self.dims)]) not in self.cube:
                self.cube[tuple(['*' for i in range(self.dims)])] = len(input)
                outElem = ['*' for j in range(self.dims)]
                outElem.append(len(input))
                self.outList.append(outElem)
            
        return  
    
    
    def getResults(self):
        #return [ str(str(key) + ': ' + str(value)) for (key,value) in self.cube.items() if value >= self.minsup ]
        return self.outList

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
    data = processData('data/testData.txt') 
    start = time.time()
    tdc = TDC(CARDINALITY, NUM_DIMS, MINSUP)
    tdc.tdc(data, [i for i in range(NUM_DIMS)])
    end = time.time()
    print('Tuples in datase: ', len(data), '\nTotal tdc() time: ', end-start, '\nTotal iceberg cube size: ', len(tdc.outList))
    for e in tdc.getResults():
        print(e)
    return tdc.getResults()

if __name__ == '__main__':
    main()