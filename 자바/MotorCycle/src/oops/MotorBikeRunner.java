package oops;

public class MotorBikeRunner {
    public static void main(String[] args){
        MotorBike Ducati = new MotorBike();
        MotorBike Honda = new MotorBike();

        Ducati.start();
        Honda.start();

        Ducati.setSpeed(100);
        Honda.setSpeed(80);

        System.out.println(Ducati.getSpeed());
        System.out.println(Honda.getSpeed());

        Ducati.setSpeed(20);
        Honda.setSpeed(0);
        System.out.println(Ducati.getSpeed());
        System.out.println(Honda.getSpeed());
    }
}
