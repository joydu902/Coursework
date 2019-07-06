"""
The LinkedList and LinkedListNode classes from lecture.

__str__ has also been provided so we can print the LinkedList in the docstring.
"""
from typing import Union, Any

class LinkedListNode:
    """
    A Node to be used in a LinkedList.

    next_ - The successor to this LinkedListNode
    value - The data represented by this LinkedListNode.
    """
    next_: Union["LinkedListNode", None]
    value: Any

    def __init__(self, value: Any,
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

    def append(self, value: Any) -> None:
        """
        Insert value to the end of this LinkedList (after self.back).

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> print(lnk)
        0 -> 1 -> |
        """
        new_node = LinkedListNode(value)
        if self.size ==  0:
            self.front = new_node
        else:
            self.back.next_ = new_node
        self.back = new_node
        self.size += 1
        

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
    
    def remove(self, value: Any) -> None:
        """
        Remove value from this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        >>> lnk.remove(1)
        >>> print(lnk)
        0 -> |
        """
        prev_node = None
        current_node = self.front
        
        while current_node is not None and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next_
        
        if not current_node: # Same as if current_node == None
            return 
        
        if not prev_node: # current_node is the front
            self.front = current_node.next_
        else:
            prev_node.next_ = current_node.next_
        
        if not current_node.next_: # current_node is the back of our list
            self.back = prev_node
        
        self.size -= 1
        

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
