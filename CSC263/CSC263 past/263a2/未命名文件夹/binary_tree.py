

class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
    """

    def __init__(self, data, left=None, right=None):
        """
        Create BinaryTree self with data and children left and right.

        @param BinaryTree self: this binary tree
        @param object data: data of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.

        @param BinaryTree self: this binary tree
        @param Any other: object to check equivalence to self
        @rtype: bool

        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        @param BinaryTree self: this binary tree
        @rtype: str

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.data),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder.  Indent by indent.

        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = (self.right.__str__(
            indent + "    ") if self.right else "")
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return (right_tree + "{}{}\n".format(indent, str(self.data)) +
                left_tree)

    def __contains__(self, value):
        """
        Return whether tree rooted at node contains value.

        @param BinaryTree self: binary tree to search for value
        @param object value: value to search for
        @rtype: bool

        >>> 7 in BinaryTree(5, BinaryTree(7), BinaryTree(9))
        True
        >>> 7 in BinaryTree(5)
        False
        """
        # handling the None case will be trickier for a method

        return (self.data == value or
                (self.left and value in self.left) or
                (self.right and self.right.__contains__(value)))


def is_avl(root):
    """

    >>> t1 = BinaryTree(5, BinaryTree(7), BinaryTree(9))
    >>> is_avl(t1)
    True
    >>> t2 = BinaryTree(5, None, BinaryTree(7, None, BinaryTree(9)))
    >>> is_avl(t2)
    False

    """
    if not root:
        return True
    else:
        return is_avl(root.left) and is_avl(root.right) and \
               abs(height(root.left) - height(root.right)) <= 1


def height(root):
    """
    Return the height of BinaryTree t, that is 1 more than the
    maximum of the height of its chidren, 1 if t has no
    children, or 0 if t is the empty tree.
    @param BinaryTree|None t: possibly empty BinaryTree
    @rtype: int
    >>> height(None)
    0
    >>> t1 = BinaryTree(5)
    >>> t2 = BinaryTree(4, t1, None)
    >>> height(t1)
    1
    >>> height(t2)
    2
    """
    if not root:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


def evaluate(b):
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float data.  Otherwise, evaluate b.left and
    b.right and combine them with b.data.

    Assume:  -- b is a non-empty binary tree
             -- interior nodes contain data in {"+", "-", "*", "/"}
             -- interior nodes always have two children
             -- leaves contain float data

     @param BinaryTree b: binary tree representing arithmetic expression
     @rtype: float

    >>> b = BinaryTree(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
    >>> evaluate(b)
    12.0
    >>> b = BinaryTree("+", BinaryTree('*', BinaryTree(3.0), BinaryTree(4.0)),\
    BinaryTree(7.0))
    >>> evaluate(b)
    19.0
    """
    if not b.left and not b.right:
        return b.data
    else:
        return eval('{} {} {}'.format(evaluate(b.left),
                                      b.data, evaluate(b.right)))

def inorder_visit(root, act):
    """
    Visit each node of binary tree rooted at root in order and act.

    @param BinaryTree root: binary tree to visit
    @param (BinaryTree)->object act: function to execute on visit
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.data)
    >>> inorder_visit(b, f)
    2
    4
    6
    8
    10
    12
    14
    """
    if root is None:
        pass
    else:
        inorder_visit(root.left, act)
        act(root)
        inorder_visit(root.right, act)


# assume binary search tree order property
def bst_contains(node, value):
    """
    Return whether tree rooted at node contains value.

    Assume node is the root of a Binary Search Tree

    @param BinaryTree|None node: node of a Binary Search Tree
    @param object value: value to search for
    @rtype: bool

    >>> bst_contains(None, 5)
    False
    >>> bst_contains(BinaryTree(7, BinaryTree(5), BinaryTree(9)), 5)
    True
    """
    if node is None:
        return False
    elif value < node.data:
        return bst_contains(node.left, value)
    elif value > node.data:
        return bst_contains(node.right, value)
    else:
        return True


def insert(node, data):
    """
    Insert data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param BinaryTree node: root of a binary search tree.
    @param object data: data to insert into BST, if necessary.

    >>> b = BinaryTree(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """
    return_node = node
    if not node:
        return_node = BinaryTree(data)
    elif data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:  # nothing to do
        pass
    return return_node


def find_parent(curr, value):
    if curr is None:
        return None
    else:
        if curr.data == value:
            return curr
        else:
            node = find_parent(curr.left, value)
            if node is None:
                node = find_parent(curr.right, value)
            return node

if __name__ == '__main__':
    import doctest
    doctest.testmod()
