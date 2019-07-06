"""EX1 MIN DU"""
class Course:
    """
    A class representing a Course.
    """
    def __init__(self, course_name: str) -> None:
        """
        Initialize the Course with class class.

        >>> a = Course("MAT223")
        >>> a.course_name
        'MAT223'
        >>> a.student_list
        []
        >>> a.waitlist
        []
        >>> a.capacity
        0
        """
        self.course_name = course_name
        self.student_list = []
        self.waitlist = []
        self.capacity = 0

    def set_course_capacity(self, capacity: int) -> None:
        """
        Set capacity to course.

        >>> a = Course("MAT223")
        >>> a.set_course_capacity(3)
        >>> a.capacity
        3
        """
        self.capacity = capacity

    def __str__(self) -> str:
        """
        Return a string representing this course.
         >>> a = Course("MAT223")
         >>>

        """
        return "The course {} has {} student(s) enrolled with {} student(s) " \
               "on the waitlist.".format\
            (self.course_name, len(self.student_list), len(self.waitlist))

    def add_student(self, name: str) -> None:
        """
        Add a student with name name to course.

        >>> a = Course("MAT223")
        >>> a.set_course_capacity(3)
        >>> a.add_student("Taeyeon")
        >>> a.add_student("Jessica")
        >>> a.add_student("Tiffany")
        >>> a.student_list
        ['Taeyeon', 'Jessica', 'Tiffany']
        >>> a.add_student("Angela")
        >>> a.waitlist
        ['Angela']
        """
        if len(self.student_list) >= self.capacity:
            self.waitlist.append(name)
        else:
            self.student_list.append(name)

    def get_enrolled_students(self) -> list:
        """
        Return all the students enorlled in this course in order.

        >>> a = Course("MAT223")
        >>> a.set_course_capacity(3)
        >>> a.add_student("Taeyeon")
        >>> a.add_student("Jessica")
        >>> a.add_student("Tiffany")
        >>> a.get_enrolled_students()
        ['Jessica', 'Taeyeon', 'Tiffany']
        """
        result = self.student_list.copy()
        result.sort()
        return result

    def get_waitlist(self) -> list:
        """
        Return all the students in waitlist in the order they added

        >>> a = Course("MAT223")
        >>> a.add_student("Taeyeon")
        >>> a.add_student("Jessica")
        >>> a.add_student("Tiffany")
        >>> a.get_waitlist()
        ['Taeyeon', 'Jessica', 'Tiffany']
        """
        return self.waitlist

    def remove_student(self, name: str) -> None:
        """
        Remove student with name from list.

        >>> a = Course("MAT223")
        >>> a.set_course_capacity(2)
        >>> a.add_student("Taeyeon")
        >>> a.add_student("Jessica")
        >>> a.add_student("Tiffany")
        >>> a.add_student("Angela")
        >>> a.remove_student("Taeyeon")
        >>> a.remove_student("Jessica")
        >>> a.student_list
        ['Tiffany', 'Angela']
        >>> a.waitlist
        []
        """
        if name in self.student_list:
            self.student_list.remove(name)
            self.student_list.append(self.waitlist.pop(0))
        elif name in self.waitlist:
            self.waitlist.remove(name)

    def __eq__(self, other) -> bool:
        """
        Return True if the enrolled students are the same,
        the waitlist is the same (in the same order),
        and the course code and capacity are the same.

        >>> a = Course("MAT223")
        >>> a.set_course_capacity(2)
        >>> a.add_student("Taeyeon")
        >>> a.add_student("Jessica")
        >>> a.add_student("Tiffany")
        >>> a.add_student("Angela")
        >>> b = Course("MAT223")
        >>> b.set_course_capacity(2)
        >>> b.add_student("Taeyeon")
        >>> b.add_student("Jessica")
        >>> b.add_student("Tiffany")
        >>> b.add_student("Angela")
        >>> a == b
        True
        """
        other.student_list.sort()
        result = self.student_list.copy()
        result.sort()
        return other.student_list == result \
               and other.waitlist == self.waitlist \
               and other.course_name == self.course_name \
               and other.capacity == self.capacity


if __name__ == '__main__':
    c = Course("CSC148")
    c.set_course_capacity(2)  # You may assume this number will always be a
    # positive integer and that set_course_capacity()
    # will be called before adding students and
    # never after adding students.

    c.add_student("Sophia")
    c.add_student("Danny")
    c.add_student("Jacqueline")

    assert str(c) == ("The course CSC148 has 2 student(s) enrolled with" +
                      " 1 student(s) on the waitlist.")

    # get_enrolled_students() should return the enrolled students in sorted
    # order.
    assert c.get_enrolled_students() == ['Danny', 'Sophia']

    # get_waitlist() should return the students on the waitlist in the order
    # that they were added.
    assert c.get_waitlist() == ['Jacqueline']

    c.add_student("David")
    assert c.get_waitlist() == ['Jacqueline', 'David']

    # if remove_student() removes an enrolled student, add in the first
    # waitlisted student to enrolled students.
    # HINT: The list method .pop() might be useful here.
    #       See help(list.pop) for details.
    c.remove_student("Danny")
    assert c.get_enrolled_students() == ['Jacqueline', 'Sophia']
    assert c.get_waitlist() == ['David']

    c.remove_student("David")
    assert c.get_waitlist() == []

    # When comparing 2 courses, they are the same if the enrolled students
    # are the same (regardless of order), the waitlist is the same
    # (and in the same order), and the course code and capacity are the same.
    c2 = Course("CSC148")
    c2.set_course_capacity(2)
    c2.add_student("Jacqueline")
    c2.add_student("Sophia")
    assert c == c2

    c2.add_student("David")
    assert c != c2

    # Below is how python_ta (PythonTA/pyTA/etc.) is called.
    # When run, your code should produce no errors from python_ta.
    # You must have python_ta installed for this to work (see Lab 1 and
    # the Software Installation page).
    import python_ta

    python_ta.check_all(config="ex1_pyta.txt")
