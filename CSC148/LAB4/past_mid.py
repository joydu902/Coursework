"""
Provided is a LinkedList and LinkedListNode class.

Implement the LinkedList method 'swap_front_back'.
"""

from typing import Union, Any

class LinkedListNode:
    """
    A Node to be used in a LinkedList.

    next_ - The successor to this LinkedListNode
    value - The data represented by this LinkedListNode.
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None] = None) -> None:
        """
        Initialize this LinkedListNode with the value value and successor next.

        >>> LinkedListNode(3).value
        3
        >>> LinkedListNode(3).next_ == None
        True
        """
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedListNode.

        >>> print(LinkedListNode(3))
        3 ->
        """
        return "{} -> ".format(self.value)


class LinkedList:
    """
    Collection of LinkedListNodes.

    front - first node of this LinkedList
    back - last node of this LinkedList
    size - the number of nodes in this LinkedList (>= 0)
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Initialize an empty LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.size
        0
        """
        self.front = None
        self.back = None
        self.size = 0

    def prepend(self, value: Any) -> None:
        """
        Insert value to the start of this LinkedList (before self.front).

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        self.front = LinkedListNode(value, self.front)
        if self.back is None:
            self.back = self.front
        self.size += 1

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        cur_node = self.front
        result = ''
        while cur_node is not None:
            result += str(cur_node)
            cur_node = cur_node.next_
        return result + '|'

    def append(self, value):
        """
        Insert a new LinkedListNode with value after self.back.

        @param LinkedList self: this LinkedList.
        @param object value: value of new LinkedListNode
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk)
        5 -> |
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk)
        5 -> 6 -> |
        """
        new_node = LinkedListNode(value)
        if self.size == 0:
            self.back = new_node
        else:
            self.back.next_ = new_node
            self.back = new_node
        self.size += 1



        # new_node = LinkedListNode(value)
        # if self.front is None:
        #     # append to an empty LinkedList
        #     self.front = self.back = new_node
        # else:
        #     # self.back better not be None
        #     assert self.back, 'Unexpected None node'
        #     self.back.next_ = new_node
        #     self.back = new_node
        # self.size += 1

    def remove_first_double(self):
        """
        Remove second of two adjacent nodes with duplicate values.
        If there is no such node, leave self as is. No need
        to deal with subsequent adjacent duplicate values.
        @param LinkedList self: this linked list
        @rtype: None
        >>> list_ = LinkedList()
        >>> list_.append(3)
        >>> list_.append(2)
        >>> list_.append(2)
        >>> list_.append(3)
        >>> list_.append(3)
        >>> print(list_)
        3 -> 2 -> 2 -> 3 -> 3 -> |
        >>> list_.remove_first_double()
        >>> print(list_)
        3 -> 2 -> 3 -> 3 -> |
        >>> list_.remove_first_double()
        >>> print(list_)
        3 -> 2 -> 3 -> |
        """
        current_node = self.front
        prev_node = None
        if self.size < 2:
            return
        else:
            while current_node is not None and current_node.value!= current_node.next_.value:
                prev_node = current_node
                current_node = current_node.next_
            if current_node.next_ is not None:
                prev_node.next_ = current_node.next_
            else:
                self.back = current_node
            self.size -= 1



        # if self.size < 2:
        #     # no room for doubles
        #     return None
        # else:
        #     current_node = self.front
        #     while current_node.next_ and current_node.value != current_node.next_.value:
        #         current_node = current_node.next_
        #
        #     if current_node.next_:
        #         current_node.next_ = current_node.next_.next_
        #         if not current_node.next_:
        #             self.back = current_node
        #         self.size -= 1

    def remove_first_satisfier(self, predicate):
        """
        Remove first node whose value satisfies (returns True for)
        predicate. If there is no such node, leave self as is.
        @param LinkedList self: this linked list
        @param (object)->bool predicate: boolean function
        @rtype: None
        >>> list_ = LinkedList()
        >>> list_.append(5)
        >>> list_.append(3)
        >>> print(list_)
        5 -> 3 -> |
        >>> def f(n): return n > 4
        >>> list_.remove_first_satisfier(f)
        >>> print(list_)
        3 -> |
        >>> list_.append(5)
        >>> list_.append(7)
        >>> list_.remove_first_satisfier(f)
        >>> print(list_)
        3 -> 7 -> |
        """
#

        previous_node, current_node = None, self.front
        while current_node and not predicate(current_node.value):
            previous_node = current_node
            current_node = current_node.next_
        if current_node:
            # current_node.value satisfies predicate
            if not previous_node:
                # current_node was front
                self.front = current_node.next_
            else:
                # previous_node is a LinkedListNode
                previous_node.next_ = current_node.next_
            if self.back is current_node:
                self.back = previous_node
            self.size -= 1
        else:
            pass


def absorb_value(lnk, value):
    """
    @type lnk: LinkedList
    @type value: int

    >>> lnk = LinkedList()
    >>> lnk.append(6)
    >>> lnk.append(7)
    >>> lnk.append(8)
    >>> lnk.append(7)
    >>> print(lnk)
    6 -> 7 -> 8 -> 7 -> |
    >>> absorb_value(lnk, 7)
    >>> print(lnk)
    6 -> 15 -> 7 -> |
    """
    if lnk.front:
        prev_node, cur_node = None, lnk.front
        while cur_node and not cur_node.value == value:
            prev_node = cur_node
            cur_node = cur_node.next_
        if cur_node and cur_node.next_:
            cur_node.next_.value += value
            if prev_node:
                prev_node.next_ = cur_node.next_
            else:
                lnk.front = cur_node.next_
            lnk.size -= 1
        else:
            pass


def split_back(lnk):
    """
    @type lnk: LinkedList

    >>> lnk = LinkedList()
    >>> lnk.append(7)
    >>> split_back(lnk)
    >>> print(lnk)
    3 -> 4 -> |
    >>> split_back(lnk)
    >>> print(lnk)
    3 -> 2 -> 2 -> |
    >>> split_back(lnk)
    >>> print(lnk)
    3 -> 2 -> 1 -> 1 -> |
    """
    if lnk.front:
        prev_node, cur_node = None, lnk.front
        while cur_node.next_:
            prev_node = cur_node
            cur_node = cur_node.next_
        new_node = LinkedListNode(cur_node.value // 2, cur_node)
        cur_node.value -= cur_node.value // 2
        if not prev_node:
            lnk.front = new_node
        else:
            prev_node.next_ = new_node
        lnk.size += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()