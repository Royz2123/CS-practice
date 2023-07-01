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
		int changes = Exercise_5_1.countChanges(arr1);
        testFramework.assertEquals(0, changes, "Changes in [7]");

		int arr2[] = {6, 6};
        testFramework.assertEquals(0, Exercise_5_1.countChanges(arr2), "Changes in [6, 6]");

		int arr3[] = {9, 8, 9};
        testFramework.assertEquals(2, Exercise_5_1.countChanges(arr3), "Changes in [9, 8, 9]");

		int arr4[] = {5, 5, 1, 3, 5, 3, 3, 3};
        testFramework.assertEquals(4, Exercise_5_1.countChanges(arr4), "Changes in [5, 5, 1, 3, 5, 3, 3, 3]");

        // Print the results back
        testFramework.printTestResults();
	}
}