import java.util.HashMap;

public class StudentMarkHashMap {
    // TODO: declare your variables
    public String courseCode;
    public Integer courseNumber;
    public HashMap<String, Integer> info;

    /**
     * TODO: Implement a constructor that takes a course code and course number
     * and initializes the HashMap.
     *
     * @param courseCode the course code. e.g. CSC
     * @param courseNumber the course number. e.g. 207
     */
    public StudentMarkHashMap(String courseCode, Integer courseNumber){
        this.courseCode = courseCode;
        this.courseNumber = courseNumber;
        this.info = new HashMap <String, Integer>();
    }


    /**
     * TODO: Implement the toString according to the example output shown above.
     *
     *  @return formatted String representation of this class's instance
     */
    @Override
    public String toString() {
        String result = "HashMap for course CSC207:\n";
        for (String key : info.keySet()) {
            int value = info.get(key);
            String ss = key + " scored: " + Integer.toString(value) + "\n";
            result += ss;
        }
        return result;

    }

    /**
     * TODO: Define a addStudentWithMark method that tries to add a student mark information to the HashMap,
     * and returns a boolean value to nidicate whether it was successfully added.
     *
     * @param studentName the student name to be added
     * @param mark the mark that student scored
     * @return true if the student information was recorded successfully. If the student
     *          already exist in the HashMap, then return false.
     */
    public Boolean addStudentWithMark(String studentName, int mark){
        if (!info.containsKey(studentName)){
            info.put(studentName, mark);
            return true;
        }
        else{
            return false;
        }

    }


    /**
     * TODO: Define a hasStudent method that tells if the HashMap contains a specific student.
     * @param studentName the student name to check for
     * @return true if the student is in the HashMap otherwise false
     */
    public Boolean hasStudent(String studentName){
        if (info.containsKey(studentName)){
            return true;
        }
        else{
            return false;
        }
    }



    /**
     * TODO: Define a hasMark method that return whether the course has a student who scored a given mark.
     * @param mark the mark to check for
     * @return true if the mark exists otherwise false
     */
    public Boolean hasMark(int mark){
        if (info.containsValue(mark)){
            return true;
        }
        else{
            return false;
        }
    }
}