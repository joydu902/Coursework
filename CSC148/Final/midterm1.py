from typing import Dict, List
from adts import Container, Queue, Stack
from typing import Union, Any


#class design
class ShopCatalogue:
    def __init__(self, store: str) -> None:
        self.store = store
        self.products = {}

    def add_item(self, name: str, price: float, quantity: int) -> None:
        if name in self.products:
            self.products[name][1] += quantity
        else:
            self.products[name] = [price, quantity]

    def remove_item(self, name: str, quantity: int) -> None:
        if quantity >= self.products[name][1]:
            self.products.pop(name)
        else:
            self.products[name][1] -= quantity

    def get_items_below(self, price: float) -> list:
        lst = []
        for item in self.products:
            if self.products[item][0] < price:
                lst.append(item)
        return lst

    def __str__(self) -> str:
        ss = []
        for item in self.products:
            ss += ["{} (x{}) for {:.2f} each".format(item, self.products[item][1], self.products[item][0])]
        s = ", ".join(ss)
        return "{} has: {}".format(self.store, s)

class AppList:
    def __init__(self) -> None:
        """
        Initialize this AppList.

        >>> a = AppList()
        >>> a.apps
        {}
        """
        self.apps = {}

    def add_app(self, name: str, genre: str) -> None:
        """
        Add an app with name name and genre genre to this AppList.

        Precondition: name is not in this AppList yet.

        >>> a = AppList()
        >>> a.add_app("Flappy Bird", "Arcade")
        >>> a.add_app("1024", "Puzzle")
        >>> print(a)
        Arcade: Flappy Bird
        Puzzle: 1024
        """
        self.apps[name] = genre

    def get_apps_by_genre(self, genre: str) -> List[str]:
        """
        Return all of the apps in this AppList with genre genre in alphabetical
        order.

        >>> a = AppList()
        >>> a.add_app("Flappy Bird", "Arcade")
        >>> a.add_app("1024", "Puzzle")
        >>> a.get_apps_by_genre("Arcade")
        ['Flappy Bird']
        """
        lst = []
        for app in self.apps:
            if self.apps[app] == genre:
                lst.append(app)
        lst.sort()
        return lst

    def __str__(self) -> str:
        """
        Return a string representation of this AppList, listing the games
        by their genre.

        >>> a = AppList()
        >>> a.add_app("Flappy Bird", "Arcade")
        >>> a.add_app("1024", "Puzzle")
        >>> a.add_app("Frogger", "Arcade")
        >>> print(a)
        Arcade: Flappy Bird, Frogger
        Puzzle: 1024
        """
        apps_by_genre = {}
        for app in self.apps:
            genre = self.apps[app]
            if genre in apps_by_genre:
                apps_by_genre[genre].append(app)
            else:
                apps_by_genre[genre] = [app]


        ss = []
        genres = list(apps_by_genre.keys())
        genres.sort()
        for genre in genres:
            apps = ", ".join(apps_by_genre[genre])
            ss.append("{}: {}".format(genre, apps))
        return "\n".join(ss)

