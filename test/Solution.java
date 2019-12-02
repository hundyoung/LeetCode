package test;

import java.util.ArrayList;
import java.util.Collections;

/**
 * Definition for binary tree public class TreeNode { int val; TreeNode left;
 * TreeNode right; TreeNode(int x) { val = x; } }
 */
public class Solution {
	public int run(TreeNode root) {
		ArrayList<TreeNode> nodeList = new ArrayList<TreeNode>();
		char a='a';
		nodeList.sort((TreeNode t1,TreeNode t2)-> t1.val - t2.val);
		Collections.reverse(nodeList);
		nodeList.add(root);
		int depth = 0;
		while (nodeList.size() > 0) {

			depth += 1;
			ArrayList<TreeNode> next = new ArrayList<TreeNode>();
			while(nodeList.size()>0) {
				TreeNode currentNode = nodeList.remove(0);
				if (currentNode.left == null && currentNode.right == null) {
					return depth;
				}
				if (currentNode.left != null) {

					next.add(currentNode.left);
				}
				if (currentNode.right != null) {

					next.add(currentNode.right);
				}
			}
			nodeList = next;

		}
		return depth;
	}
}