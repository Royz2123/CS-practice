/**
 * Exercise_5_3 - Calculate the multiplication of all items that are smaller than 10.
 *
 */
public class Exercise_5_3_sol {

    /**
     * Calculates the multiplication of all items that are smaller than 10.
     *
     * @param arr the array of given integers.
     * @return the multiplication of all items that are smaller than 10.
     */
    public static int calcDigitMultiplication(int[] arr) {
        int result = 1;
        boolean foundValue = false;

        // Loop through the array
        for (int i = 0; i < arr.length; i++) {
            int value = arr[i];
            if (value < 10) {
                result *= value;
                foundValue = true;
            }
        }

        // Return the multiplication if found and 1 otherwise
        if (foundValue) {
            return result;
        } else {
            return -1;
        }
    }

    public static void main(String[] args) {
		// Run your solution here
    }
}
