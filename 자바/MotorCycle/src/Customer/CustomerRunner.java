package Customer;

public class CustomerRunner {
    public static void main(String[] args){
        Address homeAddress = new Address("line1", "Seoul", "50035");
        Customer customer = new Customer("NuNu", homeAddress);
        //Customer customer = Customer("NuNu", homeAddress);
        Address workAddress = new Address("line2", "Seoul", "50030");

    }
}
