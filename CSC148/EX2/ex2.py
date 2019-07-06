""" EX2 MIN DU """
class Person:
    """
    A class representing a Person.
    """
    def __init__(self, name: str) -> None:
        """
        Initialize Person with name.

        >>> p2 = Person("Joy")
        >>> p2.name
        'Joy'
        >>> p2.food_list
        []
        """
        self.name = name
        self.food_list = []

    def eat(self, food: str) -> None:
        """
        Add food to person's food list.

        >>> p2 = Person("Joy")
        >>> p2.eat("Milk")
        >>> p2.eat("Cake")
        >>> p2.food_list
        ['Milk', 'Cake']

        """
        self.food_list.append(food)

    def get_eaten_food(self) -> list:
        """
        Return person's food list.

        >>> p2 = Person("Joy")
        >>> p2.eat("Milk")
        >>> p2.eat("Cake")
        >>> p2.food_list
        ['Milk', 'Cake']
        >>> p2.get_eaten_food()
        ['Milk', 'Cake']
        """
        return self.food_list

    def change_name(self, new_name: str) -> None:
        """
        Change name of person.

        >>> p2 = Person("Joy")
        >>> p2.change_name("Jeff")
        >>> p2.name
        'Jeff'

        """
        self.name = new_name

    def __eq__(self, other) -> bool:
        """
        Return True if person have the \
        same name and eaten foods as the other person.

        >>> p2 = Person("Joy")
        >>> p2.eat("Milk")
        >>> p2.eat("Cake")
        >>> p3 = Person("Alice")
        >>> p3.eat("Milk")
        >>> p3.eat("Cake")
        >>> p2 == p3
        False
        >>> s2 = Student("Joy")
        >>> s2.eat("Milk")
        >>> s2.eat("Cake")
        >>> p2 == s2
        True
        >>> p3 == s2
        False

        """
        if isinstance(other, Person) :
            return self.name == other.name and self.food_list == other.food_list
        return NotImplemented

    def __str__(self) -> str:
        """
        Return a string representing food people has eaten.

        >>> p2 = Person("Joy")
        >>> p2.eat("Milk")
        >>> p2.eat("Cake")
        >>> p2.eat("Takoyaki")
        >>> print(p2)
        Joy is a Person who has eaten 3 thing(s).

        """
        return "{} is a Person who has eaten {} thing(s).".\
            format(self.name, len(self.food_list))


class Student(Person):
    """
    A class representing a Student.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize Student with name.

        >>> s2 = Student("Anna")
        >>> s2.name
        'Anna'
        >>> s2.food_list
        []
        >>> s2.course_list
        []
        """
        super().__init__(name)
        self.food_list = []
        self.course_list = []

    def __str__(self) -> str:
        """
        Return a string representing food student has eaten.

        >>> s2 = Student("Anna")
        >>> s2.eat("Juice")
        >>> s2.eat("Cake")
        >>> print(s2)
        Anna is a Student who has eaten 2 thing(s).

        """
        return "{} is a Student who has eaten {} thing(s).".\
            format(self.name, len(self.food_list))

    def add_course(self, course_name: str) -> None:
        """
        Add course to student's course list.

        >>> s2 = Student("Anna")
        >>> s2.add_course("CSC165")
        >>> s2.add_course("CSC209")
        >>> s2.course_list
        ['CSC165', 'CSC209']

        """
        self.course_list.append(course_name)

    def get_courses(self) -> list:
        """
        Get the course list of the Student.

        >>> s2 = Student("Anna")
        >>> s2.add_course("CSC165")
        >>> s2.add_course("CSC209")
        >>> s2.add_course("MAT137")
        >>> s2.get_courses()
        ['CSC165', 'CSC209', 'MAT137']

        """
        return self.course_list


