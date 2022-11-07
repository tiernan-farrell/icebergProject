#from crypt import methods
import random
from Algorithms.starCube import starCube
from Algorithms.tdc import TDC
from Algorithms.apriori import Apriori
from Algorithms.buc import BUC
from numpy import partition
import time
from flask import Flask, request
from flask_cors import CORS

NUM_DIMS = 5
CARDINALITY = [7 for i in range(NUM_DIMS)]
MINSUP = 10000

outList = []
dataCount = []

app = Flask(__name__)
CORS(app)      
times = {}
            
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
    with open('data/data.txt', 'r') as d: 
        return d.readlines()

@app.route('/buc', methods=["GET"])   
def runBuc():

    minsup = request.args.get('minsup', default=1, type = int)
    numDims = request.args.get('numDims', default=1, type = int)
    card = request.args.get('card', default=1, type = int)


    print('\n\nMinsup: ', minsup, '\n\n\n')
    data = processData('data/data.txt') 
    start = time.perf_counter()
    buc = BUC([card for i in range(numDims)], numDims, minsup)
    buc.buc(data, 0, ['*' for i in range(numDims)])
    end = time.perf_counter()
    times['buc'] = end - start
    print('Tuples in datase: ', len(data), '\nTotal buc() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return buc.getResults()


@app.route('/apriori', methods=["GET"])   
def runApriori():
    
    minsup = request.args.get('minsup', default=1, type = int)
    numDims = request.args.get('numDims', default=1, type = int)
    card = request.args.get('card', default=1, type = int)


    data = processData('data/data.txt') 
    start = time.perf_counter()
    apriori = Apriori([card for i in range(numDims)], numDims, minsup)
    apriori.apriori(data)
    end = time.perf_counter()
    times['apriori'] = end - start
    print('Tuples in datase: ', len(data), '\nTotal apriori() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return apriori.getResults()

@app.route('/tdc', methods=["GET"])   
def runTdc():
    
    minsup = request.args.get('minsup', default=1, type = int)
    numDims = request.args.get('numDims', default=1, type = int)
    card = request.args.get('card', default=1, type = int)

    data = processData('data/data.txt') 
    start = time.perf_counter()
    tdc = TDC([card for i in range(numDims)], numDims, minsup)
    tdc.tdc(data, [i for i in range(numDims)])
    end = time.perf_counter()
    times['tdc'] = end - start
    print('Tuples in datase: ', len(data), '\nTotal Top Down Computation() time: ', end-start, '\nTotal iceberg cube size: ', len(outList))
    return tdc.getResults()

@app.route('/starCube', methods=["GET"])   
def runStarCube():

    start = time.perf_counter()
    star = starCube("data/data.csv", MINSUP)
    res = star.getResults()
    end = time.perf_counter()
    print('\nTotal star cubing() time: ', end-start)
    return res

@app.route('/getComputationTimes', methods=["GET"])
def getTimes(): 
    if 'buc' not in times: 
        sbuc = time.perf_counter()
        runBuc()
        ebuc = time.perf_counter()
        times['buc'] = ebuc - sbuc
    if 'tdc' not in times: 
        stdc = time.perf_counter()
        runTdc()
        etdc = time.perf_counter()
        times['tdc'] = etdc - stdc
    if 'apriori' not in times: 
        sap = time.perf_counter()
        runBuc()
        eap = time.perf_counter()
        times['apriori'] = eap - sap
    return times
    
@app.route('/generateData', methods=["GET"])
def generateData():
    numTuples = request.args.get('numTuples', default=1, type = int)
    numDims = request.args.get('numDims', default=1, type = int)
    card = request.args.get('card', default=1, type = int)
    data = []
    with open('data/data.txt', 'w') as f:
        for i in range (numTuples): 
            print(i)
            listVal = []
            random.seed(i)
            for j in range(numDims):
                listVal.insert(j, random.randint(0,card-1))
            f.write(str(listVal))
            f.write('\n')
            data.append(listVal)
    f.close()        
    return data


if __name__ == "__main__": 
    app.run("localhost", 6969)
