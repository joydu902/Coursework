import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ClassList implements Iterable<Student> {
    private List<Student> studentsEnrolled = new ArrayList<>();

    public void add(Student s) { this.studentsEnrolled.add(s); }

    public void drop(Student s) {
        this.studentsEnrolled.remove(s);
    }

    @Override
    public Iterator<Student> iterator() {
        return new ClassListIterator();
    }



    private class ClassListIterator implements Iterator<Student> {

        /** The index of the next item in the class list. */
        int nextIndex = 0;
        @Override
        public boolean hasNext() {
            return nextIndex != studentsEnrolled.size();
        }

        @Override
        public Student next() {
            Student result = studentsEnrolled.get(nextIndex);
            nextIndex++;
            return result;
        }
    }

    public static void main(String[] args) {
        ClassList class_5009 = new ClassList();
        Student jeff = new Student("wufenglu", new String[] {"F", "W"}, 123);
        Student joy = new Student("dumin2", new String[] {"M", "D"}, 456);
        class_5009.add(jeff);
        class_5009.add(joy);


//        while (class_5009.iterator().hasNext()){
//            Student s = class_5009.iterator().next();
//            System.out.println(s.getID());
//        }
        Iterator<Student> iter = class_5009.iterator();
        while (iter.hasNext()){
            Student s = iter.next();
            System.out.println(s.getID());
        }
    }

}
