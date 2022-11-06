package Interface;

public class ChessGame implements GamingConsole{
    public void up(){
        System.out.println("Move piece up");
    }
    public void down(){
        System.out.println("Move piece down");
    }
    public void left(){
        System.out.println("Move piece left");
    }
    public void right(){
        System.out.println("Move piece right");
    }
}