class Course:
    """
    A class representing a Course.
    """
    def __init__(self, course_name: str) -> None:
        """
        Initialize Course with course name.

        >>> c2 = Course("CSC263")
        >>> c2._course_name
        'CSC263'
        >>> c2.student_list
        []
        """
        self._course_name = course_name
        self.student_list = []

    def add_student(self, student: Student) -> None:
        """
        Add Student to course's student list, \
        and add the course to student's course list at the same time.

        >>> c2 = Course("CSC263")
        >>> s2 = Student("Jeff")
        >>> s3 = Student("Joy")
        >>> c2.add_student(s2)
        >>> c2.add_student(s3)
        >>> type(c2.student_list[0])
        <class '__main__.Student'>
        >>> type(c2.student_list[1])
        <class '__main__.Student'>
        >>> s2.get_courses()
        ['CSC263']
        """
        self.student_list.append(student)
        student.add_course(self._course_name)

    def __str__(self) -> str:
        """
        Return a string representing amount
        of food students enrolled in CSC148 ate.

        >>> c2 = Course("CSC263")
        >>> s2 = Student("Jeff")
        >>> s3 = Student("Joy")
        >>> c2.add_student(s2)
        >>> c2.add_student(s3)
        >>> s3.eat("Chips")
        >>> print(c2)
        CSC263 Student log:
        Jeff is a Student who has eaten 0 thing(s).
        Joy is a Student who has eaten 1 thing(s).
        """
        result = self._course_name + " Student log:"
        for student in self.student_list:
            result += "\n{} is a Student who has eaten {} thing(s)."\
                .format(student.name, len(student.get_eaten_food()))
        return result


# ---- Everything below this is client code. Do NOT modify anything! ----
if __name__ == '__main__':
    s = Student("Sophia")
    p = Person("Jen")

    # A Student should be a Person, but a Person should not be a Student
    assert isinstance(s, Person), "A Student should also be a Person"
    assert not isinstance(p, Student), "A Person should not be a Student"

    s.eat("Cupcake")
    s.eat("Apple")

    # get_eaten_food() should return a list of foods in the order they were
    # eaten
    expected = ("s.get_eaten_food() returned {} instead " +
                "of ['Cupcake, 'Apple']").format(s.get_eaten_food())
    assert s.get_eaten_food() == ['Cupcake', 'Apple'], expected

    p.eat("Cupcake")
    p.eat("Apple")

    expected = ("p.get_eaten_food() returned {} instead " +
                "of ['Cupcake, 'Apple']").format(s.get_eaten_food())
    assert p.get_eaten_food() == ['Cupcake', 'Apple'], expected

    assert p != s, ("A Person should only be equal to another object if they" +
                    " have the same name and eaten foods.")

    p.change_name("Sophia")

    assert p == s, ("A Person should be equal to another object if they" +
                    " have the same name and eaten foods.")
    assert s == p, ("A Student should be equal to another object if they" +
                    " have the same name and eaten foods.")

    error = ("str(p) was expected to return\nSophia is a Person who has " +
             "eaten 2 thing(s).\nBut got\n{}\ninstead.").format(str(p))

    assert str(p) == "Sophia is a Person who has eaten 2 thing(s).", error

    error = ("str(s) was expected to return\nSophia is a Student who has " +
             "eaten 2 thing(s).\nBut got\n{}\ninstead.").format(str(s))
    assert str(s) == "Sophia is a Student who has eaten 2 thing(s).", error

    c = Course("CSC148")
    c.add_student(s)

    # Assume that get_courses() returns a list in the order that the
    # courses were added
    expected = ("After adding a Student to a Course, that Student should " +
                "have that course in the list returned by get_courses but " +
                "got {} instead.").format(s.get_courses())
    assert s.get_courses() == ["CSC148"], expected

    assert s == p, ("After adding a course to a Student, that Student should " +
                    "be equal to a Person with the same foods eaten and name.")
    assert p == s, ("After adding a course to a Student, that Person should " +
                    "be equal to a Student with the same foods eaten and name.")

    assert not getattr(p, 'get_courses', None), ("Person should not have a " +
                                                 "get_courses() method.")

    expected = ("When printing a Course, the string\n" +
                "CSC148 Student log:\nSophia is a Student " +
                "who has eaten 2 thing(s).\nWas expected" +
                ", but we got\n{}\ninstead").format(str(c))
    assert str(c) == ("CSC148 Student log:\nSophia is a Student " +
                      "who has eaten 2 thing(s)."), expected

    s2 = Student("Jacqueline")
    c.add_student(s2)

    expected = ("When printing a Course, the string\n" +
                "CSC148 Student log:\nSophia is a Student " +
                "who has eaten 2 thing(s).\nJacqueline " +
                "is a Student who has eaten 0 thing(s).\nWas expected" +
                ", but we got\n{}\ninstead").format(str(c))
    assert str(c) == ("CSC148 Student log:\nSophia is a Student " +
                      "who has eaten 2 thing(s).\nJacqueline is a Student " +
                      "who has eaten 0 thing(s)."), expected

    # Below is how python_ta (PythonTA/pyTA/etc.) is called.
    # When run, your code should produce no errors from python_ta.
    # You must have python_ta installed for this to work (see Lab 1 and
    # the Software Installation page).
    import python_ta

    python_ta.check_all(config="ex2_pyta.txt")
