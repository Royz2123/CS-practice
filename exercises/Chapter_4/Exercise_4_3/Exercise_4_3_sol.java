/**
 * Exercise_4_3_sol - Find if pattern exists in DNA.
 */
public class Exercise_4_3_sol {

    /**
     * Finds if pattern exists in DNA exactly.
     *
     * @param genome the DNA genome which we are seacrhing on.
     * @param pattern the DNA pattern which we are seacrhing for.
     * @return does the pattern exist in the genome.
     */
    public static boolean doesPatternExist(String genome, String pattern) {
        int genomeLength = genome.length();
        int patternLength = pattern.length();

        for (int i = 0; i <= genomeLength - patternLength; i++) {
            boolean match = true;
            for (int j = 0; j < patternLength; j++) {
                if (genome.charAt(i + j) != pattern.charAt(j)) {
                    match = false;
                    break;
                }
            }
            if (match) {
                return true;
            }
        }
        return false;
    }

    /**
     * Finds if pattern exists in DNA with at most X mismatches.
     *
     * @param genome the DNA genome which we are seacrhing on.
     * @param pattern the DNA pattern which we are seacrhing for.
     * @param allowedMismatches the number of allowed substituion mismatches.
     * @return does the pattern almost exist in the genome.
     */
    public static boolean doesPatternAlmostExist(String genome, String pattern, int allowedMismatches) {
        int genomeLength = genome.length();
        int patternLength = pattern.length();
        int mismatches = 0;

        for (int i = 0; i <= genomeLength - patternLength; i++) {
            mismatches = 0;
            for (int j = 0; j < patternLength; j++) {
                if (genome.charAt(i + j) != pattern.charAt(j)) {
                    mismatches++;
                    if (mismatches > allowedMismatches) {
                        break;
                    }
                }
            }
            if (mismatches <= allowedMismatches) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        // Run your solution here
    }

}