from typing import Union, Any, List


class LinkedListNode:
    """
    A very small LinkedListNode class for recursion examples.

    next_ - The node that comes after this LinkedListNode.
    value - The value of this LinkedListNode.
    """
    next_: Union[None, 'LinkedListNode']
    value: Any

    def __init__(self, value: Any,
                 next_: Union[None, 'LinkedListNode'] = None) -> None:
        """
        Initialize this LinkedListNode with value value and next_ next_.
        """
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        """
        Return a string containing all elements in the LinkedList starting from
        this LinkedListNode.

        >>> x = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
        >>> print(x)
        1 -> 2 -> 3 -> |
        """
        all_values = []
        cur_node = self
        while cur_node != None:
            all_values.append(str(cur_node.value))
            cur_node = cur_node.next_

        return " -> ".join(all_values) + " -> |"


def ternary_if_return(x: int) -> int:
    """
    Uses a ternary if condition to return according to x.

    The if-statement equivalent of the code in ternary_if_return is

    if x == 10:
        return 100
    else: # You can also omit this else-statement
        return 0
    """
    return 100 if x == 10 else 0

def return_sum(x: Union[list, int]) -> int:
    """
    Return a sum of all of the ints in x or its sublists.
    If x is an int: return x.

    >>> return_sum(1)
    1
    >>> return_sum([1, 2, 3])
    6
    >>> return_sum([1, [2, 3], [4, [5]]])
    15
    """
    sum = 0
    if isinstance(x, int):
        return x
    else:
        for item in x:
            sum += return_sum(item)
        return sum

def get_factorial(x: int) -> int:
    """
    Return x! (the factorial of x).
    Implemented using recursion instead of a loop.

    Precondition: x is a positive int (x > 0)

    >>> get_factorial(1)
    1
    >>> get_factorial(3)
    6
    >>> get_factorial(5)
    120
    """
    if x == 1:
        return 1
    return x * get_factorial(x-1)


def get_max(x: Union[list, int]) -> int:
    """
    Return the largest number in x or its sublists.
    If x is an int, return x.

    >>> get_max(10)
    10
    >>> get_max([1, [2, [3, [4]]]])
    4
    >>> get_max([1, [2, [3, 4], [5, [6], [7, [[8]]]]]])
    8
    """
    result = []
    if isinstance(x, int):
        return x
    else:
        for item in x:
            result.append(get_max(item))
    return max(result)

def count_occurrences(x: Union[list, int], value: int) -> int:
    """
    Return the number of times value appears in x or its sublists.
    If x is an int, return 0 if x == value, and 1 otherwise.

    >>> count_occurrences(2, 5)
    0
    >>> count_occurrences(5, 5)
    1
    >>> count_occurrences([1, 2, 5, 5], 5)
    2
    >>> count_occurrences([1, [2, [5], [3, [[5]]], 5], 5], 5)
    4
    """
    count = 0
    if isinstance(x, int):
        if x == value:
            return 1
        else:
            return 0
    else:
        for item in x:
            count += count_occurrences(item, value)
        return count



#More Recursion

def get_all_elements(x: Union[list, int]) -> List[int]:
    result = []
    if isinstance(x, int):
        return [x]
    else:
        for item in x:
            result.extend(get_all_elements(item))
        return result

    # # Base case: x is not a list
    # #            In this case, we just return a list containing x.
    # if not isinstance(x, list):
    #     return [x]
    #
    # # Recursive step: x is a list
    # #                 We get all elements inside of each item in x and put all
    # #                 of those results together.
    # return sum([get_all_elements(item) for item in x], [])

def f(x) -> bool:
    return x > 15

def passes_condition(f, x: Union[list, int]) -> List[int]:
    result = []
    if isinstance(x, int):
        if f(x):
            return [x]
        else:
            return []
    else:
        for item in x:
            result.extend(passes_condition(f, item))
        return result


def count_number_of_lists(x: Union[list, int]) -> int:
    count = 0
    if isinstance(x, int):
        return 0
    else:
        for item in x:
            count += count_number_of_lists(item)
        return count + 1

    #     # Base case: If x is not a list, we return 0.
    # if not isinstance(x, list):
    #     return 0
    #
    #     # Recursive step: x is a list.
    #     #                 We return 1 + the sum of the results of the recursive
    #     #                 calls to each item in x.
    # return 1 + sum([count_number_of_lists(item) for item in x])

