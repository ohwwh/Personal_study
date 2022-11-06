package Map;

public class MapRunner {
	public static void main(String[] args) {
		String string = "This is a great thing";

		StringCheck check = new StringCheck(string);
		check.letterCheck();
		check.wordCheck();
	}
}
