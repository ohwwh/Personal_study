package Abstract;

public class RecipeRunner {
    public static void main(String[] args){
        Recipe1 recipe1 = new Recipe1();
        Recipe2 recipe2 = new Recipe2();

        recipe1.execute();
        recipe2.execute();

    }
}
