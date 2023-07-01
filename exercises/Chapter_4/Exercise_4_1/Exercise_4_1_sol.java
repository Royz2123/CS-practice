/**
 * Exercise_4_1_sol - Compute factorial
 */
public class Exercise_4_1_sol {

    /**
     * Calculates the factorial of a given integer.
     *
     * @param n the input integer
     * @return the factorial of n
     */
    public static int factorial(int n) {
        if (n < 0) {
            return -1;
        }

        if (n == 0 || n == 1) {
            return 1;
        }

        int result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }

        return result;
    }

    public static void main(String[] args) {
        // Run your solution here
    }

}