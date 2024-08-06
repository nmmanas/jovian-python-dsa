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
    Implement depth first search from a given node in a graph using Python.

    Constraints:
    NA

    Problem statement (Step 1):
    Given num_nodes and edges of a graph, implement depth first search and find
    the nodes from the graph.

    Input/Output formats (Step 1):
    Input:
    num_nodes: number of nodes in the graph from 0 to n-1
    edges: list of pairs, denoting each edge in the graph

    Output:
    result: list of nodes in dfs order
    """
    def traverse_dfs(self, num_nodes: int, edges: List[int]) -> int:
        """
        Pseudo Code (Step 3):
        1. iterate through each node starting from root
        2. recursively iterate neighbors before moving to next
        Analyze Complexity (Step 5):
        
        """
        if num_nodes == 0:
            return []
        seen = [False] * num_nodes
        results = []

        seen[0] = True

        def dfs(graph, node):
            results.append(node)
            neighbours = graph.data[node]

            for n in neighbours:
                if not seen[n]:
                    seen[n] = True
                    dfs(graph, n)

        graph = Graph(num_nodes, edges)

        dfs(graph, 0)

        return results

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. random nodes and edges
    2. one node
    3. two nodes
    4. no nodes
    """
    test_cases = []
    
    test_cases.append({
        'input': {
            'num_nodes': 5,
            'edges': [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]
        }, 'output': [0, 1, 2, 3, 4]
    })
    
    test_cases.append({
        'input': {
            'num_nodes': 1,
            'edges': []
        }, 'output': [0]
    })
    
    test_cases.append({
        'input': {
            'num_nodes': 2,
            'edges': [(0,1)]
        }, 'output': [0, 1]
    })
    
    test_cases.append({
        'input': {
            'num_nodes': 0,
            'edges': []
        }, 'output': []
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.traverse_dfs, test_cases)