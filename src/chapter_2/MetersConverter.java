package chapter_2;

public class MetersConverter {

    // קבלת 2 ערכי רגלים ואינצ'ים, וחישוב והחזרה של הערך המתאים במטרים
    public static double convertToMeters(double feet, double inches) {
        // המרה של רגלים לאינצ'ים
        double totalInches = feet * 12 + inches;
        // המרה של אינצ'ים למטרים
        double meters = totalInches * 0.0254;
        return meters;
    }

    public static void main(String[] args) {
        double feet = 5.0;
        double inches = 11.0;
        double meters = convertToMeters(feet, inches);
        System.out.println(feet + " רגלים ו-" + inches + " אינצ'ים הומרו ל-" + meters + " מטרים.");
    }
}
