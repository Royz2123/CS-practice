/**
 * Exercise 2.2 - Convert feet to meters
 *
 */
public class Exercise_2_2_sol {

    /**
     * Convert the given length - represented in feet & inches - into meters
     *
     * @param feet the number of feet
     * @param feet the number of inches
     * @return the length in meters
     **/
	public static double convertToMeters(double feet, double inches) {
        // Convert the feet into inches as well
        double totalInches = feet * 12 + inches;
        
        // Convert the total inches into meters
        double meters = totalInches * 0.0254;
        return meters;
    }
	
	public static void main(String[] args) {
        double feet = 5.0;
        double inches = 11.0;
        double meters = convertToMeters(feet, inches);
        System.out.println(feet + " feet and " + inches + " inches are " + meters + " meters.");	
    }
}