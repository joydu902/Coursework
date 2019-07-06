from typing import List, Union, Type, Any, Callable


# Practice Problems: Recursion with Nested Lists
def count_strings_with_length(x: Union[list, str]) -> dict:######
    """
    Return a dictionary mapping the length of each word in x to the number of
    times that length appears.

    >>> count_strings_with_length('cat')
    {3: 1}
    >>> count_strings_with_length(['cat', ['a', 'dog'], [[['b'], 'no'], 'yes']])
    {3: 3, 1: 2, 2: 1}
    """
    new_dict = {}
    if not isinstance(x, list):
        return {len(x) : 1}
    else:
        for item in x:
            lengths = count_strings_with_length(item)
            for key in lengths:
                if key in new_dict:
                    new_dict[key] += lengths[key]
                else:
                    new_dict[key] = lengths[key]
        return new_dict



    # if isinstance(x, str):
    #     return {len(x): 1}
    # else:
    #     new_dict = {}
    #     for item in x:
    #         lengths = count_strings_with_length(item)
    #         for key in lengths:
    #             if key in new_dict:
    #                 new_dict[key] += lengths[key]
    #             else:
    #                 new_dict[key] = lengths[key]
    #     return new_dict


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
    result = []
    if not isinstance(x, list):
        if type(x) == t:
            return [x]
        else:
            return []
    else:
        for item in x:
            result += return_values_with_type(item, t)
        return result


def get_max(x: Union[list, int]) -> int:
    """
    Return largest int in x.

    >>> get_max(1)
    1
    >>> get_max([1, [[3], 0], 2])
    3
    """
    result = []
    if isinstance(x, int):
        return x
    else:
        for item in x:
            result += [get_max(item)]
        return max(result)


def get_min(x: Union[list, int]) -> int:
    """
    Return smallest int in x.

    >>> get_min(1)
    1
    >>> get_min([1, [[3], 0], 2])
    0
    """
    result = []
    if isinstance(x, int):
        return x
    else:
        for item in x:
            result += [get_min(item)]
        return min(result)


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
    result = []
    if isinstance(x, bool):
        return x
    else:
        for item in x:
            result += [all_true(item)]
        return all(result)


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
    result = []
    if isinstance(x, bool):
        return x
    else:
        for item in x:
            result += [any_true(item)]
        return any(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
