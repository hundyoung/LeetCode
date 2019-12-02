package test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class Graph {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		Integer input = scan.nextInt();
		while (input != null) {
			Integer n = input;
			Integer m = scan.nextInt();
//				Integer[][] graph = new Integer[n][n];
			HashMap<Integer, HashMap<Integer, Boolean>> graph = new HashMap<Integer, HashMap<Integer, Boolean>>();
			for (int i = 0; i < m; i++) {
				Integer node_1 = scan.nextInt();
				Integer node_2 = scan.nextInt();
				HashMap<Integer, Boolean> nodeMap;
				if (graph.containsKey(node_1)) {
					nodeMap = graph.get(node_1);
				} else {
					nodeMap = new HashMap<Integer, Boolean>();
				}
				nodeMap.put(node_2, true);
				graph.put(node_1, nodeMap);
				if (graph.containsKey(node_2)) {
					nodeMap = graph.get(node_2);
				} else {
					nodeMap = new HashMap<Integer, Boolean>();
				}
				nodeMap.put(node_1, true);
				graph.put(node_2, nodeMap);
//					graph[node_1][node_2] = 1;
//					graph[node_1][node_1] = 1;

			}
			Iterator<HashMap.Entry<Integer, HashMap<Integer, Boolean>>> entries = graph.entrySet().iterator();
			boolean flag = true;
			while (entries.hasNext()) {
				HashMap.Entry<Integer, HashMap<Integer, Boolean>> entry = entries.next();
				Integer node = entry.getKey();
				List<Integer> toProcess = new ArrayList<Integer>();
				HashMap<Integer, Boolean> processed = new HashMap<Integer, Boolean>();
				toProcess.add(node);
				while (toProcess.size() > 0) {
					Integer currentNode = toProcess.remove(0);
					HashMap<Integer, Boolean> ajaNodes = graph.get(currentNode);
					processed.put(currentNode, true);
					for (Integer node_2 : ajaNodes.keySet()) {
						if (processed.containsKey(node_2)) {
							continue;
						}
						if(toProcess.contains(node_2)) {
							continue;
						}
						toProcess.add(node_2);
					}
					graph.get(node).put(currentNode, true);
				}
				if (graph.get(node).keySet().size() < n) {
//					System.out.println(graph.get(node).keySet().size());
					System.out.println("NO");
					flag=false;
					break;
				}
			}
			if(flag==true) {

				System.out.println("YES");
			}
			if (!scan.hasNext()) {
				break;
			}else {
				input = scan.nextInt();
			}
		}
	}

}
