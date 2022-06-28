#!/usr/bin/python3
class Node:
    """The class for the node of a singly linked list

    Args:
        data: The data to be inputed into a singly linked list
    """
    def __init__(self, data, next_node=None):
        """ Initialiazing the class blueprint"""
        self.__data = data
        if type(data) != int:
            raise TypeError('data must be an integer')
        self.__next_node = next_node
        if type(self.__next_node) != Node and self.__next_node != None:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """ Method for retriving the private data attribute"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Method for resetting the private data attribute"""
        self.__data = value
        if type(data) != int:
            raise TypeError('data must be an integer')
    
    @property
    def next_node(self):
        """ Method for retriving the next_node private attribute"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Method for resetting the node of the singly linked list"""
        self.__next_node = value
        if type(self.__next_node) != Node and self.__next_node != None:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """ Class for the singly linked list

    Args:
        no args
    """
    def __init___(self):
        """ Initializing the singly linked list class"""
        self.__head = None

    def sorted_insert(self, value):
        """ Method for inserting a new node in the correct sorted position"""
        ptr = self.head()

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
    
    def __str__(self):
        """ Method for displaying basic information about a class"""
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    @property
    def head(self):
        """ Method for returning the value of the head """
        return (self.__head)

    @head.setter
    def head(self, value):
        """ Method for changing the value of the head"""
        self.__head = value
