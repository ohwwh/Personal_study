package FunctionalProgramming;
import java.util.List;
import java.util.stream.IntStream;

public class operatorExercise {
	public static void main(String[] args) {
		IntStream.range(1, 11).map(e -> e*e).forEach(e -> System.out.println(e));
		List<String> strings = List.of("Apple", "Banana", "Cat", "Dog");
		strings.stream().map(e -> e.toLowerCase()).forEach(e -> System.out.println(e));
		strings.stream().map(e -> e.length()).forEach(e -> System.out.println(e));
		System.out.println(IntStream.range(1, 11).sum());
		System.out.println(IntStream.range(1, 11).max().getAsInt());
	}
}
