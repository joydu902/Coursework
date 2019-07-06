#slides
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



    def sum_values(self) -> int:
        """
        Return the sum of all of the values in this Tree.

        >>> t = Tree(5, [Tree(3, [Tree(2)]), Tree(1)])
        >>> t.sum_values()
        11
        """
        # sum = 0
        # if self.children == []:
        #     return self.value
        # else:
        #     for child in self.children:
        #         sum += child.sum_values()
        #     return sum + self.value

        result = [self.value]
        for child in self.children:
            result += [child.sum_values()]
        return sum(result)

    def get_values(self) -> List:
        """
        Return a list of all values in this Tree.
        >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
        >>> t2 = Tree(2, [Tree(8)])
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> t.get_values()
        [0, 1, 3, 4, 2, 8, 9, 7, 5]
        """
        result = [self.value]
        for child in self.children:
            result.extend(child.get_values())
        return result

    def get_leaves(self) -> List:
        """
        Return a list of all of the leaves in this Tree.

        >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
        >>> t2 = Tree(2, [Tree(8)])
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> t.get_leaves()
        [4, 8, 7, 5]
        """
        result =[]
        if self.children == []:
            return [self.value]
        else:
            for child in self.children:
                result += child.get_leaves()
            return result

    def get_height(self) -> int:
        """
        Return the height of this Tree.

        >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
        >>> t2 = Tree(2, [Tree(8)])
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> t.get_height()
        4
        """
        result = []
        if self.children == []:
            return 1
        for child in self.children:
            result += [child.get_height()]
        return max(result) + 1

    def contains(self, value: Any) -> bool:
        """
        Return whether value appears anywhere in this Tree.

        >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
        >>> t2 = Tree(2, [Tree(8)])
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> t.contains(5)
        True
        >>> t.contains(20)
        False
        """
        result = []
        if self.value == value:
            return True
        else:
            for child in self.children:
                result += [child.contains(value)]
            return any(result)

    # def get_closest_common_ancestor(self, value1: Any, value2: Any) -> Any:
    #     """
    #     Return the value of the closest common ancestor of the node with
    #     value value1 and the node with value value2, None if no such nodes
    #     exist.
    #
    #     >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
    #     >>> t2 = Tree(2, [Tree(8)])
    #     >>> t3 = Tree(9, [Tree(7), Tree(5)])
    #     >>> children = [t1, t2, t3]
    #     >>> t = Tree(0, children)
    #     >>> print(t)
    #           0
    #     1   2     9
    #     3   8   7   5
    #     4
    #     >>> t.get_closest_common_ancestor(5, 7)
    #     9
    #     >>> t.get_closest_common_ancestor(5, 9)
    #     0
    #     >>> t.get_closest_common_ancestor(0, 5) == None
    #     True
    #     >>> t.get_closest_common_ancestor(10, 3) == None
    #     True
    #     """
    #


    # def get_closest_common_ancestor(self, value1: Any, value2: Any) -> Any:
    #     """
    #     Return the value of the closest common ancestor of the node with
    #     value value1 and the node with value value2, None if no such nodes
    #     exist.
    #
    #     >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
    #     >>> t2 = Tree(2, [Tree(8)])
    #     >>> t3 = Tree(9, [Tree(7), Tree(5)])
    #     >>> children = [t1, t2, t3]
    #     >>> t = Tree(0, children)
    #     >>> t.get_closest_common_ancestor(5, 7)
    #     9
    #     >>> t.get_closest_common_ancestor(5, 9)
    #     0
    #     >>> t.get_closest_common_ancestor(0, 5) == None
    #     True
    #     >>> t.get_closest_common_ancestor(10, 3) == None
    #     True
    #     """
    #     recursive_calls = []
    #     for child in self.children:
    #         recursive_calls += [child.get_closest_common_ancestor(value1, value2)]
    #     for result in recursive_calls:
    #         if result != []:
    #             return result
    #     found_value1 = any([child.contains(value1) for child in self.children])
    #     found_value2 = any([child.contains(value2) for child in self.children])
    #     if found_value1 and found_value2:
    #         return self.value
    #     else:
    #         return None

    def print_preorder(self) -> None:
        """
        Print the nodes in this Tree in pre-order.

        >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
        >>> t2 = Tree(2, [Tree(8)])
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> t.print_preorder()
        0
        1
        3
        4
        2
        8
        9
        7
        5
        """
        print(self.value)
        for child in self.children:
            child.print_preorder()

    def print_postorder(self) -> None:
        """
        Print the nodes in this Tree in post-order.

        >>> t1 = Tree(1, [Tree(3, [Tree(4)])])
        >>> t2 = Tree(2, [Tree(8)])
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> t.print_postorder()
        4
        3
        1
        8
        2
        7
        5
        9
        0
        """
        for child in self.children:
            child.print_postorder()
        print(self.value)

    def count_occurrences(self, value: Any) -> int:
        """
        Return the number of times value occurs in this Tree.

        >>> large_tree.count_occurrences(3)
        2
        """
        count = 0
        if self.value == value:
            return 1
        else:
            for child in self.children:
                count += child.count_occurrences(value)
            return count

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

        # result = []
        # if self.children == []:
        #     return []
        # else:
        #     for child in self.children:
        #             result.extend(child.get_internal_values())
        #     return [self.value] + result

    def get_depth_of(self, value: Any) -> int:################
        """
        Return the depth of value in this Tree.
        If value is not in this Tree, return -1.

        >>> large_tree.get_depth_of(3)
        2
        >>> large_tree.get_depth_of(5)
        0
        """
        depth = 0
        if self.value == value:
            return 0
        else:
            for child in self.children:
                depth = child.get_depth_of(value)
                if depth > -1:
                    return depth + 1
            return -1


        # if self.value == value:
        #         return 0
        # else:
        #     for child in self.children:
        #         depth = child.get_depth_of(value)
        #         if depth > -1:
        #             return depth + 1
        #     return -1

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
        else:
            for child in self.children:
                result.extend(child.get_values_at_depth(depth - 1))
            return result

    # def get_max_branching_factor(self) -> int:###############
    #     """
    #     Return the maximum branching factor in this Tree.
    #
    #     >>> large_tree.get_max_branching_factor()
    #     4
    #     """
    #     if not self.children:
    #         return 0
    #     else:
    #         lst_of_child_bf = []
    #         for child in self.children:
    #             lst_of_child_bf.append(child.get_max_branching_factor())
    #         largest_child_bf = max(lst_of_child_bf)
    #         return max([largest_child_bf, len(self.children)])

    def get_max_branching_factor(self) -> int:###############
        """
        Return the maximum branching factor in this Tree.

        >>> large_tree.get_max_branching_factor()
        4
        """
        return max(self.get_all_branching_factor())

    def get_all_branching_factor(self) -> list:
        if not self.children:
            return [0]
        else:
            result = [len(self.children)]
            for child in self.children:
                result += child.get_all_branching_factor()
            return result


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
        new_children = []
        for child in self.children:
            new_children.extend([child.copy()])
        return Tree(self.value, new_children)

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
        q = [self]
        while q:
            result = q.pop(0)
            print(result.value)
            for child in result.children:
                q.append(child)

    def add_subtree_to(self, subtree: 'Tree', value: Any) -> bool:
        """
        Return whether we could add subtree as a subtree to the node with the
        value value in this Tree.

        >>> t = Tree(3, [Tree(2), Tree(4)])
        >>> copied_tree = large_tree.copy() # So we don't modify the original
        >>> print(copied_tree)
                      5
            1       7       3       8
        4   3   2       5     8
        6                   9   1
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
        else:
            for child in self.children:
                result = child.add_subtree_to(subtree, value)
                if result:
                    return True
            return False

    #Midterm Practice
    def __eq__(self, other: Any) -> bool:#######
        """
        Return True iff self and other are both Trees with the same subtrees.

        >>> Tree(1) == Tree(2)
        False
        >>> Tree(1, [Tree(2, [Tree(3)])]) == Tree(1, [Tree(2, [Tree(5)])])
        False
        >>> Tree(1, [Tree(2, [Tree(3)])]) == Tree(1, [Tree(2, [Tree(3)])])
        True
        """
        if self.value != other.value:
            return False
        for i in range(len(self.children)):
            if self.children[i] != other.children[i]:
                return False
        return True

    # def able_to_spell(self, word: str) -> bool:
    #     """
    #     Return whether a path from one node to another (from lowest to highest)
    #     contains all of the letters needed to spell word.
    #
    #     (Original wording of the question was wrong.)
    #
    #     >>> t = Tree('A', [Tree('T', [Tree('E'),
    #     ...                          Tree('A', [Tree('C'), Tree('H')])]),
    #     ...                      Tree('H'),
    #     ...                      Tree('S', [Tree('I')])])
    #     >>> t.able_to_spell('CAT')
    #     True
    #     >>> t.able_to_spell('HI')
    #     False
    #     """
    #     if word == '':
    #         return True
    #
    #     if self.value == word[-1]:
    #         # The we search for the remainder of the word (up to but not
    #         # including the last letter)
    #         new_word = word[:-1]
    #
    #         if new_word == '':
    #             return True
    #
    #         for child in self.children:
    #             if child.able_to_spell(new_word):
    #                 return True
    #
    #     for child in self.children:
    #         if child.able_to_spell(word):
    #             return True
    #
    #     return False


