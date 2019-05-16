from node import Node

class LinkedList:
    '''This class presents a linked list to hold information'''

    def __init__(self):
        '''This function creates an empty linked list.'''
        self._head = None
        self._size = 0
        self._tail = self._head

    def add_data(self, data):
        '''This function adds new node to linked list.'''
        if not isinstance(data, Node):
            data = Node(data)
        if self._head != None:
            self._tail.next = data
            self._tail = self._tail.next
        else:
            self._head = data
            self._tail = self._head
        self._size += 1

    def __len__(self):
        '''This function retuns a lenght of linked list.'''
        return self._size
