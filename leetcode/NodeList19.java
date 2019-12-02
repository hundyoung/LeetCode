package leetcode;

public class NodeList19 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListNode head = new ListNode(new int[] {1,2,3,4,5});
		ListNode currentNode = head;

		while (currentNode.next != null) {
			System.out.println(currentNode.val);
			currentNode = currentNode.next;
		}
	}

	public ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode currentNode = head;
		int count = 0;
		while (currentNode.next != null) {
			currentNode = currentNode.next;
			count++;
		}
		currentNode = head;
		int newCount = 0;
		while (currentNode.next != null) {
			if (count - newCount == n) {
				ListNode nextNode = currentNode.next.next;
				currentNode.next = nextNode;
			}

			newCount++;
			currentNode = currentNode.next;
		}
		return head;
	}



}
