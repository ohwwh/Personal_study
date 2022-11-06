package Person;

public class Person {
    private String name;
    private String email;
    private String phoneNumber;

    public Person(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }

    public String getEmail(){
        return email;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public String getPhoneNumber(){
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber){
        this.phoneNumber = phoneNumber;
    }
}
