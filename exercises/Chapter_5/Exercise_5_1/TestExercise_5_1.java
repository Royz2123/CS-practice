import java.util.Arrays;

/**
 * Test Exercise_5_1, using the test framework
 * 
 */
public class TestExercise_5_1 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
		int arr1[] = {7};
        testFramework.assertEquals(1, Exercise_5_1.countIdenticalSequences(arr1), "Sequences in [7]");

		int arr2[] = {6, 6};
        testFramework.assertEquals(1, Exercise_5_1.countIdenticalSequences(arr2), "Sequences in [6, 6]");

		int arr3[] = {9, 8, 9};
        testFramework.assertEquals(3, Exercise_5_1.countIdenticalSequences(arr3), "Sequences in [9, 8, 9]");

		int arr4[] = {5, 5, 1, 3, 5, 3, 3, 3};
        testFramework.assertEquals(5, Exercise_5_1.countIdenticalSequences(arr4), "Sequences in [5, 5, 1, 3, 5, 3, 3, 3]");

		int arr5[] = {};
        testFramework.assertEquals(0, Exercise_5_1.countIdenticalSequences(arr5), "Sequences in []");

        // Print the results back
        testFramework.printTestResults();
	}
}