#past tests
def count_odd_above(t, n):
    """
    Return the number of nodes with depth less than n that have odd values.
    Assume t’s nodes have integer values.
    @param Tree t: tree to list values from
    @param int n: depth above which to list values
    @rtype: int
    >>> t1 = Tree(4)
    >>> t2 = Tree(3)
    >>> t3 = Tree(5, [t1, t2])
    >>> count_odd_above(t3, 1 )
    1
    """
    if n == 0:
        return 0
    else:
        count = 0
        if t.value % 2 == 1:
            count += 1
        else:
            for child in t.children:
                count += count_odd_above(child, 1)
        return count



    # if n == 0:
    #     return 0
    # else:
    #     count = 0
    #     if t.value % 2 == 1:
    #         count += 1
    #     for child in t.children:
    #         count += count_odd_above(child, n -1)
    #     return count

def count_at_depth(t, d):
    """ Return the number of nodes at depth d of t.
    @param Tree t: tree to explore --- cannot be None
    @param int d: depth to report from, non-negative
    @rtype: int
    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> count_at_depth(t, 0)
    1
    >>> count_at_depth(t, 1)
    4
    >>> count_at_depth(t, 2)
    2
    >>> count_at_depth(t, 5)
    0
    """
    count = 0
    if d == 0:
        return 1
    for child in t.children:
        count += count_at_depth(child, d - 1)
    return count

