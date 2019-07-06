"""
Solutions to Midterm 2 Practice (Part 2)
"""
from typing import List, Union, Type, Any, Callable

# Practice Problems: Recursion with Nested Lists
# def count_strings_with_length(x: Union[list, str]) -> dict:
#     """
#     Return a dictionary mapping the length of each word in x to the number of
#     times that length appears.
#
#     >>> count_strings_with_length('cat')
#     {3: 1}
#     >>> count_strings_with_length(['cat', ['a', 'dog'], [[['b'], 'no'], 'yes']])
#     {3: 3, 1: 2, 2: 1}
#     """
#     if isinstance(x, str):
#         return {len(x): 1}
#
#     new_dict = {}
#     for word in x:
#         lengths = count_strings_with_length(word)
#         for key in lengths:
#             if key in new_dict:
#                 new_dict[key] += lengths[key]
#             else:
#                 new_dict[key] = lengths[key]
#
#     return new_dict

def count_strings_with_length(x: Union[list, str]) -> dict:
    """
    Return a dictionary mapping the length of each word in x to the number of
    times that length appears.

    >>> count_strings_with_length('cat')
    {3: 1}
    >>> count_strings_with_length(['cat', ['a', 'dog'], [[['b'], 'no'], 'yes']])
    {3: 3, 1: 2, 2: 1}
    """
    if isinstance(x, str):
        return {len(x): 1}
    else:
        result = {}
        for item in x:
            temp = count_strings_with_length(item)
            for key in temp:
                if key in result:
                    result[key] += temp[key]
                else:
                    result[key] = temp[key]
        return result


def return_values_with_type(x: Any, t: Type) -> List[Any]:
    """
    Return all of the values in x that have type t.
    
    >>> return_values_with_type(1, int)
    [1]
    >>> return_values_with_type(1, str)
    []
    >>> return_values_with_type([1, [[3], 'yes'], 'b', 2], int)
    [1, 3, 2]
    """
    if not isinstance(x, list):
        return [x] if type(x) == t else []
    
    return sum([return_values_with_type(item, t) for item in x], [])

def get_max(x: Union[list, int]) -> int:
    """
    Return largest int in x.
    
    >>> get_max(1)
    1
    >>> get_max([1, [[3], 0], 2])
    3
    """
    if isinstance(x, int):
        return x
    
    return max([get_max(item) for item in x])

def get_min(x: Union[list, int]) -> int:
    """
    Return smallest int in x.
    
    >>> get_min(1)
    1
    >>> get_min([1, [[3], 0], 2])
    0
    """
    if isinstance(x, int):
        return x
    
    return min([get_min(item) for item in x])

def all_true(x: Union[list, bool]) -> bool:
    """
    Return True if all booleans in x are True.
    
    >>> all_true(True)
    True
    >>> all_true([])
    True
    >>> all_true([True, [[False, True], True], [True]])
    False
    """
    if isinstance(x, bool):
        return x
    
    return all([all_true(item) for item in x])

def any_true(x: Union[list, bool]) -> bool:
    """
    Return True if there is at least one boolean in x that is True.
    
    >>> any_true(True)
    True
    >>> any_true([])
    False
    >>> any_true([True, [[False, True], True], [True]])
    True
    """
    if isinstance(x, bool):
        return x
    
    return any([any_true(item) for item in x])

