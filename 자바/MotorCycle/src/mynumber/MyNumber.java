package mynumber;

public class MyNumber {

    private int number;

    public MyNumber(int number){
        this.number = number;
    }

    public boolean isPrime(){
        for (int i = 2; i < this.number; i ++)
        {
            if (this.number % i == 0)
                return (false);
        }
        return (false);
    }

    public int sumUptoN()
    {
        int ret;

        ret = 0;
        for (int i=1;i<=this.number;i ++)
            ret += i;
        return (ret);
    }

    public int SumOfDivisors()
    {
        int ret;

        ret = 0;
        for (int i = 2;i<this.number;i ++)
        {
            if (this.number % i == 0)
                ret += i;
        }
        return (ret);
    }
}
