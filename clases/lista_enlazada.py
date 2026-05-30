from __future__ import annotations
class Node:
    def __init__(self, data: any, next: 'Node' | None):
        self.__data = data
        self.__next = next
    
    def get_data(self):
        return self.__data
    
    def set_data(self, newData):
        self.__data = newData
    
    def get_next(self):
        return self.__next
    
    def set_next(self, newNext):
        if type(newNext) is Node:
            self.__next = newNext
        else:
            self.__next = None
    
    def __str__(self):
        return f"Node carrying({self.get_data()}) followed by ({hex(id(self.get_next()))})"

    def __repr__(self):
        return f"Object Node(data: {self.get_data()}, next: {self.get_next()})"

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0
    
    def __str__(self):
        if self.get_head() == None: return "[]"
        current = self.get_head()
        product = []
        while current != None:
            next = current.get_next()
            product.append(current.get_data())
            current = next
        return str(product)

    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def get_length(self):
        return self.__length
        
    def add(self, data):
        tail = self.get_tail()
        if data is None:
            return False
            
        elif tail:
            self.add_last(data)
            return True

        elif not tail:
            new = Node(data, None)
            self.__head, self.__tail = new, new
            self.__length += 1
            return True
    
    def add_last(self, data):
        last = self.get_tail()
        node_to_add = Node(data, None)
        last.set_next(node_to_add)
        self.__length += 1
        self.__tail = node_to_add
        return node_to_add
    
    def remove(self, data):
        current = self.get_head()
        last = None
        target = data
        if data == None: return
        while current:
            if current.get_data() == target:
                if last == None:
                    if current.get_next() == None:
                        self.__head = None
                        self.__tail = None
                        self.__length -= 1
                        return current
                    elif current.get_next():
                        self.__head = current.get_next()
                        self.__length -= 1
                        return current
                elif last:
                    if current.get_next() == None:
                        last.set_next(None)
                        self.__tail = last
                        self.__length -= 1
                        return current
                    elif current.get_next():
                        last.set_next(current.get_next())
                        self.__length -= 1
                        return current
            elif current.get_data() != data:
                last = current
                current = current.get_next()
    
    def search(self, data):
        if self.get_head():
            current = self.get_head()
            counter = 0
            while current.get_data() != data:
                next = current.get_next()
                if next != None:
                    current = next
                    counter += 1
                else: return False
            if current.get_data() == data:
                return counter
    
    def wipe(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def get_index(self, index: int):
        counter = 0
        current = self.get_head()
        while current:
            if counter == index: return current.get_data()
            current = current.get_next()
            counter += 1
        return None