class Bookshelf:
    def __init__(self, capacity: int) -> None:
        """
        Initialize this Bookshelf with capacity capacity.

        >>> b = Bookshelf(2)
        >>> b.books
        {}
        >>> b.capacity
        2
        """
        self.capacity = capacity
        self.books = {}

    def add_book(self, name: str, author: str) -> None:
        """
        Add a book with name name and author author to this Bookshelf.

        Precondition: name is not already in this Bookshelf.

        >>> b = Bookshelf(2)
        >>> b.add_book("Cinderella", "Brothers Grimm")
        >>> b.add_book("Rapunzel", "Brothers Grimm")
        >>> b.books
        {'Cinderella': 'Brothers Grimm', 'Rapunzel': 'Brothers Grimm'}
        >>> b.add_book("Snow White", "Brothers Grimm")
        >>> b.books
        {'Cinderella': 'Brothers Grimm', 'Rapunzel': 'Brothers Grimm'}
        """
        if len(self.books) < self.capacity:
            self.books[name] = author

    def get_all_books(self) -> List[str]:
        """
        Return all of the books in this Bookshelf in alphabetical order.

        >>> b = Bookshelf(3)
        >>> b.add_book("Cinderella", "Brothers Grimm")
        >>> b.add_book("Snow White", "Brothers Grimm")
        >>> b.add_book("Rapunzel", "Brothers Grimm")
        >>> b.get_all_books()
        ['Cinderella', 'Rapunzel', 'Snow White']
        """
        lst = list(self.books.keys())
        lst.sort()
        return lst

    def remove_book(self, name: str) -> None:
        """
        Remove the book with the name name from this Bookshelf.

        >>> b = Bookshelf(3)
        >>> b.add_book("Cinderella", "Brothers Grimm")
        >>> b.add_book("Snow White", "Brothers Grimm")
        >>> b.remove_book("Cinderella")
        >>> b.books
        {'Snow White': 'Brothers Grimm'}
        """
        self.books.pop(name)

    def get_books_by_author(self, author: str) -> List[str]:
        """
        Return all of the books on this Bookshelf with the author author in
        alphabetical order.

        >>> b = Bookshelf(3)
        >>> b.add_book("Cinderella", "Brothers Grimm")
        >>> b.add_book("Snow White", "Brothers Grimm")
        >>> b.add_book("The Snow Queen", "Hans Christian Andersen")
        >>> b.get_books_by_author("Brothers Grimm")
        ['Cinderella', 'Snow White']
        """
        lst = []
        for book in self.books:
            if self.books[book] == author:
                lst.append(book)

        lst.sort()
        return lst


#Stack Queue
def list_container(lst: List[int], c: Container) -> None:
    """
    Empty out c according to the algorithm from lecture after filling it with
    items from lst.

    When c is a Stack, the elements of lst should be printed in reverse order.
    When c is a Queue, the elements of lst should be printed out in level order.

    Precondition: c is empty.

    >>> lst = [1, [[[2], 3]], [4, [5]]]
    >>> list_container(lst, Stack())
    5
    4
    3
    2
    1
    >>> list_container(lst, Queue())
    1
    4
    3
    5
    2
    """
    contents = []
    for item in lst:
        c.add(item)
    while not c.is_empty():
        term = c.remove()
        if not isinstance(term, list):
            print(term)
        else:
            for item in term:
                c.add(item)


    # for item in lst:
    #     c.add(item)
    #
    # while not c.is_empty():
    #     removed = c.remove()
    #
    #     if not isinstance(removed, list):
    #         print(removed)
    #     else:
    #         for item in removed:
    #             c.add(item)


def list_nestedness(lst: List[int], q: Queue) -> List[List[int]]:
    """
    Return a list of elements of lst in each level of nestedness using q.

    Precondition: q is empty.
                  lst contains only ints.

    >>> lst = [1, [[[2], 3]], [4, [5]]]
    >>> list_nestedness(lst, Queue())
    [[1], [4], [3, 5], [2]]
    """
    for item in lst:
        q.add(item)
    level = []
    all_levels = []
    q.add('End')
    while not q.is_empty():
        removed = q.remove()
        if not isinstance(removed, list):
            if removed == 'End':
                all_levels.append(level)
                level = []
                if not q.is_empty():
                    q.add('End')
            else:
                level.append(removed)
        else:
            for item in removed:
                q.add(item)
    return all_levels


