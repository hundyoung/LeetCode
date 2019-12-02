package leetcode;

import java.util.ArrayList;

public class ZigZagConversion6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(convert("AB",1));

	}
    public static String convert(String s, int numRows) {
    	ArrayList<ArrayList<Character>> resultArray = new ArrayList<ArrayList<Character>>();
    	for(int i=0;i<numRows;i++) {
    		resultArray.add(new ArrayList<Character>());
    	}
    	int i =0;
    	boolean direction = true;
    	int level = 0;

    	String result = "";
    	if(numRows>1) {
    		while(i<s.length()) {
        		resultArray.get(level).add(s.charAt(i++));
        		if(direction) {
        			if(level<numRows-1) {
            			level++;
        			}else {
        				direction = false;
            			level--;
        			}
        		}else {
        			if(level>0) {
            			level--;
        			}else {
        				direction = true;
            			level++;
        			}
        		}
        	}
    	}else {
    		result = s;
    	}
    	for(i=0;i<numRows;i++) {
    		ArrayList<Character> charArray = resultArray.get(i);
    		for(Character c : charArray) {
    			result = result+String.valueOf(c);
    		}
    	}
		return result;
    }
}
