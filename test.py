

import enum
import sqlite3

NUM_DIMS = 3


def getSubsets(row: tuple, numStars: int):
    subSet = []
    starIdxs = []
    finalStarIdxs = []
    
    # Generate beginning star and final star index arrays
    for i in range(numStars):
        starIdxs.append(i)
        finalStarIdxs.insert(0, len(row)-i-1)
    # Gets subsets of tuple as strings that could be found in candCombs dict
    # print('Final: ', str(finalStarIdxs))
    # print('Starting: ', str(starIdxs))
    
    while starIdxs != finalStarIdxs:
        #Check last ele in starIdxs increment if possible 
        # print(starIdxs)
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
    # print(starIdxs)
                        
    

    return subSet


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
                print(d) 
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


def main():

    # conn = sqlite3.connect('db/players.db')
    # c = conn.cursor()
    # res = c.execute(" SELECT * FROM playerData;")
    # print(res.fetchone())
    # print(getSubsets((0, 1, 2, 3, 4), 2))
    
    # print(getCandidateCombs( ["['0', '1', '*', '*', '*']", "['0', '*', '2', '*', '*']", "['0', '*', '*', '3', '*']", "['0', '*', '*', '*', '4']", "['*', '1', '2', '*', '*']", "['*', '1', '*', '3', '*']", "['*', '1', '*', '*', '4']", "['*', '*', '2', '3', '*']", "['*', '*', '2', '*', '4']", "['*', '*', '*', '3', '4']"]))
    
    # print(getCandidateCombs([ ['1', '4', '*'], 
    #                     ['6', '*', '6'],
    #                     ['*', '4', '6']]))

    l = "['*', '1', '*']"
    l =l.strip('[')
    l = l.strip(']')
    l = l.replace(",", "")
    l = l.replace("'", "")
    l = l.replace(" ", "")
    print(l)
    print(list(l))
        
if __name__ == "__main__":
    main()