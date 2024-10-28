
RED = 1
BLACK = 0

TRADUCTOR = {
    RED: "R",
    BLACK: "B"
}


def defaultCmp(a,b):
    if a > b:
        return -1
    if a == b:
        return 0
    if a < b:
        return 1


class RBT():

    def __init__(self, cmpFunction = defaultCmp):
        self._root = None
        self._cmpFunction = cmpFunction


    ## PUBLIC FUNCTIONS
    def insert(self, key, value):
        newNode = RBTNode(key, value)
        if self._root is None:
            newNode.setBlack()
            self._root = newNode
        else:
            self._insertNode(self._root, newNode)
            self._root = self._root._balanceCase1()
            self._root = self._root._balanceCase2()
            self._root = self._root._balanceCase3()
            self._root.updateSize()
        
        self._root.setBlack()


    def remove(self, key):
        try:
            pass
        except KeyError:
            pass
    
    def get(self,key):
        try:
            node = self._getNode(self._root, key)
            return node.getKey(), node.getValue()
        except KeyError as e:
            return None
    
    def keySet(self):
        return self._root.getInorder(selector = lambda x: x.getKey())
    
    def valueSet(self):
        return self._root.getInorder(selector = lambda x: x.getValue())
    
    def keys(self, keyLow, keyHigh):

        def tempFunction(node):
            cmpLow = self._cmpFunction(node.getKey(), keyLow)
            cmpHigh = self._cmpFunction(node.getKey(), keyHigh)
            return cmpLow != 1 and cmpHigh != -1
        
        return self._root.getInorder(selector = lambda x: x.getKey(), crit = lambda x: tempFunction(x))
    
    def values(self, keyLow, keyHigh):

        def tempFunction(node):
            cmpLow = self._cmpFunction(node.getKey(), keyLow)
            cmpHigh = self._cmpFunction(node.getKey(), keyHigh)
            return cmpLow != 1 and cmpHigh != -1
        
        return self._root.getInorder(selector = lambda x: x.getValue(), crit = lambda x: tempFunction(x) )
    
    def rank(self, key):
        """
        Retorna el numero de llaves en el arbol estrictamente menores que key:
        """

        def tempFunction(node):
            return self._cmpFunction(node.getKey(), key)  == 1
        
        return len(self._root.getInorder(selector = lambda x: None, crit = lambda x: tempFunction(x)))

    def select(self, pos):
        """
        Retorna la k-esima pareja llave valor más pequeña del arbol
        """
        k = 0
        for i in self:
            if k == pos:
                return i
            k += 1
        raise IndexError("pos index out of range")



    def height(self):
        return self._root.getHeight()
    

    ##PRIVATE FUNCTIONS
    def _insertNode(self, root, newNode):

        cmp = self._cmpFunction(root.getKey(), newNode.getKey())
        if cmp == 0: #ELEMENTS ARE EQUAL
            root.setValue(newNode.getValue())
        elif cmp == -1: #NEWNODE IS LESS THAN ROOT
            if root.getLeftNode() is None:
                root.setLeftNode(newNode)
            else:
                self._insertNode(root.getLeftNode(), newNode)
        elif cmp == 1: #NEW NODE IS MORE THAN ROOT
            if root.getRightNode() is None:
                root.setRightNode(newNode)
            else:
                self._insertNode(root.getRightNode(), newNode)
        
        
        ##Balancing logic
        ##  FATHER OF THE NODE IS RESPONSIBLE OF BALANCING CHILDREN
        if root.getLeftNode():
            root.setLeftNode(root.getLeftNode()._balanceCase1())
            root.setLeftNode(root.getLeftNode()._balanceCase2())
            root.setLeftNode(root.getLeftNode()._balanceCase3())
            root.getLeftNode().updateSize()
        
        if root.getRightNode():
            root.setRightNode(root.getRightNode()._balanceCase1())
            root.setRightNode(root.getRightNode()._balanceCase2())
            root.setRightNode(root.getRightNode()._balanceCase3())
            root.getRightNode().updateSize()

        ##update Size
        root.updateSize()



    
    def _getNode(self, root, key):
        if root is None:
            raise KeyError(f"{key} not found on the RBT")

        cmp = self._cmpFunction(root.getKey(), key)
        if cmp == 0:
            return root
        elif cmp == -1:
            return self._getNode(root.getLeftNode(), key)
        elif cmp == 1:
            return self._getNode(root.getRightNode(), key)

    ## GETTERS

    def getSize(self):
        return self._root.getSize()




    ## MAGIC METHODS
    def __repr__(self) -> str:
        return f"RBT({repr(self._root)})"
    
    def __len__(self) -> str:
        return self.getSize()
    
    def __iter__(self):
        self.__nodeStack = self._root
        self._getInorderStack = []
        return self
    
    def __next__(self):
        try:
            while self.__nodeStack:
                self._getInorderStack.append(self.__nodeStack)
                self.__nodeStack = self.__nodeStack.getLeftNode()
            ret = self._getInorderStack.pop()
            self.__nodeStack = ret.getRightNode()
            return ret.getKey(), ret.getValue()
        except IndexError:
            raise StopIteration
    
    def __hash__(self):
        raise TypeError("unhashable type: 'RBT'")
    

            


        

