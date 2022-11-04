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
            print('list to be trimmed: ', l)
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
        print(self.checkedDims)
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
                    # prune[starredKey].append(row) 
                else: 
                    d[starredKey] = 1 
                    # prune[starredKey] = []
                    # prune[starredKey].append(row) 
        for key in d: 
            if key not in self.cube:
                if d[key] >= self.minsup:
                    self.cube[key] = d[key]
                # else: 
                    # #prune input 
                    # for row in prune[key]:
                    #     input = input.delete(row)
        # Recursive calls happen dimension list is not empty 
        f = True
        while len(dimensionList) > 0 and f:
            print(dimensionList)
            # if dimension list needs to be trimmed
            if self.needsTrimmed(dimensionList):
                dimensionList = self.trim(dimensionList)
            else: 
                dimensionList = self.inc(dimensionList)
            if dimensionList not in self.checkedDims: 
                f = False 
                print('Recursive call: ', dimensionList)
                self.tdc(input, dimensionList)            
                    
            
        if len(dimensionList) == 0: 
            self.cube[tuple(['*' for i in range(self.dims)])] = len(input)
            
        return  
    
    
    def getResults(self):
        return [ str(str(key) + ': ' + str(value)) for (key,value) in self.cube.items() if value >= self.minsup ]
