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
                 next: Union["LinkedListNode", None] = None) -> None:
        """
        Initialize this LinkedListNode with the value value and successor next.

        >>> LinkedListNode(3).value
        3
        >>> LinkedListNode(3).next_ == None
        True
        """
        self.value = value
        self.next_ = next

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

    def find_second_last(self) -> LinkedListNode:
        """
        Return the node that points to the back of the LinkedList.

        Return None if there is no such node.

        >>> lnk = LinkedList()
        >>> lnk.find_second_last() == None
        True
        >>> lnk.prepend(3)
        >>> lnk.find_second_last() == None
        True
        >>> lnk.prepend(2)
        >>> lnk.find_second_last().value
        2
        >>> lnk.prepend(1)
        >>> lnk.find_second_last().value
        2
        """
        current_node = self.front
        prev_node = None
        while current_node.next_ is not None:
            prev_node = current_node
            current_node = current_node.next_

        if self.size < 2 :
            return None
        if self.size >= 2:
            return prev_node

        # Otherwise, there are at least 2 LinkedListNodes (one which points to
        # the back)
        # prev_node = None
        # cur_node = self.front
        #
        #
        # while cur_node.next_ != None:
        #     prev_node = cur_node
        #     cur_node = cur_node.next_
        #
        # return prev_node

    def get_values(self) -> list:
        """
        Return a list of all of the values within the LinkedList.
        >>> lnk = LinkedList()
        >>> lnk.get_values()
        []
        >>> lnk.prepend(3)
        >>> lnk.get_values()
        [3]
        >>> lnk.prepend(2)
        >>> lnk.get_values()
        [2, 3]
        >>> lnk.prepend(1)
        >>> lnk.get_values()
        [1, 2, 3]
        """
        nodess = []
        current_node = self.front
        while current_node:
            nodess.append(current_node.value)
            current_node = current_node.next_
        return nodess

    def __eq__(self, other) -> bool:
        """
        Return whether self and other are equal.

        >>> lnk1 = LinkedList()
        >>> lnk2 = LinkedList()
        >>> lnk1 == lnk2
        True
        >>> lnk1.prepend(3)
        >>> lnk1 == lnk2
        False
        >>> lnk2.prepend(3)
        >>> lnk1 == lnk2
        True
        >>> lnk1.prepend(2)
        >>> lnk2.prepend(2)
        >>> lnk1 == lnk2
        True
        >>> lnk1.prepend(1)
        >>> lnk1 == lnk2
        False

        """
        current_node = self.front
        other_node = other.front
        if self.size != other.size:
            return False
        else:
            while current_node is not None:
                if current_node.value != other_node.value:
                    return False
                current_node = current_node.next_
                other_node = other_node.next_
            return True

        # if not type(other) == type(self):
        #     return False
        #
        # # If the sizes of the LinkedLists differ, simply return False.
        # if self.size != other.size:
        #     return False
        #
        # # Otherwise, loop over both LinkedLists in parallel and compare their
        # # values. If one of the values differ, then we return False.
        # # Alternatively:
        # #     - Get the values of both LinkedLists (via something like
        # #       get_values()) and return whether those lists are equal or not.
        #
        # # We use 2 variables to keep track of our place within each of the
        # # linked lists
        # cur_self = self.front
        # cur_other = other.front
        #
        # # Since they're of the same length, we just need to check whether one
        # # of the current nodes are None or not.
        # while cur_self != None:
        #     # If the values of the nodes are different, then we can exit
        #     # and return False
        #     if cur_self.value != cur_other.value:
        #         return False
        #
        #     # Otherwise, we can move on to the next nodes in each LinkedList
        #     cur_self = cur_self.next_
        #     cur_other = cur_other.next_
        #
        # # If we get through the entire LinkedList without returning False,
        # # then that means every value has matched, so we can return True.
        # return True

    def find_value(self, value: object) -> LinkedListNode:
        """
        Return the first LinkedListNode in this LinkedList with the value value.

        >>> lnk = LinkedList()
        >>> lnk.prepend(3)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.find_value(1) == lnk.front
        True
        >>> lnk.find_value(3) == lnk.back
        True
        >>> lnk.find_value(2).next_ == lnk.back
        True
        """
        current_node = self.front

        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_

        # while cur_node != None and cur_node.value != value:
        #     cur_node = cur_node.next_
        #
        # return cur_node

    def add_after(self, to_add: object, to_add_after: object) -> None:
        """
        Add to_add after the first node with the value to_add_after.
        >>> lnk = LinkedList()
        >>> lnk.prepend(3)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.add_after(10, 2)
        >>> print(lnk)
        1 -> 2 -> 10 -> 3 -> |

        """
        current_node = self.front
        new_node = LinkedListNode(to_add)

        while current_node is not None and current_node.value != to_add_after:
            current_node = current_node.next_

        new_node.next_ = current_node.next_
        current_node.next_ = new_node

        if new_node.next_ == None:
            self.back = new_node

        self.size += 1





    def add_after_every(self, to_add: object, to_add_after: object) -> None:
        """
        Add to_add after the every node with the value to_add_after.

        >>> lnk = LinkedList()
        >>> lnk.prepend(3)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.add_after_every(10, 2)
        >>> print(lnk)
        1 -> 2 -> 10 -> 1 -> 2 -> 10 -> 3 -> |

        """
        current_node = self.front
        count = 0
        while current_node is not None :
            if current_node.value == to_add_after:
                new_node = LinkedListNode(to_add)
                new_node.next_ = current_node.next_
                current_node.next_ = new_node
                count += 1
            current_node = current_node.next_
        self.size += count






        # new_node = LinkedListNode(to_add)
        # current_node = self.front
        # count = 0
        # while current_node is not None:
        #     if current_node.value == to_add_after:
        #         new_node = LinkedListNode(to_add)
        #         new_node.next_ = current_node.next_
        #         current_node.next_ = new_node
        #         count += 1
        #     current_node = current_node.next_
        #
        # cur_node = self.front









if __name__ == "__main__":
    import doctest
    doctest.testmod()

