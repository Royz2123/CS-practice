import java.util.Scanner;

/**
 * Exercise 2.2 - Convert feet to meters
 *
 */
public class Exercise_2_2_io_sol {

    /**
     * Accept the given length - represented in feet & inches - from the console and print as meters
     *
     **/
	public static void convertToMeters() {
		// Get parameters
	    Scanner scanner = new Scanner(System.in);
	    System.out.print("Enter feet: ");
	    double feet = scanner.nextDouble();
	    System.out.print("Enter inches: ");
	    double inches = scanner.nextDouble();
	    scanner.close();

        // Convert the feet into inches as well
        double totalInches = feet * 12 + inches;
        
        // Convert the total inches into meters
        double meters = totalInches * 0.0254;

        // Print length
        System.out.printf("%f feet %f inches is equal to %f meters", feet, inches, meters);
	}
	
	public static void main(String[] args) {
        convertToMeters();
    }
}