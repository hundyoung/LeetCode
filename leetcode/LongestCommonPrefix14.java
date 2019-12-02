package leetcode;

public class LongestCommonPrefix14 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	public String longestCommonPrefix(String[] strs) {
		String result = "";
		if(strs.length==0) {
			return "";
		}
		String first = strs[0];
		int index = 0;
		while (index < first.length()) {
			boolean flag = true;
			for (int i = 1; i < strs.length; i++) {
				if (index>=strs[i].length()||strs[i].charAt(index) != first.charAt(index)) {
					flag = false;
					break;
				}
			}
			if(flag) {
				result=result+first.charAt(index);
				index++;
			}else {
				break;
			}
		}

		return result;
	}
}
