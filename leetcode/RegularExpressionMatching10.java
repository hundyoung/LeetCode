package leetcode;

public class RegularExpressionMatching10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(isMatch("", ".*"));

	}

	public static boolean isMatch(String s, String p) {
		boolean[][] matrix = new boolean[p.length()][s.length()];
		if(s.length()==0) {
			if(p.length()>0) {
				int star_count =0;
				for(int i=0;i<p.length();i++) {
					if(p.charAt(i)=='*') {
						star_count++;
					}
				}
				if(star_count*2==p.length()) {
					return true;
				}else {
					return false;
				}
			}else {
				return true;
			}
		}
		if(p.length()==0) {
			return false;
		}
		if (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.') {
			matrix[0][0] = true;
		}else {
			matrix[0][0] = false;
		}
		for (int j = 1; j < s.length(); j++) {
			matrix[0][j] = false;
		}
		int star_count =0;
		for(int i = 1; i < p.length(); i++) {
			if(p.charAt(i)=='*') {
				star_count++;
				matrix[i][0] = matrix[i-1][0]||(i-2>=0&&matrix[i-2][0]);
			}else {
				if(p.charAt(i) == s.charAt(0) || p.charAt(i) == '.') {
					if(i-star_count*2==0) {
						matrix[i][0] = true;
					}else {
						matrix[i][0] = false;
					}
				}else {
					matrix[i][0] = false;
				}
			}
			
			
		}
		for (int i = 1; i < p.length(); i++) {
			for (int j = 1; j < s.length(); j++) {
				if (p.charAt(i) == s.charAt(j) || p.charAt(i) == '.') {
					
					matrix[i][j] = matrix[i-1][j-1];
				}else if(p.charAt(i) == '*') {
					if(p.charAt(i-1) == s.charAt(j) || p.charAt(i-1) == '.') {
						matrix[i][j] = matrix[i-1][j]||matrix[i][j-1]||matrix[i-1][j-1];
						if(i-2>=0) {
							matrix[i][j] = matrix[i][j]||matrix[i-2][j-1]||matrix[i-2][j];
						}
					}else {
						if(i-2>=0) {
							matrix[i][j] = matrix[i-2][j];
						}else {
							matrix[i][j] = false;
						}
					}
				}else {
					matrix[i][j] = false;
				}
			}
		}
		return matrix[p.length()-1][s.length()-1];
	}

}
