package Generic;
import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;

public class GenericRunner {

	static <X> X doubleValue(X value){
		return value;
	}

	static <X extends Number> X mustbeInteger(X value){
		return value;
		// 제네릭에 넣고 싶은 값을 오직 int, long 으로 제한하고 싶을 때 사용
	}

	static <X extends List> void duplicate(X list){
		list.addAll(list);
	}
	public static void main(String[] args) {
		MyCustomList<String> list1 = new MyCustomList<>(); 
		//MyCustomList<String> list1 = new MyCustomList<String>(); 
		//<>안에 뭐가 들어가고 안들어가고의 차이는 뭐임??
		//Java SE7부터는 저 자리에 생략이 가능. 즉 생략된거
		MyCustomList<Integer> list2 = new MyCustomList<>();
		list1.addElement("ss");
		list2.addElement(1);
		System.out.println(list1.get(0));
		System.out.println(list2.get(0));
		list1.removeElement("ss");
		list2.removeElement(1);
		//System.out.println(list1.get(0));
		//System.out.println(list2.get(0));
		ArrayList<Integer> numbers = new ArrayList<>(List.of(1, 2, 3));
		duplicate(numbers);
		System.out.println(numbers);
	}
}
