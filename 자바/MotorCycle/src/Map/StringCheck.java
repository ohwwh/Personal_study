package Map;
import java.util.Map;
import java.util.TreeMap;

public class StringCheck {

	private String string;

	public StringCheck(String string)
	{
		this.string = string;
	}

	public void letterCheck()
	{
		Map<Character, Integer> map= new TreeMap<Character, Integer>();
		char	c;
		Integer g;

		for (int i = 0; i < string.length(); i ++)
		{
			c = string.charAt(i);
			g = map.get(c);
			if (c != ' ')
			{
				if (g == null)
				map.put(c, 1);
			else
				map.put(c, g + 1);
			}
		}
		System.out.println(map);
	}

	public void wordCheck()
	{
		Map<String, Integer> map= new TreeMap<String, Integer>();
		String[] split = string.split(" ");
		Integer g;

		for (String words: split)
		{
			g = map.get(words);
			if (g == null)
				map.put(words, 1);
			else
				map.put(words, g + 1);
		}
		System.out.println(map);
	}
}
