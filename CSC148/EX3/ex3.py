"""
MIN DU 1002602230
The DictionaryStack class for ex3.
Do NOT change the __init__ method.
Part of the __str__ method has been provided for you.

You need to implement:
    - add
    - remove
    - is_empty
    - __str__
"""
class DictionaryStack:
    """
    A class representing a DictionaryStack.
    """
    
    def __init__(self) -> None:
        """
        Initialize this DictionaryStack.
        
        >>> d = DictionaryStack()
        >>> d.is_empty()
        True
        """
        self._content = {}
        self._next_index = 0

    def __str__(self) -> str:
        """
        Return a string representation of this Stack.

        >>> d = DictionaryStack()
        >>> d.add(3)
        >>> d.add("Apple")
        >>> print(d)
        3, Apple <- Top

        """
        # You should be adding the string version of each item in the stack
        # into the list.
        # They should be in the order they were added (i.e. oldest -> newest)
        # so the last item is the one we're removing last.

        list_to_return = []
        for i in range(self._next_index):
            list_to_return.append(str(self._content[i]))

        return  ", ".join(list_to_return) + " <- Top"

    def add(self, value: object) -> None:
        """
        Add value to the DictionaryStack.

        >>> d = DictionaryStack()
        >>> d.add(3)
        >>> d.add("Apple")
        >>> d._content
        {0: 3, 1: 'Apple'}
        """
        self._content[self._next_index] = value
        self._next_index += 1

    def is_empty(self) -> bool:
        """
        Check if DictionaryStack is empty or not.

        >>> d = DictionaryStack()
        >>> d.add(3)
        >>> d.is_empty()
        False
        >>> d.remove()
        3
        >>> d.is_empty()
        True
        """
        return self._content == {}

    def remove(self) -> object:
        """

        >>> d = DictionaryStack()
        >>> d.add(3)
        >>> d.add("Apple")
        >>> d.remove()
        'Apple'
        >>> d.remove()
        3
        """
        item = self._content.pop(self._next_index - 1)
        self._next_index -= 1
        return item




# ---- Everything below this is client code. Do NOT modify anything! ----
# ---- Everything below this is client code. Do NOT modify anything! ----
if __name__ == '__main__':
    d = DictionaryStack()

    # The format for assert is as follows:
    # assert <thing we want to check>, <error message>

    d.add(3)
    error_message = ("After adding 3 to the DictionaryStack, we " +
                     "expected False to be returned when " +
                     "we called d.is_empty but got {} " +
                     "instead").format(d.is_empty())
    assert not d.is_empty(), error_message

    removed_item = d.remove()
    error_message = ("After adding 3 to the DictionaryStack, we expected " +
                     "3 to be removed when we called d.remove() but got " +
                     "{} instead").format(removed_item)
    assert 3 == removed_item, error_message

    error_message = ("After adding 3 and removing it from the " +
                     "DictionaryStack, we expected True to be returned when " +
                     "we called d.is_empty but got {} " +
                     "instead").format(d.is_empty())
    assert d.is_empty(), error_message

    d.add(1)
    d.add("A")
    d.add(5)

    removed_item = d.remove()
    error_message = ("After adding 5 to the DictionaryStack, we expected " +
                     "5 to be removed when we called d.remove() but got " +
                     "{} instead").format(removed_item)
    assert 5 == removed_item, error_message

    expected_string = "1, A <- Top"
    error_message = ("A DictionaryStack that had 1 added to it and then " +
                     "'A' should return the string {} but got " +
                     "{} instead").format(expected_string, str(d))
    assert expected_string == str(d), error_message

    removed_item = d.remove()
    error_message = ("After removing from a stack containing 1 and 'A'," +
                     " we expected 'A' to be removed when we called " +
                     "d.remove() but we got {} instead").format(removed_item)
    assert 'A' == removed_item, error_message

    expected_string = "1 <- Top"
    error_message = ("A DictionaryStack that has 1 in it " +
                     "should return the string {} but got " +
                     "{} instead").format(expected_string, str(d))
    assert expected_string == str(d), error_message

    # Below is how python_ta (PythonTA/pyTA/etc.) is called.
    # When run, your code should produce no errors from python_ta.
    # You must have python_ta installed for this to work (see Lab 1 and
    # the Software Installation page).
    import python_ta

    python_ta.check_all(config="ex3_pyta.txt")
