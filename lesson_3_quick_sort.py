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
    Write a program to sort a list of numbers using quick sort.

    Constraints:
    N/A

    Problem statement (Step 1):
    Given a list of n elements, return the sorted list using quick sort

    Input/Output formats (Step 1):
    Input:
        nums = [5, 1, 6, 4, 6, 7, -1, 0, 34, -44]

    Output:
        result = [-44, -1, 0, 1, 4, 5, 6, 6, 7, 34]

    Method signature:
        def quick_sort(nums: List[int]) -> List[int]:
            pass
    """

    def partition_pivot_last(self, nums, start, end):
        """
        Pseudo code:
        1. identify pivot index ie. end
        2. move pivot to somewhere in the middle where
        elements on left are <= pivot
        elements on right are >= pivot
            a. get start, end (end-1) indexes, excluding pivot (ie. end)
            b. while start < end
                i. check if start <= pivot, if yes, start += 1
                ii. if start > pivot,
                    - check if end >= pivot, if yes, end -= 1
                    - if end < pivot,
                    - switch start and end, start+=1 end-=1
            c. finally switch pivot with end (or start since both are same)
        3. return pivot index
        """
        pivot = end
        
        left = start
        right = end - 1

        while left < right:
            if nums[left] <= nums[pivot]:
                left += 1
            elif nums[right] > nums[pivot]:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]

        if nums[right] > nums[pivot]:
            nums[right], nums[pivot] = nums[pivot], nums[right]
            return right

        return pivot

    def partition_pivot_first(self, nums, start, end):
        """
        Pseudo code:
        1. consider first element as pivot
        2. use two sliders left, right, where left = start, right = left + 1
        3. check if right >= pivot,
            a. if yes, then move right + 1
            b. else: move left+1, and switch with right
            c. do until right is equal to end
        4. finally switch pivot with left
        """

        left = start
        right = left + 1
        count = 0

        while left < right <= end:
            if nums[right] > nums[start]:
                right += 1
            else:
                left += 1
                
                nums[left], nums[right] = nums[right], nums[left]

                right += 1
            count+=1

        nums[left], nums[start] = nums[start], nums[left]

        return left

    def quick_sort(self, nums: List[int], start=0, end = None) -> List[int]:
        """
        Pseudo Code (Step 3):
        1. identify a pivot in the input
        2. partition the list such that elements <= pivot are on left
        and elements >= pivot are on right
        3. recursively identify pivot and partition both left and right sides
        4. if input has one or less elements, return input

        Analyze Complexity (Step 5):
        
        """
        if end is None:
            end = len(nums)-1
        
        if start < end:
            pivot = self.partition_pivot_first(nums, start, end)

            # sort left partition
            self.quick_sort(nums, start, pivot-1)

            # sort right partition
            self.quick_sort(nums, pivot+1, end)

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

    # # 0. random shuffled
    # nums0 = list(range(9))
    # output0 = list(range(9))
    # random.shuffle(nums0)
    # test_cases.append({
    #     'input': {
    #         'nums': nums0
    #     }, 'output': output0
    # })

    # 1. list with random numbers
    test_cases.append({
        'input': {
            'nums': [4, 7, 5, 3, 0, 6, 2, 8, 1]
        }, 'output': [0, 1, 2, 3, 4, 5, 6, 7, 8]
    })

    test_cases.append({
        'input': {
            'nums': [6, 10, 13, 5, 8, 3, 2, 1]
        }, 'output': [1, 2, 3, 5, 6, 8, 10, 13]
    })
    test_cases.append({
        'input': {
            'nums': [8, 3, 1, 2, 0, 7, 6, 4, 5]
        }, 'output': [0, 1, 2, 3, 4, 5, 6, 7, 8]
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
    nums1 = list(range(10000))
    output1 = list(range(10000))
    random.shuffle(nums1)
    test_cases.append({
        'input': {
            'nums': nums1
        }, 'output': output1
    })

    # 8. large list
    nums0 = list(range(100000))
    output0 = list(range(100000))
    random.shuffle(nums0)
    test_cases.append({
        'input': {
            'nums': nums0
        }, 'output': output0
    })

    # # 9. large list, sorted
    # nums2 = list(range(10000))
    # output2 = list(range(10000))

    # test_cases.append({
    #     'input': {
    #         'nums': nums2
    #     }, 'output': output2
    # })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.quick_sort, test_cases)