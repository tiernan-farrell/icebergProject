from apriori import Apriori
from buc import BUC
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


if __name__ == "__main__": 
    app.run("localhost", 6969)