# Practice Problems: Trees
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

    def level_sums(self) -> List[int]:
        """
        Return a list containing the sum of each level of this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.level_sums()
        [10, 15, 12, 9]
        """
        # This is just 1 of many different approaches. Other approaches include:
        #    - Writing a helper function to get the items at each depth of self
        #      and returning the sum of each of those depths.
        #      (You would also need to get the max depth too; and just get all
        #       items from depth 0 to max depth.)
        #      See level_sums_using_depth() for this solution, along with its
        #      helper functions get_values_at_depth and get_max_depth.
        # 
        #    - Using a Queue to get the items in level order; you would need
        #      to indicate the end of each level though (i.e. with a dummy
        #      value)
        #      See level_sums_using_queue() for this solution.
        
        # Get the sums from each of the children
        child_sums = [child.level_sums() for child in self.children]
        
        # Merge all of those sums into one list
        all_sums = []
        for child in child_sums:
            for i in range(len(child)):
                if i < len(all_sums):
                    all_sums[i] += child[i]
                else:
                    all_sums.append(child[i])
        
        # Add self.value to the front of all of those sums.
        return [self.value] + all_sums
    
    def level_sums_using_depth(self) -> List[int]:
        """
        Return a list containing the sum of each level of this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.level_sums_using_depth()
        [10, 15, 12, 9]
        """
        max_depth = self.get_max_depth()
        
        all_sums = []
        
        # Alternatively, use height instead of max_depth + 1.
        # These are equivalent.
        for i in range(max_depth + 1):
            all_sums.append(sum(self.get_values_at_depth(i)))
            
        return all_sums
    
    def get_max_depth(self) -> int:
        """
        Return the maximum depth of this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_max_depth()
        3
        """
        if self.children == []:
            return 0
        
        return 1 + max(child.get_max_depth() for child in self.children)

    def get_values_at_depth(self, depth: int) -> List[Any]:
        """
        Return the values at depth depth in this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_values_at_depth(2)
        [5, 6, 1]
        """
        if depth == 0:
            return [self.value]
        
        return sum([child.get_values_at_depth(depth - 1) 
                    for child in self.children], [])
    
    def level_sums_using_queue(self) -> List[int]:
        """
        Return a list containing the sum of each level of this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.level_sums_using_queue()
        [10, 15, 12, 9]
        """
        # We can use "END" to indicate the end of a level -- once we see END
        # we know we've finished going through all the items in a level.
        q = [self, "END"]

        all_sums = []
        current_sum = 0
        while q:
            item = q.pop(0)
            if item == "END":
                # When we're done with a level, add its sum to our list of
                # sums
                all_sums.append(current_sum)
                
                # Reset our sum counter to 0
                current_sum = 0
                
                # If there are still elements in q, that means there are more
                # to process. If not; that means we're done going through
                # the entire queue.
                if q:
                    q.append("END")
            else:
                current_sum += item.value
                for child in item.children:
                    q.append(child)
        return all_sums
    
    def get_condition_passers(self, f: Callable) -> List[Any]:
        """
        Return all of the items in self that pass f in pre-order.
        
        >>> def less_than_7(val):
        ...     return val < 7
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_condition_passers(less_than_7)
        [3, 4, 5, 6, 1, 2]
        """
        to_return = [self.value] if f(self.value) else []
        return to_return + \
               sum([child.get_condition_passers(f) for child in self.children],
                   [])

    def get_condition_passers_postorder(self, f: Callable) -> List[Any]:
        """
        Return all of the items in self that pass f in post-order.
        
        >>> def less_than_7(val):
        ...     return val < 7
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_condition_passers_postorder(less_than_7)
        [3, 5, 6, 4, 2, 1]
        """
        to_return = [self.value] if f(self.value) else []
        return sum([child.get_condition_passers_postorder(f) for child in self.children], []) + to_return
    

    def get_condition_passers_levelorder(self, f: Callable) -> List[Any]:
        """
        Return all of the items in self that pass f in pre-order.
        
        >>> def less_than_7(val):
        ...     return val < 7
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_condition_passers_levelorder(less_than_7)
        [3, 4, 5, 6, 1, 2]
        """
        q = [self]
        passers = []
        
        while q:
            item = q.pop(0)
            if f(item.value):
                passers.append(item.value)
            
            for child in item.children:
                q.append(child)
        
        return passers
    
    def get_longest_path(self) -> List[Any]:
        """
        Return the longest path in this Tree from the root to a leaf.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_longest_path()
        [10, 4, 6, 7]
        """
        if self.children == []:
            return [self.value]
        
        paths = [child.get_longest_path() for child in self.children]
        longest_path = paths[0]
        for path in paths:
            if len(path) > len(longest_path):
                longest_path = path
                
        return [self.value] + longest_path
    
    def all_values_in_tree(self, values: List[Any]) -> bool:
        """
        Return True iff all values in values are in this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.all_values_in_tree([3, 1, 4])
        True
        >>> t.all_values_in_tree([3, 9])
        False
        """
        # We can take advantage of the fact that lists are mutable -- if we
        # modify values and remove from it whenever we find a value.
        # Alternatively:
        #    Use a helper function that checks whether a value is in self or not
        #    and return True only iff all values in values are found.
        
        if self.value in values:
            values.remove(self.value)
            
        if values == []:
            return True
        
        return any([child.all_values_in_tree(values) for child in self.children])
    
    def count_strings_with_length(self) -> dict:
        """
        Return a dictionary mapping the length of each word in this Tree
        to the number of times that length appears.

        >>> t = Tree('cat', [Tree('a'),
        ...                  Tree('dog', [Tree('b'), 
        ...                               Tree('no', [Tree('yes')])])])
        >>> t.count_strings_with_length()
        {3: 3, 1: 2, 2: 1}
        """
        new_dict = {len(self.value): 1}
        for child in self.children:
            lengths = child.count_strings_with_length()
            for key in lengths:
                if key in new_dict:
                    new_dict[key] += lengths[key]
                else:
                    new_dict[key] = lengths[key]
        
        return new_dict
    
    def return_values_with_type(self, t: Type) -> List[Any]:
        """
        Return all of the values in this Tree that have type t.
        
        >>> t = Tree(1, [Tree(3),
        ...              Tree('yes', [Tree('b'), 
        ...                           Tree(2)])])
        >>> t.return_values_with_type(int)
        [1, 3, 2]
        """
        to_return = [self.value] if type(self.value) == t else []
        
        return to_return + \
               sum([child.return_values_with_type(t)
                    for child in self.children], [])
    
    def get_max(self) -> int:
        """
        Return largest int in this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_max()
        10
        """
        return max([self.value] + [child.get_max() for child in self.children])
    
    def get_min(self) -> int:
        """
        Return smallest int in this Tree.
        
        >>> t = Tree(10, [Tree(3),
        ...               Tree(4, [Tree(5), 
        ...                        Tree(6, [Tree(7)])]),
        ...               Tree(8, [Tree(1, [Tree(2)])])])
        >>> t.get_min()
        1
        """
        return min([self.value] + [child.get_min() for child in self.children])
    
    def all_true(self) -> bool:
        """
        Return True if all booleans in this Tree are True.
        
        >>> t = Tree(True, [Tree(True),
        ...                 Tree(True, [Tree(True), 
        ...                             Tree(False, [Tree(True)])]),
        ...                 Tree(True, [Tree(False, [Tree(True)])])])
        >>> t.all_true()
        False
        """
        if not self.value:
            return False
        
        return all([child.all_true() for child in self.children])
    
    def any_true(self) -> bool:
        """
        Return True if any booleans in this Tree are True.
        
        >>> t = Tree(True, [Tree(True),
        ...                 Tree(True, [Tree(True), 
        ...                             Tree(False, [Tree(True)])]),
        ...                 Tree(True, [Tree(False, [Tree(True)])])])
        >>> t.any_true()
        True
        """
        if self.value:
            return True
        
        return any([child.all_true() for child in self.children])
    
