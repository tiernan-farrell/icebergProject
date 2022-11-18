def parseInput(list):
    
    valueCounts = []
    referenceTable = []
    tabelIndex = 0

    for x in list:
        countsIndex = 0
        referenceTable.append([])

        for y in x:
            referenceTable[tabelIndex].append(str(y))

            if len(valueCounts) < len(x):
                valueCounts.append({})
                valueCounts[countsIndex][str(y)] = 1
            elif str(y) in valueCounts[countsIndex]:
                hold = valueCounts[countsIndex][str(y)]
                valueCounts[countsIndex][str(y)] = hold + 1
            else:
                valueCounts[countsIndex][str(y)] = 1

            countsIndex += 1
        
        tabelIndex += 1
        
    return valueCounts, referenceTable

def starCubing(starTree,cur_node,min_sup):
    tree = None
    if cur_node.nValue >= min_sup:
        if not cur_node.checkIsRoot():
            # print(cur_node.nValue)
            pass
        if cur_node.checkIsLeaf():
            # print(cur_node.nValue)
            pass
        else:
            tree = CuboidTree(cur_node.nValue, cur_node.nName+'_tree')
            starTree.addANode(tree)

    if not cur_node.checkIsLeaf():
        starCubing(starTree, cur_node.getFirstNode(), min_sup)
    if tree is not None:
        starCubing(tree, tree, min_sup)
        starTree.deleteNode(tree)
    siblings = cur_node.getSiblings()
    if siblings is not None:
        if cur_node in siblings:
            siblings.remove(cur_node)
        for sibling in siblings:
            starCubing(starTree, sibling, min_sup)

    return starTree

class CuboidTree(object):

    def __init__(self, nValue, nName='root', nChildren=None):
        self.nName = nName
        self.nValue = nValue
        self.nParent = None
        self.nChildren = []
        if nChildren is not None:
            for child in nChildren:
                self.addANode(child)

    def getFirstNode(self):
        assert len(self.nChildren) > 0
        return self.nChildren[0]

    def checkIsLeaf(self):
        return len(self.nChildren) == 0

    def checkIsRoot(self):
        return self.nName == 'root'

    def addANode(self, node):
        assert isinstance(node, CuboidTree)
        node.nParent = self
        self.nChildren.append(node)

    def retrieveNode(self,node):
        for child in self.nChildren:
            if child.nName == node:
                return child
        return None

    def depthCheck(self):
        temp = self
        depthCount = 0
        while len(temp.nChildren) > 0:
            temp = temp.getFirstNode()
            depthCount += 1
        return depthCount

    def updateNode(self, node, count):
        for child in self.nChildren:
            if child.nName == node:
                child.nValue += count
                return child
        child = CuboidTree(count,node)
        child.nParent = self
        self.nChildren.append(child)
        return child

    def getSiblings(self):
        if self.nParent is not None:
            siblings = self.nParent.nChildren
            return siblings
        return None

    def deleteNode(self, node):
        if node in self.nChildren:
            self.nChildren.remove(node)

class StarReduction(object):

    def __init__(self, min_sup, referenceTable, count_table):
        self.min_sup = min_sup
        self.referenceTable = referenceTable
        self.count_table = count_table
        self.starTable = []

    def createStarTable(self):
        base_table = self.referenceTable[:]
        dictionary = {}
        for x in base_table:
            self.x_len = len(x)
            for y in range(len(x)):
                if self.count_table[y][x[y]] < self.min_sup:
                    self.updateStarTable(y, x[y])
                    x[y] = '*'
        self.base_table = base_table
        for x in base_table:
            tx = tuple(x)
            if tx in dictionary:
                dictionary[tx] += 1
            else:
                dictionary[tx] = 1
        self.compressed_table = dictionary
        return dictionary

    def updateStarTable(self, y, nValue):
        if y < len(self.starTable):
            self.starTable[y][nValue] = '*'
        else:
            temp = y - len(self.starTable) + 1
            while temp > 0:
                self.starTable.append(dict())
                temp -= 1
            self.starTable[y][nValue] = '*'

    def createStarTree(self):
        root_value = sum(self.compressed_table.values())
        starTree = CuboidTree(root_value)
        for x,nValue in self.compressed_table.items():
            subTree = starTree
            for node in x:
                subTree = subTree.updateNode(node, nValue)

        self.star_tree =  starTree
        return starTree

    def createCuboidTree(self):
        root_value = 0
        cuboidTree = CuboidTree(root_value)

        for x in self.referenceTable:
            subTree = cuboidTree
            for node in x:
                subTree = subTree.updateNode(node,0)
                
def createReadableList(starReduce):
    
    starCube = []
    starCubeList = []

    for node in starReduce.compressed_table:
        starCube.append(str(node) + ': ' + str(starReduce.compressed_table.get(node)))
    
    j = 0
    for line in starCube:
        i = 0
        unit = ''
        starCubeList.append([])

        while i < len(line):
            
            if line[i] == '*':
                unit = '*'
            elif (ord(line[i]) > 47 and ord(line[i]) < 58) or (ord(line[i]) > 64 and ord(line[i]) < 91) or (ord(line[i]) > 96 and ord(line[i]) < 123):
                unit += line[i]
            if line[i] == ')' or line[i] == ',' or i == len(line)-1:
                try:
                    starCubeList[j].append(int(unit))

                except:
                    starCubeList[j].append(unit) 
                unit = ''
            i +=1
        j += 1

    return starCubeList
                
class starCube:

    def __init__(self, data, minSup):
        self.fileName = data
        self.minSup = minSup
        self.starReduce = []
        self.starTree = None
        self.starCube = None

    def generateCube(self):
        count_table, referenceTable = parseInput(self.data)

        starReduce = StarReduction(self.minSup, referenceTable, count_table)

        starReduce.createStarTable()
        self.starReduce = starReduce
        self.starTree = starReduce.createStarTree()

        self.starCube = starCubing(self.starTree, self.starTree, self.minSup)

    def getResults(self):

        return createReadableList(self.starReduce)
