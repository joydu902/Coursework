"""
Solutions to the final practice questions.

Download the final_practice_imports file to be able to run this one (it just
contains the Stack, LinkedList, etc. classes to be used here -- I just wanted
to keep this file shorter.):
https://www.teach.cs.toronto.edu/~csc148h/summer/tests/final_practice_imports.py
"""
from typing import Any, Union, List
from final_practice_imports import Stack, LinkedList, LinkedListNode, Tree, \
     BinaryTree, BinarySearchTree

# Class Design Question
class Food:
    """
    A class representing food.
    
    name - The name of the Food
    quantity - The quantity of the Food
    expiration_date - The expiration date of the food
    """
    name: str
    quantity: int
    expiration_date: str
    
    def __init__(self, name: str, quantity: int, expiration_date: str) -> None:
        """
        Initialize this food with the name name, quantity quantity, and
        expiration date expiration_date.
        
        >>> f = Food("Chips", 3, "2020/01/01")
        >>> f.name
        'Chips'
        """
        self.name = name
        self.quantity = quantity
        self.expiration_date = expiration_date

    def __str__(self) -> str:
        """
        Return the string format of this Food.
        
        >>> f = Food("Chips", 3, "2020/01/01")
        >>> print(f)
        Chips x3 (Expires: 2020/01/01)
        """
        return ("{} x{} (Expires: {})").format(self.name, self.quantity,
                                               self.expiration_date)
    
    def __eq__(self, other: Any) -> bool:
        """
        Return True if this Food and other represent the same Food item.
        
        >>> f = Food("Chips", 3, "2020/01/01")
        >>> g = Food("Chips", 1, "2020/01/01")
        >>> f == g
        True
        >>> h = Food("Apples", 1, "2020/01/01")
        >>> f == h
        False
        """
        if not isinstance(other, Food):
            return False
        
        return self.name == other.name and \
               self.expiration_date == other.expiration_date
    
class Storage:
    """
    An abstract class representing a Storage.
    
    capacity - The capacity of this Storage
    """
    capacity: int
    
    def __init__(self, capacity: int) -> None:
        """
        Initialize this Storage with the capacity capacity.
        """
        self.capacity = capacity
        self._current_capacity = 0
        self._contents = []
    
    def store(self, item: Any) -> bool:
        """
        Adds item to this Storage and returns True iff item was successfully 
        stored in this Storage.
        """
        raise NotImplementedError
    
    def remove(self) -> Any:
        """
        Remove an item from this Storage.
        """
        raise NotImplementedError
    
    def get_contents(self) -> list:
        """
        Return a list of items in this Storage.
        
        [This wasn't mentioned in the handout; but since I chose to make 
        self._contents private, I need a getter in order to implement __eq__.
        Remember: You shouldn't be accessing private attributes!]
        """
        return self._contents[:]
    
    def __str__(self) -> str:
        """
        Return the string format of this Storage.
        """
        contents = [str(item) for item in self._contents]
        return "\n".join(contents)
    
    def __eq__(self, other: Any) -> bool:
        """
        Return True if this Storage and other are both Storages that contain
        the same items (but possibly in different orders).
        """
        if not isinstance(other, Storage):
            return False
        
        other_content = other.get_contents()
        if len(self._contents) == len(other_content):
            for item in self._content:
                if item not in other_content:
                    return False
            
            return True
        
        return False
    
class Fridge(Storage):
    """
    A class representing a Fridge.
    
    capacity - The capacity of this Fridge
    """
    capacity: int
    
    def store(self, item: Food) -> bool:
        """
        Adds item to this Food and returns True iff item was successfully 
        stored in this Food.
        
        >>> f = Food("Chips", 3, "2020/01/01")
        >>> fridge = Fridge(5)
        >>> fridge.store(f)
        True
        >>> print(fridge)
        Chips x3 (Expires: 2020/01/01)
        >>> f2 = Food("Chips", 2, "2020/01/01")
        >>> fridge.store(f2)
        True
        >>> print(fridge)
        Chips x5 (Expires: 2020/01/01)
        >>> f3 = Food("Candy", 2, "2030/01/01")
        >>> fridge.store(f3)
        False
        >>> print(fridge)
        Chips x5 (Expires: 2020/01/01)
        """
        if self._current_capacity + item.quantity > self.capacity:
            return False
        
        self._current_capacity += item.quantity
        
        for food in self._contents:
            if food == item:
                food.quantity += item.quantity
                return True
        
        self._contents.append(item)
        return True
    
    def remove(self) -> Food:
        """
        Remove the food with the earliest expiration date from this Fridge.
        
        Pre-condition: There is at least one item in this Fridge.
        
        >>> f = Food("Chips", 3, "2020/01/01")
        >>> fridge = Fridge(5)
        >>> fridge.store(f)
        True
        >>> f3 = Food("Candy", 2, "2030/01/01")
        >>> fridge.store(f3)
        True
        >>> print(fridge)
        Chips x3 (Expires: 2020/01/01)
        Candy x2 (Expires: 2030/01/01)
        >>> print(fridge.remove())
        Chips x3 (Expires: 2020/01/01)
        >>> print(fridge)
        Candy x2 (Expires: 2030/01/01)
        """
        earliest_item = self._contents[0]
        earliest_item_index = 0
        
        for i in range(len(self._contents)):
            item = self._contents[i]
            if item.expiration_date < earliest_item.expiration_date:
                earliest_item = item
                earliest_item_index = i

        return self._contents.pop(earliest_item_index)

