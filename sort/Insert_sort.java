package sort;

public class Insert_sort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

	}
	public void insertSort(int [] a) {
		int len = a.length;
		int target;
		for(int i=1;i<len;i++) {
			target = a[i];
			int j =i-1;
			while(j>=0&&a[j]>target) {
				a[j+1]=a[j];
				j--;
			}
			a[j+1] = target;
		}
	}
}
