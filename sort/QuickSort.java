package sort;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class QuickSort {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = readFile();
		writeFile(nums);
	}

	public static int[] readFile() {
		String pathname = "1.txt";
		int[] nums = null;
		try (FileReader reader = new FileReader(pathname); BufferedReader br = new BufferedReader(reader)) {
			String line = br.readLine();
			String[] arr = line.split(",");
			nums = new int[arr.length];
			for (int i = 0; i < arr.length; i++) {
				nums[i] = Integer.parseInt(arr[i]);
			}
			quickSort(nums, 0, arr.length);

		} catch (IOException e) {
			e.printStackTrace();
		}
		return nums;
	}

	public static void writeFile(int[] nums) {
		try {
			File writeName = new File("2.txt"); 
			writeName.createNewFile(); 
			try (FileWriter writer = new FileWriter(writeName); BufferedWriter out = new BufferedWriter(writer)) {
				for(int i=0;i<nums.length;i++) {
					out.write(nums[i]+",");
				}
				out.flush(); 

			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void quickSort(int[] a, int start, int end) {
		if (start < end) {
			int baseNum = a[start];// 选基准值
			int midNum;// 记录中间值
			int i = start;
			int j = end;
			do {
				while ((a[i] < baseNum) && i < end) {
					i++;
				}
				while ((a[j] > baseNum) && j > start) {
					j--;
				}
				if (i <= j) {
					midNum = a[i];
					a[i] = a[j];
					a[j] = midNum;
					i++;
					j--;
				}
			} while (i <= j);
			if (start < j) {
				quickSort(a, start, j);
			}
			if (end > i) {
				quickSort(a, i, end);
			}
		}
	}
}
