class TDC:
    def __init__(self, card, dims, minsup): 
        self.cardinality = card
        self.dims = dims
        self.minsup = minsup 
        self.dc = [[0 for _ in range(card[i])]for i in range(dims)]
        self.outList = []
        self.cube = {}
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
            return True
        
        return False

    def trim(self, lis: list): 
        newList = [i for i in range(len(lis)-2)]
        newList.append(self.dims-1)
        return newList
        
    def inc(self, lis: list): 
        newList = lis
        check = len(lis)-2
        end = len(lis) - 1
        flag = True
        while flag and len(lis) > 1 and check >= 0:
            if lis[check] < lis[end]-1:
                newList[check] = newList[check] + 1
                flag = False
            else: 
                check -= 1
                end -= 1
        return newList
        
        
    def tdc(self, input: list, dimensionList: list):
        sortedInput = sorted(input, key=lambda x: tuple([x[dimensionList[i]]] for i in range(len(dimensionList))))
        d = {}
        prune = {}
        # Loop through input sorted on dimension order and insert counts into cube
        for row in sortedInput: 
            for i in range(len(dimensionList)):
                key = [dimensionList[j] for j in range(i+1)]
                # print('Row: ', row, '   key: ', key, '  ')
                # With the dimensions we are checking on we check the sorted table and update the cube 
                starredKey = self.starKey(row, key)
                if starredKey in d:
                    d[starredKey] += 1 
                else: 
                    d[starredKey] = 1 
        for key in d: 
            if key not in self.cube:
                if d[key] >= self.minsup:
                    self.cube[key] = d[key]
                else: 
                    #prune input 
                    pass 
        # Recursive calls happen dimension list is not empty 
        if len(dimensionList) > 1:
            # if dimension list needs to be trimmed
            if self.needsTrimmed(dimensionList):
                dimensionList = self.trim(dimensionList)
                print(dimensionList)
            else: 
                dimensionList = self.inc(dimensionList)
            
            self.tdc(input, dimensionList)            
        else: 
            self.cube[tuple(['*' for i in range(self.dims)])] = len(input)
            
        return  
    
    
    def getResults(self):
        return [ str(str(key) + ': ' + str(value)) for (key,value) in self.cube.items() if value >= self.minsup ]
    
    