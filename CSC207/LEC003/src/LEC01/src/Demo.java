package LEC01.src;

import java.util.ArrayList;
import java.util.List;

/**
 * Demonstrate printing, Strings, arrays, and instantiating an object.
 */
public class Demo {

    /**
     * The main method.
     *
     * @param args the command-line arguments.
     */
    public static void main(String[] args) {

        // Expressions, printing, Strings, and arrays.
        System.out.println(3 + 4 * 2 - (-6 * 5));
        String myName = "Paul";
        String anotherVariable;
        String[] myStrings = new String[]{"Paul", "Mike"};
        myStrings[1] = "Jeff";
        System.out.println(myStrings[1]);

        // A person.
        Person p = new Person("griespau", myStrings);
        System.out.println(p.getId());
        System.out.println(p.getName()[1]);
        String[] evilVillain = p.getName();
        evilVillain[1] = "Mario";
        System.out.println(p.getName()[1]); // Eww
        // Moral: never return a mutable instance variable.

        String[] jjj = {"DU", "DUUU"};
        Person md = new Person("Joy", jjj);
        System.out.println(md.getName()[1]);
        System.out.println(md.getId());

//        String[] myStrings = new String[]{"Paul", "Mike"};
//        String[] myStrings2 = new String[6];
//        int[][] dddd = new int[3][4];
//
//
//        List<Integer> dd = new ArrayList<Integer>();
//        String ddd = new String("doudou");
//


    }
}
