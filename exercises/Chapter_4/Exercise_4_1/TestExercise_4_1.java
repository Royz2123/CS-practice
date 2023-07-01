/**
 * Test Exercise_4_1, using the test framework
 * 
 */
public class TestExercise_4_1 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
        testFramework.assertEquals(6, Exercise_4_1.factorial(3), "3!");
        testFramework.assertEquals(120, Exercise_4_1.factorial(5), "5!");
        testFramework.assertEquals(3628800, Exercise_4_1.factorial(10), "10!");
        testFramework.assertEquals(1, Exercise_4_1.factorial(0), "0!");
        testFramework.assertEquals(-1, Exercise_4_1.factorial(-1), "(-1)! (undefined)");

        // Print the results back
        testFramework.printTestResults();
	}
}