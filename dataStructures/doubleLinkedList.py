#Double linked list


class Node():
    
    def __init__(self, content) -> None:
        
        self._content = content
        
        self._next = None
        self._prev = None
    
    
    def putNext(self, node: 'Node') -> None:
        self._next = node
    
    def putPrev(self, node: 'Node') -> None:
        self._prev = node
    
    def hasNext(self) -> bool:
        return bool(self._next)
    
    def hasPrev(self) -> bool:
        return bool(self._prev)
    
    def getNext(self) -> 'Node':
        return self._next
    
    def getPrev(self) -> 'Node':
        return self._prev
    
    def changeContent(self, newContent) -> None:
        self._content = newContent
    
    def getContent(self) -> any:
        return self._content
    
    
    #Overriding python magic  methods
    
    def __str__(self) -> str:
        return f"Node(content: {repr(self._content)}, prev: {self._prev}, next: {self._next})"
    
    def __format__(self, format_spec: str) -> str:
        if format_spec == "content":
            return f"{repr(self._content)}"
        elif format_spec == "next":
            if self._next:
                return f"{self._next:content}"
            else:
                return f"{self._next}"
        elif format_spec == "prev":
            if self._prev:
                return f"{self._prev:content}"
            else:
                return f"{self._prev}"
        else: 
            return f"Node(content: {self:content}, prev: {self:prev}, next: {self:next})"
    
    def __repr__(self) -> str:
        return f"Node({repr(self._content)})"


class DoubleLinkedList():
    
    def __init__(self, initial_elements = None, elementClass = None):
        
        self._length = 0
        
        self._firstElement = None
        self._lastElement = None
        
        self._current = None
    
    
    def insertFirst(self, element) -> None:
        newElement = Node(element)
        
        if self._length == 0:
            self._lastElement = newElement
            
        if self._firstElement:
            self._firstElement.putPrev(newElement)
        
        newElement.putNext(self._firstElement)
        self._firstElement = newElement
        
        self._length += 1
    
    def insertLast(self, element) -> None:
        newElement = Node(element)
        
        if self._length == 0:
            self._firstElement = newElement
        
        newElement.putPrev(self._lastElement)
        
        if self._lastElement:
            self._lastElement.putNext(newElement)
        
        self._lastElement = newElement
        
        self._length += 1
    
    def insertElement(self, pos: int, element) -> None:
        
        assert(isinstance(pos, int)), f"pos must be an integer but got {repr(pos)} of class {pos.__class__}"
        
        if (pos < 0 or pos > self._length):
            raise IndexError("Position out of bounds")
        
        if pos == 0:
            self.insertFirst(element)
        elif pos == self._length:
            self.insertLast(element)
        else:
            half = self._length//2
            newElement = Node(element)
            if pos > half:
                nextElement = self._getElement(pos, half)
                prevElement = nextElement.getPrev()
                
                newElement.putNext(nextElement)
                newElement.putPrev(prevElement)
                
                nextElement.putPrev(newElement)
                prevElement.putNext(newElement)
                
                pass
            else:
                prevElement = self._getElement(pos-1, half)
                nextElement = prevElement.getNext()
                
                newElement.putNext(nextElement)
                newElement.putPrev(prevElement)
                
                nextElement.putPrev(newElement)
                prevElement.putNext(newElement)
                pass
    
    def isEmpty(self) -> bool:
        return not bool(self._length)
    
    def size(self) -> int:
        return self._length
    
    
    #private methods:
    
    def _getElement(self, pos: int, half: int = None) -> Node|None:
        
        if self.isEmpty():
            raise IndexError("List is emtpy")
        assert(isinstance(pos, int)), f"pos must be an integer, but got '{repr(pos)}' of class {pos.__class__}"
        if (pos < 0 or pos >= self._length):
            raise IndexError("Position out of bounds")
        
        if pos == 0:
            return self._firstElement
        elif pos == self._length - 1:
            return self._lastElement
        else:
            if half is not None:
                assert(isinstance(half, int) and not isinstance(half, bool)), f"half must be an integer, but got '{repr(half)}' of class {half.__class__}"
                
                if pos >= half:
                    index = self._length - 1
                    current_Node = self._lastElement
                    while (index != pos):
                        index -= 1
                        current_Node = current_Node.getPrev()
                    return current_Node
                else:
                    index = 0
                    current_Node = self._firstElement
                    while (index != pos):
                        index += 1
                        current_Node = current_Node.getNext()
                    return current_Node
            else:
                index = 0
                current_Node = self._firstElement
                while (index != pos):
                    index += 1
                    current_Node = current_Node.getNext()
                return current_Node
    
    #Overriding python native methods
    
    def __len__(self) -> int:
        return self.size()
    
    def __iter__(self):
        self._current = self._firstElement
        return self
    
    def __next__(self) -> Node:
        if self._current is None:
            raise StopIteration
        else:
            node = self._current
            self._current = self._current.getNext()
            return node
    
    def __str__(self) -> str:
        elements = ', '.join(repr(node) for node in self)
        return f"[{elements}]"



if __name__ == "__main__":
    
    myList = DoubleLinkedList()
    
    for i in range(3):
        myList.insertLast(i)
        
    
    print(myList)
    
    myList.insertElement(4, "test")
    
    
    print(myList)
    
    print("debug")
    
    for node in myList:
        print(node)
    