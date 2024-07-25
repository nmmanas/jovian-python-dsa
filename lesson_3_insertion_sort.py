import random
from typing import List

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
    Write a program to sort a list of numbers using insertion sort.

    Constraints:
    N/A

    Problem statement (Step 1):
    Given a list of numbers, return the list with elements sorted 
    in ascending order using insertion sort algorithm

    Input/Output formats (Step 1):
    Input:
        nums = [5, 1, 6, 4, 6, 7, -1, 0, 34, -44]

    Output:
        result = [-44, -1, 0, 1, 4, 5, 6, 6, 7, 34]

    Method signature:
        def sort(nums: List[int]) -> List[int]:
            pass
    """
    def sort(self, nums: List[int]) -> List[int]:
        """
        Pseudo Code (Step 3):
        1. start from second element
        2. check where it should be placed in the left side
        3. check if the element is less then subsequent previous elements
        4. swap positions if the current element is less than element being
            checked on left

        Analyze Complexity (Step 5):
        - we iterate over the full list for each of the elements
        therefore time complexity is O(n2)
        - space complexity is O(1) since the space used doesn't change
        with the input
        - however, if we also consider the the space of the input,
        then space complexity becomes O(n)
        """

        for i in range(1, len(nums)):
            j = i - 1
            k = i
            while j >= 0:
                if nums[k] < nums[j]:
                    nums[k], nums[j] = nums[j], nums[k]
                    k = j
                else:
                    break
                j -= 1
        return nums

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. list with random numbers
    2. list with repeating numbers
    3. list already sorted
    4. list sorted in decreasing order
    5. empty list
    6. list with one item
    7. list with one item repeated
    8. large list
    """
    test_cases = []
    # 1. list with random numbers
    test_cases.append({
        'input': {
            'nums': [5, 1, 6, 4, 8, 7, -1, 0, 34, -44]
        }, 'output': [-44, -1, 0, 1, 4, 5, 6, 7, 8, 34]
    })

    # 2. list with repeating numbers
    test_cases.append({
        'input': {
            'nums': [5, 1, 6, 4, 6, 7, -1, 0, 34, -44]
        }, 'output': [-44, -1, 0, 1, 4, 5, 6, 6, 7, 34]
    })

    #3. list already sorted
    test_cases.append({
        'input': {
            'nums': [-44, -1, 0, 1, 4, 5, 6, 6, 7, 34]
        }, 'output': [-44, -1, 0, 1, 4, 5, 6, 6, 7, 34]
    })

    # 4. list sorted in decreasing order
    test_cases.append({
        'input': {
            'nums': [34, 7, 6, 6, 5, 4, 1, 0, -1, -44]
        }, 'output': [-44, -1, 0, 1, 4, 5, 6, 6, 7, 34]
    })

    # 5. empty list
    test_cases.append({
        'input': {
            'nums': []
        }, 'output': []
    })

    # 6. list with one item
    test_cases.append({
        'input': {
            'nums': [5]
        }, 'output': [5]
    })

    # 7. list with one item repeated
    test_cases.append({
        'input': {
            'nums': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        }, 'output':  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    })

    # 8. large list
    nums0 = list(range(10000))
    output0 = list(range(10000))
    random.shuffle(nums0)
    test_cases.append({
        'input': {
            'nums': nums0
        }, 'output': output0
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.sort, test_cases)