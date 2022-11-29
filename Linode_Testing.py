from Algorithms.apriori import Apriori
from Algorithms.buc import BUC
from Algorithms.tdc import TDC
import time
import tracemalloc

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


# def convert_to_percent(load_tuple):
#     num_log_cpus = psutil.cpu_count()

#     percent_lst = []

#     for load in load_tuple:
#         percent = (load / num_log_cpus) * 100
#         percent_lst.append(percent)
    
#     return tuple(percent_lst)

# txt_List = []
# csv_List = []
# algo_Input = ' '


def testDataSet(fileName: str, data: list, card: int, numDims):
    minsup =1 
    while minsup <= 100:
        #Apriori

        tracemalloc.start()
        currMem = tracemalloc.get_traced_memory()[0]
        aprioriStart = time.perf_counter()
        apriori = Apriori([card for _ in range(numDims)], numDims, minsup)
        apriori.apriori(data)
        aprioriEnd = time.perf_counter()
        afterMem = tracemalloc.get_traced_memory()[1]
        aprioriTime = aprioriEnd - aprioriStart
        f = open('results/Apriori_Results.txt', 'a')
        f.write('\n\n')
        f.write(fileName)
        writeAprioriTime = 'Apriori time: ' + str(aprioriTime) + ' seconds \n'
        f.write(writeAprioriTime)
        writeAprioriMem = 'Apriori memory usage: ' + str(afterMem-currMem) + ' bytes \n'
        f.write(writeAprioriMem)
        # f.write('The average CPU usage is: ', convert_to_percent(psutil.getloadavg()))
        print('*List printed to file Apriori_Results.txt*')
        tracemalloc.stop()


        # BUC
        tracemalloc.start()
        bucStart = time.perf_counter()
        buc = BUC([card for i in range(numDims)], numDims, minsup)
        currMem = tracemalloc.get_traced_memory()[0]
        buc.buc(data, 0, ['*' for i in range(numDims)])
        bucEnd = time.perf_counter()
        bucTime = bucEnd - bucStart
        f = open('results/BUC_Results.txt', 'a')
        f.write('\n\n')
        f.write(fileName)
        writeBucTime = 'BUC time: ' + str(bucTime) + ' seconds \n'
        f.write(writeBucTime)
        writeBucMem = 'BUC memory usage: ' + str(tracemalloc.get_traced_memory()[1]-currMem) + ' bytes \n'
        f.write(writeBucMem)
        # f.write('The average CPU usage is: ', convert_to_percent(psutil.getloadavg()))
        print('*List printed to file BUC_Results.txt*')
        tracemalloc.stop()
    
        #TDC
        tracemalloc.start()
        tdcStart = time.perf_counter()
        tdc = TDC([card for i in range(numDims)], numDims, minsup)
        currMem = tracemalloc.get_traced_memory()[0]
        tdc.tdc(data, [i for i in range(numDims)])
        tdcEnd = time.perf_counter()
        tdcTime = tdcEnd - tdcStart
        f = open('results/TDC_Results.txt', 'a')
        f.write('\n\n')
        f.write(fileName)
        writeTdcTime = 'TDC time: ' + str(tdcTime) + ' seconds \n'
        f.write(writeTdcTime)
        writeTdcMem = 'TDC memory usage: ' + str(tracemalloc.get_traced_memory()[1]-currMem) + ' bytes \n'
        f.write(writeTdcMem)
        # f.write('The average CPU usage is: ', convert_to_percent(psutil.getloadavg()))
        print('*List printed to file TDC_Results.txt*')
        tracemalloc.stop()
        
        if minsup == 1: 
            minsup = 10
        else: 
            minsup += 10
    
        
# Call test dataSet with each data set in our data folder 
dataSets = ['data/100tuples5dims2card.txt', 'data/100tuples5dims5card.txt', 'data/100tuples3dims3card.txt', 'data/100tuples3dims8card.txt', 'data/500tuples5dims2card.txt', 'data/500tuples5dims5card.txt', 'data/500tuples3dims3card.txt', 'data/500tuples3dims8card.txt', 'data/1000tuples5dims2card.txt', 'data/1000tuples5dims5card.txt', 'data/1000tuples3dims3card.txt', 'data/1000tuples3dims8card.txt', 'data/10000tuples5dims2card.txt', 'data/10000tuples5dims5card.txt', 'data/10000tuples3dims3card.txt', 'data/10000tuples3dims8card.txt']
for dataFile in dataSets:
    dims = int(dataFile.split('tuples')[1][0])
    card = int(dataFile.split('dims')[1][0])
    data = processData(dataFile)
    testDataSet(dataFile, data, card, dims)