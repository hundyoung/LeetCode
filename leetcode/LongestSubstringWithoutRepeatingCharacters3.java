package leetcode;

import java.util.HashMap;

public class LongestSubstringWithoutRepeatingCharacters3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(lengthOfLongestSubstring("pwwkew"));
	}
	public static int lengthOfLongestSubstring(String s) {
    	int left =0;
    	int right = 0;
    	int max_length = 0;
    	HashMap<Character,Character> exsistMap = new HashMap<Character,Character>();
    	while(left <s.length()&&right<s.length()) {
    		if(!exsistMap.containsKey(s.charAt(right))) {
    			exsistMap.put(s.charAt(right), s.charAt(right));
    			right++;
    			if(right-left>max_length) {
    				max_length=right-left;
    			}
    		}else {
    			exsistMap.remove(s.charAt(left));
    			left++;
    		}
    	}
        return max_length;
    }
}