# class StackQueue(Container):
#     """
#     An implementation of the class Queue but using Stacks to store the
#     content.
#     """
#
#     def __init__(self) -> None:
#         """
#         Initialize this StackQueue.
#
#         >>> q = StackQueue()
#         >>> q.is_empty()
#         True
#         """
#         # Create 2 stacks as attributes
#         # self._add_to: This will be the stack that we always add to when
#         #               add() is called.
#         # self._remove_from: This will be the stack that we use to remove from
#         #               when remove() is called.
#         self._add_to = Stack()
#         self._remove_from = Stack()

    # def add(self, value: object) -> None:
    #     """
    #     Add value to this StackQueue.
    #
    #     >>> q = StackQueue()
    #     >>> q.add(5)
    #     >>> q.add(3)
    #     >>> q.remove()
    #     5
    #     >>> q.remove()
    #     3
    #     """
    #     self._add_to.add(value)

#Linkedlist
class LinkedListNode:
    """
    A Node to be used in a LinkedList.

    next_ - The successor to this LinkedListNode
    value - The data represented by this LinkedListNode.
    """
    next_: Union["LinkedListNode", None]
    value: Any

    def __init__(self, value: Any,
                 next: Union["LinkedListNode", None] = None) -> None:
        """
        Initialize this LinkedListNode with the value value and successor next.

        >>> LinkedListNode(3).value
        3
        >>> LinkedListNode(3).next_ == None
        True
        """
        self.value = value
        self.next_ = next

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedListNode.

        """
        return "{} -> ".format(self.value)

class LinkedList:
    """
    Collection of LinkedListNodes.

    front - first node of this LinkedList
    back - last node of this LinkedList
    size - the number of nodes in this LinkedList (>= 0)
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Initialize an empty LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.size
        0
        """
        self.front = None
        self.back = None
        self.size = 0

    def append(self, value: Any) -> None:
        """
        Insert value to the end of this LinkedList (after self.back).

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> print(lnk)
        0 -> 1 -> |
        """
        new_node = LinkedListNode(value)
        if self.size == 0:
            self.front = new_node
        else:
            self.back.next_ = new_node
        self.back = new_node
        self.size += 1


    def prepend(self, value: Any) -> None:
        """
        Insert value to the start of this LinkedList (before self.front).

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        self.front = LinkedListNode(value, self.front)
        if self.back is None:
            self.back = self.front
        self.size += 1

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        cur_node = self.front
        s = ''
        while cur_node is not None:
            s += str(cur_node)
            cur_node = cur_node.next_
        return s + "|"

    def remove(self, value: Any) -> None:
        """
        Remove value from this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        >>> lnk.remove(1)
        >>> print(lnk)
        0 -> |
        """
        prev_node = None
        cur_node = self.front
        while cur_node is not None and cur_node.value != value:
            prev_node = cur_node
            cur_node.next_ = cur_node

        if not cur_node:
            return None

        if not prev_node:
            self.front = cur_node.next_
        else:
            prev_node.next_ = cur_node.next_

        if not cur_node.next_:
            self.back = prev_node

        self.size -= 1

    def find_second_last(self) :
        """
        Return the node that points to the back of the LinkedList.

        Return None if there is no such node.

        >>> lnk = LinkedList()
        >>> lnk.find_second_last() == None
        True
        >>> lnk.prepend(3)
        >>> lnk.find_second_last() == None
        True
        >>> lnk.prepend(2)
        >>> lnk.find_second_last().value
        2
        >>> lnk.prepend(1)
        >>> lnk.find_second_last().value
        2
        """
        prev_node = None
        cur_node = self.front
        if self.size < 2:
            return None
        else:
            while cur_node.next_ is not None:
                prev_node = cur_node
                cur_node = cur_node.next_
            return prev_node

    def get_values(self) -> list:
        """
        Return a list of all of the values within the LinkedList.
        >>> lnk = LinkedList()
        >>> lnk.get_values()
        []
        >>> lnk.prepend(3)
        >>> lnk.get_values()
        [3]
        >>> lnk.prepend(2)
        >>> lnk.get_values()
        [2, 3]
        >>> lnk.prepend(1)
        >>> lnk.get_values()
        [1, 2, 3]
        """
        cur_node = self.front
        lst = []
        while cur_node is not None:
            lst.append(cur_node.value)
            cur_node = cur_node.next_
        return lst

    def __eq__(self, other: 'LinkedList') -> bool:
        """
        Return whether self and other are equal.

        >>> lnk1 = LinkedList()
        >>> lnk2 = LinkedList()
        >>> lnk1 == lnk2
        True
        >>> lnk1.prepend(3)
        >>> lnk1 == lnk2
        False
        >>> lnk2.prepend(3)
        >>> lnk1 == lnk2
        True
        >>> lnk1.prepend(2)
        >>> lnk2.prepend(2)
        >>> lnk1 == lnk2
        True
        >>> lnk1.prepend(1)
        >>> lnk1 == lnk2
        False
        """
        cur_node = self.front
        oth_node = other.front

        if self.size != other.size:
            return False
        else:
            while cur_node != None:
                if cur_node.value != oth_node.value:
                    return False
                cur_node = cur_node.next_
                oth_node = oth_node.next_
            return True

    def find_value(self, value: object) -> LinkedListNode:
        """
        Return the first LinkedListNode in this LinkedList with the value value.

        >>> lnk = LinkedList()
        >>> lnk.prepend(3)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.find_value(1) == lnk.front
        True
        >>> lnk.find_value(3) == lnk.back
        True
        >>> lnk.find_value(2).next_ == lnk.back
        True
        """
        cur_node = self.front
        while cur_node is not None:
            if cur_node.value == value:
                return cur_node
            else:
                cur_node = cur_node.next_

    def add_after(self, to_add: object, to_add_after: object) -> None:
        """
        Add to_add after the first node with the value to_add_after.

        >>> lnk = LinkedList()
        >>> lnk.prepend(3)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.add_after(10, 2)
        >>> print(lnk)
        1 -> 2 -> 10 -> 3 -> |
        """
        new_node = LinkedListNode(to_add)
        cur_node = self.front

        while cur_node is not None and cur_node.value != to_add_after:
            cur_node = cur_node.next_
        new_node.next_ = cur_node.next_
        cur_node.next_ = new_node

        self.size += 1

    def add_after_every(self, to_add: object, to_add_after: object) -> None:
        """
        Add to_add after the every node with the value to_add_after.

        >>> lnk = LinkedList()
        >>> lnk.prepend(3)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> lnk.add_after_every(10, 2)
        >>> print(lnk)
        1 -> 2 -> 10 -> 1 -> 2 -> 10 -> 3 -> |
        """

        current_node =self.front
        while current_node is not None:
            if current_node.value == to_add_after:
                new_node = LinkedListNode(to_add)

                new_node.next_ = current_node.next_
                current_node.next_ = new_node

                if current_node.next_ is None:
                    self.back = new_node
                current_node = new_node
                self.size += 1
            else:
                current_node = current_node.next_


        # cur_node = self.front
        #
        # while cur_node != None:
        #     if cur_node.value == to_add_after:
        #         new_node = LinkedListNode(to_add)######
        #         new_node.next_ = cur_node.next_
        #         cur_node.next_ = new_node
        #
        #         if new_node.next_ == None:
        #             self.back = new_node
        #
        #         cur_node = new_node.next_
        #         self.size += 1
        #     else:
        #         cur_node = cur_node.next_

