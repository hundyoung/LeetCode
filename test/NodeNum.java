package test;

import java.util.Scanner;

public class NodeNum {

	public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[] toProcess = new int[n+1];
        int node = m;
        System.out.println(findChild(n,m));
    }
    public static int findChild(int father,int n){
        if(father<=n){
            return findChild(2*father,n)+findChild(2*father+1,n)+1;
        }else {

            return 0;
        }
    }

}
