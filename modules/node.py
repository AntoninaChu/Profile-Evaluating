class Node(object):
    '''This class creates a node to hold data and a link to next node.'''

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

    def __str__(self):
        '''This function returns a string with data from node.'''
        return str(self.data)
