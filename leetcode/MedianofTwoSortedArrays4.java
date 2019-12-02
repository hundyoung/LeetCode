package leetcode;

public class MedianofTwoSortedArrays4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(findMedianSortedArrays(new int[] {}, new int[] { 1 }));
	}

	public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
		int length_sum = nums1.length + nums2.length;
		boolean evenFlag;
		int med_index;
		if (length_sum % 2 == 0) {
			evenFlag = true;
			med_index = length_sum / 2 - 1;
		} else {
			evenFlag = false;
			med_index = (length_sum - 1) / 2;
		}
		int i1 = 0;
		int i2 = 0;
		double result = 0;
		int cur_num = 0;
		while (i1 < nums1.length && i2 < nums2.length) {
			if (i1 + i2 - 1 == med_index) {
				if (evenFlag) {
					int next_num;
					if (nums1[i1] <= nums2[i2]) {
						next_num = nums1[i1];
					} else {
						next_num = nums2[i2];
					}
					result = (double) (cur_num + next_num) / 2;
				} else {
					result = (double) cur_num;
				}
				return result;
			}
			if (nums1[i1] <= nums2[i2]) {
				cur_num = nums1[i1];
				i1++;
			} else {
				cur_num = nums2[i2];
				i2++;
			}
		}
		while (i1 < nums1.length) {
			if (i1 + i2 - 1 == med_index) {
				if (evenFlag) {
					result = (double) (cur_num + nums1[i1]) / 2;
				} else {
					result = (double) cur_num;
				}
				return result;
			} else {
				cur_num = nums1[i1];
				i1++;
			}
		}
		while (i2 < nums2.length) {
			if (i1 + i2 - 1 == med_index) {
				if (evenFlag) {
					result = (double) (cur_num + nums2[i2]) / 2;
				} else {
					result = (double) cur_num;
				}
				return result;
			} else {
				cur_num = nums2[i2];
				i2++;
			}
		}
		return (double) cur_num;
	}

}
