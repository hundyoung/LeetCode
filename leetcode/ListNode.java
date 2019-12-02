package leetcode;


public class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
	}
	ListNode(int [] a) {
		val = a[0];
		ListNode c =new ListNode(val);
		for(int i=1;i<a.length;i++) {

			ListNode n =new ListNode(a[1]);
			c.next = n;
			c=n;
		}
		
	}
}
