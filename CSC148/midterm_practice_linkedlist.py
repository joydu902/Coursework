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
    
    def add_before(self, new_value: Any, to_find: Any):
        """
        Add new_value to this LinkedList so it comes immediately 
        before to_find.
        
        If to_find isn't in this LinkedList, don't modify this LinkedList.
        
        >>> lnk = LinkedList()
        >>> lnk.prepend("H")
        >>> lnk.add_before("A", "H")
        >>> print(lnk)
        A -> H -> |
        >>> lnk.size
        2
        >>> lnk.add_before("C", "H")
        >>> print(lnk)
        A -> C -> H -> |
        >>> lnk.size
        3
        >>> lnk.add_before("O", "B")
        >>> print(lnk)
        A -> C -> H -> |
        >>> lnk.size
        3
        """
        new_node = LinkedListNode(new_value)
        
        prev_node = None
        cur_node = self.front
        
        # Find to_find in the LinkedList
        # We need to update the next_ pointer of the node that comes before
        # to_find, so we keep track of the previous node too.
        while cur_node != None and cur_node.value != to_find:
            prev_node = cur_node
            cur_node = cur_node.next_
        
        # If cur_node is None after the loop, then to_find wasn't in the
        # LinkedList so we don't do anything
        if cur_node == None:
            return
        
        # If prev_node is None, then cur_node was at the start of the LinkedList
        # so we need to set front to be new_node
        if prev_node == None:
            self.front = new_node
        else:
            # Otherwise, prev_node should point to new_node
            prev_node.next_ = new_node
        
        # Make new_node point to cur_node
        new_node.next_ = cur_node
        
        # Increase size by 1
        self.size += 1
    
class LinkedListStack:
    """
    A class representing a Stack, formed using a LinkedList.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty LinkedListStack.
        
        >>> s = LinkedListStack()
        >>> s.add(3)
        >>> s.add(2)
        >>> s.add(1)
        >>> s.remove()
        1
        >>> s.remove()
        2
        >>> s.remove()
        3

        """
        self._content = LinkedList()
    
    def add(self, value: object) -> None:
        """
        Add value to this LinkedListStack.
        
        >>> s = LinkedListStack()
        >>> s.add(3)
        >>> s.add(2)
        >>> s.add(1)
        >>> s.remove()
        1
        >>> s.remove()
        2
        >>> s.remove()
        3
        """
        new_node = LinkedListNode(value)

        if self._content.front is None:
            self._content.front = new_node
        else:
            new_node.next_ = self._content.front
            self._content.front = new_node
        self._content.size += 1



        # # Create the new LinkedListNode
        # new_node = LinkedListNode(value)
        #
        # # Make it point to the current front
        # new_node.next_ = self._content.front
        #
        # # Make the new node the front of our LinkedList
        # self._content.front = new_node
        #
        # # If we didn't have any nodes in our LinkedList previously,
        # # set the new_node to be the back as well
        # if self._content.back == None:
        #     self._content.back = new_node
        #
        # # Increase the size of the LinkedList by 1
        # self._content.size += 1
        

    def remove(self) -> object:
        """
        Remove a value from the top of this LinkedListStack.
        
        Precondition: self.is_empty() == False
        
        >>> s = LinkedListStack()
        >>> s.add(3)
        >>> s.add(2)
        >>> s.add(1)
        >>> s.remove()
        1
        >>> s.remove()
        2
        >>> s.remove()
        3
        """
        results = self._content.front.value

        self._content.front = self._content.front.next_

        self._content.size -= 1

        if self._content.size == 0:
            self.front = None

        return results




        # # Get the value of the front of the LinkedList
        # value_to_return = self._content.front.value
        #
        # # Set the front to be the node after the current front (i.e.
        # # essentially removing the front of our LinkedList.)
        # self._content.front = self._content.front.next_
        #
        # # Reduce the size by 1
        # self._content.size -= 1
        #
        # # If the size is now 0, set back to None as well
        # if self._content.size == 0:
        #     self._content.back = None
        #
        # return value_to_return
    
    def is_empty(self) -> bool:
        """
        Return True if this Stack is empty.
        
        >>> s = LinkedListStack()
        >>> s.is_empty()
        True
        >>> s.add(3)
        >>> s.is_empty()
        False
        """
        return self._content.size == 0
