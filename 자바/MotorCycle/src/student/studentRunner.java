package student;

public class studentRunner {
    public static void main(String[] args) {
        int[] marks = {70, 80, 90};
        Student student = new Student("NuNu", marks);
        int number = student.getNumberOfMarks();
        int sum = student.getTotalSumOfMarks();
        int maximumMark = student.getMaximumMark();

    }
}
