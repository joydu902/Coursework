from typing import Union, Any, List

class Container:
    """
    An abstract Container class.
    """
    
    def __init__(self) -> None:
        """
        Initialize this Container.
        """
        raise NotImplementedError

    def add(self, value) -> None:
        """
        Add value this Container.
        """
        raise NotImplementedError

    def remove(self) -> object:
        """
        Remove an item from this Container.
        """
        raise NotImplementedError
    
    def is_empty(self) -> bool:
        """
        Return whether this container is empty or not (whether there's nothing
        left to remove.)
        """
        raise NotImplementedError
    
class Stack(Container):
    """
    An implementation of Stack.
    """
    
    def __init__(self) -> None:
        """
        Initialize this Stack.
        
        >>> s = Stack()
        >>> s.is_empty()
        True
        """
        self._content = []

    def add(self, value: object) -> None:
        """
        Add value this Stack.
        
        >>> s = Stack()
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        self._content.append(value)

    def remove(self) -> object:
        """
        Remove an item from the top of this Stack.
        
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add("A")
        >>> s.remove()
        'A'
        """
        return self._content.pop()
    
    def is_empty(self) -> bool:
        """
        Return whether this Stack is empty or not (whether there's nothing
        left to remove.)
        
        >>> s = Stack()
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        return self._content == []

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
    
class Tree:
    """
    A class representing a Tree.
    
    value - The value of the root of this Tree.
    children - The subtrees of this Tree.
    """
    value: Any
    children: List['Tree']
    
    def __init__(self, value: Any, children: List['Tree'] = None) -> None:
        """
        Initialize this Tree with the value value and children children.
        """
        self.value = value
        self.children = children[:] if children else []
    
    # For convenience when trying to make a Tree.
    def __str__(self) -> str:
        """
        Return the string representation of this Tree, such that the root
        node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).
        
        >>> t1 = Tree(1, [Tree(3, [Tree(4), Tree(6)])])
        >>> print(t1)
          1  
          3  
        4   6
        >>> t2 = Tree(2, [Tree(8)])
        >>> print(t2)
        2
        8
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> print(t3)
          9  
        7   5
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> print(t)
                0        
          1     2     9  
          3     8   7   5
        4   6            
        """
        child_strings = [str(child).split('\n') for child in self.children]
        
        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])
        
        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]
        
        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                if i < len(child):
                    new_string[i].append(child[i])
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * len(child[0]))
        
        # Put 3 spaces between each subtree
        new_string_joined = [(' ' * 3).join(child) for child in new_string]
        
        # Add in the value of the current Tree
        str_width = 0
        if new_string_joined:
            str_width = len(new_string_joined[0])
        
        left_padding = str_width // 2
        right_padding = (str_width - str_width // 2) - 1
        
        new_string_joined.insert(0, "{}{}{}".format(" " * left_padding,
                                                    self.value,
                                                    " " * right_padding))
        
        # Return the new string
        return "\n".join(new_string_joined)
    

class BinaryTree:
    """
    A class representing a BinaryTree.
    
    value - The value of the root of this BinaryTree.
    left - The left subtree of this BinaryTree.
    right - The right subtree of this BinaryTree.
    """
    value: Any
    left: Union['BinaryTree', None]
    right: Union['BinaryTree', None]
    
    def __init__(self, value: Any, left: Union['BinaryTree', None] = None, 
                 right: Union['BinaryTree', None] = None) -> None:
        """
        Initialize this BinaryTree with the value value, left subtree left,
        and right subtree right.
        """
        self.value = value
        self.left = left
        self.right = right
    

    def __str__(self) -> str:
        """
        Return the string representation of this BinaryTree, such that the root
        node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).
        
        >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
        >>> print(t1)
          1
          3
        4   6
        >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
        >>> print(t2)
          9
        7   5
        >>> t = BinaryTree(0, t1, t2)
        >>> print(t)
              0
          1       9
          3     7   5
        4   6
        """
        children = []
        if self.left:
            children.append(str(self.left))
        else:
            children.append("")
        
        if self.right:
            children.append(str(self.right))
        else:
            children.append("")
        
        
        child_strings = [child.split('\n') for child in children]
        
        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])
        
        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]
        child_lengths = []
        
        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                child_length = max([len(line) for line in child])
                child_lengths.append(child_length)
                
                if i < len(child):
                    padding_needed = child_length - len(child[i])
                    new_string[i].append(child[i] + " " * padding_needed) 
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * child_length)
        
        # Put 3 spaces between each subtree
        new_string_joined = [(' ' * 3).join(child) for child in new_string]
        
        # Add in the value of the current Tree
        left_padding = child_lengths[0] + 2
        
        new_string_joined.insert(0, "{}{}".format(" " * left_padding,
                                                  self.value))
        
        new_string_joined = [line.rstrip() for line in new_string_joined]
        
        # Return the new string
        return "\n".join(new_string_joined).rstrip()     


class BinarySearchTree:
    """
    A class representing a BinarySearchTree.
    
    value - The value of the BinarySearchTree's root
    left - The root node of this BinarySearchTree's left subtree.
    right - The root node of this BinarySearchTree's right subtree.
    """
    value: Any
    left: Union['BinarySearchTree', None]
    right: Union['BinarySearchTree', None]
    
    def __init__(self, value: Any, left: 'BinarySearchTree' = None,
                 right: 'BinarySearchTree' = None) -> None:
        """
        Initialize this BinarySearchTree with the root value value, left subtree
        left, and right subtree right.
        """
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        """
        Return the string representation of this BinarySearchTree, such that the 
        root node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).
        
        >>> t1 = BinarySearchTree(4, BinarySearchTree(2, BinarySearchTree(1), 
        ...                                              BinarySearchTree(3)))
        >>> print(t1)
                   4
             2
          1     3
        """
        children = []
        if self.left:
            children.append(str(self.left))
        else:
            children.append("")
        
        if self.right:
            children.append(str(self.right))
        else:
            children.append("")
        
        
        child_strings = [child.split('\n') for child in children]
        
        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])
        
        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]
        child_lengths = []
        
        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                child_length = max([len(line) for line in child])
                child_lengths.append(child_length)
                
                if i < len(child):
                    padding_needed = child_length - len(child[i])
                    new_string[i].append(child[i] + " " * padding_needed) 
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * child_length)
        
        # Put 3 spaces between each subtree
        new_string_joined = [(' ' * 3).join(child) for child in new_string]
        
        # Add in the value of the current Tree
        left_padding = child_lengths[0] + 2
        
        new_string_joined.insert(0, "{}{}".format(" " * left_padding,
                                                  self.value))
        
        new_string_joined = [line.rstrip() for line in new_string_joined]
        
        # Return the new string
        return "\n".join(new_string_joined).rstrip()    

    
def insert(t: Union['BinarySearchTree', None], value: Any) -> bool:
    """
    Insert value into t, maintaining the BinarySearchTree properties. Return
    the root node of t.
    
    Pre-condition: value is not in t.
    
    >>> print(insert(None, 2))
      2
    >>> print(insert(BinarySearchTree(4, BinarySearchTree(2), 
    ...                                  BinarySearchTree(6, 
    ...                                      BinarySearchTree(5))), 3))
            4
      2           6
         3     5
    """
    if t is None:
        return BinarySearchTree(value)
    
    if value < t.value:
        t.left = insert(t.left, value)
    else:
        t.right = insert(t.right, value)
    
    return t