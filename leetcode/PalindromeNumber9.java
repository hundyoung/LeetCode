package leetcode;

public class PalindromeNumber9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
    public boolean isPalindrome(int x) {
        String str = ""+x;
        int len = str.length();
        int med;
        if(len%2==0) {
        	med = len/2-1;
        }else {
        	med =(len-1)/2;
        }
        boolean result = true;
        for(int i =0;i<=med;i++) {
        	if(str.charAt(i)!=str.charAt(len-1-i)) {
        		result = false;
        		break;
        	}
        }
        return result;
    }
}
