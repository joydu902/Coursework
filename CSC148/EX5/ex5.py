"""
Implement the get_all_evens() method below.
"""

from typing import Union, List

def get_all_evens(x: Union[list, int]) -> List[int]:
    """
    Return a list of all of the even ints in x or in any sublists within x.
    
    Order doesn't matter.

    >>> x = 16
    >>> get_all_evens(x)
    [16]
    >>> x = [[[[7, 8, [[[100]]]], 9], 12, 11]]
    >>> get_all_evens(x)
    [8, 100, 12]
    >>> x = [1, [3, 5]]
    >>> get_all_evens(x)
    []
    """
    results = []

    if isinstance(x, int):
        if x % 2 == 0:
            results.append(x)
    else:
        for item in x:
            results.extend(get_all_evens(item))

    return results


if __name__ == '__main__':
    single_int = 1
    assert get_all_evens(single_int) == []

    lst = [1, 2, 3, 4]
    assert sorted(get_all_evens(lst)) == [2, 4]

    nested_lst = [1, [2, 3, [4]], [[4], 6]]
    assert sorted(get_all_evens(nested_lst)) == [2, 4, 4, 6]

    import python_ta

    python_ta.check_all(config="ex5_pyta.txt")
