package leetcode;

import java.util.ArrayList;

public class AddTwoNumbers2 {
	public class ListNode {
		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
		}
	}

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		Boolean plusFlag = false;
//    	ArrayList<Integer> outputList = new ArrayList<Integer>();
		int sum = l1.val + l2.val;
		if (sum > 9) {
			plusFlag = true;
		}
		sum = sum % 10;
		ListNode head = new ListNode(sum);
		ListNode currentNode = head;
		while (l1.next != null && l2.next != null) {
//        	int plus = 0;
			ListNode preNode = currentNode;
			sum = l1.next.val + l2.next.val;
			if (plusFlag) {
				sum += 1;
				plusFlag = false;
			}
			if (sum > 9) {
				plusFlag = true;
			}

			sum = sum % 10;
			currentNode = new ListNode(sum);
			preNode.next = currentNode;
			l1 = l1.next;
			l2 = l2.next;
//        	outputList.add(sum);
		}

		while (plusFlag) {
			ListNode preNode = currentNode;
			if (l1.next != null) {
				sum = l1.next.val + 1;
				l1 = l1.next;
			} else if (l2.next != null) {
				sum = l2.next.val + 1;
				l2 = l2.next;
			} else {
				sum = 1;
			}
			if (sum > 9) {
				plusFlag = true;
			}else {
				plusFlag = false;
			}
			sum = sum % 10;
			currentNode = new ListNode(sum);
			preNode.next = currentNode;
		}
		while (l1.next != null) {
			ListNode preNode = currentNode;
			currentNode = new ListNode(l1.next.val);
			preNode.next = currentNode;
			l1 = l1.next;

		}
		while (l2.next != null) {
			ListNode preNode = currentNode;
			currentNode = new ListNode(l2.next.val);
			preNode.next = currentNode;
			l2 = l2.next;
		}
		return head;
	}
}
