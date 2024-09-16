#Array List



class ArrayList():
    
    def __init__(self, initial_elements = None, elementClass = None):
        
        self._length = 0
        
        self._elementClass = elementClass
        
        self._content: list = []
        
        if initial_elements and '__iter__' in dir(initial_elements):
            assert(elementClass is None), f"initial_elements's class overrides elementClass parameter. \n Remove elementClass parameter to initialize lsit with initial_elements"
            for element in initial_elements:
                self.insertLast(element)
    
    
    #public methods for accesing the list content and functions:
    
    def insertFirst(self, element: any) -> None:
        
        if self._elementClass is None:
            self._elementClass = element.__class__
        else:
            assert(element.__class == self._elementClass), f"item must be of type {self._elementClass.__name__}, but got {element.__class__}"
        
        self._content.insert(0, element)
    
    
    def insertLast(self, element: any) -> None:
        
        if self._elementClass is None:
            self._elementClass = element.__class__
        
        else:
            assert(element.__class == self._elementClass), f"item must be of type {self._elementClass.__name__}, but got {element.__class__}"
        
        self._content.append(element)
    
    
    def insertElement(self, pos: int, element: any) -> None:
        
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        if (pos < 0 or pos > self._length):
            raise IndexError("Position out of bounds")
        
        if self._elementClass is None:
            self._elementClass = element.__class__
        else:
            assert(element.__class__ == self._elementClass), f"item must be of type {self._elementClass}, but got {element.__class__}"
        
        self._content.insert(pos, element)
    
    def isEmpty(self) -> bool:
        
        return not self._content
    
    def size(self) -> int:
        
        return len(self._content)
    
    def firstElement(self) -> any:
        
        return self._content[0]
    
    def lastElement(self) -> any:
        
        return self._content[-1]
    
    def getElement(self, pos: int) -> any:
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        if (pos < 0 or pos >= self._length):
            raise IndexError("Position out of bounds")
        return self._content[pos]
    
    def deleteFirst(self) -> any:
        if self.isEmpty():
            raise IndexError("List is empty")
        
        return self._content.pop(0)
    
    def deleteLast(self) -> any:
        if self.isEmpty():
            raise IndexError("List is emtpy")
        
        return self._content.pop(-1)
    
    def deleteElement(self, pos: int) -> any:
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        if (pos < 0 or pos >= self._length):
            raise IndexError("Position out of bounds")
        
        return self._content.pop(pos)
    
    def changeContent(self, pos: int, newContent) -> None:
        
        assert(newContent.__class__ == self._elementClass) ,f"item {repr(newContent)} must be {self._elementClass}, but got {newContent.__class__}"
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        if (pos < 0 or pos >= self._length):
            raise IndexError("Position out of bounds")
        self._content[pos] = newContent
    
    
    def exchange(self, pos1: int, pos2: int) -> None:
        
        origin1 = self.getElement(pos1)
        origin2 = self.getElement(pos2)
        
        self.changeContent(pos1, origin2)
        self.changeContent(pos2, origin1)
    
    def subList(self, pos1: int, pos2: int) -> 'ArrayList':
        if self.isEmpty():
            raise IndexError("List is empty")
        if (pos1 < 0 or pos1 >= self._length):
            raise IndexError("Position out of bounds: pos1")
        if (pos2 < 0 or pos2 >= self._length):
            raise IndexError("Position out of bounds: pos2")
        if (pos1 > pos2):
            raise IndexError("pos1 must be less than pos2")
        
        return ArrayList(self._content[pos1:pos2])
    
    def concatenate(self, otherList: 'ArrayList') -> None:
        assert(otherList.__class__ == ArrayList), f"parameter 'otherList' must be SingleLinkedList, but got {otherList.__class__}"
        
        self._content = self._content + otherList._content
    
    def reverse(self) -> None:
        self._content.reverse()
    
    
    #Over riding python native methods
    
    def __len__(self) -> int:
        return self.size()
    
    def __iter__(self):
        return iter(self._content)
    
    def __str__(self) -> str:
        return f"{self._content}"
    
    def __repr__(self) -> str:
        return f'ArrayList(elements: {self._content}, size: {len(self)})'
    
    def __getitem__(self, key) -> any:
        return self._content[key]
    
    def __setitem__(self, key, value) -> None:
        self.insertElement(key, value)
    
    def __delitem__(self, key) -> None:
        self.deleteElement(key)
    
    def __reverse__(self) -> None:
        self.reverse()
    
    def __contains__(self, item) -> bool:
        for element in self:
            if item == element:
                return True
        return False