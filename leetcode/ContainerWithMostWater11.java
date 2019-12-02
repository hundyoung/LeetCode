package leetcode;

public class ContainerWithMostWater11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	public int maxArea(int[] height) {
		int max = 0;
		int l = 0, r = height.length - 1;
		while (l < r) {
			int min;
			if (height[l] < height[r]) {
				min = height[l];
			} else {
				min = height[r];
			}
			int area = min * (r - l);
			if (area > max) {
				max = area;
			}
			if(height[l]<height[r]) {
				l++;
			}else {
				r--;
			}
		}
		return max;
	}
}
