package PCRS.src;

public class SimpleLinkedList<T> {
    private Node<T> first;

    /**
     * Constructor for SimpleLinkedList.
     */
    public SimpleLinkedList() {
        first = null;
    }

    /**
     * Returns the Node of the first element in the LinkedList.
     *
     * @return the Node of the first element.
     */
    public Node<T> getFirst() {
        return first;
    }

    /**
     * Sets the first element to first.
     *
     * @param first the Node to set the first element to
     */
    public void setFirst(Node<T> first) {
        this.first = first;
    }
}