#midterm1 practice
class Ghost:
    """
    A class representing a Ghost.

    age - The age of the ghost
    """
    age: int

    def __init__(self, age: int) -> None:
        """
        Initialize this Ghost with the age age.
        """
        self.age = age

    def make_sound(self) -> None:
        """
        Make this Ghost make a sound.
        """
        print("Boo!")

    def __str__(self) -> str:
        raise NotImplementedError

class Spectre(Ghost):
    """
    A class representing a Spectre.

    age - The age of the spectre
    size - The size of the spectre
    """
    age: int
    size: int

    def __init__(self, age: int, size: int) -> None:
        """
        Initialize this Spectre with the age age and size size.

        >>> s = Spectre(10, 3)
        >>> s.size
        3
        """
        super().__init__(age)
        self.size = size

    def __str__(self) -> str:
        """
        Return a string representation of this Spectre.

        >>> s = Spectre(10, 3)
        >>> print(s)
        Spectre (10)
        """
        return 'Spectre ({})'.format(self.age)


class Ghoul(Ghost):
    def __init__(self, age: int, name: str) -> None:
        super().__init__(age)
        self.name = name

    def __str__(self) -> str:
        """
        Return a string representation of this Ghoul.

        >>> g = Ghoul(10, 'Sophia')
        >>> print(g)
        Ghoul (10)
        """
        return 'Ghoul ({})'.format(self.age)

    def make_sound(self) -> None:
        """
        Make this Ghoul make a sound.

        >>> g = Ghoul(10, 'Sophia')
        >>> g.make_sound()
        Boo!
        Grr...
        """
        super().make_sound()
        print('Grr...')


