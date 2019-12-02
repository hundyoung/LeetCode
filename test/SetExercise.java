package test;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class SetExercise {
	public static void main(String[] args) {
		Set<String> result = new HashSet<String>();
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()) {
			result.add(scan.next());
		}
		System.out.println(result.size());
	}
	
}
