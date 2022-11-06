package Fan;

import javax.print.event.PrintEvent;

public class FanRunner {
    public static void main(String[] args)
    {
        System.out.println()
        Fan fan = new Fan("Samsung", 0.34567, "Green");
        System.out.println(fan.toString());
    }
}
