package FunctionalProgramming;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Stream;

class EvenNumberPredicate implements Predicate<Integer>{
	public boolean test(Integer number){
		return number%2 == 0;
	}
}

public class FunctionalInterfaceRunner {
	public static void main(String[] args) {
		List.of(23,43,34,45).stream().filter(n -> n%2 == 0)
		.forEach(e -> System.out.println(e));

		List.of(23,43,34,45).stream().filter(new EvenNumberPredicate())
		.forEach(e -> System.out.println(e));

		//Stream<T> filter(Predicate<? super T> predicate);
	}
}
