package charex;

public class MyChar{
    private char c;
    public MyChar(char c){
        this.c = c;
    }
    public boolean isVowel(){
        if (c == 'a' | c == 'e' | c == 'i' |  c== 'o' | c == 'u')
            return (true);
        else if (c == 'A' | c == 'E' | c == 'I' |  c== 'O' | c == 'U')
            return (true);
        else
            return (false);
    }
    public boolean isNumber(){
        if ('0' <= c && c <= '9')
            return (true);
        else
            return (false);
    }
    public boolean isAlphabet(){
        if ('a' <= c && c <= 'z')
            return (true);
        else if ('A' <= c && c <= 'Z')
            return (true);
        else
            return (false);
    }

    public boolean isConsonant(){
        if (isAlphabet() && !isVowel()){
            return (true);
        }
        else
            return (false);
    }
    public void printLowerCaseAlphabets(){
        if (!isAlphabet()){
            System.out.println("this is not an Alphabet");
        }
        else
            System.out.printf("%d", Character.toLowerCase(c));
    }

    public void printUpperCaseAlphabets(){
        if (!isAlphabet()){
            System.out.println("this is not an Alphabet");
        }
        else
            System.out.printf("%d", Character.toUpperCase(c));
    }
}
