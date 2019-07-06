"""
Lab 6 solutions

For large_tree:
    Pre-order Traversal
        5, 1, 4, 6, 3, 2, 7, 3, 5, 8, 9, 1, 8
    Post-order Traversal
        6, 4, 3, 2, 1, 7, 5, 9, 1, 8, 3, 8, 5
    Level-order Traversal
        5, 1, 7, 3, 8, 4, 3, 2, 5, 8, 6, 9, 1
"""
from typing import Any, List

class Tree:
    """
    A class representing a Tree.
    
    value - The value of the Tree's root
    children - The root nodes of the children of this Tree.
    """
    value: Any
    children: List['Tree']
    
    def __init__(self, value: Any, children: List['Tree'] = None) -> None:
        """
        Initialize this Tree with the root value value and children children.
        """
        self.value = value
        
        # We make this a copy of the list children, in case it gets modified
        # at some point elsewhere.
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
                child_length = max([len(line) for line in child])

                if i < len(child):
                    padding_needed = child_length - len(child[i])
                    new_string[i].append(child[i] + " " * padding_needed)
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * child_length)

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

        new_string_joined = [line.rstrip() for line in new_string_joined]

        # Return the new string
        return "\n".join(new_string_joined)

    def count_occurrences(self, value: Any) -> int:
        """
        Return the number of times value occurs in this Tree.
        
        >>> large_tree.count_occurrences(3)
        2
        """
        # result = 0
        # if self.value == value:
        #     result = 1
        # if not self.children:
        #     return result
        #
        # else:
        #     for child in self.children:
        #         result += child.count_occurrences(value)
        # return result
        #
        result = 0
        for child in self.children:
            result += child.count_occurrences(value)

        if self.value == value:
            result += 1
        return result

        # # Count all occurrences in the subtrees
        # count_occurrences_in_children = sum([child.count_occurrences(value) for
        #                                      child in self.children])
        #
        # # And then add 1 to the sum of those counts if self.value == value
        # return count_occurrences_in_children + (1 if self.value == value else 0)

    
    def get_internal_values(self) -> List[Any]:
        """
        Return a list of all of the values of the internal nodes of this Tree.
        (In pre-order)
        
        >>> large_tree.get_internal_values()
        [5, 1, 4, 3, 8]
        """
        result = []
        if self.children:
            result += [self.value]

        for child in self.children:
            result += child.get_internal_values()

        return result

    def get_depth_of(self, value: Any) -> int:
        """
        Return the depth of value in this Tree.
        If value is not in this Tree, return -1.
        
        >>> large_tree.get_depth_of(3)
        2
        >>> large_tree.get_depth_of(5)
        0
        """
        if self.value == value:
            return 0

        for child in self.children:
            depth = child.get_depth_of(value)
            if depth > -1:
                return 1 + depth

        return -1

    
    def get_values_at_depth(self, depth: int) -> List[Any]:
        """
        Return a list of all values of the Tree nodes depth depth from this
        Tree's root.
        
        Precondition: depth >= 0
        
        >>> large_tree.get_values_at_depth(2)
        [4, 3, 2, 5, 8]
        """
        result = []
        if depth == 0:
            return [self.value]
        for child in self.children:
            result += child.get_values_at_depth(depth - 1)
        return result


    
    def get_max_branching_factor(self) -> int:
        """
        Return the maximum branching factor in this Tree.
        
        >>> large_tree.get_max_branching_factor()
        4
        """
        # if not self.children:
        #     return 0
        # for child in self.children:
        #     child.get_max_branching_factor()
        pass


    
    def copy(self) -> 'Tree':
        """
        Return a Tree that's a copy of this Tree.
        
        >>> large_tree_copy = large_tree.copy()
        >>> large_tree_copy.value = 10
        >>> large_tree_copy.children[0].value = 3
        >>> print(large_tree.value)
        5
        >>> print(large_tree_copy.value)
        10
        >>> print(large_tree.children[0].value)
        1
        >>> print(large_tree_copy.children[0].value)
        3
        """
        copy_s = []
        for child in self.children:
            copy_s += child.copy()
        return Tree(self.value, copy_s)

    def print_level_order(self) -> None:
        """
        Prints out the elements of this Tree in level-order (without modifying
        the Tree).
        
        >>> large_tree.print_level_order()
        5
        1
        7
        3
        8
        4
        3
        2
        5
        8
        6
        9
        1
        """
        pass

    
    def add_subtree_to(self, subtree: 'Tree', value: Any) -> bool:
        """
        Return whether we could add subtree as a subtree to the node with the 
        value value in this Tree.
        
        >>> t = Tree(3, [Tree(2), Tree(4)])
        >>> copied_tree = large_tree.copy() # So we don't modify the original
        >>> copied_tree.add_subtree_to(t, 3)
        True
        >>> print(copied_tree)
                        5
              1         7       3       8
        4     3     2       5     8
        6     3                 9   1
            2   4
        """
        if self.value == value:
            self.children.append(subtree)
            return True
        for child in self.children:
            result = child.add_subtree_to(subtree, value)
            if result:
                return True
        return False

    
if __name__ == '__main__':
    t1 = Tree(1, [Tree(3)])
    t2 = Tree(2)
    t = Tree(0, [t1, t2])
    
    # Creating large tree
    # You can create this tree in any way you want (i.e. making multiple
    # trees, or a single one, or making each subtree, etc.)
    
    # Start with the subtrees: The subtree with root 1
    subtree4 = Tree(4, [Tree(6)])
    subtree3_leaf = Tree(3)
    subtree2 = Tree(2)
    subtree1_children = [subtree4, subtree3_leaf, subtree2]
    subtree1 = Tree(1, subtree1_children)
    
    # The subtree with 7 is just a leaf, same with 8
    subtree7 = Tree(7)
    subtree8_leaf = Tree(8)
    
    # The subtree with 3 has 5, and a tree rooted at an 8
    subtree8 = Tree(8, [Tree(9), Tree(1)])
    subtree3 = Tree(3, [Tree(5), subtree8])
    
    root_children = [subtree1, subtree7, subtree3, subtree8_leaf]
    
    large_tree = Tree(5, root_children)

    # print(large_tree.count_occurrences(3))

    # print(large_tree.get_internal_values())

    print(large_tree.get_depth_of(6))
    print(large_tree.get_depth_of(3))
    print(large_tree.get_values_at_depth(2))
    print(large_tree.value)

    import doctest
    doctest.testmod()