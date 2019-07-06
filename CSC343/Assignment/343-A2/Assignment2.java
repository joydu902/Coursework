import java.sql.*;
import java.util.List;

// If you are looking for Java data structures, these are highly useful.
// Remember that an important part of your mark is for doing as much in SQL (not Java) as you can.
// Solutions that use only or mostly Java will not receive a high mark.
import java.util.ArrayList;
//import java.util.Map;
//import java.util.HashMap;
//import java.util.Set;
//import java.util.HashSet;
public class Assignment2 extends JDBCSubmission {

    public Assignment2() throws ClassNotFoundException {

        Class.forName("org.postgresql.Driver");
    }

    @Override
    public boolean connectDB(String url, String username, String password) {
        try{
            connection = DriverManager.getConnection(url, username, password);
            PreparedStatement ps = connection.prepareStatement("SET search_path TO markus;");
            ps.execute();
            return true;
        } catch (SQLException sqle){
            return false;
	}
    }

    @Override
    public boolean disconnectDB() {
         try{
            connection.close();
            return true;
        } catch (SQLException sqle){
            return false;
	}
    }

    @Override
    public ElectionCabinetResult electionSequence(String countryName) {
        ResultSet rs;
        String queryString;
        List<Integer> elections = new ArrayList<Integer>();
        List<Integer> cabinets = new ArrayList<Integer>();
	
    try {
		queryString = "select election, c.id as cabinet from cabinet c RIGHT JOIN" 
        + " (select election.id as election, e_date from election, country where country.name = ? and country.id = election.country_id)" 
        + " temp ON temp.election = c.election_id order by extract(year from e_date) DESC";
		PreparedStatement ps = connection.prepareStatement(queryString);
		ps.setString(1, countryName);
		rs = ps.executeQuery();

		while (rs.next()) {
			int election = rs.getInt("election");
            int cabinet = rs.getInt("cabinet");
			elections.add(election);
            cabinets.add(cabinet);
		}
	} catch (SQLException se) {
		System.err.println("SQL Exception." +
                        "<Message>: " + se.getMessage());
	   }
       return new ElectionCabinetResult(elections, cabinets);
    }

    @Override
    public List<Integer> findSimilarPoliticians(Integer politicianName, Float threshold) {
        ResultSet rs1;
        ResultSet rs2;
        String queryString1;
        String queryString2;
        List<Integer> result = new ArrayList<Integer>();
    
    try {
        queryString1 = "SELECT p.id, concat(p.comment, ' ', p.description) as cd FROM politician_president p WHERE p.id != ?";
        PreparedStatement ps1 = connection.prepareStatement(queryString1);
        ps1.setInt(1, politicianName);
        rs1 = ps1.executeQuery();

        queryString2 = "SELECT p.id, concat(p.comment, ' ', p.description) as cd FROM politician_president p WHERE p.id = ?";
        PreparedStatement ps2 = connection.prepareStatement(queryString2);
        ps2.setInt(1, politicianName);
        rs2 = ps2.executeQuery();

        String pres_cd = null;
        while (rs2.next()) {
            pres_cd = rs2.getString("cd");
        }

        while (rs1.next()) {
            String other_cd = rs1.getString("cd");
            if (similarity(other_cd, pres_cd) >= threshold) {
                int id = rs1.getInt("id");
                result.add(id);
            }
        }
    } catch (SQLException se) {
        System.err.println("SQL Exception." +
                        "<Message>: " + se.getMessage());
       }
    return result;
    }

    public static void main(String[] args) {
        // You can put testing code in here. It will not affect our autotester.
        System.out.println("Hello");
    }

}

