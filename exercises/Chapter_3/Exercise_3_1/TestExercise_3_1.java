/**
 * Test Exercise_3_1, using the test framework
 * 
 */
public class TestExercise_3_1 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
	    boolean haveSameDigits1 = Exercise_3_1.haveSameDigits(13, 31);
        testFramework.assertEquals(true, haveSameDigits1, "13 and 31 have the same digits");
        
		// Run some tests
	    boolean haveSameDigits2 = Exercise_3_1.haveSameDigits(13, 32);
        testFramework.assertEquals(false, haveSameDigits2, "13 and 32 have different digits");

        // Print the results back
        testFramework.printTestResults();
	}
}