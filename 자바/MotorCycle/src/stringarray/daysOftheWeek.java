package stringarray;

public class daysOftheWeek {

    private String[] days;

    public daysOftheWeek(String[] days){
        this.days = days;
    }

    public void dayWithMostCharacters(){
        String most = "";

        for (String day: days){
            if (day.length() > most.length())
                most = day;
        }
        System.out.println(most);
        
    }

    public void printReverse(){
        for (int i = days.length - 1; i >= 0; i --)
            System.out.println(days[i]);
    }
}