# Practice Problems: BinaryTrees
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
    """
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
    
    if t.left is not None and t.right is not None:
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
    
    non_none_child = t.left if t.left is not None else t.right
    
    return LinkedListNode(t.value, turns_to_linked_list(non_none_child))

def bt_level_sums(t: Union['BinaryTree', None]) -> List[int]:
    """
    Return a list containing the sum of each level of this BinaryTree.
    
    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(8, BinaryTree(1), 
    ...                                                BinaryTree(2))),
    ...                    BinaryTree(4, BinaryTree(5), 
    ...                                  BinaryTree(6, BinaryTree(7))))
    >>> bt_level_sums(t)
    [10, 7, 19, 10]
    """
    # This is just 1 of many different approaches. Other approaches include:
    #    - Writing a helper function to get the items at each depth of t
    #      and returning the sum of each of those depths.
    #      (You would also need to get the max depth too; and just get all
    #       items from depth 0 to max depth.)
    #      See level_sums_using_depth() for this solution, along with its
    #      helper functions get_values_at_depth and get_max_depth.
    # 
    #    - Using a Queue to get the items in level order; you would need
    #      to indicate the end of each level though (i.e. with a dummy
    #      value)
    #      See level_sums_using_queue() for this solution.
    if t is None:
        return []
    
    # Merge all of those sums into one list
    all_sums = bt_level_sums(t.left)
    
    right_sums = bt_level_sums(t.right)
    for i in range(len(right_sums)):
        if i < len(all_sums):
            all_sums[i] += right_sums[i]
        else:
            all_sums.append(right_sums[i])
    
    # Add t.value to the front of all of those sums.
    return [t.value] + all_sums

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
    
    all_sums = []
    
    # Alternatively, use height instead of max_depth + 1.
    # These are equivalent.
    for i in range(max_depth + 1):
        all_sums.append(sum(bt_get_values_at_depth(t, i)))
        
    return all_sums

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
    
    return 1 + max(bt_get_max_depth(t.left), bt_get_max_depth(t.right))

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
    
    return bt_get_values_at_depth(t.left, depth - 1) + \
           bt_get_values_at_depth(t.right, depth - 1)

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
    # We can use "END" to indicate the end of a level -- once we see END
    # we know we've finished going through all the items in a level.
    q = [t, "END"]

    all_sums = []
    current_sum = 0
    # We don't want to add when our level consisted only of Nones
    add_to_list = False
    
    while q:
        item = q.pop(0)
        if item == "END":
            # When we're done with a level, add its sum to our list of
            # sums
            if add_to_list:
                all_sums.append(current_sum)
                
            add_to_list = False
            
            # Reset our sum counter to 0
            current_sum = 0
            
            # If there are still elements in q, that means there are more
            # to process. If not; that means we're done going through
            # the entire queue.
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
    
    to_return = [t.value] if f(t.value) else []
    return to_return + \
           bt_get_condition_passers(t.left, f) + \
           bt_get_condition_passers(t.right, f)

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
    
    to_return = [t.value] if f(t.value) else []
    return bt_get_condition_passers_postorder(t.left, f) + \
           bt_get_condition_passers_postorder(t.right, f) + \
           to_return

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
    
    to_return = [t.value] if f(t.value) else []
    return bt_get_condition_passers_inorder(t.left, f) + \
           to_return + \
           bt_get_condition_passers_inorder(t.right, f)


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
    
    i = 0
    while q:
        item = q.pop(0)
        if item is not None:
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
    # We can take advantage of the fact that lists are mutable -- if we
    # modify values and remove from it whenever we find a value.
    # Alternatively:
    #    Use a helper function that checks whether a value is in t or not
    #    and return True only iff all values in values are found.

    if t is None:
        return values == []
    
    if t.value in values:
        values.remove(t.value)
        
    if values == []:
        return True
    
    return bt_all_values_in_tree(t.left, values) or \
           bt_all_values_in_tree(t.right, values)

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
    
    to_return = [t.value] if type(t.value) == type_ else []
    
    return to_return + bt_return_values_with_type(t.left, type_) + \
           bt_return_values_with_type(t.right, type_)

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
    
    return max(t.value, bt_get_max(t.left), bt_get_max(t.right))

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
    
    left_min = bt_get_min(t.left)
    right_min = bt_get_min(t.right)
    
    if left_min == -1:
        left_min = t.value
    
    if right_min == -1:
        right_min = t.value
    
    return min(t.value, left_min, right_min)

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
