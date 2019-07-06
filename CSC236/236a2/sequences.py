# count subsequences
from typing import Union

def count_subsequences(s1: str, s2: str,
                       i: int, j: int) -> int:
    """ Return the number of times s1[: i] occurs as a
    subsequence of s2[: j].

    Precondition: 0 <= i <= len(s1), 0 <= j <= len(s2)

    >>> count_subsequences("", "Danny", 0, 5)
    1
    >>> count_subsequences("Danny", "", 5, 0)
    0
    >>> count_subsequences("AAA", "AAAAA", 3, 5)
    10
    >>> count_subsequences("TAGAC", "ATAGGACCA ", 5, 9)
    4
    >>>

    Postcondition: returns number of times s1[: i} occurs as a
    subsequence of s2[: j]
    """
    if i == 0:
        return 1
    elif i > j:
        return 0
    elif s1[i-1] != s2[j-1]:
        return count_subsequences(s1, s2, i, j-1)
    else:
        return (count_subsequences(s1, s2, i, j-1)
                + count_subsequences(s1, s2, i-1, j-1))

def count_subsequences_memoized(s1: str, s2: str, i: int, j: int,
                                seen: Union[dict, None]=None) -> int:
    """ Return the number of times s1[: i] occurs as a
    subsequence of s2[: j].
   
    Precondition: 0 <= i < len(s1), 0 <= j < len(s2)
   
    >>> count_subsequences_memoized("", "Danny", 0, 5, None)
    1
    >>> count_subsequences_memoized("Danny", "", 5, 0, None)
    0
    >>> count_subsequences_memoized("AAA", "AAAAA", 3, 5, None)
    10
   
    Postcondition: returns number of times s1[: i} occurs as a
    subsequence of s2[: j]
    """
    if seen is None:
        seen = {}
    else:
        pass
    if (i , j) not in seen:
        if i == 0:
            seen[(i, j)] = 1
        elif i > j:
            seen[(i, j)] = 0
        elif s1[i-1] != s2[j-1]:
            seen[(i, j)] = count_subsequences_memoized(s1, s2, i, j-1, seen)
        else:
            seen[(i, j)] = (count_subsequences_memoized(s1, s2, i, j-1, seen)
                            + count_subsequences_memoized(s1, s2, i-1, j-1, seen))
    return seen[(i, j)]



if __name__ == "__main__":
    from doctest import testmod
    testmod()

