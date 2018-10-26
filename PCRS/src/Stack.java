import java.util.ArrayList;
import java.lang.Throwable;

public class Stack<T> {

    // the maximum size of the stack
    protected int stackSize;

    // the internal structure of the stack
    protected ArrayList<T> stack;

    // the last popped element
    protected T lastPoppedElement;

    // the constructor
    public Stack(int size) {
        stack = new ArrayList<>();
        stackSize = size;
    }

    /**
     * TODO: This method adds an new Element to the stack.
     *
     * @param newElement the new element to be added
     * @throws StackOverflowException when the new stack size exceeds the size limit
     */
    public void push(T newElement) throws StackOverflowException {
        if (stack.size() == stackSize) {
            throw new StackOverflowException();
        } else {
            this.stack.add(newElement);
        }
    }

    /**
     * This method pops an element from the top of the stack.
     * TODO: This method should handle IndexOutOfBoundsException which is thrown by the private
     * variable stack, an ArrayList, when the referencing index is out of bound. Then it should print
     * "The stack is empty." and return the lastPoppedElement.
     *
     * @return the last popped element from the stack
     */
    public T pop() throws IndexOutOfBoundsException {
        try {
            int indexLast = stack.size()-1;
            lastPoppedElement = stack.remove(indexLast);
            return lastPoppedElement;
        } catch (IndexOutOfBoundsException e) {
            return lastPoppedElement;
        }

    }

    public static void main(String[] args) throws StackOverflowException{
        Stack myStack = new Stack<>(4);

        myStack.push(1);
        myStack.push(2);
        myStack.push(3);
        myStack.push(4);
        myStack.push(5);
    }



}