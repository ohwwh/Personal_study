package stringarray;

public class StringRunner {
    public static void main(String[] args)
    {
        String[] d = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        daysOftheWeek n = new daysOftheWeek(d);
        n.dayWithMostCharacters();
        n.printReverse();
    }
    
}
