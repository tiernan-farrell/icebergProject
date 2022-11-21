
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
        
class Tree: 
    
    def __init__(self, root):
        self.root = root

    def addBranch(self, root, tup, count):
        
        if len(root.descendents) > 0:
            needsNode = True
            for descendent in root.descendents:
                if descendent.attrVal == tup[0]:
                    descendent.count += count
                    needsNode = False
            
            if needsNode:
                newNode = Node(tup[0], count)
                root.descenents.append[newNode]

        else:
            newNode = Node(tup[0], count)
            root.descenents.append[newNode]

        forNewTuple = []
        index = 0
        while index < len(tup):
            if not index == 0:
                forNewTuple.append(tup[index])

        self.addBranch(newNode, tuple(forNewTuple), count)
    
    def addSiblings(self,descendents):
            for descendentx in descendents:

               for descendenty in descendents:
                if not descendentx.attrVal == descendenty.attrVal:
                    descendentx.siblings.append(descendenty)
            
            self.addSiblings(descendentx.descendents) 

class Node: 
    
    def __init__(self, attrVal, count, descendents=None, siblings=None):
        self.val = attrVal
        self.count = count
        self.descendents = descendents
        self.siblings = siblings
        





class starCube:

    # Notes from paper 
        # We are combining TDC, BUC and APRIORI
        # Globally use a top-down traversal with a sub-layer based on BUC 
        # The sub-layer expolores the notion of shared dimensions
        # Allows for aggregation on multiple dimensions while still partition parent group bys and prune child group bys
        
        # What is a shared dimension ?
            # Common dimensions shared on subtrees (TDC checks all shared dimensions multiple times)
            # The introduction of shared dimensions facilitates shared computation
            # If the value of a shared dimension does not meet minsup, the whoel sub-tree rooted at the 
            # start of the shared dimension can be pruned. 
            # Aggregate values of shared dimensions MUST be calculated FIRST
                # Before aggregating a partition in ABD, the partition must be aggregated in the shared dimension AB already

        # Cuboid tree representation
            # Each level is a dimesnion     (A)
            # Each node is an attribute     (a1)
            # Node has four fields: (1) Value of attribute (2) aggregate count (3) Pointers to possible descendents and (4) Pointers to possible siblings
            # Path from root to node is a tuple
            # Tree rep collapses common prefixes to save memory usage 
            # allows aggregation of values at internal nodes which allows for pruning on shared dimensions
            
    
    
    # What is star cubing Doing? 
        # Base cuboid table is our input list (self.data)
        # Reduce base table to star nodes who dont meet minsup and non star nodes who do 
        # Compress the base table with stars and add update counts (initially we dont store counts since they are all 1)
        # Construct a star cuboid tree based on the compressed base table 
        # Construct star table from the compressed base table
        # Once star tree and star table are created we can begin traversal in a top down depth-first manner
        

    # Child tree pruning: 
        # Prune useless child trees based on these 2 conditions
        # (1) the measure of the current node must satisfy the iceberg condition;
        # (2) the tree to be generated must include at least one non-star (i.e., non- trivial) node. 
        # A node could just barely satisfy the iceberg condition in the base tree, but when it is divided in the child trees, 
        # it no longer satisfies the condition. For this reason, it is required that all the nodes be checked again in the construction of child trees. 
        # That is, all child trees will have their own star table which will count the nodes and make them star-nodes where appropriate.
    
    
    # Memory management 
        # Memory can become an issue with constant construction and destruction of cuboid trees
        # Solution: Maintain a "free node list"
        # To initialize the free node list, the algorithm will allocate kdn nodes into a node buffer, 
        # where d is the number of dimensions, n is the number of tuples, and k is a scaling factor dependent
        # on the iceberg condition. The larger the minimum support is, the smaller k is. In practice, 
        # a value of 0.2 is usually sufficient for k.
        # Similar to the free node list, the algorithm main- tains a free cuboid tree list as well.


    def __init__(self, data, numDims, minSup):
        # Given values from user
        self.data = data
        self.numDims = numDims
        self.minSup = minSup
        # Init empty node/tree lists
        #self.freeNodes = [Node(0, 0) for i in range(.2*len(data)*numDims)]
        #self.freeTrees = [Tree() for i in range(.2*len(data)*numDims)]
        # Create value count dictionary to create star table and compressed table
        self.countValues = self.getValueCountDictionary(self.data)
        # Compress base table
        self.compressedTable = self.compressTable(self.data, self.countValues, self.minSup)
        # Create star table
        self.starTable = self.createStarTable(self.countValues, self.minSup)
        # Allocate kdn nodes into a buffer
        
    # Takes in processed data input and returns a list of dimension dictionarys with their value counts 
    # For Example [(1,2), (3,3)] = [{1:1, {2:2}, {3:2} ]
    def getValueCountDictionary(self, data):
        countValues = []


        for tuples in data:
            dimensionIndex = 0

            for value in tuples:
                # Creates new dem dict and adds first value of dim to countValues list if length of tuple (# of columns) 
                # is more then num of dicts (# of dims) in countValues
                if len(countValues) < len(tuples):
                    countValues.append({})
                    countValues[dimensionIndex][value] = 1
                # if value in tuple is already in dict then increase count
                elif value in countValues[dimensionIndex]:
                    hold = countValues[dimensionIndex][value]
                    countValues[dimensionIndex][value] = hold + 1
                # otherwise add new value to dict and set it to 1
                else:
                    countValues[dimensionIndex][value] = 1

                dimensionIndex += 1

        return countValues

    # Compresses data input table through countValues and minSup. If count of value in data table is less than minSup
    # then replace it with '*'. Then makes a compressed table dict with tuples and counts of number of tuples that 
    # are the same.
    def compressTable(self, data, countValues, minSup):
        compressedTable = {}
        tempTable = []
        tupleIndex = 0

        for tuples in data:
            tempList = []
            dimIndex = 0

            for value in tuples:
                if countValues[dimIndex].get(value) < minSup:
                    tempList.append('*')
                else:
                    tempList.append(value)
                dimIndex += 1
            tempTable.append(tuple(tempList))
            tupleIndex += 1

        for tuples in tempTable:
            if not tuples in compressedTable.keys():
                compressedTable[tuples] = tempTable.count(tuples)

        return compressedTable

    # Creates the star table in from countValues and minSup. If count for value in countValues is less than minSup
    # add value to starTable.  StarTable is filled with tuples (partitioned by dimension) of values less than minSup.
    def createStarTable(self, countValues, minSup):
        starTable = []

        for dimension in countValues:
            tempList = []
            
            for value in dimension:
                if dimension.get(value) < minSup:
                    tempList.append(value)
            
            starTable.append(tuple(tempList))
        
        return starTable

    def createStarTree(self, compressedTable):

        countList = compressedTable.values()
        rootCount = 0

        for value in countList:
            rootCount += value 

        root = Node('root', rootCount)

        starTree = Tree(root)
        dim = 0

        while dim < len(compressedTable[0]):
            for tuple in compressedTable:
                count = compressedTable.get(tuple)
                starTree.addBranch(root, tuple, count)

        starTree.addSiblings(starTree.root.descendents)

        return starTree
    
        
data = processData('../data/data.txt')
sc = starCube(data, 3, 1)