class RBTNode():

    def __init__(self, key = None, value = None):

        hash(key)

        self._key = key
        self._value = value

        self._leftNode = None
        self._rightNode = None

        self._color = RED

        self._size = 1
    
    
    ## GETTERS
    def getLeftNode(self):
        return self._leftNode
    
    def getRightNode(self):
        return self._rightNode
    
    def getKey(self):
        return self._key

    def getValue(self):
        return self._value

    def getColor(self):
        return self._color
    
    def getSize(self):
        return self._size
    
    def getHeight(self):
        leftSide = 0
        rightSide = 0
        if self.getLeftNode():
            leftSide = self.getLeftNode().getHeight()
        if self.getRightNode():
            rightSide = self.getRightNode().getHeight()
        
        return max(leftSide, rightSide) + 1
    
    def getInorder(self, selector = lambda x: x, crit = lambda x: True):

        if not crit(self):
            return []
        
        leftSide = []
        rightSide = []
        if self.getLeftNode():
            leftSide = self.getLeftNode().getInorder(selector,crit)
        if self.getRightNode():
            rightSide = self.getRightNode().getInorder(selector,crit)
        
        return leftSide + [selector(self)] + rightSide


    ## SETTERS
    def setLeftNode(self, node):
        self._leftNode = node
    
    def setRightNode(self, node):
        self._rightNode = node

    def setKey(self, key):
        self._key = key
    
    def setValue(self, value):
        self._value = value
    
    def setBlack(self):
        self._color = BLACK

    def setRed(self):
        self._color = RED
    
    def setColor(self, color):
        self._color = color
    
    def flipColors(self):
        self._color = not self._color
    
    def setSize(self, size):
        self._size = size

    ## OTHER PUBLIC METHODS

    def isRed(self):
        return self._color == RED
    
    def updateSize(self):
        leftSize = 0
        rightSize = 0
        if self.getLeftNode():
            leftSize = self.getLeftNode().getSize()
        if self.getRightNode():
            rightSize = self.getRightNode().getSize()
        
        self._size = leftSize + rightSize + 1
    
    
    ## PRIVATE METHODS

    def _balanceCase1(self):
        if self.getRightNode() and self.getRightNode().isRed():
            if self.getLeftNode() is None or not self.getLeftNode().isRed():
                return self._rotateLeft()
        return self
    
    def _balanceCase2(self):
        if self.getLeftNode() and self.getLeftNode().isRed():
            if self.getLeftNode().getLeftNode() and self.getLeftNode().getLeftNode().isRed():
                return self._rotateRight()
        return self

    def _balanceCase3(self):
        if self.getLeftNode() and self.getRightNode():
            if self.getLeftNode().isRed() and self.getRightNode().isRed():
                self.getLeftNode().flipColors()
                self.getRightNode().flipColors()
                self.flipColors()
        return self
    

    def _rotateLeft(self):
        newRoot = self.getRightNode()
        self.setRightNode(newRoot.getLeftNode())
        newRoot.setLeftNode(self)

        newRoot.setColor(self.getColor())
        self.setRed()

        newRoot.setSize(self.getSize())

        self.updateSize()

        return newRoot
    
    def _rotateRight(self):
        newRoot = self.getLeftNode()
        self.setLeftNode(newRoot.getRightNode())
        newRoot.setRightNode(left)

        newRoot.setColor(self.getColor())
        self.setRed()

        newRoot.setSize(self.getSize())

        self.updateSize()

        return newRoot
    
            
        

        

    


    ## MAGIC METHODS
    def __str__(self) -> str:
        return f"RBTNode(key:{self._key},\tvalue: {self._value})"
    
    def __repr__(self) -> str:
        return f"RBTNode[{TRADUCTOR[self._color]}](key: {self._key}, left:({repr(self._leftNode)}) right:({repr(self._rightNode)}))"
    
    def __hash__(self):
        raise TypeError("unhashable type: 'RBTNode'")



if __name__ == "__main__":

    newTree = RBT()

    for i in [10,15,18,25,28,38,40,50]:
        newTree.insert(i,i*2)
    
    print(repr(newTree))

    print(len(newTree))

    for k,v in newTree:
        print(k,v)
    
    print(newTree.keySet())
    print(newTree.valueSet())

    print(newTree.keys(1,3))
    print(newTree.values(1,3))

    print(newTree.height())

    print(newTree.rank(28), "rank")

    print(newTree.select(3))

    #print(newTree.get(0))
    #print(newTree.get(-1))
    #print(newTree.getSize())