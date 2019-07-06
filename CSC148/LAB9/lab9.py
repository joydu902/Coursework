"""
Solutions to Lab 8
"""
from typing import Any, List, Union


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


def insert(t: Union['BinarySearchTree', None], value: Any):
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


def find_min(t: 'BinarySearchTree') -> int:
    """
    Return the minimum value in t.
    """
    # We keep looking as far left as we possibly can and
    # return the leftmost value.
    if t.left:
        return find_min(t.left)
    else:
        return t.value


    # if t.left:
    #     return find_min(t.left)
    #
    # return t.value


def delete_right(t: Union['BinarySearchTree', None],
                 value: Any) -> Union['BinarySearchTree', None]:
    """
    Delete a node by swapping with the smallest value in the right subtree.
    Return the root of t.
    """
    if t is None:
        return None

    if value < t.value:
        t.left = delete_right(t.left, value)
    elif value > t.value:
        t.right = delete_right(t.right, value)
    else:
        # t.value == value in this case
        if not t.left and not t.right:
            return None

        if t.left and not t.right:
            return t.left

        if t.right and not t.left:
            return t.right

        min_value = find_min(t.right)
        t.value = min_value
        t.right = delete_right(t.right, min_value)

    return t


def find_max(t: 'BinarySearchTree') -> int:
    """
    Return the maximum value in t.
    (To help with is_valid_bst)
    """
    if t.right:
        return find_max(t.right)

    return t.value


def is_valid_bst(t: Union['BinarySearchTree', None]) -> bool:
    """
    Return True if t is a valid BST.
    """
    # The runtime of this is n * height
    # find_max and find_min take O(height) at worst, and this gets
    # called for every single node in the BST, which is n node.
    # Hence a runtime of O(n * height)
    # Best-case: O(nlgn) -- this is for a completely balanced BST
    # Worst-case: O(n^2) -- this is for a completely unbalanced BST
    if t is None:
        return True
    if t.left and find_max(t.left) > t.value:
        return False
    if t.right and find_min(t.right) < t.value:
        return False
    return is_valid_bst(t.left) and is_valid_bst(t.right)


    # if t is None:
    #     return True
    #
    # if t.left is not None and find_max(t.left) > t.value:
    #     return False
    #
    # if t.right is not None and find_min(t.right) < t.value:
    #     return False
    #
    # return is_valid_bst(t.left) and is_valid_bst(t.right)


def count_nodes(t: Union['BinarySearchTree', None]) -> int:
    """
    Return the number of nodes in t.
    """
    # The runtime of this is always O(n). No matter what,
    # we have to check every node in the BST once.
    if t is None:
        return 0
    else:
        return 1 + count_nodes(t.left) + count_nodes(t.right)

    # if t is None:
    #     return 0
    #
    # return 1 + count_nodes(t.left) + count_nodes(t.right)
    #

def find_nth_smallest(t: Union['BinarySearchTree', None], n: int) -> int:
    """
    Return the nth smallest value in t.

    If such a value doesn't exist, return -1 instead.
    (Or some other arbitrary value; we'll just pretend this BST only has
    positive numbers in it)
    """
    if t is None:
        return -1
    left_count = count_nodes(t.left)
    if n < left_count:
        return find_nth_smallest(t.left, n)
    if n == left_count + 1:
        return t.value
    else:
        return find_nth_smallest(t.right, n - (left_count + 1))


    # # If we have no nodes to check, just return -1.
    # if t is None:
    #     return -1
    #
    # left_count = count_nodes(t.left)
    #
    # # If n <= the number of nodes in the left subtree, then we return the
    # # nth smallest in the left subtree.
    # if n <= left_count:
    #     return find_nth_smallest(t.left, n)
    #
    # # If n == the number of nodes in the left subtree + 1, then this node's
    # # value is the nth smallest
    # # (e.g. if there are 0 items in the left subtree and n == 1, then that means
    # # the root is the smallest)
    # if n == left_count + 1:
    #     return t.value
    #
    # # Otherwise, we search the right subtree, but n is reduced by left_count + 1
    # return find_nth_smallest(t.right, n - (left_count + 1))


def rotate_right(t: Union['BinarySearchTree', None]) -> Union['BinarySearchTree', None]:
    """
    Rotate a BST clockwise.
    """
    if t is None:
        return None

    if t.left is None:
        return t

    # The root of the left subtree becomes the new root of this BST
    new_root = t.left

    # The new root's right subtree becomes t's new left subtree
    t.left = new_root.right

    # The old root is now the new root's right subtree
    new_root.right = t

    return new_root

# def count_edges_to_root(t: Union['BinarySearchTree', None], value: int) -> int:
#     if t is None:
#         return -1
#     edges = 0
#     if t.value == value:
#         edges += 1
#     if count_edges_to_root(t.left, value) >= 0:
#         edges += 1
#     if count_edges_to_root(t.right, value) >= 0:
#         edges += 1
#     return edges

def count_edges_to_root(t: Union['BinarySearchTree', None], value: int) -> int:
    if t is None:
        return -1
    if t.value == value:
        return 0
    else:
        if t.value > value:
            return 1 + count_edges_to_root(t.left, value)
        else:
            return 1 + count_edges_to_root(t.right, value)

def FCP(t: Union['BinarySearchTree', None], k: int, m:int) -> int:
    root = t.value
    if t.value > max(k, m):
        return FCP(t.left, k, m)
    elif t.value < min(k, m):
        return FCP(t.right, k, m)
    else:
        return root

def Istaway(t: Union['BinarySearchTree', None], k: int, m:int, tt:int) -> bool:
    fcp = FCP(t, k, m)
    return (count_edges_to_root(fcp, k) + count_edges_to_root(fcp, m)) <= tt



if __name__ == '__main__':
    t = BinarySearchTree(10)
    insert(t, 8)
    insert(t, 6)
    insert(t, 9)
    insert(t, 12)

    tt = BinarySearchTree(30)
    insert(tt, 10)
    insert(tt, 7)
    insert(tt, 15)
    insert(tt, 20)
    insert(tt, 45)
    insert(tt, 33)
    insert(tt, 50)
    insert(tt, 47)
    print(tt)

    print(count_edges_to_root(tt, 47))
    print(FCP(tt, 15, 45))
    print(FCP(tt, 7, 20))
    print(FCP(tt, 50, 47))
    print(Istaway(tt, 15, 45, 3))
    print(Istaway(tt, 7, 20, 2))




    import doctest

    doctest.testmod()
    # # Inserting in level-order (or relative to each subtree at least) will give
    # # us the BST that we want
    # large_tree = BinarySearchTree(7)
    # insert(large_tree, 4)
    # insert(large_tree, 15)
    # insert(large_tree, 1)
    # insert(large_tree, 10)
    # insert(large_tree, 18)
    # insert(large_tree, 3)
    # insert(large_tree, 8)
    # insert(large_tree, 12)
    # insert(large_tree, 2)


    # For the Tree t, if we inserted 6 before 8, then 6 would be the
    # root of the left subtree, and 8 would be its right child, with 9
    # being the right child of 8.

    # Inserting 9 before 8 (but after 6) would result in 9 being the
    # right subtree of 6, and 8 being the left subtree of 9.
