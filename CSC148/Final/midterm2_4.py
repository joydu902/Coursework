from typing import List, Union, Type, Any, Callable
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


def is_partitioned(t: Union['BinaryTree', None]) -> bool:
    """
    Return True if all values in t.left are less than all values in t.right
    and all of the subtrees in t are also partitioned.

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> is_partitioned(t)
    False
    >>> t2 = BinaryTree(10, BinaryTree(3), BinaryTree(6))
    >>> is_partitioned(t2)
    True
    """
    if t is None:
        return True

    if bt_get_max(t.left) > bt_get_min(t.right):
        return False

    return is_partitioned(t.left) and is_partitioned(t.right)



def could_be_a_linked_list(t: Union['BinaryTree', None]) -> bool:
    """
    Return True if t could be a linked list (i.e. all trees in t have at most
    1 subtree).

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> could_be_a_linked_list(t)
    False
    """
    if t is None:
        return True

    if t.left and t.right:
        return False

    return could_be_a_linked_list(t.left) and could_be_a_linked_list(t.right)



class LinkedListNode:
    """
    A LinkedListNode class for turns_to_linked_list()

    value - The value of this LinkedListNode
    next_ - The next LinkedListNode in this LinkedList.
    """
    value: Any
    next_: Union['LinkedListNode', None]

    def __init__(self, value: Any,
                 next_: Union['LinkedListNode', None]) -> None:
        """
        Initialize this LinkedListNode with value value and next_ next_.
        """
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedListNode.
        """
        if self.next_ is None:
            return "{} -> |".format(self.value)

        return "{} -> {}".format(self.value, str(self.next_))


def turns_to_linked_list(t: Union['BinaryTree', None]) -> LinkedListNode:
    """
    Return a LinkedListNode that is the front of the LinkedList formed by
    turning t into a LinkedList.

    Pre-condition: could_be_a_linked_list(t) returns True.

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, None,
    ...                                                BinaryTree(2))))
    >>> could_be_a_linked_list(t)
    True
    >>> print(turns_to_linked_list(t))
    10 -> 3 -> 8 -> 2 -> |
    """
    if t is None:
        return None

    if t.left:
        child = t.left
    else:
        child = t.right

    return LinkedListNode(t.value, turns_to_linked_list(child))


# def bt_level_sums(t: Union['BinaryTree', None]) -> List[int]:
#     """
#     Return a list containing the sum of each level of this BinaryTree.
#
#     >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
#     ...                                                BinaryTree(2))),
#     ...                    BinaryTree(4, BinaryTree(5),
#     ...                                  BinaryTree(6, BinaryTree(7))))
#     >>> bt_level_sums(t)
#     [10, 7, 19, 10]
#     """

def bt_level_sums_using_depth(t: Union['BinaryTree', None]) -> List[int]:
    """
    Return a list containing the sum of each level of this BinaryTree.

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_level_sums_using_depth(t)
    [10, 7, 19, 10]
    """
    max_depth = bt_get_max_depth(t)
    result = []
    for i in range(max_depth + 1):
        result.extend([sum(bt_get_values_at_depth(t, i))])
    return result

def bt_get_max_depth(t: Union['BinaryTree', None]) -> int:
    """
    Return the maximum depth of this BinaryTree.

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_max_depth(t)
    3
    """
    if t is None:
        return -1

    if not t.left and not t.right:
        return 0

    return max(bt_get_max_depth(t.left), bt_get_max_depth(t.right)) + 1


def bt_get_values_at_depth(t: Union['BinaryTree', None],
                           depth: int) -> List[Any]:
    """
    Return the values at depth depth in this BinaryTree.

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_values_at_depth(t, 2)
    [8, 5, 6]
    """
    if t is None:
        return []
    if depth == 0:
        return [t.value]
    return bt_get_values_at_depth(t.left, depth - 1) + bt_get_values_at_depth(t.right, depth - 1)


def bt_level_sums_using_queue(t: Union['BinaryTree', None]) -> List[int]:
    """
    Return a list containing the sum of each level of this BinaryTree.


    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_level_sums_using_queue(t)
    [10, 7, 19, 10]
    """
    q = [t, "END"]
    all_sums = []
    current_sum = 0
    add_to_list = False

    while q:
        item = q.pop(0)
        if item == "END":
            if add_to_list:
                all_sums.append(current_sum)
            add_to_list = False
            current_sum = 0
            if q:
                q.append("END")
        else:
            if item is not None:
                current_sum += item.value
                q.append(item.left)
                q.append(item.right)
                add_to_list = True

    return all_sums
def bt_get_condition_passers(t: Union['BinaryTree', None],
                             f: Callable) -> List[Any]:
    """
    Return all of the items in t that pass f in pre-order.

    >>> def less_than_7(val):
    ...     return val < 7

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_condition_passers(t, less_than_7)
    [3, 1, 2, 4, 5, 6]
    """
    if t is None:
        return []
    if f(t.value):
        result = [t.value]
    else:
        result = []
    return result + bt_get_condition_passers(t.left, f) + bt_get_condition_passers(t.right, f)


def bt_get_condition_passers_postorder(t: Union['BinaryTree', None],
                                       f: Callable) -> List[Any]:
    """
    Return all of the items in t that pass f in post-order.

    >>> def less_than_7(val):
    ...     return val < 7
    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_condition_passers_postorder(t, less_than_7)
    [1, 2, 3, 5, 6, 4]
    """
    if t is None:
        return []
    if f(t.value):
        result = [t.value]
    else:
        result = []
    return bt_get_condition_passers_postorder(t.left, f) + bt_get_condition_passers_postorder(t.right, f) + result


