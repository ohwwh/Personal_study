package Person;

public class Employee extends Student{
    private String title;
    private String employerName;
    private char employeeGrade;
    private int salary;

    public Employee(String name, String title){
        super(name); //부모생성자를 따로 호출하지 않으면, 부모클래스의 "기본생성자"가 호출된다.
        //super(); -> 이렇게... 하지만 부모생성자를 인수를 받도록 따로 설정해 놨으니 에러가 뜰 것
        this.title = title;
    }
    public String getTitle(){
        return title;
    }

    public String getEmployerName(){
        return employerName;
    }

    public char getEmployeeGrade(){
        return employeeGrade;
    }

    public int getSalary(){
        return salary;
    }

    public void setTitle(String title){
        this.title = title;
    }

    public void setEmplyerName(String employerName){
        this.employerName = employerName;
    }

    public void setEmployeeGrade(char employeeGrade){
        this.employeeGrade = employeeGrade;
    }

    public void setSalary(int salary){
        this.salary = salary;
    }

    public String toString(){
        return super.toString() + "#" + title;
    }
}
