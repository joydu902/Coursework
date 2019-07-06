from typing import Union, Any, List


def count_odd(x: Union[int, list]) -> int:
    """
    Return the number of odd elements in x.
    If x is an int, return 1 if x is odd.

    >>> count_odd(1)
    1
    >>> count_odd(0)
    0
    >>> count_odd([1, 2, [3], [[4], [5, 6, 7]]])
    4
    """
    count = 0
    if isinstance(x, int):
        if x % 2 == 1:
            return 1
        else:
            return 0
    else:
        for item in x:
            count += count_odd(item)
        return count


def count_longer_than(x: Union[str, list], length: int) -> int:
    """
    Return the number of strings in x with a length greater than length.
    If x is an str, return 1 if x is longer than length.

    >>> count_longer_than('ab', 1)
    1
    >>> count_longer_than('ab', 2)
    0
    >>> count_longer_than(['a', ['ab', 'abc'], [['abcd'], ['d', ['def']]]], 2)
    3
    """
    count = 0
    if isinstance(x, str):
        if len(x) > length:
            return 1
        else:
            return 0
    else:
        for item in x:
            count += count_longer_than(item, length)
        return count


def get_max_depth(x: Union[list, Any]) -> int:
    """
    Return the maximum depth of x.
    If x is not a list, return 0.

    >>> get_max_depth(0)
    0
    >>> get_max_depth([1, 2, [3]])
    2
    >>> get_max_depth([1, 2, [3], [[4], [5, 6, 7]]])
    3
    """
    if not isinstance(x, list):
        return 0
    else:
        result = []
        for item in x:
            result += get_max_depth(item)
        return max(result) + 1


    # result = []
    # if not isinstance(x, list):
    #     return 0
    # else:
    #     for item in x:
    #         result += [get_max_depth(item)]
    #     return max(result) + 1


def get_at_depth(x: Union[list, Any], depth: int) -> list:
    """
    Return all non-list elements at a depth of x.

    >>> get_at_depth(0, 2)
    []
    >>> get_at_depth(1, 0)
    [1]
    >>> get_at_depth([1, 2, [3]], 1)
    [1, 2]
    >>> get_at_depth([1, 2, [3], [[4], [5, 6, 7], 8]], 2)
    [3, 8]
    """
    result = []
    if not isinstance(x, list):
        if depth == 0:
            return [x]
        else:
            return []
    else:
        for item in x:
            result.extend(get_at_depth(item, depth -1))
        return result

