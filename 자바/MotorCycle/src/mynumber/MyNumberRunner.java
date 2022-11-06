package mynumber;

public class MyNumberRunner {
    public static void main(String[] args)
    {
        MyNumber number = new MyNumber(9);
        boolean isPrime = number.isPrime();
        int     sum = number.sumUptoN();
        int     sumD = number.SumOfDivisors();
        System.out.println(isPrime);
        System.out.println(sum);
        System.out.println(sumD);
    }
}
