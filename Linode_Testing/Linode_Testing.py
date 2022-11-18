from Linode_Apriori import Apriori
from Linode_BUC import BUC
from Linode_Star_Cube import starCube
from Linode_TDC import TDC
import time

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


txt_List = []
csv_List = []
algo_Input = ' '

while(not algo_Input == '5'):
    print('Please enter which algorithm you would like to run.')
    algo_Input = input('1: Apriori 2: BUC 3: Star-Cube 4: TDC 5: to quit\n')

    match algo_Input:
        case '1': #Apriori
            data = processData('data/data.txt') 
            start = time.perf_counter()
            apriori = Apriori([card for i in range(numDims)], numDims, minsup)
            apriori.apriori(data)
            end = time.perf_counter()
            time = end - start
            toContinue = input('Algorithm finshed output list to txt? y/n: ')
            if(toContinue == 'y'):
                apriori_Results = apriori.getResults()
                f = open('results/Apriori_Results.txt', 'w')
                f.write('Apriori time: ' + time + '\n')
                f.write('List: \n' + apriori_Results)
                print('*List printed to file Apriori_Results.txt*')

        case '2': #BUC

            data = processData('data/data.txt') 
            start = time.perf_counter()
            buc = BUC([card for i in range(numDims)], numDims, minsup)
            buc.buc(data, 0, ['*' for i in range(numDims)])
            end = time.perf_counter()
            time = end - start
            toContinue = input('Algorithm finshed output list to txt? y/n: ')
            if(toContinue == 'y'):
                buc_Results = buc.getResults()
                f = open('results/BUC_Results.txt', 'w')
                f.write('BUC time: ' + time + '\n')
                f.write('List: \n' + buc_Results)
                print('*List printed to file BUC_Results.txt*')

        case '3': #Star-Cube
            
            data = processData('data/data.txt') 
            start = time.perf_counter()
            star = starCube(data, MINSUP)
            star.generateCube()
            end = time.perf_counter()
            time = end - start
            toContinue = input('Algorithm finshed output list to txt? y/n: ')
            if(toContinue == 'y'):
                starCube_results = star.getResults()
                f = open('results/StarCube_Results.txt', 'w')
                f.write('Star-Cube time: ' + time + '\n')
                f.write('List: \n' + starCube_results)
                print('*List printed to file StarCube_Results.txt*')
            
        case '4': #TDC
            data = processData('data/data.txt') 
            start = time.perf_counter()
            tdc = TDC([card for i in range(numDims)], numDims, minsup)
            tdc.tdc(data, [i for i in range(numDims)])
            end = time.perf_counter()
            time = end - start
            toContinue = input('Algorithm finshed output list to txt? y/n: ')
            if(toContinue == 'y'):
                tdc_results = tdc.getResults()
                f = open('results/TDC_Results.txt', 'w')
                f.write('TDC time: ' + time + '\n')
                f.write('List: \n' + tdc_results)
                print('*List printed to file TDC_Results.txt*')
 