# Stacks and Queues
class PriorityStack(Stack):
    """
    A class representing a PriorityStack.
    """
    
    def __init__(self) -> None:
        """
        Initialize this PriorityStack.
        
        >>> p = PriorityStack()
        >>> p.add("Yes", 2)
        >>> p.add("Maybe", 1)
        >>> p.add("No", 2)
        >>> p.remove()
        'Maybe'
        >>> p.remove()
        'No'
        """
        self._content = Stack()
    
    def add(self, item: Any, priority: int) -> None:
        """
        Add item to this PriorityStack with the priority priority.
        
        >>> p = PriorityStack()
        >>> p.add("Yes", 2)
        >>> p.remove()
        'Yes'
        """
        self._content.add((item, priority))
    
    def remove(self) -> Any:
        """
        Remove the newest lowest-priority item from this PriorityStack.
        
        Pre-condition: There is at least 1 item in this PriorityStack
        
        >>> p = PriorityStack()
        >>> p.add("Yes", 2)
        >>> p.add("Maybe", 1)
        >>> p.add("No", 2)
        >>> p.remove()
        'Maybe'
        >>> p.remove()
        'No'
        """
        lowest_item = self._content.remove()
        contents = [lowest_item]

        while not self._content.is_empty():
            removed = self._content.remove()
            contents.append(removed)

            if removed[1] < lowest_item[1]:
                lowest_item = removed

        contents.remove(lowest_item)

        contents.reverse()
        for item in contents:
            self._content.add(item)

        return lowest_item[0]


    
    def is_empty(self) -> bool:
        """
        Return True if this PriorityStack is empty.
        
        >>> p = PriorityStack()
        >>> p.is_empty()
        True
        >>> p.add("Yes", 2)
        >>> p.is_empty()
        False
        """
        return self._content.is_empty()
    
    def __str__(self) -> str:
        """
        Return the contents of this PriorityStack with their priority attached.
        
        >>> p = PriorityStack()
        >>> p.add("Yes", 2)
        >>> p.add("Maybe", 1)
        >>> p.add("No", 2)
        >>> print(p)
        Top: No (2) -> Maybe (1) -> Yes (2)
        """
        contents = []
        
        while not self._content.is_empty():
            contents.append(self._content.remove())
        
        item_strings = ['{} ({})'.format(item[0], item[1]) for 
                        item in contents]
        
        contents.reverse()
        for item in contents:
            self._content.add(item)
        
        return "Top: {}".format(" -> ".join(item_strings))

        
# Linked Lists
# -- I've created a subclass called LL so I don't have to re-define the entire
# -- LinkedList here; this way you can just see the solution.

