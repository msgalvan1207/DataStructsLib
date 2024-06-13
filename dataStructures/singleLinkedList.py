#Single linked list

import copy

class Node():
    
    def __init__(self, content) -> None:
        
        self._content = content
        
        self._next = None
    
    def assignNext(self,node) -> None:
        self._next = node
    
    def hasNext(self) -> bool:
        return bool(self._next)
    
    #Get next could be changed to __next__ function to use it using next(Node)
    def getNext(self) -> 'Node'|None:
        return self._next
    
    def getContent(self) -> any:
        return self._content
    
    def changeContent(self, newContent) -> None:
        self._content = newContent
    
    
    #Overriding python functions
    def __str__(self) -> str:
        return f"Node(content: {self._content}, next: {self._next})"
    
    def __format__(self, format_spec: str) -> str:
        if format_spec == "content":
            return f"{self._content}"
        elif format_spec == "next":
            if self._next:
                return f"{self._next:content}"
            else:
                return f"{self._next}"
        else:
            return f"Node (content: {self._content}, next: {self._next})"
    
    def __repr__(self) -> str:
        return f'Node({repr(self._content)})'


class SingleLinkedList():
    
    def __init__(self, initial_elements = None, elementClass = None):
        """
            Funcion de inilización de una lista enlazada simple. La crea vacia si initial_elements es None
            parametros:
            initial_elements: un iterable que permite iniciar la creación de la lista. Todos los elementos de la lista deben ser del mismo tipo
            elementClass: una clase que representa que tipo de variables se pueden poner en la lista
                se incluye para que el comportamiento de esta madre sea similar a java y evitar problemas de comparación
                si no se pasa como parametro, se va a tomar como clase de elemento el elemento de lo primero que se meta.
                IMPORTANTE: si se quiere inicializar la lista anteriormente, elementClass tiene que ser None
        """
        
        self._length = 0
        
        self._firstElement = None
        self._lastElement = None
        
        self._elementClass = elementClass
        
        
        #self._current solo se utiliza para iterar sobre la lista
        self._current = None
        
        if initial_elements and '__iter__' in dir(initial_elements):
            assert(elementClass is None), f"initial_elements's elements class overrides elementClass parameter.\n Remove elementClass parameter to initialice list with initial_elements"
            for element in initial_elements:
                self.insertLast(element)
        
    
    
    
    #public methods for accesing the list content and functions
    
    def insertFirst(self,element) -> None:
        """inserta un elemento a la lista en la primera posición

        Args:
            element (_type_ debe ser ser igual a SingleLinkedList._elementClass): elemento que se va a insertar al principio de la lista
        """
        
        if self._elementClass is None:
            self._elementClass = element.__class__
        else: 
            assert(element.__class__ == self._elementClass) ,f"item must be of type {self._elementClass.__name__}, but got {element.__class__}"
        
        newElement = Node(element)
        
        if self._firstElement:
            newElement.assignNext(self._firstElement)
            self._firstElement = newElement
        else:
            self._firstElement = newElement
        
        if self._lastElement is None:
            self._lastElement = newElement
        
        self._length += 1
    
    def insertLast(self, element) -> None:
        """Inserta un elemento al final de la lista

        Args:
            element (_type_ debe ser igual a SingleLinkedList._elementClass): elemento que se va a insertar al final de la lista
        """
        
        if self._elementClass is None:
            self._elementClass = element.__class__
        else:
            assert(element.__class__ == self._elementClass) ,f"item {repr(element)} must be {self._elementClass}, but got {element.__class__}"
        
        
        newElement = Node(element)
        
        if self._lastElement:
            self._lastElement.assignNext(newElement)
            self._lastElement = newElement
        else:
            self._lastElement = newElement
        
        if self._firstElement is None:
            self._firstElement = newElement
        
        self._length += 1
    
    def insertElement(self, pos: int, element) -> None:
        """Inserta un elemento en una posición dada

        Args:
            pos (int): posición en la que se va a insertar el elemento. Debe ser un número entero positivo y usa indexing en 0
            element (_type_ debe ser igual a SingleLinkedList._elementClass): elemento que se va a insertar en la lista

        Raises:
            IndexError: se lanza si la posición es menor a 0 o mayor a la longitud de la lista
        """
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        if (pos < 0 or pos > self._length):
            raise IndexError("Position out of bounds")
        if self._elementClass is None:
            self._elementClass = element.__class__
        else:
            assert(element.__class__ == self._elementClass) ,f"item must be of type {self._elementClass}, but got {element.__class__}"
        
        if pos == 0:
            self.insertFirst(element)
        elif pos == self._length:
            self.insertLast(element)
        else:
            newElement = Node(element)
            prevNode = self._getElement(pos-1)
            postNode = prevNode.getNext()
            prevNode.assignNext(newElement)
            newElement.assignNext(postNode)
            self._length += 1
    
    def isEmpty(self) -> bool:
        """función que indica si la lista está vacía

        Returns:
            bool: True si la lista está vacía, False en caso contrario
        """
        return not bool(self._length)
    
    def size(self) -> int:
        """Función que devuelve el tamaño de la lista

        Returns:
            int: tamaño de la lista
        """
        return self._length
    
    def firstElement(self) -> any:
        """Función que devuelve el primer elemento de la lista. Especificamente su contenido

        Returns:
            _type_: el contenido del primer elemento de la lista. Su tipo es igual a SingleLinkedList._elementClass
        """
        if self._firstElement:
            return self._firstElement.getContent()
        else:
            return None
    
    def lastElement(self) -> any:
        """Funcion que devuelve el último elemento de la lista. Especificamente su contenido

        Returns:
            _type_: el contenido del último elemento de la lista. Su tipo es igual a SingleLinkedList._elementClass
        """
        if self._lastElement:
            return self._lastElement.getContent()
        else:
            return None
    
    def getElement(self, pos: int) -> any:
        """función que devuelve el contenido de un elemento en una posición dada

        Args:
            pos (int): posición del elemento que se quiere obtener. Debe ser un número entero positivo y usa indexing en 0

        Returns:
            _type_: el contenido del elemento en la posición pos. Su tipo es igual a SingleLinkedList._elementClass
        """
        return self._getElement(pos).getContent()
    
    def deleteFirst(self) -> any:
        """Función que elimina el primer elemento de la lista y devuelve su contenido

        Raises:
            IndexError: se lanza si la lista está vacía

        Returns:
            _type_: el contenido del primer elemento de la lista. Su tipo es igual a SingleLinkedList._elementClass
        """
        if self.isEmpty():
            raise IndexError("List is emtpy")

        if self._firstElement is self._lastElement:
            firstElement = self._firstElement
            self._firstElement = None
            self._lastElement = None
            self._length -= 1
            return firstElement.getContent()

        if self._firstElement:
            firstElement = self._firstElement
            self._firstElement = self._firstElement.getNext()
            self._length -= 1
            return firstElement.getContent()
    
    def deleteLast(self) -> any:
        """Función que elimina el último elemento de la lista y devuelve su contenido

        Raises:
            IndexError: se lanza si la lista está vacía

        Returns:
            _type_: el contenido del último elemento de la lista. Su tipo es igual a SingleLinkedList._elementClass
        """
        if self.isEmpty():
            raise IndexError("List is Empty")
        if self._lastElement is self._firstElement:
            lastElement = self._lastElement
            self._firstElement = None
            self._lastElement = None
            self._length -= 1
            return lastElement.getContent()
        
        if self._lastElement:
            lastElement = self._lastElement
            self._lastElement = self._getElement(self._length-2)
            self._lastElement.assignNext(None) 
            self._length -= 1
            return lastElement.getContent()
    
    def deleteElement(self, pos: int) -> any:
        """Función que elimina un elemento en una posición dada y devuelve su contenido

        Args:
            pos (int): posición del elemento que se quiere eliminar. Debe ser un número entero positivo y usa indexing en 0

        Raises:
            IndexError: se lanza si la lista está vacía
            IndexError: se lanza si pos es menor a 0 o mayor a la longitud de la lista

        Returns:
            Node._element.__class__: el contenido del elemento en la posición pos. Su tipo es igual a SingleLinkedList._elementClass
        """
        if self.isEmpty():
            raise IndexError("List is emtpy")
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        if (pos < 0 or pos >= self._length):
            raise IndexError("Position out of bounds")
        
        if pos == 0:
            return self.deleteFirst()
        elif pos == self._length - 1:
            return self.deleteLast()
        else:
            index = 0
            prevElement = self._firstElement
            while (index != pos - 1):
                index += 1
                prevElement = prevElement.getNext()
            posElement = prevElement.getNext()
            postElement = posElement.getNext()
            prevElement.assignNext(postElement)
            self._length -= 1
            return posElement.getContent()
    
    def changeContent(self, pos: int, newContent) -> None:
        """Funcion que cambia el contenido de un elemento en una posición dada

        Args:
            pos (int): posición del elemento que se quiere cambiar. Debe ser un número entero positivo y usa indexing en 0
            newContent (_type_): nuevo contenido que se le va a asignar al elemento en la posición pos. Su tipo es igual a SingleLinkedList._elementClass
        """
        assert(newContent.__class__ == self._elementClass) ,f"item {repr(newContent)} must be {self._elementClass}, but got {newContent.__class__}"
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        self._getElement(pos).changeContent(newContent)
    
    def exchange(self, pos1: int, pos2: int) -> None:
        """Función que intercambia los contenidos de dos elementos en posiciones dadas

        Args:
            pos1 (int): posición del primer elemento que se va a intercambiar. Debe ser un número entero positivo y usa indexing en 0
            pos2 (int): posición del segundo elemento que se va a intercambiar. Debe ser un número entero positivo y usa indexing en 0
        """
        
        node1 = self._getElement(pos1)
        node2 = self._getElement(pos2)
        
        content1 = node1.getContent()
        content2 = node2.getContent()
        
        node1.changeContent(content2)
        node2.changeContent(content1)
    
    def subList(self, pos1: int, pos2: int) -> 'SingleLinkedList':
        """Función que devuelve una sublista de la lista original desde una posición pos1 hasta una posición pos2

        Args:
            pos1 (int): posición inicial de la sublista. Debe ser un número entero positivo y usa indexing en 0
            pos2 (int): posición final de la sublista. Debe ser un número entero positivo y usa indexing en 0

        Raises:
            IndexError: la lista está vacía
            IndexError: pos1 es menor a 0 o mayor a la longitud de la lista
            IndexError: pos2 es menor a 0 o mayor a la longitud de la lista
            IndexError: pos1 es mayor a pos2

        Returns:
            SingleLinkedList: sublista de la lista original desde pos1 hasta pos2
        """
        if self.isEmpty():
            raise IndexError("List is empty")
        if (pos1 < 0 or pos1 >= self._length):
            raise IndexError("Position out of bounds: pos1")
        if (pos2 < 0 or pos2 >= self._length):
            raise IndexError("Position out of bounds: pos2")
        if (pos1 > pos2):
            raise IndexError("pos1 must be less than pos2")
        newList = SingleLinkedList()
        currentNode = self._getElement(pos1)
        print(currentNode)
        newList.insertLast(currentNode.getContent())
        index = pos1
        
        while (index != pos2):
            index += 1
            currentNode = currentNode.getNext()
            newList.insertLast(currentNode.getContent())
        
        return newList
    
    def copy(self) -> 'SingleLinkedList':
        """Funcion que genera una copia profunda de la listas

        Returns:
            SingleLinkedList: copia profunda de la lista original
        """
        return copy.deepcopy(self)
    
    def concatenate(self, otherList: 'SingleLinkedList'):
        """Función que concatena la lista original con otra lista

        Args:
            otherList (SingleLinkedList): lista que se va a concatenar con la lista original
        """
        assert(otherList.__class__ == SingleLinkedList), f"parameter 'otherList' must be SingleLinkedList, but got {otherList.__class__}"
        for element in otherList:
            self.insertLast(element)
    
    def reverse(self) -> None:
        """Función que invierte el orden de los elementos de la lista original
        """
        if (self._length <= 1):
            pass
        else:
            prevElement = None
            currElement = self._firstElement
            self._lastElement = currElement
            while (currElement is not None):
                nextElement = currElement.getNext()
                currElement.assignNext(prevElement)
                prevElement = currElement
                currElement = nextElement
            self._firstElement = prevElement
    
    #private methods:
    def _getElement(self, pos: int) -> Node|None:
        """Funcion que devuelve un nodo en una posición dada

        Args:
            pos (int): posición del nodo que se quiere obtener. Debe ser un número entero positivo y usa indexing en 0

        Raises:
            IndexError: se lanza si la lista está vacía
            IndexError: se lanza si pos es menor a 0 o mayor a la longitud de la lista

        Returns:
            Node: nodo en la posición pos
        """
        if self.isEmpty():
            raise IndexError("List is empty")
        assert(isinstance(pos, int)), f"pos must be an integer, but got {repr(pos)} of class {pos.__class__}"
        if (pos < 0 or pos >= self._length):
            raise IndexError("Position out of bounds")
        
        if pos == 0:
            return self._firstElement
        elif pos == self._length - 1:
            return self._lastElement
        else:
            index = 0
            current_Node = self._firstElement
            while (index != pos):
                index += 1
                current_Node = current_Node.getNext()
            return current_Node
    
    
    
    #Over riding python native methods
    def __len__(self) -> int:
        return self.size()
    
    def __iter__(self):
        self._current = self._firstElement
        return self
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            node = self._current
            self._current = self._current.getNext()
            return node.getContent()
    
    def __str__(self) -> str:
        elements = ', '.join(repr(node) for node in self)
        return f"[{elements}]"
    
    def __repr__(self) -> str:
        if self._length != 0:
            elements = ', '.join(repr(node) for node in self)
            return f'SingleLinkedList(first element: {self._firstElement:content}, last element: {self._lastElement:content}, elements:[{elements}], size: {self._length})'
        else:
            return f'SingleLinkedList(first element: {None}, last element: {None}, elements:[ ], size: {self._length})'
    
    def __getitem__(self,key) -> any:
        return self.getElement(key)
    
    def __setitem__(self,key, value) -> None:
        self.insertElement(key, value)
    
    def __delitem__(self, key) -> None:
        self.deleteElement(key)
    
    def __reverse__(self) -> None:
        self.reverse()
    
    def __contains__(self, item) -> bool:
        for element in self:
            try:
                if item == element:
                    return True
            except:
                pass
        return False




if __name__ == "__main__":
    
    
    print(repr(SingleLinkedList()))
    
    algo = SingleLinkedList([1,2,3,4])
    otro = SingleLinkedList([6,7,8,9,10])
    
    algo.concatenate(otro)
    
    print(algo["pingu"])
    
    
    
    