class Pet:
    """
    A class representing a Pet.

    name - The pet's name.
    fullness - The pet's fullness
    """
    name: str
    fullness: int

    def __init__(self, name: str) -> None:
        """
        Initialize this Pet with the name name and no fullness.

        >>> p = Pet("Froggy")
        >>> p.name
        'Froggy'
        >>> p.fullness
        0
        """
        self.name = name
        self.fullness = 0

    def __eq__(self, other: object) -> bool:
        """
        Return whether self and other are equal.

        >>> p1 = Pet("Stinky")
        >>> p2 = Pet("Stinky")
        >>> p1 == p2
        True
        >>> p3 = Pet("Smelly")
        >>> p1 == p3
        False
        """
        if type(self) != type(other):
            return False
        return (self.name == other.name) and (self.fullness == other.fullness)

    def __str__(self) -> str:
        """
        Return the string representation of this Pet.

        >>> p1 = Pet("Stinky")
        >>> print(p1)
        Stinky (0)
        """
        return "{} ({})".format(self.name, self.fullness)


class Owner:
    """
    A class representing an Owner.

    pet - The pet of this Owner.
    name - The Owner's name.
    """
    pet: Pet
    name: str

    def __init__(self, name: str, pet: Pet) -> None:
        """
        Initialize this Owner with the name name and pet pet.

        >>> o = Owner("Sophia", Pet("Stinky"))
        >>> o.name
        'Sophia'
        """
        self.name = name
        self.pet = pet

    def feed_pet(self) -> None:
        """
        Feed this owner's pet.

        >>> o = Owner("Sophia", Pet("Stinky"))
        >>> o.pet.fullness
        0
        >>> o.feed_pet()
        >>> o.pet.fullness
        5
        """
        self.pet.fullness += 5

    def __eq__(self, other: object) -> bool:
        """
        Return whether self and other are equal.

        >>> o1 = Owner("Sophia", Pet("Stinky"))
        >>> o2 = Owner("Sophia", Pet("Stinky"))
        >>> o1 == o2
        True
        >>> o3 = Owner("Sophia", Pet("Smelly"))
        >>> o1 == o3
        False
        """
        if type(self) != type(other):
            return False
        return (self.name == other.name) and (self.pet == other.pet)

    def __str__(self) -> str:
        """
        Return the string representation of this Owner.

        >>> o1 = Owner("Sophia", Pet("Stinky"))
        >>> print(o1)
        Sophia: Stinky (0)
        """
        return "{}: {}".format(self.name, self.pet)######


class Meal:
    """
    A Meal class.

    name - name of the meal
    price - price of the meal
    """
    name: str
    price: int

    def __init__(self, name: str, price: int) -> None:
        """
        Initialize this Meal with the name name and price price.
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Return the string representation of this Meal.
        """
        return "{} (${})".format(self.name, self.price)

    def is_healthy(self) -> bool:
        """
        Return whether this meal is healthy or not.
        """
        raise NotImplementedError

