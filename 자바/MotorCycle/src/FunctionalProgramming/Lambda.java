package FunctionalProgramming;
import java.util.List;

public class Lambda {

	private static int oddSumFP(List<Integer> numbers) {
		return numbers.stream().filter(element -> element%2 == 1).
		reduce(0, (number1, number2) -> number1 + number2);
	}

	private static int oddSumFPwithPrint(List<Integer> numbers) {
		return numbers.stream().filter(element -> element%2 == 1).
		reduce(0, (number1, number2) -> {
			System.out.println(number1 + " " + number2);
			return number1 + number2;
			}
		);
	}
}
