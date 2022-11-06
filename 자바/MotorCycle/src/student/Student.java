package student;

public class Student{
    private String name;
    private int[] marks;
    public Student(String name, int[] marks) {
        this.name = name;
        this.marks = marks;
    }
    
    public int getNumberOfMarks(){
        return this.marks.length;
    }

    public int getTotalSumOfMarks(){
        int sum = 0;
        for(int mark:marks){
            sum += mark;
        }
        return sum;
    }

    public int getMaximumMark(){
        int max = 0;
        for (int mark:marks){
            if (max < mark)
                max = mark;
        }
        return max;
    }
}