def all_sections_are_words(word, word_list) -> bool:
    if not word in word_list:
        return False
    if len(word) <= 3:
        return word in word_list

    return all_sections_are_words(word[:len(word) // 2], word_list) and all_sections_are_words(word[len(word) // 2:], word_list)

def get_nth_fibonacci(n:int) -> int:
    if n < 3:
        return 1
    else:
        return get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)

def x_in_list(x, lst) -> bool:
    if len(lst) == 1:
        return lst[0] == x
    if lst == []:
        return False
    return x_in_list(x, lst[:(len(lst)//2)]) or x_in_list(x, lst[(len(lst)//2):])

    # # Base case: If there's only 1 item in the list, we return whether that
    # #            item is x or not
    # if len(lst) == 1:
    #     return lst[0] == x
    #
    # # Base case #2: If there are no items in the list, we return False.
    # if lst == []:
    #     return False
    #
    # # Recursive step: Split lst into 2 halves.
    # #                 Make recursive calls on each half, returning True if
    # #                 either recursive call returned True.
    # return x_in_list(x, lst[:len(lst) // 2]) or x_in_list(x, lst[len(lst) // 2:])

def x_in_sorted_list(x, lst) -> bool:
    if lst == []:
        return False
    if len(lst) == 1:
        return lst[0] == x
    mid_index = len(lst) // 2
    mid = lst[mid_index]
    if x < mid:
        return x_in_sorted_list(x, lst[:mid_index])
    else:
        return x_in_sorted_list(x, lst[mid_index:])

    # # Base case: If there's only 1 item in the list, we return whether that
    # #            item is x or not
    # if len(lst) == 1:
    #     return lst[0] == x
    #
    # # Base case #2: If there are no items in the list, we return False.
    # if lst == []:
    #     return False
    #
    # # Recursive step: Split lst into 2 halves.
    # #                 If the middle of our list (where we split on) is
    # #                 larger than x, we make a recursive call to the left half
    # #                 (which contains all numbers smaller than the middle).
    # #                 Otherwise, we make a recursive call on the right half
    # #                 which contains all numbers >= x.
    #
    # mid_index = len(lst) // 2
    # middle = lst[mid_index]
    #
    # if x < middle:
    #     return x_in_sorted_list(x, lst[:mid_index])
    # return x_in_sorted_list(x, lst[mid_index:])

def binary_search(x, lst) -> int:
    if len(lst) == 1:
        if lst[0] == x:
            return 0
        else:
            return -1
    # if not lst:
    #     return -1
    mid_index = len(lst)//2
    if x < lst[mid_index]:
        return binary_search(x,lst[:mid_index])
    else:
        right = binary_search(x,lst[mid_index:])
        if right > -1:
            return mid_index + right
        else:
            return -1

    # # Base case: If there's only 1 item in the list, we return 0 if that item
    # #            is x, otherwise we return -1
    # if len(lst) == 1:
    #     return 0 if lst[0] == x else -1
    #
    # # Base case #2: If there are no items in the list, we return -1.
    # if lst == []:
    #     return -1
    #
    # # Recursive step: Split lst into 2 halves.
    # #                 If the middle of our list (where we split on) is
    # #                 larger than x, we make a recursive call to the left half
    # #                 (which contains all numbers smaller than the middle).
    # #                 Otherwise, we make a recursive call on the right half
    # #                 which contains all numbers >= x.
    # mid_index = len(lst) // 2
    # middle = lst[mid_index]
    #
    # if x < middle:
    #     left = binary_search(x, lst[:mid_index])
    #
    #     # If it was in the left half, we can just return the index returned
    #     # by the recursive call
    #     return left
    #
    # # If it was in the right half, we adjust the index returned by the
    # # recursive call in order to account for the length of the left half of
    # # the list if the index wasn't -1. If the index was -1, we return -1.
    # right = binary_search(x, lst[mid_index:])
    # return mid_index + right if right > -1 else -1
    #

def get_nth_fibonacci_memoized(n: int, fibonaccis: dict={}) -> int:
    if n < 3:
        fibonaccis[n] = 1
    if n in fibonaccis:
        return fibonaccis[n]
    fibonaccis[n] = get_nth_fibonacci_memoized(n-1, fibonaccis) + get_nth_fibonacci_memoized(n-2, fibonaccis)
    return fibonaccis[n]

    # # Base case: If n == 1 or n == 2 then we can return 1.
    # if n < 3:
    #     return 1
    #
    # # Recursive step: If we've already calculated the nth fibonacci number,
    # #                 we can return it.
    # if n in fibonaccis:
    #     return fibonaccis[n]
    #
    # # Otherwise, get the (n - 1)th and (n - 2)th fibonacci numbers and get
    # # their sum (the nth fibonacci number)
    # new_fibonacci = (get_nth_fibonacci_memoized(n - 1, fibonaccis) +
    #                  get_nth_fibonacci_memoized(n - 2, fibonaccis))
    #
    # # Store the nth fibonacci number in our dictionary
    # fibonaccis[n] = new_fibonacci
    #
    # return new_fibonacci

#Exercise 5

def get_all_evens(x: Union[list, int]) -> List[int]:
    """
    Return a list of all of the even ints in x or in any sublists within x.

    Order doesn't matter.
    """
    result = []
    if isinstance(x, int):
        if x % 2 == 0:
            return [x]
        else:
            return []
    else:
        for item in x:
            result.extend(get_all_evens(item))
        return result

# Midterm2 practice
def count_elements_in(x: Union[list, int], lst: List[int]) -> int:
    count = 0
    if isinstance(x, int):
        if x in lst:
            return 1
        else:
            return 0
    else:
        for item in x:
            count += count_elements_in(item, lst)
        return count

def  sum_at_depth(x: Union[list, int], depth: int) -> int:
    result = []
    if isinstance(x, int):
        if depth == 0:
            return x
        else:
            return 0
    else:
        for item in x:
            result += [sum_at_depth(item, depth -1)]
        return sum(result)




#Lab5
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
    result = []
    if isinstance(x, int):
        return 0
    else:
        for item in x:
            result += [get_max_depth(item)]
        return max(result) + 1

    # if not isinstance(x, list):
    #     return 0
    #
    #
    # return max([get_max_depth(item) for item in x]) + 1

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
    if isinstance(x, int):
        if depth == 0:
            return [x]
        else:
            return []
    else:
        for item in x:
            result += get_at_depth(item, depth -1)
    return result


if __name__ == '__main__':
    assert get_at_depth(5, 0) == [5]
    assert get_at_depth(5, 1) == []
    assert get_at_depth([1, 2, 3], 1) == [1, 2, 3]
    assert get_at_depth([[1], 2, [3], 4], 1) == [2, 4]
    assert get_at_depth([1, [[3], 2, [4]], 8, [[5]]], 3) == [3, 4, 5]
    assert get_at_depth([1, [2, [3]], [[[4], 6], 5]], 3) == [3, 6]


    assert get_max_depth(5) == 0
    assert get_max_depth([1, 2, 3]) == 1
    assert get_max_depth([[1], 2]) == 2
    assert get_max_depth([1, [[3]], 8]) == 3
    assert get_max_depth([1, [2, [3]], [[[4]], 5]]) == 4

    assert count_longer_than('cat', 3) == 0
    assert count_longer_than('cat', 2) == 1
    assert count_longer_than(['', 'a', 'at', 'hat'], 1) == 2
    assert count_longer_than([['yes', 'no', [['ok', 'hat'], 'cat']], 'a'],
                             2) == 3
    assert count_longer_than(['a', [['baby'], 'cat'],
                              [['doll'], 'hat', [['cake'], 'hats']]], 3) == 4

    assert count_odd(1) == 1
    assert count_odd(2) == 0
    assert count_odd([1, 3, 4]) == 2
    assert count_odd([[1, 5, [[4, 6], 7]], 9]) == 4
    assert count_odd([1, [2, 3], [4, [5], [[6, 7], 8], 9]]) == 5

    assert sum_at_depth([5] , 1) == 5
    assert sum_at_depth([1, [3, [4, 5, [[6]]], 7], [2, [10]]], 2) == 12


    assert count_elements_in([1, 2, [3, 4], [5, [3], 2], [[1]]], [2, 3]) == 4
    assert count_elements_in(5, [1, 2, 3]) == 0
    assert count_elements_in([[1, 2], [3, [[4], 1], [5], [[7, 8], 1], 5], 3], [1, 3, 5]) == 7

    single_int = 1
    assert get_all_evens(single_int) == []

    lst = [1, 2, 3, 4]
    assert sorted(get_all_evens(lst)) == [2, 4]

    nested_lst = [1, [2, 3, [4]], [[4], 6]]
    assert sorted(get_all_evens(nested_lst)) == [2, 4, 4, 6]

    assert get_nth_fibonacci_memoized(1) == 1
    assert get_nth_fibonacci_memoized(2) == 1
    assert get_nth_fibonacci_memoized(3) == 2
    assert get_nth_fibonacci_memoized(10) == 55
    assert get_nth_fibonacci_memoized(50) == 12586269025
    # assert get_nth_fibonacci_memoized(100) == 354224848179261915075

    assert binary_search(2, [-1, 0, 1]) == -1
    assert binary_search(1, [-5, 0, 1]) == 2
    assert binary_search(10, [1, 10, 11, 15, 20]) == 1
    assert binary_search(15, [1, 2, 4, 10, 15, 18]) == 4
    assert binary_search(20, [1, 5, 7, 8, 10, 20]) == 5
    assert binary_search(25, [1, 5, 7, 8, 10, 20]) == -1

    assert x_in_sorted_list(2, [-1, 0, 1]) == False
    assert x_in_sorted_list(1, [-5, 0, 1]) == True
    assert x_in_sorted_list(10, [1, 10, 11, 15, 20]) == True
    assert x_in_sorted_list(15, [1, 2, 4, 10, 15, 18]) == True
    assert x_in_sorted_list(20, [1, 5, 7, 8, 10, 20]) == True
    assert x_in_sorted_list(25, [1, 5, 7, 8, 10, 20]) == False

    assert x_in_list(2, [-1, 0, 1]) == False
    assert x_in_list(1, [-5, 3, 1]) == True
    assert x_in_list(10, [1, -2, 10, -1, 15, 20]) == True
    assert x_in_list(15, [-1, 0, -4, 15, 3, 1]) == True
    assert x_in_list(20, [-1, 0, -4, 15, 3, 1]) == False

    assert get_nth_fibonacci(1) == 1
    assert get_nth_fibonacci(2) == 1
    assert get_nth_fibonacci(3) == 2
    assert get_nth_fibonacci(10) == 55
    assert get_nth_fibonacci(15) == 610

    assert all_sections_are_words("today", ['to', 'today']) == False
    assert all_sections_are_words("today", ['to', 'day', 'today']) == True
    assert all_sections_are_words("sometome", ['so', 'me', 'to']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'some']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'some', 'tome']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'some', 'tome', 'sometome']) == True
    assert all_sections_are_words("sometome", ['so', 'me', 'some', 'tome', 'sometome']) == False
    assert all_sections_are_words("sometome", ['so', 'me', 'to', 'tome', 'sometome']) == False

    assert count_number_of_lists(5) == 0
    assert count_number_of_lists([5]) == 1
    assert count_number_of_lists([[5], [3], [1]]) == 4
    assert count_number_of_lists([[5], 3, [1, [2], [3]]]) == 5

    assert get_all_elements(5) == [5]
    assert get_all_elements([5, 15]) == [5, 15]
    assert get_all_elements([5, 15, [[25, 30], 45]]) == [5, 15, 25, 30, 45]
    assert get_all_elements([[5], 3, [1, [2], [3]]]) == [5, 3, 1, 2, 3]
    assert get_all_elements([[1, 2], [3, [4], [[5]]], [6, [7, [8, 9]], 10]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert passes_condition(f, 5) == []
    assert passes_condition(f, 25) == [25]
    assert passes_condition(f, [15, 25, 30]) == [25, 30]
    assert passes_condition(f, [[100, 3], [[15, 25, 30]], 45]) == [100, 25, 30, 45]
    assert passes_condition(f, [100, [[25, 3], 150, 10], [[30, [15, 20]], 5]]) == [100, 25, 150, 30, 20]

    assert count_number_of_lists(5) == 0
    assert count_number_of_lists([5]) == 1
    assert count_number_of_lists([[5], [3], [1]]) == 4
    assert count_number_of_lists([[5], 3, [1, [2], [3]]]) == 5
