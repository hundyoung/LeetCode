package test;

import java.util.Scanner;

public class SubString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		String s =scan.next();
		String t =scan.next();
		isSubstringExist(s,t);
	}

	private static void isSubstringExist(String s, String t) {
		char[] char_s = s.toCharArray();
		char[] char_t = t.toCharArray();
		int s_index = 0;
		int t_index = 0;
		boolean outterFlag = true;
		for (int i = 0; i < char_t.length; i++) {
			boolean flag = false;
			for (int j = s_index; j < char_s.length; j++) {
				if (char_t[i] == char_s[j]) {
					s_index = j + 1;
					flag = true;
					break;
				}
			}
			if (!flag) {
				System.out.println("No");
				outterFlag = false;
				break;
			}
		}
		if(outterFlag) {
			System.out.println("Yes");
		}
	}
}
