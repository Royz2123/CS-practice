/**
 * Exercise_5_1 - Remove consecutive integers from an array
 *
 */
public class Exercise_5_1_sol {


    /**
     * Prints a horizontal line of tavs of length len.
     *
     * @param arr the a
     */
    public static int countChanges(int arr[]) {
        // Fill in your solution here
        int count = 0;
        if (arr.length <= 1) {
            return 0;
        }
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


