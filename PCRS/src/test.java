package PCRS.src;

public class test {

    /**
     * Counts the number of elements in array that are smaller than element.
     * @param array: an array to compare with element
     * @param element: an element to be compared with array
     * @return: the number of elements smaller than element
     */
    public <T extends Comparable<T>> int countSmallerThan(T[] array, T element) {
        int count = 0;
        for (int i = 0; i < array.length; i ++){
            if ((array[i]).compareTo(element) < 0){
                count += 1;
            }
        }
        return count;
    }

}
