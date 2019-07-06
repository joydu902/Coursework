"""
The LinkedList implementation of a Queue from lecture.

Go to the bottom for the actual LinkedListQueue class.
"""
from typing import Union

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

class LinkedListQueue:
    """
    A class representing a Queue, using a LinkedList as an implementation.
    """
    
    def __init__(self) -> None:
        """
        Initialize this LinkedListQueue.
        
        >>> q = LinkedListQueue()
        >>> q.add(1)
        >>> q.add(2)
        >>> q.remove()
        1
        """
        self._content = LinkedList()
    
    def add(self, value: object) -> None:
        """
        Add value to this LinkedListQueue.
        
        >>> q = LinkedListQueue()
        >>> q.add(1)
        >>> q.add(2)
        >>> q.remove()
        1
        """
        new_node = LinkedListNode(value)

        if self._content.size > 0:
            self._content.back.next_ = new_node
        else:
            self._content.front = new_node

        self._content.back = new_node
        self._content.size += 1
    
    def remove(self) -> object:
        """
        Remove an item from this LinkedListQueue.
        
        Precondition: self.is_empty() == False
        
        >>> q = LinkedListQueue()
        >>> q.add(1)
        >>> q.add(2)
        >>> q.remove()
        1

        """
        to_return = self._content.front.value
        self._content.front = self._content.front.next_
        self._content.size -= 1
        
        return to_return
    
    def is_empty(self) -> bool:
        """
        Return whether this LinkedListQueue is empty or not.
        >>> q = LinkedListQueue()
        >>> q.is_empty()
        True
        >>> q.add(1)
        >>> q.is_empty()
        False
        """
        return self._content.size == 0
