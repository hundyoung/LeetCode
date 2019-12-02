package leetcode;

import java.util.HashMap;
import java.util.Map;

public class Cards914 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(hasGroupsSizeX(new int[] {1,1}));
	}

	public static boolean hasGroupsSizeX(int[] deck) {
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		int minLength = Integer.MAX_VALUE;
		for (int i = 0; i < deck.length; i++) {
			int v = 1;
			if (map.containsKey(deck[i])) {
				v = map.get(deck[i]) + 1;
			}
			map.put(deck[i], v);
		}
		for (Integer key : map.keySet()) {
			if (minLength > map.get(key)) {
				minLength = map.get(key);
			}
		}
		for (int i = minLength; i > 1; i--) {
			boolean flag = true;
			for (Integer key : map.keySet()) {
				if (map.get(key) % i != 0) {
					flag = false;
					break;
				}
			}
			if (flag) {
				return true;
			}
		}
		return false;

	}
}
