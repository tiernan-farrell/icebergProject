
from numpy import partition
import time
from flask import Flask
from flask_cors import CORS

NUM_DIMS = 3
CARDINALITY = [7 for i in range(NUM_DIMS)]
MINSUP = 1

outList = []
dataCount = []

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello(): 
    return "Hello, world"

# class BUC:
    
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
    outList.append(str(prettyPrintLocation) + ': ' + str(len(input)))
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
        
        

def generateDataCount(input: list): 
    dc = []
    if len(input) >= MINSUP:
        first = str(['*' for i in range(NUM_DIMS)]) + ': ' + str(len(input))
        outList.append(first)
    for i in range(NUM_DIMS): 
        dc.append([0 for i in range(CARDINALITY[i])])
    # This is first pass loop over input table one time 
    for row in input:
        for idx, num in enumerate(row): 
            dc[idx][num] = dc[idx][num] + 1

    return dc

def getFirstPassCombs(dc: list):
    combs = []
    for idx, row in enumerate(dc): 
        stringRep = ['*' for i in range(NUM_DIMS)]
        for i, val in enumerate(row):
            if (val >= MINSUP):
                stringRep1 = stringRep
                stringRep1[idx] = str(i)
                combs.append(stringRep1.copy())
                s = str(stringRep1) + ': ' + str(val)
                outList.append(s)
    return combs
                


def getCandidateCombs(combs: list):
    if (len(combs) < 2):
        return {}
    rval = {}
    candCombs = []
    for indx, row in enumerate(combs):
        j = indx + 1 
        for i in range(j, len(combs)): 
            cand = ['*' for i in range(NUM_DIMS)]
            next = combs[i]
            flag = True
            for d in range(NUM_DIMS):
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
            if flag: 
                candCombs.append(cand)
                

    for comb in candCombs: 
        rval[str(comb)] = 0
    return rval

def getCombs(candCombs: dict, input:list, currLocation: int):
    #Get counts for cand Combinations dictionary 
    numStars = NUM_DIMS - currLocation - 1
    for row in input: 
        subsets = getSubsets(row,numStars)
        for subset in subsets: 
            if str(subset) in candCombs:
                candCombs[str(subset)] = candCombs[str(subset)] + 1

    #Filter based on minsup
    combs = []
    for comb in candCombs: 
        if candCombs[comb] >= MINSUP:
            c = comb
            c = c.strip('[')
            c = c.strip(']')
            c = c.replace(",", "")
            c = c.replace("'", "")
            c = c.replace(" ", "")
            combs.append(list(c))
            s = comb + ': ' + str(candCombs[comb])
            outList.append(s)
    return combs

    
def getSubsets(row: tuple, numStars: int):
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
                s[idx] = str(val)
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
            s[idx] = str(val)
    if s not in subSet:
        subSet.append(s)
    return subSet

def apriori(input: list):
    dc = generateDataCount(input)
    combs = getFirstPassCombs(dc)
    candCombs = getCandidateCombs(combs)
    count = 1
    while (len(candCombs) > 0 and count <= NUM_DIMS):
        print('Count: ', count)
        print('combs: ', combs)
        print('cand combs: ', candCombs)
        combs = getCombs(candCombs, input, count)
        candCombs = getCandidateCombs(combs)
        count +=1
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
        
@app.route('/data', methods=["GET"])
def data():
    print('This is the data endpoint')
    with open('data.txt', 'r') as d: 
        return d.readlines()

@app.route('/buc', methods=["GET"])   
def runBuc():
    data = processData('data.txt') 
    initDataCount()
    start = time.time()
    buc(data, 0, ['*' for i in range(NUM_DIMS)])
    end = time.time()
    print('Tuples in datase: ', len(data), '\nTotal buc() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return outList


@app.route('/apriori', methods=["GET"])   
def runApriori():
    data = processData('data.txt') 
    initDataCount()
    start = time.time()
    apriori(data)
    end = time.time()
    print('Tuples in datase: ', len(data), '\nTotal apriori() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return outList


if __name__ == "__main__": 
    app.run("localhost", 6969)
