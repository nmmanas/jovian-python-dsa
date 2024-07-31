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
    You're in charge of selecting a football (soccer) team from a large pool 
    of players. Each player has a cost, and a rating. You have a limited budget.
    What is the highest total rating of a team that fits within your budget. 
    Assume that there's no minimum or maximum team size.

    Constraints:
    No minimum or maximum team size
    Length of costs is equal to length of ratings

    Problem statement (Step 1):
    Given two lists of costs and ratings, and a budget, select a team with maximum
    rating with maximum possible rating within the given budget. Return the highest
    possible rating.

    Input/Output formats (Step 1):
    Input:
    `costs`: list of costs for the players
    `ratings`: list of ratings for the players
    `budget`: integer mentioning the available budget to select max rated team

    Output:
    `max_rating`: maximum possible rating that can be obtained for the given budget
    """
    def maximum_rating_recursive(self, costs: List[int], ratings: List[int], budget: int, idx: int = 0) -> int:
        """
        Pseudo Code (Step 3):
        1. Process one by one ie. idx=0...n-1
        2. if costs[idx] > remaining budget, don't include it
        3. else we have two options,
            a. include current one
            b. don't include current
        4. get the max of both options
        5. base case is idx==n

        Analyze Complexity (Step 5):
        """
        if  idx==len(costs):
            return 0
        elif costs[idx] > budget:
            return self.maximum_rating_recursive(costs, ratings, budget, idx+1)
        else:
            option1 = ratings[idx] + self.maximum_rating_recursive(costs, ratings, budget-costs[idx], idx+1)
            option2 = self.maximum_rating_recursive(costs, ratings, budget, idx+1)
        return max(option1, option2)

    def maximum_rating_memo(self, costs: List[int], ratings: List[int], budget: int, idx: int = 0) -> int:
        """
        Pseudo Code (Step 3):
        1. Process one by one ie. idx=0...n-1
        2. if costs[idx] > remaining budget, don't include it
        3. else we have two options,
            a. include current one
            b. don't include current
        4. get the max of both options
        5. base case is idx==n
        6. if a budget, index pair is already computed, then add it to memo and reuse

        Analyze Complexity (Step 5):
        """
        memo = {}

        def recursive(costs, ratings, budget, idx=0):
            key = (budget, idx)
            if key in memo:
                return memo[key]
            if  idx==len(costs):
                memo[key] = 0
            elif costs[idx] > budget:
                memo[key] = recursive(costs, ratings, budget, idx+1)
            else:
                option1 = ratings[idx] + recursive(costs, ratings, budget-costs[idx], idx+1)
                option2 = recursive(costs, ratings, budget, idx+1)
                memo[key] = max(option1, option2)
            return memo[key]
        return recursive(costs, ratings, budget)

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. all elements can be included
    2. none of the elements can be included
    3. only one element can be included
    4. 1 element each in both lists
    5. budget leftover after finding maximum rating
    6. test cases from jovian
    """
    test_cases = []
    # 1. all elements can be included
    test_cases.append({
        'input': {
            'costs': [1, 2, 3],
            'ratings': [9, 8, 7],
            'budget': 6
        },
        'output': 24
    })
    # 2. none of the elements can be included
    test_cases.append({
        'input': {
            'costs': [4, 5, 6],
            'ratings': [9, 8, 7],
            'budget': 3
        },
        'output': 0
    })
    # 3. only one element can be included
    test_cases.append({
        'input': {
            'costs': [4, 5, 6],
            'ratings': [9, 8, 7],
            'budget': 4
        },
        'output': 9
    })
    # 4. 1 element each in both lists
    test_cases.append({
        'input': {
            'costs': [4],
            'ratings': [9],
            'budget': 4
        },
        'output': 9
    })
    test_cases.append({
        'input': {
            'costs': [4],
            'ratings': [9],
            'budget': 3
        },
        'output': 0
    })
    # 5. budget leftover after finding maximum rating
    # budget > sum(costs)
    test_cases.append({
        'input': {
            'costs': [4, 5, 6],
            'ratings': [9, 8, 7],
            'budget': 20
        },
        'output': 24
    })
    # budget < sum(cost)
    test_cases.append({
        'input': {
            'costs': [4, 5, 6],
            'ratings': [9, 8, 7],
            'budget': 10
        },
        'output': 17
    })
    # 6. test cases from jovian
    test0 = {
        'input': {
            'budget': 165,
            'costs': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            'ratings': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
        },
        'output': 309
    }

    test1 = {
        'input': {
            'budget': 3,
            'costs': [4, 5, 6],
            'ratings': [1, 2, 3]
        },
        'output': 0
    }

    test2 = {
        'input': {
            'budget': 4,
            'costs': [4, 5, 1],
            'ratings': [1, 2, 3]
        },
        'output': 3
    }

    test3 = {
        'input': {
            'budget': 170,
            'costs': [41, 50, 49, 59, 55, 57, 60],
            'ratings': [442, 525, 511, 593, 546, 564, 617]
        },
        'output': 1735
    }

    test4 = {
        'input': {
            'budget': 15,
            'costs': [4, 5, 6],
            'ratings': [1, 2, 3]
        },
        'output': 6
    }

    test5 = {
        'input': {
            'budget': 15,
            'costs': [4, 5, 1, 3, 2, 5],
            'ratings': [2, 3, 1, 5, 4, 7]
        },
        'output': 19
    }

    test_cases += [test0, test1, test2, test3, test4, test5]

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.maximum_rating_memo, test_cases)