class HealthyMeal(Meal):
    def __init__(self, name: str, price: int, main_ingredient: str) -> None:
        super().__init__(name, price)
        self.main_ingredient = main_ingredient

    def is_healthy(self):
        return True
    def __str__(self):
        return "{}: {}".format(super().__str__(), self.main_ingredient)

class JunkMeal(Meal):
    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)

    def is_healthy(self):
        return False


class StringStack:
    """
    An implementation of Stack for a stack that contains only single
    character strings.
    """

    def __init__(self) -> None:
        """
        Initialize this StringStack.

        >>> s = StringStack()
        >>> s.is_empty()
        True
        """
        self._content = ""

    def add(self, value: str) -> None:
        """
        Add value this StringStack.

        Precondition: value is a string
                      len(value) == 1

        >>> s = StringStack()
        >>> s.add('5')
        >>> s.is_empty()
        False
        """
        self._content += value

    def remove(self) -> object:
        """
        Remove an item from the top of this StringStack.

        >>> s = StringStack()
        >>> s.add("5")
        >>> s.add("A")
        >>> s.remove()
        'A'
        >>> s.remove()
        '5'
        """
        removed = self._content[-1]
        self._content = self._content[:-1]
        return removed

    def is_empty(self) -> bool:
        """
        Return whether this StringStack is empty or not (whether there's nothing
        left to remove.)

        >>> s = StringStack()
        >>> s.add('5')
        >>> s.is_empty()
        False
        """
        return self._content == ''


class StringQueue:
    """
    An implementation of Queue for a queue that contains only single
    character strings.
    """

    def __init__(self) -> None:
        """
        Initialize this StringQueue.

        >>> s = StringQueue()
        >>> s.is_empty()
        True
        """
        self._content = ''

    def add(self, value: str) -> None:
        """
        Add value this StringQueue.

        Precondition: value is a string
                      len(value) == 1

        >>> s = StringQueue()
        >>> s.add('5')
        >>> s.is_empty()
        False
        """
        self._content += value

    def remove(self) -> object:
        """
        Remove an item from the top of this StringQueue.

        >>> s = StringQueue()
        >>> s.add("5")
        >>> s.add("A")
        >>> s.remove()
        '5'
        >>> s.remove()
        'A'
        """
        removed = self._content[0]
        self._content = self._content[1:]
        return removed

    def is_empty(self) -> bool:
        """
        Return whether this StringQueue is empty or not (whether there's nothing
        left to remove.)

        >>> s = StringQueue()
        >>> s.add('5')
        >>> s.is_empty()
        False
        """
        return self._content == ''


class Stack:
    """
    An implementation of Stack.
    """

    def __init__(self) -> None:
        """
        Initialize this Stack.

        >>> s = Stack()
        >>> s.is_empty()
        True
        """
        self._content = []

    def add(self, value: object) -> None:
        """
        Add value this Stack.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        self._content.append(value)

    def remove(self) -> object:
        """
        Remove an item from the top of this Stack.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add("A")
        >>> s.remove()
        'A'
        """
        return self._content.pop()

    def is_empty(self) -> bool:
        """
        Return whether this Stack is empty or not (whether there's nothing
        left to remove.)

        >>> s = Stack()
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        return self._content == []

    def __str__(self) -> str:
        """
        Return the string representation of this Stack.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add('A')
        >>> print(s)
        Top -> A, 5
        """
        contents = []
        while not self.is_empty():
            contents.append(self.remove())

        str_content = []
        for item in contents:
            str_content += [str(item)]

        ss = ', '.join(str_content)

        contents.reverse()
        for item in contents:
            self.add(item)

        return 'Top -> {}'.format(ss)


