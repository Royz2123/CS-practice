/**
 * Test Exercise_5_4, using the test framework
 *
 */
public class TestExercise_5_4 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
		int arr1a[] = {1, 3, 5, 7};
		int arr1b[] = {2, 4, 6, 8};
		int resultArr1[] = {1, 2, 3, 4, 5, 6, 7, 8};
        testFramework.assertEquals(
            resultArr1,
            Exercise_5_4.mergeSortedArrays(arr1a, arr1b),
            "Merging [1, 3, 5, 7] and [2, 4, 6, 8]"
        );

		int arr2a[] = {1, 2, 3};
		int arr2b[] = {1, 2, 3};
		int resultArr2[] = {1, 1, 2, 2, 3, 3};
        testFramework.assertEquals(
            resultArr2,
            Exercise_5_4.mergeSortedArrays(arr2a, arr2b),
            "Merging [1, 2, 3] and [1, 2, 3]"
        );

        int arr3a[] = {1, 2, 3};
		int arr3b[] = {4, 5, 6};
		int resultArr3[] = {1, 2, 3, 4, 5, 6};
        testFramework.assertEquals(
            resultArr3,
            Exercise_5_4.mergeSortedArrays(arr3a, arr3b),
            "Merging [1, 2, 3] and [4, 5, 6]"
        );

        int arr4a[] = {1, 2, 3};
		int arr4b[] = {};
		int resultArr4[] = {1, 2, 3};
        testFramework.assertEquals(
            resultArr4,
            Exercise_5_4.mergeSortedArrays(arr4a, arr4b),
            "Merging [1, 2, 3] and []"
        );

        // Print the results back
        testFramework.printTestResults();
	}
}