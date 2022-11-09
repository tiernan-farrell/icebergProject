


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
        self.outList.append(str(prettyPrintLocation) + ': ' + str(len(input)))
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
    
    
