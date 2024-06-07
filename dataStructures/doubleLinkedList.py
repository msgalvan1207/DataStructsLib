#Double linked list


class DoubleLinkedList():
    
    def __init__(self, initial_elements = None, elementClass = None):
        
        self._length = 0
        
        self._firstElement = None
        self._lastElement = None
        
        self._current = None
    
    
    def insertFirst(self, element):
        newElement = Node(element)
        
        if self._length == 0:
            self._lastElement = newElement
            
        if self._firstElement:
            self._firstElement.putPrev(newElement)
        
        newElement.putNext(self._firstElement)
        self._firstElement = newElement
        
        self._length += 1
    
    def insertLast(self, element):
        newElement = Node(element)
        
        if self._length == 0:
            self._firstElement = newElement
        
        newElement.putPrev(self._lastElement)
        
        if self._lastElement:
            self._lastElement.putNext(newElement)
        
        self._lastElement = newElement
        
        self._length += 1
    
    
    #Overriding python native methods
    
    def __iter__(self):
        self._current = self._firstElement
        return self
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            node = self._current
            self._current = self._current.getNext()
            return node


class Node():
    
    def __init__(self, content) -> None:
        
        self._content = content
        
        self._next = None
        self._prev = None
    
    
    def putNext(self, node: 'Node'):
        self._next = node
    
    def putPrev(self, node: 'Node'):
        self._prev = node
    
    def hasNext(self) -> bool:
        return bool(self._next)
    
    def hasPrev(self) -> bool:
        return bool(self._prev)
    
    def getNext(self):
        return self._next
    
    def getPrev(self):
        return self._prev
    
    def changeContent(self, newContent):
        self._content = newContent
    
    
    #Overriding python magic  methods
    
    def __str__(self):
        return f"Node(content: {self._content}, prev: {self._prev}, next: {self._next})"
    
    def __format__(self, format_spec: str) -> str:
        if format_spec == "content":
            return f"{self._content}"
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
            return f"Node(content: {self._content}, prev: {self:prev}, next: {self:next})"



if __name__ == "__main__":
    
    myList = DoubleLinkedList()
    
    for i in range (4):
        myList.insertLast(i)
    
    for node in myList:
        print(node)
    
    print("debug")
    
    print(myList._firstElement)
    print(myList._lastElement)
    
    print(myList._length)