#Tree
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
        if self.value == value:
            count = 1
        else:
            count = 0
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
        if self.children:
            result = [self.value]
        else:
            result = []
        for child in self.children:
            result.extend(child.get_internal_values())
        return result


    def get_depth_of(self, value: Any) -> int:
        """
        Return the depth of value in this Tree.
        If value is not in this Tree, return -1.

        >>> large_tree.get_depth_of(3)
        2
        >>> large_tree.get_depth_of(5)

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
        else:
            for child in self.children:
                result.extend(child.get_values_at_depth(depth - 1))
            return result

    def get_max_branching_factor(self) -> int:########
        """
        Return the maximum branching factor in this Tree.

        >>> large_tree.get_max_branching_factor()
        4
        """
        mm = 0
        result = []
        if self.children == []:
            return 0
        for child in self.children:
            result.extend([child.get_max_branching_factor()])
            mm = max(result)
        return max(mm, len(self.children))

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
            copy_s += [child.copy()]
        return Tree(self.value, copy_s)


        # copy_s = []
        # for child in self.children:
        #     copy_s += [child.copy()]
        # return Tree(self.value, copy_s)

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
            item = q.pop(0)
            print(item)
            for child in item.children:
                q.append(child)

        # q = [self]
        # while q:
        #     front = q.pop(0)
        #     print(front.value)
        #     for child in front.children:
        #         q.append(child)

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



        # if self.value == value:
        #     self.children.append(subtree)
        #     return True
        # for child in self.children:
        #     result = child.add_subtree_to(subtree, value)
        #     if result:
        #         return True
        # return False

#lab7
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
    if not t:
        return []
    if not t.left and not t.right:
        return []
    else:
        return [t.value] + get_internal_values(t.left) + get_internal_values(t.right)


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
    if t is None:
        return -1
    else:
        return 1 + max([get_max_depth(t.left), get_max_depth(t.right)])

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
        return 1 + get_depth_of(t.left, value)
    if get_depth_of(t.right, value) > -1:
        return 1 + get_depth_of(t.right, value)




    # if t is None:
    #     return -1
    # if t.value == value:
    #     return 0
    # if get_depth_of(t.left, value) > -1:
    #     return 1 + get_depth_of(t.left, value)
    # if get_depth_of(t.right, value) > -1:
    #     return 1 + get_depth_of(t.right, value)
    #

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
    else:
        return get_values_at_depth(t.left, depth - 1) + get_values_at_depth(t.right, depth - 1)

def copy(t: Union[BinaryTree, None]) -> Union[BinaryTree, None]:
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
    if not t:
        return None
    else:
        return BinaryTree(t.value, copy(t.left), copy(t.right))


def print_level_order(t: Union[BinaryTree, None]) -> None:
    """
    Print the elements in t in level order.

    >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
    >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
    >>> t = BinaryTree(0, t1, t2)
    >>> print(t)
                  0
               1        9
         3           7     5
      4     6
    >>> print_level_order(t)
    0
    1
    9
    3
    7
    5
    4
    6
    """
    q = [t]
    while q:
        removed = q.pop(0)
        if removed:
            print(removed.value)
            q.append(removed.left)
            q.append(removed.right)


def insert_before(t: Union[BinaryTree, None], to_insert: Any,
                  to_find: Any) -> Union[BinaryTree, None]:
    """
    Return the root of the tree t after inserting to_insert before every
    occurrence of to_find.

    >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(1)))
    >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
    >>> t = BinaryTree(1, t1, t2)
    >>> print(t)
                  1
               1        9
         3           7     5
      4     1
    >>> print(insert_before(t, 11, 1))
                                      11
                          1
                      11        9
                   1         7     5
         3
      4        11
            1
    """
    new_root = t
    if t is None:
        return None
    if t.value == to_find:
        new_root = BinaryTree(to_insert, t)
    t.left = insert_before(t.left, to_insert, to_find)
    t.right = insert_before(t.right, to_insert, to_find)
    return new_root



    # if t is None:
    #     return None
    # new_root = t
    # if t.value == to_find:
    #     new_root = BinaryTree(to_insert, t)
    # t.left = insert_before(t.left, to_insert, to_find)
    # t.right = insert_before(t.right, to_insert, to_find)
    #
    # return new_root

#midetem2 practice

def count_elements_in(x: Union[list, int], to_count: List[int]) -> int:
    """
    Return a count of how many elements in x appear in to_count.

    >>> count_elements_in(1, [1, 3, 5])
    1
    >>> count_elements_in([[1, 2], [3, [[4], 1], [5], [[7, 8], 1], 5], 3],
    ...                   [1, 3, 5])
    7
    """
    count = 0
    if isinstance(x, int):
        if x in to_count:
            return 1
        else:
            return 0
    else:
        for item in x:
            count += count_elements_in(item, to_count)
        return count


def sum_at_depth(x: Union[list, int], depth: int) -> int:
    """
    Return the sum of all elements at depth depth in x.

    >>> sum_at_depth(1, 1)
    0
    >>> sum_at_depth([1, [3, [4, 5, [[6]]], 7], [2, [10]]], 2)
    12
    """
    result = 0
    if isinstance(x, int):
        if depth == 0:
            return x
        else:
            return 0
    else:
        for item in x:
            result += sum_at_depth(item, depth -1)
        return result


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

    def __eq__(self, other: Any) -> bool:
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

    def able_to_spell(self, word: str) -> bool:#########
        """
        Return whether a path from one node to another (from lowest to highest)
        contains all of the letters needed to spell word.

        (Original wording of the question was wrong.)

        >>> t = Tree('A', [Tree('T', [Tree('E'),
        ...                          Tree('A', [Tree('C'), Tree('H')])]),
        ...                      Tree('H'),
        ...                      Tree('S', [Tree('I')])])
        >>> t.able_to_spell('CAT')
        True
        >>> t.able_to_spell('HI')
        False
        """
        if word == '':
            return True

        if self.value == word[-1]:
            new_word = word[:-1]
            if new_word == '':
                return True
            for child in self.children:
                if child.able_to_spell(new_word):
                    return True
        for child in self.children:
            if child.able_to_spell(word):
                return True
        return False



#
# class BinaryTree:
#     """
#     A class representing a BinaryTree.
#
#     value - The value of the root of this BinaryTree.
#     left - The left subtree of this BinaryTree.
#     right - The right subtree of this BinaryTree.
#     """
#     value: Any
#     left: Union['BinaryTree', None]
#     right: Union['BinaryTree', None]
#
#     def __init__(self, value: Any, left: Union['BinaryTree', None] = None,
#                  right: Union['BinaryTree', None] = None) -> None:
#         """
#         Initialize this BinaryTree with the value value, left subtree left,
#         and right subtree right.
#         """
#         self.value = value
#         self.left = left
#         self.right = right

    # def __eq__(self, other: Any) -> bool:
    #     """
    #     Return True iff this BinaryTree and other have the same values and
    #     subtrees.
    #
    #     >>> BinaryTree(4) == BinaryTree(4)
    #     True
    #     >>> BinaryTree(4, BinaryTree(5)) == BinaryTree(4, None, BinaryTree(5))
    #     False
    #     """
    #     if self.value != other.value:
    #         return False
    #     else:
    #         return self.left == other.left and self.right == other.right



    # def rotate_left(t: 'BinaryTree') -> 'BinaryTree':
    #     """
    #     Return the root of t after left rotating it.
    #
    #     >>> t = BinaryTree(1, BinaryTree(2), BinaryTree(3))
    #     >>> rotated_t = rotate_left(t)
    #     >>> rotated_t.value
    #     3
    #     >>> rotated_t.left.value
    #     1
    #     >>> rotated_t.left.left.value
    #     2
    #     """
    #     # If we don't have anything to rotate, just return None.
    #     if t is None or t.right is None:
    #         return None
    #
    #     # Store the old left value of t.right
    #     old_left = t.right.left
    #
    #     # We want t.right to be the new root:
    #     new_root = t.right
    #
    #     # And we want t to the its new left value
    #     new_root.left = t
    #
    #     # And we want the old left value to be t's new right value:
    #     t.right = old_left
    #
    #     # Lastly, return the new root
    #     return new_root



