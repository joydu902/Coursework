"""
The BinarySearchTree class from Week 11.
"""
from typing import Any, List


class BinarySearchTree:
    """
    A class representing a BinarySearchTree.

    value - The value of the BinarySearchTree's root
    left - The root node of this BinarySearchTree's left subtree.
    right - The root node of this BinarySearchTree's right subtree.
    """
    value: Any
    left: 'BinarySearchTree'
    right: 'BinarySearchTree'

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


def contains(t: BinarySearchTree, value: Any) -> bool:
    """
    Return whether value appears in t or not.

    >>> contains(None, 2)
    False
    >>> contains(BinarySearchTree(4, BinarySearchTree(2), BinarySearchTree(6,
    ...                                                   BinarySearchTree(5))),
    ...          2)
    True
    """
    if t is None:
        return False
    if t.value == value:
        return True
    if t.value < value:
        return contains(t.right, value)
    if t.value > value:
        return contains(t.left, value)


def insert(t: BinarySearchTree, value: Any) -> bool:
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


def find_max(t: BinarySearchTree) -> Any:
    """
    Return the highest value in t.

    Pre-condition: t is not None

    >>> find_max(BinarySearchTree(4, BinarySearchTree(2),
    ...                              BinarySearchTree(6, BinarySearchTree(5))))
    6
    """
    if t.right:
        return find_max(t.right)
    else:
        return t.value


def delete(t: BinarySearchTree, value: Any) -> Any:
    """
    Delete value from t, maintaining the BinarySearchTree properties. Return
    the root node of t.

    >>> print(delete(None, 2))
    None
    >>> print(delete(BinarySearchTree(4, BinarySearchTree(2),
    ...                                  BinarySearchTree(6,
    ...                                      BinarySearchTree(5))), 2))
      4
            6
         5
    """
    if t is None:
        return None
    if t.value > value:
        t.left = delete(t.left, value)
    elif t.value < value:
        t.right = delete(t.right, value)
    else:
        if not t.left and not t.right:
            return None
        if not t.left and t.right:
            return t.right
        if t.left and not t.right:
            return t.left
        else:
            maxleft = find_max(t.left)
            t.value = maxleft
            delete(t.left, maxleft)
    return t



if __name__ == '__main__':
    import doctest
    doctest.testmod()