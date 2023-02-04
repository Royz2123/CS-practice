package chapter_2;

import org.junit.Assert;
import org.junit.Test;

public class TestTable {
    @Test
    public void testTableConstructor() {
        Table table = new Table("blue", 4);
        Assert.assertEquals("blue", table.getColor());
        Assert.assertEquals(4, table.getNumDiners());
    }

    @Test
    public void testTableSetters() {
        Table table = new Table("blue", 4);
        table.setColor("red");
        table.setNumDiners(6);
        Assert.assertEquals("red", table.getColor());
        Assert.assertEquals(6, table.getNumDiners());
    }

    @Test
    public void testTablePrice() {
        Table table = new Table("blue", 4);
        Assert.assertEquals(1600, table.tablePrice());
    }

    @Test
    public void testNumOfFullTables() {
        Table table = new Table("blue", 4);
        Assert.assertEquals(2, table.numOfFullTables(8));
        Assert.assertEquals(1, table.numOfFullTables(5));
    }

    @Test
    public void testLeftOver() {
        Table table = new Table("blue", 4);
        Assert.assertEquals(0, table.leftOver(8));
        Assert.assertEquals(1, table.leftOver(5));
    }

    @Test
    public void testToString() {
        Table table = new Table("blue", 4);
        String toStringResult = table.toString();
        Assert.assertTrue(toStringResult.contains("blue"));
        Assert.assertTrue(toStringResult.contains("4"));
    }
}

