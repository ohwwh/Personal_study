package FunctionalProgramming;
import java.util.List;

public class FunctionalProgrammingRunner {
	public static void main(String[] args) {
		List<String> list = List.of("Apple", "Bat", "Cat", "Dog");

		printBasic(list);
		printFP(list);
		printBasicWithFilter(list);
		printFPWithFilter(list);
	}

	private static void printBasic(List<String> list){
		for (String string:list){
			System.out.println(string);
		}
	}

	private static void printFP(List<String> list){
		list.forEach(element -> System.out.println(element));
	}

	private static void printBasicWithFilter(List<String> list){
		for (String string:list){
			if (string.endsWith("at"))
				System.out.println(string);
		}
	}

	private static void printFPWithFilter(List<String> list){
		list.stream().filter(element -> element.endsWith("at")).forEach(element -> System.out.println(element));
	}
}
