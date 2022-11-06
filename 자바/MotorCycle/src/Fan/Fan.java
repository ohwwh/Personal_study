package Fan;

public class Fan {
    private String make;
    private double radius;
    private String color;
    private boolean isOn;
    private int speed;

    public Fan(String make, double radius, String color){
        this.make = make;
        this.radius = radius;
        this.color = color;
    }

    public String toString(){
        return String.format("maker - %s, radius - %f, color - %s, isOn - %b, speed - %d",
        make, radius, color, isOn, speed);
    }

    public void setSpeed(int speed){
        this.speed = speed;
    }

    public void switchOn(){
        this.isOn = true;
        setSpeed(5);
    }
    
    public void switchOff(){
        this.isOn = false;
        setSpeed(0);
    }
}