if __name__ == '__main__':

    # assert count_odd(1) == 1
    # assert count_odd(2) == 0
    # assert count_odd([1, 3, 4]) == 2
    # assert count_odd([[1, 5, [[4, 6], 7]], 9]) == 4
    # assert count_odd([1, [2, 3], [4, [5], [[6, 7], 8], 9]]) == 5
    #
    # assert count_longer_than('cat', 3) == 0
    # assert count_longer_than('cat', 2) == 1
    # assert count_longer_than(['', 'a', 'at', 'hat'], 1) == 2
    # assert count_longer_than([['yes', 'no', [['ok', 'hat'], 'cat']], 'a'],
    #                          2) == 3
    # assert count_longer_than(['a', [['baby'], 'cat'],
    #                           [['doll'], 'hat', [['cake'], 'hats']]], 3) == 4
    #
    # assert get_max_depth(5) == 0
    # assert get_max_depth([1, 2, 3]) == 1
    # assert get_max_depth([[1], 2]) == 2
    # assert get_max_depth([1, [[3]], 8]) == 3
    # assert get_max_depth([1, [2, [3]], [[[4]], 5]]) == 4
    #
    # assert get_at_depth(5, 0) == [5]
    # assert get_at_depth(5, 1) == []
    # assert get_at_depth([1, 2, 3], 1) == [1, 2, 3]
    # assert get_at_depth([[1], 2, [3], 4], 1) == [2, 4]
    # assert get_at_depth([1, [[3], 2, [4]], 8, [[5]]], 3) == [3, 4, 5]
    # assert get_at_depth([1, [2, [3]], [[[4], 6], 5]], 3) == [3, 6]

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


    import doctest
    doctest.testmod()

