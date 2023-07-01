/**
 * Exercise_5_4_sol - Merge 2 sorted arrays of integers
 *
 */
public class Exercise_5_4_sol {

    /**
     * Merges two sorted arrays into a single sorted array.
     *
     * @param arr1 the first sorted array
     * @param arr2 the second sorted array
     * @return the merged sorted array
     */
    public static int[] mergeSortedArrays(int[] arr1, int[] arr2) {
        int[] mergedArray = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;

        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] <= arr2[j]) {
                mergedArray[k] = arr1[i];
                i++;
            } else {
                mergedArray[k] = arr2[j];
                j++;
            }
            k++;
        }

        while (i < arr1.length) {
            mergedArray[k] = arr1[i];
            i++;
            k++;
        }

        while (j < arr2.length) {
            mergedArray[k] = arr2[j];
            j++;
            k++;
        }

        return mergedArray;
    }


    public static void main(String[] args) {
		// Run your solution here
    }
}
