import java.io.Serializable;
import java.util.Arrays;

public class Person implements Serializable {

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Person other = (Person) obj;
        if (dob == null) {
            if (other.dob != null)
                return false;
        } else if (!dob.equals(other.dob))
            return false;
        if (!Arrays.equals(name, other.name))
            return false;
        return true;
    }

    	private String[] name;
	private String dob;

	/**
	 * Creates a new Person with name name, and date of birth dob
	 * 
	 * @param name the name of this Person.
	 * @param dob the date of birth of this Person, in DDMMYY format.
	 */
	public Person(String[] name, String dob) {
		super();
		this.name = name;
		this.dob = dob;
	}

	public Person(String[] name) {
		super();
		this.name = name;
	}

	public String[] getName() {
		return name;
	}

	public void setName(String[] name) {
		this.name = name;
	}

	public String getDob() {
		return dob;
	}

	public void setDob(String dob) {
		this.dob = dob;
	}


	@Override
	public String toString() {
		String result = new String("");
		for (String n : this.name) {
			result = result + n + " ";
		}
		result += this.dob;
		return result;
	}
}