def bt_get_condition_passers_inorder(t: Union['BinaryTree', None],
                                     f: Callable) -> List[Any]:
    """
    Return all of the items in t that pass f in in-order.

    >>> def less_than_7(val):
    ...     return val < 7
    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_condition_passers_inorder(t, less_than_7)
    [1, 2, 3, 5, 4, 6]
    """
    if t is None:
        return []
    if f(t.value):
        result = [t.value]
    else:
        result = []
    return bt_get_condition_passers_inorder(t.left, f) + result + bt_get_condition_passers_inorder(t.right, f)


def bt_get_condition_passers_levelorder(t: Union['BinaryTree', None],
                                        f: Callable) -> List[Any]:
    """
    Return all of the items in t that pass f in pre-order.

    >>> def less_than_7(val):
    ...     return val < 7
    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_condition_passers_levelorder(t, less_than_7)
    [3, 4, 5, 6, 1, 2]
    """
    q = [t]
    passers = []
    while q:
        item = q.pop(0)
        if item != None:
            if f(item.value):
                passers.append(item.value)
            q.append(item.left)
            q.append(item.right)
    return passers


def bt_get_longest_path(t: Union['BinaryTree', None]) -> List[Any]:
    """
    Return the longest path in this BinaryTree from the root to a leaf.

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_longest_path(t)
    [10, 3, 8, 1]
    """

    if t is None:
        return []
    left_path = bt_get_longest_path(t.left)
    right_path = bt_get_longest_path(t.right)

    if len(right_path) > len(left_path):
        return [t.value] + right_path
    else:
        return [t.value] + left_path


def bt_all_values_in_tree(t: Union['BinaryTree', None],
                          values: List[Any]) -> bool:
    """
    Return True iff all values in values are in this BinaryTree.

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_all_values_in_tree(t, [3, 1, 4])
    True
    >>> bt_all_values_in_tree(t, [3, 9])
    False
    """
    if t is None:
        return values == []
    if t.value in values:
        values.remove(t.value)
    if values == []:
        return True
    return bt_all_values_in_tree(t.left, values) or bt_all_values_in_tree(t.right, values)


def bt_count_strings_with_length(t: Union['BinaryTree', None]) -> dict:
    """
    Return a dictionary mapping the length of each word in this BinaryTree
    to the number of times that length appears.

    >>> t = BinaryTree('cat', BinaryTree('a', BinaryTree('dog', BinaryTree('b'),
    ...                                                  BinaryTree('no'))),
    ...                       BinaryTree('yes'))
    >>> bt_count_strings_with_length(t)
    {3: 3, 1: 2, 2: 1}
    """
    if t is None:
        return {}
    new_dict = {len(t.value): 1}
    for child in [t.left, t.right]:
        lengths = bt_count_strings_with_length(child)
        for key in lengths:
            if key in new_dict:
                new_dict[key] += lengths[key]
            else:
                new_dict[key] = lengths[key]
    return new_dict


def bt_return_values_with_type(t: Union['BinaryTree', None],
                               type_: Type) -> List[Any]:
    """
    Return all of the values in this BinaryTree that have type t.

    >>> t = BinaryTree(1, BinaryTree(3),
    ...                   BinaryTree('yes', BinaryTree('b'),
    ...                                     BinaryTree(2)))
    >>> bt_return_values_with_type(t, int)
    [1, 3, 2]
    """
    if t is None:
        return []
    if isinstance(t.value, type_):
        result = [t.value]
    else:
        result = []
    return result + bt_return_values_with_type(t.left, type_) + bt_return_values_with_type(t.right, type_)


def bt_get_max(t: Union['BinaryTree', None]) -> int:
    """
    Return largest int in this BinaryTree.
    If t is an empty BinaryTree, return -1.

    Pre-condition: All ints in t > -1

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_max(t)
    10
    """
    if t is None:
        return -1
    return max([t.value, bt_get_max(t.left), bt_get_max(t.right)])


def bt_get_min(t: Union['BinaryTree', None]) -> int:
    """
    Return smallest int in this BinaryTree.
    If t is an empty BinaryTree, return -1.

    Pre-condition: All ints in t > -1

    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1),
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5),
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_get_min(t)
    1
    """
    if t is None:
        return -1

    left_min = bt_get_min(t.right)
    right_min = bt_get_min(t.left)

    if left_min == -1:
        left_min = t.value
    if right_min == -1:
        right_min = t.value

    return min([t.value, left_min, right_min])


def bt_all_true(t: Union['BinaryTree', None]) -> bool:
    """
    Return True if all booleans in this BinaryTree are True.

    >>> t = BinaryTree(True, BinaryTree(True, BinaryTree(True, BinaryTree(True),
    ...                                                  BinaryTree(True))),
    ...                      BinaryTree(False, BinaryTree(True),
    ...                                 BinaryTree(True, BinaryTree(True))))
    >>> bt_all_true(t)
    False
    """
    if t is None:
        return True
    if not t.value:
        return False
    return all([bt_all_true(t.left), bt_all_true(t.right)])


def bt_any_true(t: Union['BinaryTree', None]) -> bool:
    """
    Return True if any booleans in this BinaryTree are True.

    >>> t = BinaryTree(True, BinaryTree(True, BinaryTree(True, BinaryTree(True),
    ...                                                  BinaryTree(True))),
    ...                      BinaryTree(False, BinaryTree(True),
    ...                                 BinaryTree(True, BinaryTree(True))))
    >>> bt_any_true(t)
    True
    """
    if t is None:
        return False
    if t.value:
        return True
    return any([bt_any_true(t.left), bt_any_true(t.right)])






if __name__ == '__main__':
    import doctest
    doctest.testmod()
