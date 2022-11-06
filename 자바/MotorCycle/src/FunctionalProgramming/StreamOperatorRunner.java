package FunctionalProgramming;
import java.util.List;

public class StreamOperatorRunner {
	
	public static void sortNumbers(List<Integer> numbers){
		numbers.stream().sorted().forEach(e -> System.out.println(e));
	}

	public static void distinctNumbers(List<Integer> numbers){
		numbers.stream().distinct().forEach(e -> System.out.println(e));
	}

	public static void mapfloatNumbers(List<Integer> numbers){
		numbers.stream().map(e -> (float)e).forEach(e -> System.out.println(e));
	}
	public static void main(String[] args) {
		List<Integer> numbers = List.of(3, 5, 7, 3, 4, 10, 7);
		//sortNumbers(numbers);
		//distinctNumbers(numbers);
		//numbers.stream().sorted().distinct().forEach(e -> System.out.println(e));
		mapfloatNumbers(numbers);
	}
}
