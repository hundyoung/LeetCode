package leetcode;

public class TwoSum167 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	public int[] twoSum(int[] numbers, int target) {
		int half = target/2;
		int i=0;
		int j=numbers.length-1;
		int middle=0;
		while(i<=j) {
			middle= (i+j)/2;
			if(numbers[middle]<target) {
				i=middle+1;
			}else if(numbers[middle]>target) {
				j=middle-1;
			}else {
				break;
			}
		}
		if(middle>=numbers.length){
			middle--;
		}
		if(numbers[middle]>target) {
			middle--;
		}
		for(i=0;i<half;i++) {
			
		}
		return numbers;
			
	}
}
