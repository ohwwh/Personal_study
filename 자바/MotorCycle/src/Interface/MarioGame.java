package Interface;

public class MarioGame implements GamingConsole{
    public void up(){
        System.out.println("jump");
    }
    public void down(){
        System.out.println("sit");
    }
    public void left(){
        System.out.println("forward");
    }
    public void right(){
        System.out.println("backward");
    }
}
