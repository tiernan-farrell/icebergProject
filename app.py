#from crypt import methods
from starCube import starCube
from tdc import TDC
from apriori import Apriori
from buc import BUC
from numpy import partition
import time
from flask import Flask
from flask_cors import CORS

NUM_DIMS = 5
CARDINALITY = [7 for i in range(NUM_DIMS)]
MINSUP = 100

outList = []
dataCount = []

app = Flask(__name__)
CORS(app)      

            
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
    start = time.time()
    buc = BUC(CARDINALITY, NUM_DIMS, MINSUP)
    buc.buc(data, 0, ['*' for i in range(NUM_DIMS)])
    end = time.time()
    print('Tuples in datase: ', len(data), '\nTotal buc() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return buc.getResults()


@app.route('/apriori', methods=["GET"])   
def runApriori():
    data = processData('data.txt') 
    start = time.time()
    apriori = Apriori(CARDINALITY, NUM_DIMS, MINSUP)
    apriori.apriori(data)
    end = time.time()
    print('Tuples in datase: ', len(data), '\nTotal apriori() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return apriori.getResults()

@app.route('/tdc', methods=["GET"])   
def runTdc():
    data = processData('data.txt') 
    start = time.time()
    tdc = TDC(CARDINALITY, NUM_DIMS, MINSUP)
    tdc.tdc(data, [i for i in range(NUM_DIMS)])
    end = time.time()
    print('Tuples in datase: ', len(data), '\nTotal Top Down Computation() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return tdc.getResults()

@app.route('/starCube', methods=["GET"])   
def runStarCube():
    start = time.time()
    star = starCube("data.csv", MINSUP)
    star.generateCube()
    end = time.time()
    res = star.getResults()
    
    print('\nTotal star cubing() time: ', end-start)
    return res

@app.route('/getComputationTimes', methods=["GET"])
def getTimes(): 
    times = {}
    s1 = time.time()
    runBuc()
    s2 = time.time()
    times['buc'] = s2-s1
    s11 = time.time()
    runApriori()
    s22 = time.time()
    times['apriori'] = s22-s11
    s111 = time.time()
    runTdc()
    s222 = time.time()
    times['TopDown'] = s222-s111
    return times
    

if __name__ == "__main__": 
    app.run("localhost", 6969)