class Queue:
    """
    An implementation of Stack.
    """

    def __init__(self) -> None:
        """
        Initialize this Stack.

        >>> q = Queue()
        >>> q.is_empty()
        True
        """
        self._content = []

    def add(self, value: object) -> None:
        """
        Add value this Stack.

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        """
        self._content.append(value)

    def remove(self) -> object:
        """
        Remove an item from the top of this Stack.

        >>> q = Queue()
        >>> q.add(5)
        >>> q.add("A")
        >>> q.remove()
        5
        """
        return self._content.pop(0)

    def is_empty(self) -> bool:
        """
        Return whether this Stack is empty or not (whether there's nothing
        left to remove.)

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        """
        return self._content == []

    def __eq__(self, other: object) -> bool:
        """
        Return whether self and other are equal.

        >>> q1 = Queue()
        >>> q2 = Queue()
        >>> q1 == q2
        True
        >>> q1.add(5)
        >>> q1 == q2
        False
        >>> q2.add(5)
        >>> q1 == q2
        True
        """
        if type(self) != type(other):
            return False

        a_contents = []
        b_contents = []
        while not self.is_empty():
            a_contents.append(self.remove())

        while not other.is_empty():
            b_contents.append(other.remove())

        for item in a_contents:
            self.add(item)
        for item in b_contents:
            self.add(item)

        return a_contents == b_contents

    def __str__(self) -> str:
        """
        Return the string representation of this Queue.


        >>> q = Queue()
        >>> q.add(5)
        >>> q.add('A')
        >>> print(q)
        Front -> 5, A
        """
        contents = []
        while not self.is_empty():
            contents.append(self.remove())

        str_content = []
        for item in contents:
            str_content += [str(item)]

        ss = ', '.join(str_content)

        for item in contents:
            self.add(item)

        return 'Front -> {}'.format(ss)


def queue_to_stack(q: Queue) -> Stack:
    """
    Return a stack with the items from q. The stack returned should
    Have items removed in the same order as q.

    After calling this function, q should be in its original state (all
    Items in the same order).

    >>> q = Queue()
    >>> q.add(1)
    >>> q.add(2)
    >>> q.add(3)
    >>> s = queue_to_stack(q)
    >>> q.remove()
    1
    >>> s.remove()
    1
    >>> q.remove()
    2
    >>> s.remove()
    2
    >>> q.remove()
    3
    >>> s.remove()
    3
    """
    contents = []
    while not q.is_empty():
        contents.append(q.remove())
    contents.reverse()

    s = Stack()
    for item in contents:
        s.add(item)

    contents.reverse()
    for item in contents:
        q.add(item)

    return s


class LinkedListStack:
    """
    A class representing a Stack, formed using a LinkedList.
    """

    def __init__(self) -> None:
        """
        Initialize an empty LinkedListStack.

        >>> s = LinkedListStack()
        >>> s.add(3)
        >>> s.add(2)
        >>> s.add(1)
        >>> s.remove()
        1
        >>> s.remove()
        2
        >>> s.remove()
        3
        """
        self._content = LinkedList()

    def add(self, value: object) -> None:
        """
        Add value to this LinkedListStack.

        >>> s = LinkedListStack()
        >>> s.add(3)
        >>> s.add(2)
        >>> s.add(1)
        >>> s.remove()
        1
        >>> s.remove()
        2
        >>> s.remove()
        3
        """
        new_node = LinkedListNode(value)

        new_node.next_ = self._content.front
        self._content.front = new_node

        if self._content.size == 0:
            self._content.back = new_node

        self._content.size += 1

    def remove(self) -> object:
        """
        Remove a value from the top of this LinkedListStack.

        Precondition: self.is_empty() == False

        >>> s = LinkedListStack()
        >>> s.add(3)
        >>> s.add(2)
        >>> s.add(1)
        >>> s.remove()
        1
        >>> s.remove()
        2
        >>> s.remove()
        3
        """
        old_front = self._content.front
        self._content.front = self._content.front.next_

        if self._content.size == 0:
            self.back = None

        self._content.size -= 1
        return old_front.value

    def is_empty(self) -> bool:
        """
        Return True if this Stack is empty.

        >>> s = LinkedListStack()
        >>> s.is_empty()
        True
        >>> s.add(3)
        >>> s.is_empty()
        False
        """
        return self._content.size == 0

