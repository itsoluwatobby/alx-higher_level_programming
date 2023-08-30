#!/usr/bin/python3

"""Definition of a Square class"""


class Node:
    """Represents a square"""

    def __init__(self, data, next_node=None):
        """Initialize an instance of a square.

        Args:
            size (int): The size of the new square.
            next_node (Node) - pointer to the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data stored in the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data value"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a square"""

    def __init__(self):
        """Initialize an instance of singlyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted at the position in an 
        ordered manner.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
