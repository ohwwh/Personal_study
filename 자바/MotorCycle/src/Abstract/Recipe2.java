package Abstract;

public class Recipe2 extends AbstractRecipe{
    public void getready(){
        System.out.println("재료를 썰어");
    }
    public void dothedish(){
        System.out.println("오븐에 구워");
    }
    public void cleanup(){
        System.out.println("오븐 꺼");
    }
}
