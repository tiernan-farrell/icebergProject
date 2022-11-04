import csv
import os

def parseInput(filename):
    here = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(here, filename)
    file = open(filePath, newline='')

    valueCounts = []
    referenceTable = []

    csvreader = csv.reader(file)

    for x in csvreader:
        if '?' in x:
            continue
        referenceTable.append(x)
        for y in range(len(x)):
            if len(valueCounts) == len(x):
                if x[y] in valueCounts[y]:
                    valueCounts[y][x[y]] += 1
                else:
                    valueCounts[y][x[y]] = 1
            else:
                valueCounts.append({x[y]: 1})

    return valueCounts,referenceTable

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

class starCube:

    def __init__(self, fileName, minSup):
        self.fileName = fileName
        self.minSup = minSup

    def getResults(self):
        count_table, referenceTable = parseInput(self.fileName)

        starReduce = StarReduction(self.minSup, referenceTable, count_table)

        starReduce.createStarTable()
        starTree = starReduce.createStarTree()

        starCube = starCubing(starTree, starTree, self.minSup)

        return starCube