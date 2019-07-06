"""
The BinaryTree class for Lab 7.

large_tree:
    - Pre-order:    1, 2, 5, 2, 3, 4, 6, 3, 4, 7
    - Post-order:   3, 2, 5, 2, 3, 4, 6, 7, 4, 1
    - Level-order:  1, 2, 4, 5, 6, 7, 2, 3, 4, 3
    - In-order:     5, 3, 2, 2, 1, 3, 6, 4, 4, 7
    
(I've adjusted the __str__ method in this to make it a bit easier to
 differentiate the left and right subtrees.)
"""
from typing import Any, Union

class BinaryTree:
    """
    A class representing a BinaryTree.
    
    value - The value of the BinaryTree's root
    left - The root node of this BinaryTree's left subtree.
    right - The root node of this BinaryTree's right subtree.
    """
    value: Any
    left: 'BinaryTree'
    right: 'BinaryTree'
    
    def __init__(self, value: Any, left: 'BinaryTree' = None,
                 right: 'BinaryTree' = None) -> None:
        """
        Initialize this BinaryTree with the root value value, left subtree left,
        and right subtree right.
        """
        self.value = value
        self.left = left
        self.right = right

    # For convenience when trying to make a Tree.
    def __str__(self) -> str:
        """
        Return the string representation of this BinaryTree, such that the root
        node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).
        
        >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
        >>> print(t1)
                   1
             3
          4     6
        >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
        >>> print(t2)
             9
          7     5
        >>> t = BinaryTree(0, t1, t2)
        >>> print(t)
                      0
                   1        9
             3           7     5
          4     6
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

def get_internal_values(t: Union[BinaryTree, None]) -> list:
    """
    Return a list of the internal values in t in pre-order.
    
    >>> get_internal_values(None)
    []
    >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
    >>> print(t1)
               1
         3
      4     6
    >>> get_internal_values(t1)
    [1, 3]
    >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
    >>> print(t2)
         9
      7     5
    >>> get_internal_values(t2)
    [9]
    >>> t = BinaryTree(0, t1, t2)
    >>> print(t)
                  0
               1        9
         3           7     5
      4     6
    >>> get_internal_values(t)
    [0, 1, 3, 9]
    """
    if not t:######
        return []
    if not t.left and not t.right:
        return []
    else:
        result = [t.value]
        return result + get_internal_values(t.left) + get_internal_values(t.right)

        # left = get_internal_values(t.left)
        # right = get_internal_values(t.right)
        # return result + left + right



    # if t is None:
    #     return []
    #
    # if t.left is None and t.right is None:
    #     return []
    #
    # # If we wanted this in post-order:
    # #     get_internal_values(t.left) + get_internal_values(t.right) + [t.value]
    # # If we wanted this in-order:
    # #     get_internal_values(t.left) + [t.value] + get_internal_values(t.right)
    #
    # return [t.value] + get_internal_values(t.left) + \
    #        get_internal_values(t.right)

def get_max_depth(t: Union[BinaryTree, None]) -> int:
    """
    Return the maximum depth of t.
    
    (If t is None, the maximum depth should be -1 for the sake of our recursion;
    you could argue that it should return 0 though, and that a leaf should also
    return 0.)
    
    >>> get_max_depth(None)
    -1
    >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
    >>> print(t1)
               1
         3
      4     6
    >>> get_max_depth(t1)
    2
    >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
    >>> print(t2)
         9
      7     5
    >>> get_max_depth(t2)
    1
    >>> t = BinaryTree(0, t1, t2)
    >>> print(t)
                  0
               1        9
         3           7     5
      4     6
    >>> get_max_depth(t)
    3
    """
    if not t:
        return -1
    else:
        return 1 + max([get_max_depth(t.left)] + [get_max_depth(t.right)]) #######

def get_depth_of(t: Union[BinaryTree, None], value: Any) -> int:
    """
    Return the depth of value in t if value is in t. If not, return -1.

    >>> get_depth_of(None, 3)
    -1
    >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
    >>> print(t1)
               1
         3
      4     6
    >>> get_depth_of(t1, 3)
    1
    >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
    >>> print(t2)
         9
      7     5
    >>> get_depth_of(t2, 9)
    0
    >>> t = BinaryTree(0, t1, t2)
    >>> print(t)
                  0
               1        9
         3           7     5
      4     6
    >>> get_depth_of(t, 3)
    2
    """
    if t is None:
        return -1
    if t.value == value:
        return 0

    if get_depth_of(t.left, value) > -1:
        return get_depth_of(t.left, value) + 1

    if get_depth_of(t.right, value) > -1:
        return get_depth_of(t.right, value) + 1

def get_values_at_depth(t: Union[BinaryTree, None], depth: int) -> list:
    """
    Return all of the elements at depth depth in t.

    >>> get_values_at_depth(None, 0)
    []
    >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
    >>> print(t1)
               1
         3
      4     6
    >>> get_values_at_depth(t1, 1)
    [3]
    >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
    >>> print(t2)
         9
      7     5
    >>> get_values_at_depth(t2, 1)
    [7, 5]
    >>> t = BinaryTree(0, t1, t2)
    >>> print(t)
                  0
               1        9
         3           7     5
      4     6
    >>> get_values_at_depth(t, 2)
    [3, 7, 5]
    """
    if t is None:
        return []
    if depth == 0:
        return [t.value]
    return get_values_at_depth(t.left, depth - 1) + get_values_at_depth(t.right, depth - 1)

def copy(t: Union[BinaryTree, None]) -> Union[BinaryTree, None]:#########
    """
    Return a copy of t.

    >>> copy(None)
    >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
    >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
    >>> t = BinaryTree(0, t1, t2)
    >>> print(t)
                  0
               1        9
         3           7     5
      4     6
    >>> print(copy(t))
                  0
               1        9
         3           7     5
      4     6
    """
    if t is None:
        return None
    else:
        return BinaryTree(t.value, copy(t.left), copy(t.right))

# def print_level_order(t: Union[BinaryTree, None]) -> None:
#     """
#     Print the elements in t in level order.
#
#     >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
#     >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
#     >>> t = BinaryTree(0, t1, t2)
#     >>> print(t)
#                   0
#                1        9
#          3           7     5
#       4     6
#     >>> print_level_order(t)
#     0
#     1
#     9
#     3
#     7
#     5
#     4
#     6
#     """
#     pass
#
# def insert_before(t: Union[BinaryTree, None], to_insert: Any,
#                   to_find: Any) -> Union[BinaryTree, None]:
#     """
#     Return the root of the tree t after inserting to_insert before every
#     occurrence of to_find.
#
#     >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(1)))
#     >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
#     >>> t = BinaryTree(1, t1, t2)
#     >>> print(t)
#                   1
#                1        9
#          3           7     5
#       4     1
#     >>> print(insert_before(t, 11, 1))
#                                       11
#                           1
#                       11        9
#                    1         7     5
#          3
#       4        11
#             1
#     """
#     pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    t1 = BinaryTree(1, left=BinaryTree(3))
    t2 = BinaryTree(2)
    tree = BinaryTree(0, left=t1, right=t2)
    
    # You can make the BinaryTree in different ways: either all in one statement
    # or making individual subtrees.
    # Create the left subtree of large_tree with a root value of 2
    large_tree_2 = BinaryTree(2, BinaryTree(5,
                                            right=BinaryTree(2, BinaryTree(3))))
    
    # Create the right subtree of large_tree with a root value of 4
    large_tree_4 = BinaryTree(4, BinaryTree(6, BinaryTree(3), BinaryTree(4)),
                              BinaryTree(7))

    large_tree = BinaryTree(1, large_tree_2, large_tree_4)
