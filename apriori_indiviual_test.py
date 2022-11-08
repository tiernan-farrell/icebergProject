import os

def processData(filename): 
    here = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(here, filename)
    file = open(filePath, newline='')
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

class Apriori: 
    
    def __init__(self, card, dims, minsup): 
        self.dims = dims
        self.cardinality = card
        self.minsup = minsup
        self.dc = []
        self.outList = []        
        
    def generateDataCount(self, input: list): 
        if len(input) >= self.minsup:
            first = str(['*' for i in range(self.dims)]) + ': ' + str(len(input))
            self.outList.append(first)
        for i in range(self.dims): 
            self.dc.append([0 for i in range(self.cardinality[i])])
        # This is first pass loop over input table one time 
        for row in input:
            for idx, num in enumerate(row): 
                self.dc[idx][num] = self.dc[idx][num] + 1

    def getFirstPassCombs(self):
        combs = []
        for idx, row in enumerate(self.dc): 
            stringRep = ['*' for i in range(self.dims)]
            for i, val in enumerate(row):
                if (val >= self.minsup):
                    stringRep1 = stringRep
                    #Was str(i)
                    stringRep1[idx] = i
                    combs.append(stringRep1.copy())
                    s = str(stringRep1) + ': ' + str(val)
                    self.outList.append(s)
        return combs
                    


    def getCandidateCombs(self, combs: list):
        if (len(combs) < 2):
            return {}
        rval = {}
        candCombs = []
        for indx, row in enumerate(combs):
            j = indx + 1 
            for i in range(j, len(combs)): 
                cand = ['*' for i in range(self.dims)]
                next = combs[i]
                print("row = ", row)
                print("next = ", next)
                flag = True
                for d in range(self.dims):
                    print("row[", d, "] = ", row[d]) 
                    print("next[", d,"] = ", next[d])
                    #If values between the two at dim d are not equal and neither are starts
                    if row[d] != next[d] and row[d] != '*' and next[d] != '*':
                        flag = False
                        break
                    #Else if both vals are stars 
                    elif row[d] == '*' and next[d] == '*':
                        cand[d] = '*'
                    # else if one is a val and one is a star
                    elif row[d] == '*' or next[d] == '*':
                        if row[d] == '*':
                            cand[d] = next[d]
                        else: 
                            cand[d] = row[d]
                    #Else they are the same value
                    else: 
                        cand[d] = row[d]
                    print("Cand[",d,"] = ", cand)
                print("Flag = ", flag)
                if flag and (cand not in candCombs): 
                    print("APPENDED CAND = ", cand)
                    candCombs.append(cand)
                    

        for comb in candCombs: 
            rval[str(comb)] = 0
        return rval

    def getCombs(self, candCombs: dict, input:list, currLocation: int):
        #Get counts for cand Combinations dictionary 
        numStars = self.dims - currLocation - 1
        for row in input: 
            subsets = self.getSubsets(row,numStars)
            for subset in subsets: 
                if str(subset) in candCombs:
                    candCombs[str(subset)] = candCombs[str(subset)] + 1

        #Filter based on self.minsup
        combs = []
        for comb in candCombs: 
            if (candCombs[comb] >= self.minsup):
                c = comb
                c = c.strip('[')
                c = c.strip(']')
                c = c.replace(",", "")
                c = c.replace("'", "")
                c = c.replace(" ", "")
                cList=[]
                for val in c:
                    if val == '*':
                        cList.append('*')
                    else:
                        cList.append(int(val))
                if (cList not in combs):
                    combs.append(cList)
                s = comb + ': ' + str(candCombs[comb])
                self.outList.append(s)
        return combs

        
    def getSubsets(self, row: tuple, numStars: int):
        subSet = []
        starIdxs = []
        finalStarIdxs = []
        
        # Generate beginning star and final star index arrays
        for i in range(numStars):
            starIdxs.append(i)
            finalStarIdxs.insert(0, len(row)-i-1)
            
        # Gets subsets of tuple as strings that could be found in candCombs dict    
        while starIdxs != finalStarIdxs:
            #Check last ele in starIdxs increment if possible 
            #Generate current subset for given star locations
            s = ['*' for i in range(len(row))]
            for idx, val in enumerate(row):
                if idx not in starIdxs:
                    s[idx] = val
            subSet.append(s)
            if starIdxs[-1] < len(row)-1: 
                starIdxs[-1] = starIdxs[-1] + 1        
            else:
                # decrement indx until we find one that isn't -1 of next greatest index
                j = numStars - 2
                while j >= 0:
                    if starIdxs[j] != starIdxs[j+1]-1:
                        starIdxs[j] = starIdxs[j] + 1
                        for k in range(j+1, numStars):
                            starIdxs[k] = starIdxs[k-1]+1
                        break
                    j-=1
        s = ['*' for i in range(len(row))]
        for idx, val in enumerate(row):
            if idx not in starIdxs:
                s[idx] = val
        if s not in subSet:
            subSet.append(s)
        return subSet

    def apriori(self, input: list):
        self.generateDataCount(input)
        combs = self.getFirstPassCombs()
        candCombs = self.getCandidateCombs(combs)
        count = 1
        while (len(candCombs) > 0 and count <= self.dims):
            combs = self.getCombs(candCombs, input, count)
            candCombs = self.getCandidateCombs(combs)
            count +=1
            print(count)
            print("dims = ", self.dims)
            print("len(candCombs) = ", len(candCombs))
        return
    
    def getResults(self):
        return self.outList

    


data = processData('data.txt') 
apriori = Apriori([1 for i in range(3)], 3, 2)
apriori.apriori(data)

list = apriori.getResults()