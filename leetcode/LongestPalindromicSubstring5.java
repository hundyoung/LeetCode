package leetcode;

public class LongestPalindromicSubstring5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(longestPalindrome("aaaa"));
	}

	public static String longestPalindrome(String s) {
		int[][] matrix = new int[s.length()][s.length()];		
		int max = 0;
		String result = "";
		for(int i =0;i<s.length();i++) {
			matrix[i][i] = 1;
			if(i<s.length()-1) {
				if(s.charAt(i)==s.charAt(i+1)) {
					matrix[i][i+1] = 2;
					max =1;
					result = s.substring(i, i+2);
				}else {
					matrix[i][i+1] = 0;
				}
			}
		}
		if(max==0&&s.length()>0) {
			result = s.substring(s.length()-1);
		}
		for(int len=2;len<=s.length();len++) {
			for(int k =0;k<s.length()-len;k++) {
				if(s.charAt(k)==s.charAt(k+len)&&matrix[k+1][k+len-1]>0) {
					matrix[k][k+len] = matrix[k+1][k+len-1]+2;
					if(matrix[k][k+len]>max) {
						max = matrix[k][k+len];
						result = s.substring(k, k+len+1);
					}
				}else {
					matrix[k][k+len] = 0;
				}
			}
		}
		return result;
	}
}