class LL(LinkedList):
    """
    A class representing a LinkedList.
    
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - the number of nodes in this LinkedList (>= 0)
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def remove_every(self, value: Any) -> None:
        """
        Remove every occurrence of value from this LinkedList.
        
        >>> lnk = LL()
        >>> lnk.prepend('A')
        >>> lnk.prepend('B')
        >>> lnk.prepend('C')
        >>> lnk.prepend('B')
        >>> lnk.prepend('A')
        >>> print(lnk)
        A -> B -> C -> B -> A -> |
        >>> lnk.remove_every('A')
        >>> print(lnk)
        B -> C -> B -> |
        >>> lnk.size
        3
        >>> print(lnk.back)
        B -> 
        """
        previous = None
        current = self.front
        
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.front = current.next_
                else:
                    previous.next_ = current.next_
                    
                if current.next_ is None:
                    self.back = previous

                self.size -= 1
            else:
                previous = current
                
            current = current.next_
    
# Recursion

def get_most_common(x: Any) -> Any:
    """
    Return the element that occurs in lst most often.
    
    >>> get_most_common(1)
    1
    >>> get_most_common([1, 2, 1])
    1
    >>> get_most_common([[1, 2], [[1], 2], [1]])
    1
    """
    # Alternatively: Use the get_element_counts() functions from T1 and
    # return the value with the highest key.
    
    all_elements = get_all_elements(x)
    most_common_element = all_elements[0]
    most_common_count = all_elements.count(most_common_element)
    
    for item in all_elements:
        count = all_elements.count(item)
        if count > most_common_count:
            count = most_common_count
            most_common_element = item
    
    return most_common_element

def get_all_elements(x: Any) -> list:
    """
    Return all of the elements in x in a single list.
    
    >>> get_all_elements([[1, 2], [[1], 2], [1]])
    [1, 2, 1, 2, 1]
    """
    if not isinstance(x, list):
        return [x]
    
    return sum([get_all_elements(item) for item in x], [])

# Trees
# -- I've created a subclass called T so I don't have to re-define the entire
# -- Tree here.

class T(Tree):
    """
    A class representing a Tree.
    
    value - The value of the root of this Tree.
    children - The subtrees of this Tree.
    """
    value: Any
    children: List['T']
    
    def replace_all_occurrences(self, to_replace: Any, 
                                replace_with: Any) -> None:
        """
        Replace all instances of the value to_replace in this Tree
        with the value replace_with.
        >>> t = T(5, [T(5), T(2), T(5)])
        >>> t.replace_all_occurrences(5, 1)
        >>> print(t)
            1    
        1   2   1
        """
        if self.value == to_replace:
            self.value = replace_with
            
        for child in self.children:
            child.replace_all_occurrences(to_replace, replace_with)
        
# Binary Trees
def switch_all_children(t: Union[BinaryTree, None]) -> None:
    """
    Switch all of the left trees in t with the right trees.
    >>> t = BinaryTree(1, BinaryTree(2, BinaryTree(3)), 
    ...                BinaryTree(4, BinaryTree(5), 
    ...                           BinaryTree(6, BinaryTree(7))))
    >>> print(t)
            1
         2        4
      3        5        6
                     7
    >>> switch_all_children(t)
    >>> print(t)
                  1
            4        2
      6        5        3
         7
    """
    if t is None:
        return
    
    t.left, t.right = t.right, t.left
    switch_all_children(t.left)
    switch_all_children(t.right)
    
# Binary Search Trees
# 1. The left subtree of a BST contains only values < the root, and the right
#    subtree contains only values > the root. For a BinaryTree, no such
#    restrictions apply.
#
# 2. In the worst case, it's height is n (e.g. all the nodes are right children
#    of each other). In the best case, the height is lgn (e.g. all trees have
#    both a left and right child if possible).
#
# 3.     1
#            2
#                3
#                    4
#                        5
#                            6
#                                7
#
# 4.           1
#        2          3
#     4     5    6     7

def delete_children_less_than(t: Union[BinarySearchTree, None],
                              value: int) -> Union[BinarySearchTree, None]:
    """
    Remove all values less that value from t. All values in t that are > value
    should still be in t. Return the root of this BinarySearchTree or None
    if no such BinarySearchTree exists.
    >>> t = BinarySearchTree(5, BinarySearchTree(3, BinarySearchTree(1),
    ... BinarySearchTree(4)),
    ... BinarySearchTree(6))
    >>> print(t)
               5
         3        6
      1     4
    >>> print(delete_children_less_than(t, 4))
         5
      4     6
    """
    if t is None:
        return
    
    # If t.value == value, then we just delete the entire left subtree.
    if t.value == value:
        t.left = None
        return t
    
    if t.value < value:
        # We want the root of the right subtree that contains only values
        # >= value
        return delete_children_less_than(t.right, value)
    
    # Otherwise, t.value > value, so we return t but delete from the left
    # subtree.
    t.left = delete_children_less_than(t.left, value)
    return t
    
# Runtime Complexity
# 1. O(1), O(lgn), O(n), O(nlgn), O(n^2), O(2^n)
#
# 2. Binary search -- we halve the size of our input at each call to it.
#    In the end, we only look at lgn items.
#    (Anoter example is finding an item in a balanced BST.)
#
# 3. O(n)
#    a) The length gets stored as its own attribute which gets updated whenever
#       something is added/removed from the list.
#
# 4. O(n)
#    a) O(k)
#    b) In the worst-case, we'd be making a slice of size n (a copy -- e.g.
#       lst[:]). The runtime would be O(n) in that case.
#
# 5. O(n) -- it grows by 10 seconds for each increase in input size.
# 6. O(lgn) -- it grows by .001 seconds every time the input size doubles.
# 7. O(nlgn) -- The runtime grows a faster than linear, but not quite
#               quadratically (you can also see that the input size doubles).
#               Linear would be:           Quadratic would be around:
#               1  =   7.0s                1  =   7.0s
#               2  =   11.0s               2  =   10.0s
#               4  =   19.0s               4  =   22.0s
#               8  =   35.0s               8  =   70.0s
#               (Varies depending on the co-efficients you use; but in general,
#                you can see that a quadratic function would grow much faster.)
# 8. O(n^2) -- The time changes by 30 -> 50 -> 70. This difference is similar
#              to the change from 1^2 -> 2^2 -> 3^2 -> 4^2
#              (3 -> 5 -> 7)
# 9. O(2^n) -- The runtime approximately doubles with each increase of 1 in n.
#              (change is 6 -> 12 -> 24).
#
# 10. Worst-case scenario: n is a value that's not 0. Runtime: O(n)
#     Best-case scenario: n == 0. The runtime is O(1) (which is still O(n)).
#
# 11. Scenarios are the same as above.
#     Worst-case runtime is approximately O(2^n). Each n branches off into 2
#     more paths.
# 
# 12. Best-case is the same as above.
#     Worst-case runtime is lg(n) since we divide n by 2 each time and will
#     eventually reach 0.
#
# 13. Same scenarios; worst-case runtime is O(n). While we split in half,
#     the number of times we'll have the list is == n times. e.g.
#                     8
#             4               4
#         2      2         2      2
#       1   1  1   1     1   1  1   1
#     (And one more level with 16 0s in it -- which is 2n)
#     Even though we keep dividing by 2, we'll reach the base case 2n times
#     which means there are 2n + n + n // 2 + ... + 1 steps.
#     Which is still in O(n) (i.e. approximately 2n + n + (n // 2 + ... + 1))
#                                                          ^ this is at most n


# Merge Sort / Quick Sort
# 1. "Merge" refers to merging 2 sorted lists. 
#    e.g. [1, 2, 4] + [3, 5, 6] = [1, 2, 3, 4, 5, 6]
#
# 2. "Pivot" refers to how we split our list.
#    e.g. For a list like [4, 5, 2, 1, 3, 6], a pivot of 4 means we get
#    all items < 4: [2, 1, 3] and all items > 4: [5, 6]
#
# 3. Both cases are the same; any list takes O(nlgn) time.
# 4. Worst-case: O(n^2) if the pivots we pick are bad (i.e. always the min/max
#                of the list.)
#    Best-case: O(nlgn) if the pivots we pick are good (i.e. the median of the
#               list -- keep in mind finding the real median takes n time too)
# 5. [1, 2, 3, 4, 5, 6, 7]
# 6. [1, 3, 5, 7, 2, 6, 4]

# Hash Tables:
# 1. O(1) -- we only have to look at one slot which is guaranteed to contain
#    nothing (so no probing/chaining needs to be done).
#
# 2. O(1) -- appending to the end of a list is an O(1) operation.
#    (Getting an item in O(n) at worst though; we'd have to go through all the
#     items in a bucket in the worst case.)
#    a) O(n) since we have to re-add everything.
#
# 3. O(n) since, in the worst-case, we'd have to look at every item that we've
#    added previously (e.g. if everything hashes to 0 then all of those would
#    have to probe to each other.)
#
# 4. Initially: [[], []]
#    (1, 'a') : [[], [(1, 'a')]]
#    (2, 'b') : [[(2, 'b')], [(1, 'a')]]
#    (3, 'c') : [[(2, 'b'), (3, 'c')], [(1, 'a')])] -- Bucket 0 has 2 items
#               Double size of the hash table and re-add everything:
#               [[], [], [(2, 'b'), (3, 'c')], [(1, 'a')]]
#    (4, 'd') : [[(4, 'd')], [], [(2, 'b'), (3, 'c')], [(1, 'a')]]
#    (5, 'e') : [[(4, 'd')], [(5, 'e')], [(2, 'b'), (3, 'c')], [(1, 'a')]]
#
# (Note for 5: I messed up the rule -- it should have said "+ 1 if it's 0 and
#  double it otherwise.)
# 5. Initially: [None, None]
#     (1, 'a'): [None, (1, 'a')]
#     (2, 'b'): [(2, 'b'), (1, 'a')]
#     (3, 'c'): (We'd look at index 0, then + 1 -> 1, then * 2 which goes beyond
#               the hash table. So we double the size and re-insert.)
#               [None, None, (2, 'b'), (1, 'a')]
#               (Index 2 is still taken, so we multiply by 2 -> 4. This is
#               beyond the hash table, so we double the size again and re-insert)
#               [None, None, (3, 'c'), (1, 'a'), None, None, (2, 'b'), None]
#     (4, 'd'): [(4, 'd'), None, (3, 'c'), (1, 'a'), None, None, (2, 'b'), None]
#     (5, 'e'): [(4, 'd'), None, (3, 'c'), (1, 'a'), None, (5, 'e'), (2, 'b'), None]

if __name__ == '__main__':
    import doctest
    doctest.testmod()