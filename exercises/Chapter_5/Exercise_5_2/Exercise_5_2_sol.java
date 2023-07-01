/**
 * Exercise_5_2_sol - Remove consecutive duplicate values from an array of integers.
 *
 */
public class Exercise_5_2_sol {

    /**
     * Remove consecutive duplicate values from an array of integers.
     *
     * @param arr the array of given integers.
     * @return a new array, with consecutive duplicate values removed.
     */
    public static int[] removeConsecutiveDuplicates(int arr[]) {
        // First get answer in over-sized array
        int[] resultArray = new int[arr.length];
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (i == 0 || arr[i] != arr[i - 1]) {
                resultArray[count] = arr[i];
                count++;
            }
        }

        // Move to properly sized array and return
        int[] finalArray = new int[count];
        for (int i = 0; i < finalArray.length; i++) {
            finalArray[i] = resultArray[i];
        }
        return finalArray;
    }

    public static void main(String[] args) {
		// Run your solution here
    }
}
