from typing import List

from test import evaluate_test_cases

class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge):
        x, y = edge
        self.data[x].append(y)
        self.data[y].append(x)

    def remove_edge(self, edge):
        x, y = edge
        self.data[x].remove(y)
        self.data[y].remove(x)

    def __repr__(self):
        return '\n'.join([f'{n}:{neighbours}' for n, neighbours in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

class Solution:
    """
    Steps for solving the problem
    1.State the problem in own words. Identify input/output formats
    2.Figure out example input/output values covering edge cases as well
    3.Write plain English pseudo code
    4.Implement, test and fix issues
    5.Analyze complexity and efficiency
    6.Fix complexities and efficiencies, repeat 3-6

    Question:
    Write a program to check if all the nodes in a graph are connected

    Constraints:
    N/A

    Problem statement (Step 1):
    Given a graph with number of nodes and list of edges, find if all the nodes
    are connected.

    Input/Output formats (Step 1):
    Input:
    num_nodes: number of nodes in the graph, from 0 up to n-1, eg: 8
    edges: list of pairs of nodes which are connected in the graph, eg: [(0,1), (1,2), (2,3)]

    Output:
    True if all the nodes are connected
    False if all the nodes are not connected
    """
    def are_nodes_connected(self, num_nodes: int, edges: List[int]) -> bool:
        """
        Pseudo Code (Step 3):
        1. randomly select a node as root
        2. do a bfs search and find all nodes
        3. len(found nodes) == num_nodes will give if all nodes are connected
        Analyze Complexity (Step 5):
        
        """
        if num_nodes == 0:
            return False
        if len(edges) == 0:
            return False
 
        def bfs(graph, root):
            queue = []
            idx = 0

            seen = [False] * len(graph.data)
            seen[root] = True
            queue.append(root)

            while idx < len(queue):
                current = queue[idx]
                idx += 1

                for node in graph.data[current]:
                    if not seen[node]:
                        seen[node] = True
                        queue.append(node)

            return queue


        graph = Graph(num_nodes, edges)
        
        return num_nodes==len(bfs(graph, 0))

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. all nodes are connected
    2. all nodes are not connected
    3. no edges
    4. no nodes
    """
    test_cases = []
    # 1. 1 pile, hours less than pile size
    test_cases.append({
        'input': {
            'num_nodes': 5,
            'edges': [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'num_nodes': 9,
            'edges': [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'num_nodes': 3,
            'edges': []
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'num_nodes': 0,
            'edges': []
        }, 'output': False
    })
    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.are_nodes_connected, test_cases)