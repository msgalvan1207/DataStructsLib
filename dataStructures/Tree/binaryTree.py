#Binary Tree

import types

class Node():

    def __init__(self, key, content):

        self._key = key

        self._content = content

        self._leftNode = None
        self._rightNode = None
    
    def assignLeftNode(self, leftNode):
        # Should assert that leftNode is a Node
        self._leftNode = leftNode
    
    def assignRightNode(self, rightNode):
        # Should assert that leftNode is a Node
        self._rightNode = rightNode
    
    def getLeftNode(self):
        return self._leftNode
    
    def getRightNode(self):
        return self._rightNode
    
    def getContent(self):
        return self._content
    
    def getKey(self):
        return self._key


class BinaryTree():

    def __init__(self, cmpFunction:types.FunctionType = None):
        assert isinstance(cmpFunction, types.FunctionType), f"cmpFunction expected a function class object got {type(cmpFunction)} instead"



if __name__ == '__main__':

    algo = BinaryTree(cmpFunction=10)



