package FunctionalProgramming;
import java.util.List;

public class FPNumberRunner {
	public static void main(String[] args) {
		List<Integer> numbers = List.of(4,6,8,13,3,15);
		int Sum = numbers.stream().reduce(0, (number1, number2) -> number1 + number2);
		int oddSum = oddSumFP(numbers);
		oddSum = oddSumNormal(numbers);
		int evenSum = numbers.stream().filter(element -> element%2 == 0).reduce(0, (number1, number2) -> number1 + number2);
		System.out.println(Sum);
		System.out.println(oddSum);
		System.out.println(evenSum);
		System.out.println(numbers);

	}

	private static int oddSumFP(List<Integer> numbers) {
		return numbers.stream().filter(element -> element%2 == 1).
		reduce(0, (number1, number2) -> number1 + number2);
	}

	private static int oddSumNormal(List<Integer> numbers) {
		int sum = 0;
		for (Integer number:numbers){
			if (number % 2 == 1)
				sum += number;
		}
		return sum;
	}
}
