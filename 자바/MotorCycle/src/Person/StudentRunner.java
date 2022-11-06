package Person;

public class StudentRunner {
    public static void main(String[] args){
        Student student = new Student("NuNu");
        //student.setName("NuNu");
        student.setEmail("ohw1237@gmail.com");
        student.setCollegeName("Sogang");


        /*Person person = new Person();
        String value1 = person.toString();
        String value2 = student.toString();
        System.out.println(value1);
        System.out.println(value2);*/
        //System.out.println(student.name);

        Employee employee = new Employee("NuNu", "Coder");
        Student testemp = new Employee("Test", "Tester");
        //이런 식으로 클래스간의 형변환도 가능하다. 단 부모클래스만이 자식클래스를 담을 수 있으며, 오직
        //부모 클래스의 메소드만 사용할 수 있다.
        //다만 자식 클래스에서 부모클래스의 함수를 오버라이딩 했을 경우는 자식클래스에 있는 함수도 쓸수 있다.
        //employee.setName("NuNu");
        employee.setEmail("ohw1237@gmail.com");
        employee.setCollegeName("Sogang");
        testemp.setCollegeName("No");
        //testemp.getEmployerName();
        //이런식으로 만약 오버라이딩이 되어있지 않은 경우 사용할 수 없다.
        //employee.setTitle("Coder");
        String value = employee.toString();
        String testValue = testemp.toString();
        System.out.println(value);
        System.out.println(testValue);
    }
}
