from typing import Any, Union, List
from final_practice_imports import Stack, LinkedList, LinkedListNode, Tree, \
     BinaryTree, BinarySearchTree
class Food:
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
        return "{} x{} (Expires: {})".format(self.name, self.quantity, self.expiration_date)

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
        return (self.name == other.name) and (self.expiration_date == other.expiration_date)

class Storage:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._current_capacity = 0
        self._contents = []

    def store(self) -> bool:
        raise NotImplementedError

    def remove(self) -> None:
        raise NotImplementedError

    def get_contents(self) -> list:
        return self._contents[:]

    def __str__(self) -> str:
        """
        Return the string format of this Storage.
        """
        result = []
        for food in self._contents:
            result += [str(food)]
        return "\n".join(result)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Storage):
            return False
        if len(self._contents) == len(other._contents):
            for item in self._contents:
                if item not in other._contents:
                    return False
            return True
        return False

class Fridge(Storage):
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
        earlist_item = self._contents[0]
        for food in self._contents:
            if food.expiration_date <= earlist_item.expiration_date:
                earlist_item = food

        self._contents.remove(earlist_item)
        return earlist_item



        # earlist_item = self._contents[0]
        # earlist_item_index = 0
        # for i in range(len(self._contents)):
        #     item = self._contents[i]
        #     if item.expiration_date <= earlist_item.expiration_date:
        #         earlist_item = item
        #         earlist_item_index = i
        # return self._contents.pop(earlist_item_index)


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
        removed = self._content.remove()
        contents = [removed]
        while not self._content.is_empty():
            remo = self._content.remove()
            contents.append(remo)
            if remo[1] < removed[1]:
                removed = remo

        contents.remove(removed)

        contents.reverse()
        for term in contents:
            self._content.add(term)

        return removed[0]


        # removed = self._content.remove()
        # contents = [removed]
        # while not self._content.is_empty():
        #     remo = self._content.remove()
        #     contents.append(remo)
        #     if remo[1] < removed[1]:
        #         removed = remo
        # contents.remove(removed)
        # contents.reverse()
        # for item in contents:
        #     self._content.add(item)
        #
        # return removed[0]



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
        result = []
        contents = []
        while not self._content.is_empty():
            item = self._content.remove()
            contents.append(item)

        for item in contents:
            result += ["{} ({})".format(item[0], item[1])]

        contents.reverse()
        for ite in contents:
            self._content.add(ite)

        return "Top: " + " -> ".join(result)


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
        """
        # >>> print(lnk.back)
        # B ->
        pre_node = None
        cur_node = self.front
        while cur_node is not None:
            if cur_node.value == value:
                if not pre_node:
                    self.front = cur_node.next_
                else:
                    pre_node.next_ = cur_node.next_
                if cur_node.next_ is None:
                    self.back = pre_node
                self.size -= 1
            else:
                pre_node = cur_node
            cur_node = cur_node.next_


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
    lst = get_all_elements(x)
    most_common_number = lst[0]
    most_common_count = lst.count(most_common_number)
    for item in lst:
        if lst.count(item) > most_common_count:
            most_common_number = item
            most_common_count = lst.count(most_common_number)
    return most_common_number

#helper function
def get_all_elements(x: Any) -> Any:
    result = []
    if isinstance(x, int):
        return [x]
    else:
        for item in x:
            result.extend(get_all_elements(item))
    return result


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
        """
        # >>> print(t)
        #     1
        # 1   2   1

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

def delete_children_less_than(t: Union[BinarySearchTree, None],
                              value: int) -> Union[BinarySearchTree, None]:###############
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
    if t.value == value:
        t.left = None
        return t
    if t.value < value:
        t.left = None
        return delete_children_less_than(t.right, value)
    if t.value > value:
        t.left = delete_children_less_than(t.left, value)
    return t




if __name__ == '__main__':
    import doctest
    doctest.testmod()


