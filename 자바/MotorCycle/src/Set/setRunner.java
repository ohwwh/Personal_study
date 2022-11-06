package Set;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
import java.util.LinkedHashSet;

public class setRunner {
	public static void main(String[] args) {
		List<Character> characters = List.of('A', 'Z', 'A', 'B', 'Z', 'F');
		Set<Character> treeSet = new TreeSet<>(characters);
		//TreeSet<Character> treeSet = new TreeSet<>(characters);
		System.out.println("treeSet" + treeSet);
		Set<Character> linkedSet = new LinkedHashSet<>(characters);
		System.out.println("linkedSet" + linkedSet);
	}
}
