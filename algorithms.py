


#Sorts a list of tuples based on the ith index of value
def sortTupleList(input: list, i: int): 
    return sorted(input, key=lambda a: a[i])


def buc(input: list, attrIndex: int, minsup: int, state: list):
    # print('buc call made Params: ', input, ', ', attrIndex)
    # print('\n', sorted(input, key=lambda a: a[attrIndex]), '\n')
    # Here 5 is the max number of attributes 
    for i in range(attrIndex, 5):
        # print('i: ', i)
        # first sort by attribute index
        table = sortTupleList(input, i)
        # Then scan the new list and check the attribute index 
        oldVal = (0, table[0][attrIndex])
        # print(oldVal, '\n\n')
        count = 0
        for j in range(len(table)): 
            # Get the current val
            # print(j)
            newVal = (j, table[j][attrIndex])
            # Check if it is a new val 
            if (newVal[1] != oldVal[1]):
                # print('\n miss: ', newVal[1], ' ', oldVal[1], '\n')
                # we also check our count to see if it is above the minsup 
                if (count >= minsup): 
                    if (i+1 < 5):
                        newState = state
                        newState[i] = oldVal[1]
                        print('\n hit: ', newState, count, '\n')
                        buc([table[idx] for idx in range(oldVal[0], j)], i+1, minsup, newState)
                        print('exiting recursion \n')
                # When we reach a different value we update oldval 
                # print('miss')
                oldVal= (j, newVal)
                count = 0
                    
            else: 
                count += 1
        
        
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
        
        

def main():
    data = processData('data.txt')
    buc(data, 0, 2, ['*', '*', '*', '*', '*'])
    return 0

if __name__ == "__main__": 
    main()