package chapter_2;

public class Table {
    private String color;
    private int numDiners;

    // קונסטרוקטור הקובע את צבע השולחן ואת מספר האוכלים
    public Table(String color, int numDiners) {
        this.color = color;
        this.numDiners = numDiners;
    }

    // הגדרות לפעולות getter וsetter עבור כל מאפיין
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getNumDiners() {
        return numDiners;
    }

    public void setNumDiners(int numDiners) {
        this.numDiners = numDiners;
    }

    // הפונקציה מחזירה מחיר השולחן כמוצע של מספר האוכלים כפול 400
    public int tablePrice() {
        return numDiners * 400;
    }

    // פונקציית toString המחזירה מידע רלוונטי על השולחן
    @Override
    public String toString() {
        return "Table with color " + color + " and " + numDiners + " diners, price: " + tablePrice() + " ILS.";
    }

    /**
     * מחשב את מספר השולחנות שיוכלו לכלול את כל האורחים
     *
     * @param n מספר האורחים הכולל
     * @return מספר השולחנות המלאים
     */
    public int numOfFullTables(int n) {
        return n / numDiners;
    }

    /**
     * מחשב את מספר האורחים שלא יוכלו לכנס לשולחן
     *
     * @param n מספר האורחים הכולל
     * @return מספר האורחים שלא יוכלו לכנס לשולחן
     */
    public int leftOver(int n) {
        return n % numDiners;
    }
    public static void main(String[] args) {
        Table table1 = new Table("red", 4);
        System.out.println(table1);

        table1.setColor("blue");
        table1.setNumDiners(6);
        System.out.println(table1);
    }
}

