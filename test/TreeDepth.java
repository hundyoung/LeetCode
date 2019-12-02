package test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class TreeDepth {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in) ;
		int n = scan.nextInt();
		int root =0;
		HashMap<Integer,HashMap<Integer,Boolean>> graph = new HashMap<Integer,HashMap<Integer,Boolean>>();
		for(int i =0;i<n-1;i++) {
			int fa = scan.nextInt();
			if(i==0) {
				root=fa;
			}
			int child = scan.nextInt();
			HashMap<Integer,Boolean> node;
			if(graph.containsKey(fa)) {
				node = graph.get(fa);

			}else {
				 node = new HashMap<Integer,Boolean>();
			}
			node.put(child, true);
			graph.put(fa, node);
		}
		List<Integer> toProcess = new ArrayList<Integer>();
		List<Integer> layerNode = new ArrayList<Integer>();
		int depth=0;
		toProcess.add(root);
		while(toProcess.size()>0) {
			int node = toProcess.remove(0);
			HashMap<Integer,Boolean> ajdantNodes = graph.get(node);
			if(ajdantNodes!=null) {
				for(Integer adjNode:ajdantNodes.keySet()) {
					layerNode.add(adjNode);
				}
			}
			if(toProcess.size()==0) {
				toProcess=layerNode;
				depth++;
				layerNode = new ArrayList<Integer>();
			}
		}
		System.out.println(depth);
	}

}
