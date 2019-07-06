"""
The BinaryTree class from Week 10.
"""
from typing import Any, List

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
            children.append(self.left)

        if self.right:
            children.append(self.right)

        child_strings = [str(child).split('\n') for child in children]

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

    def __eq__(self, other: Any) -> bool:
        """
        Return True iff this BinaryTree and other have the same values and
        subtrees.

        >>> BinaryTree(4) == BinaryTree(4)
        True
        >>> BinaryTree(4, BinaryTree(5)) == BinaryTree(4, None, BinaryTree(5))
        False
        """
        if not isinstance(other, BinaryTree):
            return False

        if self.value != other.value:
            return False

        return self.left == other.left and self.right == other.right

def get_values(t: BinaryTree) -> List:
    """
    Return a list of values in t.

    >>> get_values(None)
    []
    >>> get_values(BinaryTree(0, BinaryTree(3), BinaryTree(2, BinaryTree(1))))
    [0, 3, 2, 1]
    """
    if t is None:
        return []
    else:
        return [t.value] + get_values(t.left) + get_values(t.right)

def count_occurrences(t: BinaryTree, value: Any) -> int:
    """
    Return the number of times value appears in t.

    >>> count_occurrences(None, 2)
    0
    >>> count_occurrences(BinaryTree(2, BinaryTree(3), BinaryTree(2, BinaryTree(1))), 2)
    2
    """
    if t is None:
        return 0
    if t.value == value:
        count = 1
    else:
        count = 0
    return count + count_occurrences(t.right, value) + count_occurrences(t.left, value)


def contains(t: BinaryTree, value: Any) -> bool:
    """
    Return whether value appears in t or not.

    >>> contains(None, 2)
    False
    >>> contains(BinaryTree(0, BinaryTree(3), BinaryTree(2, BinaryTree(1))), 2)
    True
    """
    if t is None:
        return False
    else:
        if t.value == value:
            return True
        return contains(t.left, value) or contains(t.right, value)


def get_height(t: BinaryTree) -> int:
    """
    Return the height of t.

    >>> get_height(None)
    0
    >>> get_height(BinaryTree(0, BinaryTree(3), BinaryTree(2, BinaryTree(1))))
    3
    """
    if t is None:
        return 0
    else:
        return 1 + max(get_height(t.left), get_height(t.right))


def get_result(t: BinaryTree) -> int:
    """
    Return the result of evaluating t.

    Precondition: t is an arithmetic binary tree.

    >>> get_result(BinaryTree(1))
    1
    >>> get_result(BinaryTree('+', BinaryTree(3), BinaryTree('*', BinaryTree(4), BinaryTree(2))))
    11
    """
    if t.left is None and t.right is None:
        return t.value
    else:
        left = get_result(t.left)
        right = get_result(t.right)
    if t.value == '+':
        return left + right
    if t.value == '*':
        return left * right


def print_preorder(t: BinaryTree) -> str:
    """
    Return the height of t.

    >>> print_preorder(None)
    >>> print_preorder(BinaryTree(0, BinaryTree(3), BinaryTree(2,
    ...                                                        BinaryTree(1))))
    0
    3
    2
    1
    """
    if t is None:
        return
    else:
        print(t.value)
        print_preorder(t.left)
        print_preorder(t.right)


def print_postorder(t: BinaryTree) -> str:
    """
    Return the height of t.

    >>> print_postorder(None)
    >>> print_postorder(BinaryTree(0, BinaryTree(3), BinaryTree(2,
    ...                                                         BinaryTree(1))))
    3
    1
    2
    0
    """
    if t is None:
        return
    else:
        print_postorder(t.left)
        print_postorder(t.right)
        print(t.value)

def print_inorder(t: BinaryTree) -> str:
    """
    Return the height of t.

    >>> print_inorder(None)
    >>> print_inorder(BinaryTree(0, BinaryTree(3), BinaryTree(2,
    ...                                                       BinaryTree(1))))
    3
    0
    1
    2
    """
    if t is None:
        return
    else:
        print_inorder(t.left)
        print(t.value)
        print_inorder(t.right)

#Midterm Practice
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
    #
    #     return self.left == other.left and self.right == other.right


def rotate_left(t: 'BinaryTree') -> 'BinaryTree':
    """
    Return the root of t after left rotating it.

    >>> t = BinaryTree(1, BinaryTree(2), BinaryTree(3))
    >>> rotated_t = rotate_left(t)
    >>> rotated_t.value
    3
    >>> rotated_t.left.value
    1
    >>> rotated_t.left.left.value
    2
    """
    # If we don't have anything to rotate, just return None.
    if t is None or t.right is None:
        return None

    # Store the old left value of t.right
    old_left = t.right.left

    # We want t.right to be the new root:
    new_root = t.right

    # And we want t to the its new left value
    new_root.left = t

    # And we want the old left value to be t's new right value:
    new_root.left.right = old_left

    # Lastly, return the new root
    return new_root


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    tt1 = BinaryTree(1, BinaryTree(8) , BinaryTree(4))
    tt2 = BinaryTree(2, BinaryTree(7), tt1)
    example_binary_tree = BinaryTree(6, tt2, BinaryTree(3))
