"""
Trisha Lapiz tlap632 
This is a linked list iterator program
"""
class LinkedListIterator:
    def __init__(self, node):
        self.__curr = node.get_next() #getting a node from the linked list
    
    def __next__(self):
        if self.__curr.get_data() == None: #if the list is empty or the end of the linked list has been reached
            raise StopIteration
        else: #traverse to get the next node
            item = self.__curr.get_data()
            self.__curr = self.__curr.get_next()
            return item

            
    

