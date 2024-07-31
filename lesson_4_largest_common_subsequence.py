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
    def lcs_recursive(self, sequence1: Sequence[Union[int, str]], sequence2: Sequence[Union[int, str]], idx=0, jdx=0) -> int:
        """
        Pseudo Code (Step 3):
        1. if first element of both sequences are equal,
            add 1 to result, recursively check for rest of the sequence
            in both
        2. if first elements are not equal,
            - recursively check for sequence1 second element onwards
            and sequence2 first element onwards
            - recursively check for sequence1 first element onwards
            and sequence2 second element onwards
            - return the max of above 2
        3. if one of the sequence is empty, then return 0 (recursion breaker)

        Analyze Complexity (Step 5):
        
        """
        # "serendipitous"
        # "precipitation"
        if idx==len(sequence1) or jdx==len(sequence2):
            return 0

        if sequence1[idx] == sequence2[jdx]:
            return 1 + self.lcs_recursive(sequence1, sequence2, idx+1, jdx+1)
        else:
            first = self.lcs_recursive(sequence1, sequence2, idx+1, jdx)
            second = self.lcs_recursive(sequence1, sequence2, idx, jdx+1)
            return max(first, second)
        
    def lcs_memo(self, sequence1: Sequence[Union[int, str]], sequence2: Sequence[Union[int, str]]) -> int:
        """
        Pseudo Code (Step 3):
        1. if first element of both sequences are equal,
            add 1 to result, recursively check for rest of the sequence
            in both
        2. if first elements are not equal,
            - recursively check for sequence1 second element onwards
            and sequence2 first element onwards
            - recursively check for sequence1 first element onwards
            and sequence2 second element onwards
            - return the max of above 2
        3. if one of the sequence is empty, then return 0 (recursion breaker)

        Analyze Complexity (Step 5):
        
        """
        memo = {}

        def recurse(idx=0, jdx=0):
            key = (idx, jdx)
            if key in memo:
                return memo[key]
            elif idx==len(sequence1) or jdx==len(sequence2):
                memo[key]=0
            elif sequence1[idx] == sequence2[jdx]:
                memo[key]=1 + recurse(idx+1, jdx+1)
            else:
                first = recurse(idx+1, jdx)
                second = recurse(idx, jdx+1)
                memo[key]=max(first,second)
            return memo[key]
        
        return recurse(0,0)
    
    def lcs_dynamic(self, sequence1: Sequence[Union[int, str]], sequence2: Sequence[Union[int, str]]) -> int:
        """
        Pseudo Code (Step 3):
        1. Create table with rows and columns equal to len(s1)+1 and len(s2)+1
        2. fill it with 0s
        3. skip first row and first column
        4. iterate over each sequence in a nested loop
        5. if s1[i] == s2[j], then set table[i][j] with 1 + table[i-1][j-1]
        6. else set table[i][j] with the max of table[i-1][j] and table[i][j-1]
        
        Analyze Complexity (Step 5):
        Time Complexity is O(n*m) since we traverse both sequences in a loop
        Space Complexity is also O(n*m) since we create a table with n rows and m columns
        """
        len1 = len(sequence1)
        len2 = len(sequence2)

        lcs_table = [[0] * (len2+1) for _ in range(len1+1)]

        for i in range(len1):
            for j in range(len2):
                if sequence1[i]==sequence2[j]:
                    lcs_table[i+1][j+1] = 1 + lcs_table[i][j]
                else:
                    lcs_table[i+1][j+1] = max(lcs_table[i+1][j], lcs_table[i][j+1])

        return lcs_table[-1][-1]


def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. general case (list/string/tuple)
    2. both same sequence
    3. no common subsequence
    4. 1 empty sequence
    5. both empty sequences
    6. 1 item in sequence, same
    7. 1 item in sequence, different
    8. one is subsequence of other
    9. multiple subsequences with same length
    """
    test_cases = []

    # 1. general case (list/string/tuple)
    seq0 = "serendipitous"
    seq1 = "precipitation"
    test_cases.append({
        'input': {
            'sequence1': seq0,
            'sequence2': seq1
        }, 'output': 7
    })
    test_cases.append({
        'input': {
            'sequence1': list(seq0),
            'sequence2': list(seq1)
        }, 'output': 7
    })
    test_cases.append({
        'input': {
            'sequence1': tuple(seq0),
            'sequence2': tuple(seq1)
        }, 'output': 7
    })
    test_cases.append({
        'input': {
            'sequence1': [1,2,3,4,5,6,7,8,9,10],
            'sequence2': [4,6,8]
        }, 'output': 3
    })
    # 2. both same sequence
    test_cases.append({
        'input': {
            'sequence1': "dinosaur",
            'sequence2': "dinosaur"
        }, 'output': 8
    })
    # 3. no common subsequence
    test_cases.append({
        'input': {
            'sequence1': "elephant",
            'sequence2': "dog"
        }, 'output': 0
    })
    # 4. 1 empty sequence
    test_cases.append({
        'input': {
            'sequence1': "dinosaur",
            'sequence2': ""
        }, 'output': 0
    })
    test_cases.append({
        'input': {
            'sequence1': "",
            'sequence2': "dinosaur"
        }, 'output': 0
    })
    # 5. both empty sequences
    test_cases.append({
        'input': {
            'sequence1': "",
            'sequence2': ""
        }, 'output': 0
    })
    test_cases.append({
        'input': {
            'sequence1': [],
            'sequence2': []
        }, 'output': 0
    })
    # 6. 1 item in sequence, same
    test_cases.append({
        'input': {
            'sequence1': "m",
            'sequence2': "m"
        }, 'output': 1
    })
    # 7. 1 item in sequence, different
    test_cases.append({
        'input': {
            'sequence1': "m",
            'sequence2': "n"
        }, 'output': 0
    })
    # 8. one is subsequence of other
    test_cases.append({
        'input': {
            'sequence1': "dense",
            'sequence2': "condensed"
        }, 'output': 5
    })
    test_cases.append({
        'input': {
            'sequence1': "condensed",
            'sequence2': "dense"
        }, 'output': 5
    })
    # 9. multiple subsequences with same length
    test_cases.append({
        'input': {
            'sequence1': "abcdef",
            'sequence2': "badcfe"
        }, 'output': 3
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.lcs_dynamic, test_cases)