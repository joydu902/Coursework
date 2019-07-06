import java.util.*;
import java.util.HashSet;

public class HashSetTutorial {


    /**
     * TODO: Define a static method createIntegerHashSetWithArrayList that can create a
     * HashSet containing the elements of arraylist
     *
     * @param arrayList an ArrayList contain only Integers
     * @return A HashSet containing the elements of arraylist
     */
    public static HashSet createIntegerHashSetWithArrayList(ArrayList arrayList){
        HashSet haha = new HashSet<Integer>(arrayList);
        return haha;
    }


    /**
     * TODO: Define a static method clearHashSet that can clear a hashSet.
     * (i.e. No element will be left in the set.)
     * @param hashSet The HashSet to be cleared.
     */

    public static void main(String[] args) {

        // here is an ArrayList that contain some student numbers.
        ArrayList<Integer> studentNumberArrayList = new ArrayList<>();
        studentNumberArrayList.add(10001);
        studentNumberArrayList.add(10002);
        studentNumberArrayList.add(10002);
        studentNumberArrayList.add(10003);
        studentNumberArrayList.add(10003);
        studentNumberArrayList.add(10004);



        // TODO: Create a HashSet of the student numbers using createIntegerHashSetWithArrayList method.


        // TODO: Clear the HashSet studentNumberSet using clearHashSet method.

    }

}