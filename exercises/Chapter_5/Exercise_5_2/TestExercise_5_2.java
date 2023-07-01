import java.util.Arrays;

/**
 * Test Exercise_5_2, using the test framework
 * 
 */
public class TestExercise_5_2 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
		int arr1[] = {10, 10};
		int resultArr1[] = {10};
        testFramework.assertEquals(
            resultArr1,
            Exercise_5_2.removeConsecutiveDuplicates(arr1),
            "Remove duplicates from [10, 10]"
        );

		int arr2[] = {34, 10, 34};
		int resultArr2[] = {34, 10, 34};
        testFramework.assertEquals(
            resultArr2,
            Exercise_5_2.removeConsecutiveDuplicates(arr2),
            "Remove duplicates from [34, 10, 34]"
        );

        int arr3[] = {5, 5, 1, 3, 5, 3, 3, 3};
		int resultArr3[] = {5, 1, 3, 5, 3};
        testFramework.assertEquals(
            resultArr3,
            Exercise_5_2.removeConsecutiveDuplicates(arr3),
            "Remove duplicates from [5, 5, 1, 3, 5, 3, 3, 3]"
        );

        int arr4[] = {-30};
		int resultArr4[] = {-30};
        testFramework.assertEquals(
            resultArr4,
            Exercise_5_2.removeConsecutiveDuplicates(arr4),
            "Remove duplicates from [-30]"
        );

        int arr5[] = {};
		int resultArr5[] = {};
        testFramework.assertEquals(
            resultArr5,
            Exercise_5_2.removeConsecutiveDuplicates(arr5),
            "Remove duplicates from []"
        );

        // Print the results back
        testFramework.printTestResults();
	}
}