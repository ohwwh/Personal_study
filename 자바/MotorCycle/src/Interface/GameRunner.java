package Interface;

public class GameRunner {
    public static void main(String[] args){
        //GamingConsole game = new MarioGame();
        GamingConsole game = new ChessGame();
        game.up();
        game.down();
        game.left();
        game.right();
    }
}
