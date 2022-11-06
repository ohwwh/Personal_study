package Abstract;

public class Recipe1 extends AbstractRecipe{
    public void getready(){
        System.out.println("재료를 썰어");
    }
    public void dothedish(){
        System.out.println("후라이팬에 볶아");
    }
    public void cleanup(){
        System.out.println("후라이팬 닦아");
    }
}
