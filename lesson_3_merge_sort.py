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
    Write a program to sort a list of numbers using merge sort.

    Constraints:
    N/A

    Problem statement (Step 1):
    Given a list of numbers, return the list with elements sorted 
    in ascending order using merge sort algorithm

    Input/Output formats (Step 1):
    Input:
        nums = [5, 1, 6, 4, 6, 7, -1, 0, 34, -44]

    Output:
        result = [-44, -1, 0, 1, 4, 5, 6, 6, 7, 34]

    Method signature:
        def sort(nums: List[int]) -> List[int]:
            pass
    """
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result3 = []

        r1 = 0
        r2 = 0

        while r1 < len(nums1) and r2 < len(nums2):
            if nums1[r1] < nums2[r2]:
                result3.append(nums1[r1])
                r1 += 1
            else:
                result3.append(nums2[r2])
                r2 += 1

        remainder1 = nums1[r1:]
        remainder2 = nums2[r2:]

        return result3 + remainder1 + remainder2

    def sort(self, nums: List[int]) -> List[int]:
        """
        Pseudo Code (Step 3):
        1. break list in to two and recursively call sort method
        2. for both resulted lists, merge them on ascending order
            a. compare first values and get the lowest one
            b. increment index of lowest, and continue the comparison
            c. loop until one of the index is equal to list size
        3. return the merged result + the remainder from other result list

        Analyze Complexity (Step 5):
        - Time Complexity: time it takes to merge sort a list of n is equal 
        to time takes to merge sort 2 lists of n/2 and the time it takes
        to merge those 2 arrays

        so T(n) = T(n/2) + T(n/2) + T(merge 2 n/2 lists)

        for merging two n/2 lists, it will take n/2 + n/2 + C which is n + C

        so T(n) = T(n/2) + T(n/2) + O(n)

        using regression tree method, this comes down to 
        T(n) = O(nlogn) + O(n) = O(nlogn)

        - Space Complexity: on the merge operation, space equal to initial list size is used. so for size of n
        list the space complexity is O(n). although each recursion levels also use spaces of n/2, n/4 etc for
        merging those spaces are released as soon as the merged list is released.
        
        Each level of recursion uses
        a small amount of space, but this is limited to the depth of the recursion tree, which is O(logn).
        
        therefore:
        S(n) = O(n) + O(logn)
             = O(n)
        """
        if len(nums) <= 1:
            return nums
        
        half = len(nums)//2
        nums1 = nums[:half]
        nums2 = nums[half:]
        
        result1 = self.sort(nums1)
        result2 = self.sort(nums2)

        result3 = self.merge(result1, result2)

        return result3

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