from typing import Sequence, Union

from test import evaluate_test_cases


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
    Write a function to find the length of the longest common subsequence 
    between two sequences. E.g. Given the strings "serendipitous" and 
    "precipitation", the longest common subsequence is "reipito" and
    its length is 7.

    A "sequence" is a group of items with a deterministic ordering. 
    Lists, tuples and ranges are some common sequence types in Python.

    A "subsequence" is a sequence obtained by deleting zero or more 
    elements from another sequence. For example, "edpt" is a subsequence 
    of "serendipitous".

    Constraints:
    N/A

    Problem statement (Step 1):
    Given two sequences, find the length of the largest common subsequence
    between them

    Input/Output formats (Step 1):
    Input:
    sequence1: a sequence example: "serendipitous"
    sequence2: another sequence eg: "precipitation"

    Output:
    len_lcs: length of largest common subsequence between both sequnces
    example: 7 (length of "reipito")
    """
    def common_largest_subsequence(self, sequence1: Sequence[Union[int, str]], sequence2: Sequence[Union[int, str]]) -> int:
        """
        Pseudo Code (Step 3):

        Analyze Complexity (Step 5):
        
        """
        return -1

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. first edge case
    """
    test_cases = []
    # 1. 1 pile, hours less than pile size
    test_cases.append({
        'input': {
            'piles': [30,11,23,4,20],
            'h': 6
        }, 'output': 23
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.solution, test_cases)