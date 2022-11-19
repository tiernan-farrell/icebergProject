
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
        self.data = data
        self.numDims = numDims
        self.minSup = minSup
        self.compressedTable = self.compressTable(self.data)
        self.starReduce = []
        self.starTree = None
        self.starCube = None
        # Allocate kdn nodes into a buffer
        
    def compressTable(self, data):
        star_table = []
        for dim in data: 
            dim_list = []
            # {'1': 1, '0': 4}
            for val in dim: 
                # {'1': 1}
                if dim[val] < self.minSup:
                    dim_list.append(val)
            star_table.append(dim_list)
            
        return star_table
    
        
data = processData('../data/data.txt')
sc = starCube(data, 3, 1)
