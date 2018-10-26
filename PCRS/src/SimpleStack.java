package PCRS.src;

/**
 * An implementation of the Stack data structure based on LinkedList.
 */
public class SimpleStack<T> {

    private SimpleLinkedList<T> stack;

    /**
     * Constructs an empty SimpleStack.
     */
    public SimpleStack() {
        stack = new SimpleLinkedList<T>();
    }

    /**
     * Pushes obj onto stack.
     *
     * @param obj is pushed onto stack.
     */
    public void push(T obj) {
        Node<T> node = new Node<T>();
        node.value = obj;
        node.next = stack.getFirst();
        stack.setFirst(node);
    }

    /**
     * Pops the top object on stack.
     *
     * @return the top object on stack.
     */
    public T pop() {
        Node<T> node;
        if (isEmpty()) {
            return null;
        } else {
            node = stack.getFirst();
            stack.setFirst(node.next);
            return node.value;
        }
    }

    /**
     * Returns true when the stack is empty, false otherwise.
     */
    public boolean isEmpty() {
        return (stack.getFirst() == null);
    }
}
