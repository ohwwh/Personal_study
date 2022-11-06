package GenericWithWildCard;
import java.util.List;
import java.util.ArrayList;

public class Runner {
	
	static double sumOfNumberList(List<? extends Number> numbers){
		/*numbers.add(1);
		numbers.add(1.0);
		numbers.add(1.0f);
		numbers.add(1l);*/
		double sum = 0.0;
		for (Number number:numbers){
			sum += number.doubleValue();
		}
		/*Number n = 1;
		numbers.add(n);*/
		return sum;
	}

	static void addCoupleOfValues(List<? super Number> numbers){
		numbers.add(1);
		numbers.add(1.0);
		numbers.add(1.0f);
		numbers.add(1l);
		/*for (Number number:numbers){
			sum += number.doubleValue();
		}
		*/
	}
	public static void main(String[] args) {
		List emptyList = new ArrayList<Number>();
		addCoupleOfValues(emptyList);
		System.out.println(emptyList);
	}
}