def sum_at_depth(t: Tree, d) -> int:
    """ Return the sum of node values at depth d of t.
    Assume that node values are integers and that there are no
    None values in any list of children in t or its descendants.
    @param Tree t: tree to explore, cannot be None
    5
    @param int d: depth to report from, non-negative
    @rtype: int
    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> sum_at_depth(t, 0)
    17
    >>> sum_at_depth(t, 1)
    6
    >>> sum_at_depth(t, 2)
    9
    >>> count_at_depth(t, 5)
    0
    """
    if d == 0:
        return t.value
    else:
        result = []
        for child in t.children:
            result += [sum_at_depth(child, d - 1)]
        return sum(result)

def concatenate_at_depth(t, d):
    """ Return the concatenation of node values at depth d of t.
    Assume that node values are strings and that there are no
    None values in any list of children in t or its descendants.
    @param Tree t: tree to explore, cannot be None
    @param int d: depth to report from, non-negative
    @rtype: str
    >>> t = Tree("a", [Tree("b"), Tree("c", [Tree("d")]), Tree("e", [Tree("f")]), Tree("g")])
    >>> print(t)
          a
    b   c   e   g
        d   f
    >>> concatenate_at_depth(t, 0)
    'a'
    >>> concatenate_at_depth(t, 1)
    'bceg'
    >>> concatenate_at_depth(t, 2)
    'df'
    >>> concatenate_at_depth(t, 5)
    ''
    """
    if d == 0:
        return t.value
    else:
        result = ''
        for child in t.children:
            result += concatenate_at_depth(child, d-1)
        return result

def count_nodes(t: Tree) -> int:
    """
    Return the number of nodes in this Tree.
    >>> t = Tree(1)
    >>> count_nodes(t)
    1
    """
    if t is None:
        return 0
    else:
        count = 0
        for child in t.children:
            count += count_nodes(child)
        return count + 1

def string_postorder(t: Tree) -> str:
    """
    Return t’s str values concatenated in postorder.
    Assume all values in tree rooted at t are str.

    >>> string_postorder(Tree("a"))
    'a'
    >>> t = Tree("a", [Tree("b", [Tree("c")]), Tree("d")])
    >>> string_postorder(t)
    'cbda'
    """
    if not t.children:
        return t.value
    else:
        result = ''
        for child in t.children:
            result += string_postorder(child)
        return result + t.value

def get_path(t:Tree, value: Any) -> list:
    """
    Return the path from the root to a value.

    >>> t1 = Tree(2, [Tree(5)])
    >>> t2 = Tree(3)
    >>> t3 = Tree(4, [Tree(6), Tree(7)])
    >>> t = Tree(1, [t1, t2, t3])
    >>> print(t)
          1
    2   3     4
    5       6   7
    >>> get_path(t, 5)
    [1, 2, 5]
    >>> get_path(t, 4)
    [1, 4]
    """
    result = []
    if t.value == value:
        return [t.value]
    else:
        for child in t.children:
            result = get_path(child, value)
            if result != []:
                return [t.value] + result
        return []







    #
    # if t.value == value:
    #     return [t.value]
    # else:
    #     for child in t.children:
    #         child_lst = get_path(child, value)
    #         if child_lst:
    #             return [t.value] + child_lst
    #     return []
    #

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

    example_tree = Tree('A', [Tree('T',[Tree('E'), Tree('A',[Tree('C'),Tree('H')])]), Tree('H'), Tree('S',[Tree('I')])])######

    print( Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)]))

    import doctest
    doctest.testmod()