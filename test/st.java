package test;

public class st {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Solution s = new Solution();
//		TreeNode root =new TreeNode(1);
//		root.left = new TreeNode(2);
//		root.right = new TreeNode(3);
//		root.left.left = new TreeNode(4);
//		root.right.left = new TreeNode(5);
//		int dep = s.run(root);
//		System.out.println(dep);
	 String str="abc";
		System.out.println(str);
	str=str+"de";
	System.out.println(str);
//		int target = 10;
//		int array[][] = new int[][] {{1,2,8,9},{2,4,9,12},{4,7,10,13},{6,8,11,15}};
//		System.out.println(Find(target,array));
		
	}
	public static boolean Find(int target, int [][] array) {
        int[] row_0 = array[0];
        int i=0;
        int j=row_0.length-1;
        int index=0;
        while(i<=j){
            index = (i+j)/2;
			if(row_0[index]<target) {
				i=index+1;
			}else if(row_0[index]>target){
				j=index-1;
			}else {
				break;
			}
        }
        if(i>=row_0.length) {
        	i--;
        }
        if(row_0[i]>target){
            i--;
        }else if(row_0[i]==target){
            return true;
        }
        j=0;
        int k=array.length;
        while(j<=k){
            index = (k+j)/2;
			if(array[index][i]<target) {
				j=index+1;
			}else if(array[index][i]>target){
				k=index-1;
			}else {
				return true;
			}
        }
        return false;
    }
}
