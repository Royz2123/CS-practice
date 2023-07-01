/**
 * Exercise_5_1 - Count the number of sequences of identical integers in an array
 *
 */
public class Exercise_5_1_sol {

    /**
     * Returns the number of sequences of identical integers in an array.
     *
     * @param arr the array of given integers.
     * @return the number of sequences of identical integers in the array.
     */
    public static int countIdenticalSequences(int arr[]) {
        // Handle edge cases
        if (arr.length == 0) {
            return 0;
        } else if (arr.length == 1) {
            return 1;
        }

        // Otherwise, count changes in the array
        int count = 1;
        for(int i = 1; i < arr.length; i++) {
            if(arr[i] != arr[i - 1]) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
		// Run your solution here
    }
}


