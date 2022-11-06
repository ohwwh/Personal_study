package Abstract;

public abstract class AbstractRecipe {
    
    public void execute(){
        getready();
        dothedish();
        cleanup();
    }

    public abstract void dothedish();
    public abstract void cleanup();
    public abstract void getready();
    
}
