"""
Solutions to lab 5.

Included are really lengthy explanations of each part of the lab.
"""
from typing import Union, Any

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
    if isinstance(x, int):
        if x % 2 == 1:
            return 1
        else:
            return 0
    return sum([count_odd(item) for item in x])

    # count = 0
    # if isinstance(x, int):
    #     if x % 2 == 1:
    #         count += 1
    #
    # else:
    #     for item in x:
    #         count += count_odd(item)
    # return count



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

    return sum([count_longer_than(item, length) for item in x])

    # else:
    #     for item in x:
    #         count += count_longer_than(item, length)
    # return count

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
    if isinstance(x, int):
        return 0
    return max([get_max_depth(item) for item in x]) + 1

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
    if not isinstance(x, list):
        if depth == 0:
            return [x]
        else:
            return []
    return sum([get_at_depth(item, depth -1) for item in x], [])


if __name__ == '__main__':
    assert count_odd(1) == 1
    assert count_odd(2) == 0
    assert count_odd([1, 3, 4]) == 2
    assert count_odd([[1, 5, [[4, 6], 7]], 9]) == 4
    assert count_odd([1, [2, 3], [4, [5], [[6, 7], 8], 9]]) == 5
    
    assert count_longer_than('cat', 3) == 0
    assert count_longer_than('cat', 2) == 1
    assert count_longer_than(['', 'a', 'at', 'hat'], 1) == 2
    assert count_longer_than([['yes', 'no', [['ok', 'hat'], 'cat']], 'a'],
                             2) == 3
    assert count_longer_than(['a', [['baby'], 'cat'],
                              [['doll'], 'hat', [['cake'], 'hats']]], 3) == 4

    assert get_max_depth(5) == 0
    assert get_max_depth([1, 2, 3]) == 1
    assert get_max_depth([[1], 2]) == 2
    assert get_max_depth([1, [[3]], 8]) == 3
    assert get_max_depth([1, [2, [3]], [[[4]], 5]]) == 4

    assert get_at_depth(5, 0) == [5]
    assert get_at_depth(5, 1) == []
    assert get_at_depth([1, 2, 3], 1) == [1, 2, 3]
    assert get_at_depth([[1], 2, [3], 4], 1) == [2, 4]
    assert get_at_depth([1, [[3], 2, [4]], 8, [[5]]], 3) == [3, 4, 5]
    assert get_at_depth([1, [2, [3]], [[[4], 6], 5]], 3) == [3, 6]
