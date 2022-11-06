package Rectangle;

public class Rectangle {
    private int length;
    private int width;

    public Rectangle(int length, int width){
        this.length = length;
        this.width = width;
    }

    public void setLength(int length){
        this.length = length;
    }

    public void setWidth(int width){
        this.width = width;
    }

    public int getWidth(){
        return (width);
    }

    public int getLength(){
        return (length);
    }
    
    public int getArea(){
        return (width * length);
    }

    public int getParameter(){
        return (2 * (width + length));
    }
}
