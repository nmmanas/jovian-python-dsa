from collections import defaultdict
import random
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
    Write a function to detect a cycle in a graph

    Constraints:
    NA

    Problem statement (Step 1):
    Given num_nodes and edges of a graph, return True if a cycle 
    can be detected in the graph

    Input/Output formats (Step 1):
    Input:
    num_nodes: number of nodes in the graph from 0 to n-1
    edges: list of pairs, denoting each edge in the graph

    Output:
    result: True or False depending on whether a cycle is detected or not
    """
    def detect_cycle(self, num_nodes: int, edges: List[int]) -> bool:
        """
        Pseudo Code (Step 3):
        1. keep track of how many times visited
        2. if visited twice, then detected cycle
        Analyze Complexity (Step 5):
        
        """

        if len(edges)==0:
            return False
        if num_nodes==0:
            return False

        graph = Graph(num_nodes, edges)

        queue = []
        idx = 0
        seen = defaultdict(int)

        start = random.choice(list(range(num_nodes)))

        queue.append(start)
        seen[start] += 1 


        while idx < len(queue):
            current = queue[idx]
            if seen[current] > 1:
                return True
            idx += 1

            for node in graph.data[current]:
                if seen[node] == 0:
                    queue.append(node)
                seen[node] += 1

        return False

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. 1 cycle
    2. 2 cycles
    3. one large cycle
    4. no cycle - tree
    5. line
    6. no nodes
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
            'num_nodes': 7,
            'edges': [(0,5), (5,2), (5,3), (2,3), (0,6), (6,1), (6,4), (1,4)]
        }, 'output': True
    })
  
    test_cases.append({
        'input': {
            'num_nodes': 6,
            'edges': [(0,1), (1,3), (3,2), (2,4), (4,5), (5,0)] 
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'num_nodes': 7,
            'edges': [(0,2), (2,3), (2,5), (5,1), (1,4), (1,6)]
        }, 'output': False
    })
    
    test_cases.append({
        'input': {
            'num_nodes': 5,
            'edges': [(0,1), (1,2), (2,3), (3,4)]
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
    evaluate_test_cases(solution.detect_cycle, test_cases)