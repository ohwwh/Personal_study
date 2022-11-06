package Person;

public class Student extends Person{
    private String collegeName;
    private int year;

    public Student(String name){
        super(name);
    }
    public String getcollegeName(){
        return collegeName;
    }

    public void setCollegeName(String collegeName){
        this.collegeName = collegeName;
    }

    public int getYear(){
        return year;
    }

    public void setYear(int year){
        this.year = year;
    }

    public String toString(){
        return collegeName;
    }
}
