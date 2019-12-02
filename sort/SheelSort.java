package sort;

public class SheelSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	 public void sheelSort(int [] a){
		 int gap = a.length;
		 while(gap!=0) {
			 gap=gap/2;
			 for(int i=0;i<gap;i++) {
				 for(int j=i+gap;j<a.length;j+=gap) {
					 int k=j-gap;
					 int target = a[j];
					 while(k>0&&target<a[k]) {
						 a[k+gap]=a[k];
						 k-=gap;
					 }
					 a[k+gap]=target;
				 }
			 }
		 }
	 }
}
