/**
 * Test Exercise_2_2, using the test framework
 * 
 */
public class TestExercise_2_2 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
		double feet = 5.0;
        double inches = 11.0;
        double expectedMeters = 1.8034;
        double actualMeters = Exercise_2_2.convertToMeters(feet, inches);
        testFramework.assertEquals(expectedMeters, actualMeters, "5ft 11");
        
		double feet2 = 1000.0;
        double inches2 = 0.0;
        double expectedMeters2 = 304.8;
        double actualMeters2 = Exercise_2_2.convertToMeters(feet2, inches2);
        testFramework.assertEquals(expectedMeters2, actualMeters2, "1000ft 0");
        
        // Print the results back
        testFramework.printTestResults();
	}

}


