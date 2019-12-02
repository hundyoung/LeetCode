package leetcode;

public class ReverseInteger7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(reverse(1534236469));
	}
    public static int reverse(int x) {
    	String original = ""+x;
    	String result ="";
    	if(original.charAt(0)=='-') {
    		result = result+'-';
    	}
    	for(int i=original.length()-1;i>=0;i--) {
    		if(original.charAt(i)!='-') {

        		result= result +original.charAt(i);
    		}
    	}
    	int r;
    	try {
    		r = Integer.parseInt(result);
    	}catch(Exception e){
    		r = 0;
    	}
        return r;
    }
}
