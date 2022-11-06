package oops;

public class MotorBike {
    private int speed;

    void start(){
        System.out.println("Start");
    }

    void setSpeed(int speed){
        if (speed > 0)
            this.speed = speed;
    }

    int getSpeed(){
        return this.speed;
    }

    void increaseSpeed(int howMuch){
        setSpeed(this.speed + howMuch);
    }

    void decreaseSpeed(int howMuch){
        setSpeed(this.speed - howMuch);
    }
}
