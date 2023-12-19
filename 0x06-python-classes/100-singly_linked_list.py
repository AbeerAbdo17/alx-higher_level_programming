#!/usr/bin/python3

"""define class"""


class Node:
    """class scop"""
    def __init__(self, data, next_node=None):
        """method scop"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """method scop"""
        return self.__data

    @data.setter
    def data(self, value):
        """method scop"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """method scop"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """method scop"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class scop"""
    def __init__(self):
        """method scop"""
        self.__head = None

    def sorted_insert(self, value):
        """method scop"""
        nw = Node(value)
        if self.__head is None:
            nw.next_node = self.__head
            self.__head = nw
        else:
            curr = self.__head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            nw.next_node = curr.next_node
            curr.next_node = nw

    def __str__(self):
        """method scop"""
        res = []
        curr = self.__head
        while curr is not None:
            res.append(str(curr.data))
            curr = curr.next_node
        return ('\n'.join(res))