class LinkedListNode:
    """
    A Node to be used in a LinkedList.

    next_ - The successor to this LinkedListNode
    value - The data represented by this LinkedListNode.
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next: Union["LinkedListNode", None] = None) -> None:
        """
        Initialize this LinkedListNode with the value value and successor next.

        >>> LinkedListNode(3).value
        3
        >>> LinkedListNode(3).next_ == None
        True
        """
        self.value = value
        self.next_ = next

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedListNode.

        # >>> print(LinkedListNode(3))
        # 3 ->
        """
        return "{} -> ".format(self.value)

class LinkedList:
    """
    Collection of LinkedListNodes.

    front - first node of this LinkedList
    back - last node of this LinkedList
    size - the number of nodes in this LinkedList (>= 0)
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Initialize an empty LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.size
        0
        """
        self.front = None
        self.back = None
        self.size = 0

    def prepend(self, value: Any) -> None:
        """
        Insert value to the start of this LinkedList (before self.front).

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        self.front = LinkedListNode(value, self.front)
        if self.back is None:
            self.back = self.front
        self.size += 1

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        cur_node = self.front
        result = ''
        while cur_node is not None:
            result += str(cur_node)
            cur_node = cur_node.next_
        return result + '|'

    def add_before(self, new_value: Any, to_find: Any):
        """
        Add new_value to this LinkedList so it comes immediately
        before to_find.

        If to_find isn't in this LinkedList, don't modify this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend("H")
        >>> lnk.add_before("A", "H")
        >>> print(lnk)
        A -> H -> |
        >>> lnk.size
        2
        >>> lnk.add_before("C", "H")
        >>> print(lnk)
        A -> C -> H -> |
        >>> lnk.size
        3
        >>> lnk.add_before("O", "B")
        >>> print(lnk)
        A -> C -> H -> |
        >>> lnk.size
        3
        """
        prev_node = None
        current_node = self.front
        while current_node is not None and current_node.value != to_find:
            prev_node = self.front
            current_node = current_node.next_
        if not current_node:
            return
        else:
            new_node = LinkedListNode(new_value)
            self.size += 1
            if not prev_node:
                self.front = new_node
                new_node.next_ = current_node
                current_node.next_ = None
            else:
                prev_node.next_ = new_node
                new_node.next_ = current_node



        # new_node = LinkedListNode(new_value)
        # cur_node = self.front
        # prev_node = None
        # while cur_node is not None and cur_node.value != to_find:
        #     prev_node = cur_node
        #     cur_node = cur_node.next_
        #
        # if not prev_node:
        #     self.front = new_node
        #     new_node.next_ = cur_node
        #
        #
        # if not cur_node:
        #     return
        # else:
        #     if not prev_node:
        #         self.front = new_node
        #         new_node.next_ = cur_node
        #     else:
        #         prev_node.next_ = new_node
        #         new_node.next_ = cur_node
        #     self.size += 1






if __name__ == '__main__':
    import doctest
    doctest.testmod()

    s = ShopCatalogue("UofT Bookstore")
    s.add_item("Chips", 0.99, 3)
    assert str(s) == "UofT Bookstore has: Chips (x3) for 0.99 each"
    s.add_item("Chips", 0.99, 10)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each"
    s.add_item("Pencil", 2.50, 3)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each, Pencil (x3) for 2.50 each"
    s.remove_item("Pencil", 2)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each, Pencil (x1) for 2.50 each"
    s.remove_item("Pencil", 1)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each"
    s.add_item("Pop", 1.95, 3)
    s.add_item("Pencil", 2.50, 2)
    assert s.get_items_below(2.00) == ['Chips', 'Pop']


