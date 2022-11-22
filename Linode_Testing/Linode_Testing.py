from Algorithms.apriori import Apriori
from Algorithms.buc import BUC
from Algorithms.starCube import starCube
from Algorithms.tdc import TDC
import time
import tracemalloc
import psutil

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


def convert_to_percent(load_tuple):
    num_log_cpus = psutil.cpu_count()

    percent_lst = []

    for load in load_tuple:
        percent = (load / num_log_cpus) * 100
        percent_lst.append(percent)
    
    return tuple(percent_lst)

txt_List = []
csv_List = []
algo_Input = ' '
load_tuple=psutil.getloadavg()


def testDataSet(fileName: str, card: int, numDims):
    data = processData('data/data.txt')
    minsup =1 
    while minsup <= 1000:
        #Apriori
        aprioriStart = time.perf_counter()
        tracemalloc.start()
        apriori = Apriori([card for i in range(numDims)], numDims, minsup)
        apriori.apriori(data)
        aprioriEnd = time.perf_counter()
        aprioriTime = aprioriEnd - aprioriStart
        apriori_Results = apriori.getResults()
        f = open('results/Apriori_Results.txt', 'w')
        f.write('Apriori time: ' + aprioriTime + '\n')
        f.write('Apriori memory usage: '+ tracemalloc.get_traced_memory()+ '\n')
        f.write('The average CPU usage is: '+ convert_to_percent(load_tuple))
        f.write('List: \n' + apriori_Results)
        print('*List printed to file Apriori_Results.txt*')
        tracemalloc.stop()


        # BUC
        bucStart = time.perf_counter()
        tracemalloc.start()
        buc = BUC([card for i in range(numDims)], numDims, minsup)
        buc.buc(data, 0, ['*' for i in range(numDims)])
        bucEnd = time.perf_counter()
        bucTime = bucEnd - bucStart
        buc_Results = buc.getResults()
        f = open('results/BUC_Results.txt', 'w')
        f.write('BUC time: ' + bucTime + '\n')
        f.write('BUC memory usage: '+ tracemalloc.get_traced_memory()+ '\n')
        f.write('The average CPU usage is: '+ convert_to_percent(load_tuple))
        f.write('List: \n' + buc_Results)
        print('*List printed to file BUC_Results.txt*')
        tracemalloc.stop()
    
        #TDC
        tdcStart = time.perf_counter()
        tracemalloc.start()
        tdc = TDC([card for i in range(numDims)], numDims, minsup)
        tdc.tdc(data, [i for i in range(numDims)])
        tdcEnd = time.perf_counter()
        tdcTime = tdcEnd - tdcStart
        tdc_results = tdc.getResults()
        f = open('results/TDC_Results.txt', 'w')
        f.write('TDC time: ' + tdcTime + '\n')
        f.write('TDC memory usage: '+ tracemalloc.get_traced_memory()+ '\n')
        f.write('The average CPU usage is: '+ convert_to_percent(load_tuple))
        f.write('List: \n' + tdc_results)
        print('*List printed to file TDC_Results.txt*')
            
        # Star Cubing    
        scStart = time.perf_counter()
        tracemalloc.start()
        star = starCube(data, minsup)
        star.generateCube()
        scEnd = time.perf_counter()
        scTime = scEnd - scStart
        starCube_results = star.getResults()
        f = open('results/StarCube_Results.txt', 'w')
        f.write('Star-Cube time: ' + scTime + '\n')
        f.write('Star-Cube memory usage: '+ tracemalloc.get_traced_memory()+ '\n')
        f.write('The average CPU usage is: '+ convert_to_percent(load_tuple))
        f.write('List: \n' + starCube_results)
        print('*List printed to file StarCube_Results.txt*')
        tracemalloc.stop()
        
        
        minsup *= 10