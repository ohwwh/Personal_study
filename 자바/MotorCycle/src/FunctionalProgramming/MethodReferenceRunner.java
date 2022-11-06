package FunctionalProgramming;
import java.util.List;


public class MethodReferenceRunner {
	public static void print(Integer number){
		System.out.println(number);
	}
	public static void main(String[] args) {
		List.of("Ant", "Bat", "Cat", "Dog", "Elephant")
		.stream().map(s->s.length())
		.forEach(s->MethodReferenceRunner.print(s));

		List.of("Ant", "Bat", "Cat", "Dog", "Elephant")
		.stream().map(s->s.length())
		.forEach(MethodReferenceRunner::print);

		List.of("Ant", "Bat", "Cat", "Dog", "Elephant")
		.stream().map(String::length) // 정적 메소드 뿐 아니라 인스턴스 메소드에 대해서도 사용가능
		.forEach(System.out::println);
	}
}
