#!/usr/bin/python3
"""Class for single linked list"""


class Node:
    """Init contructor"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class Represent Singly Linked list"""

    def __init__(self):
        """Initialize SLL"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a value in sorted order"""
        newNode = Node(value)
        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            newNode.next_node = temp.next_node
            temp.next_node = newNode

    def __str__(self):
        """Define the print() representation of SinglyLinkedList"""
        array_of_vals = []
        temp = self.__head
        while temp is not None:
            array_of_vals.append(str(temp.data))
            temp = temp.next_node

        return ('\n'.join(array_of_vals))
