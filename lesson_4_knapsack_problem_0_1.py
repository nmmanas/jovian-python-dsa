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
    def maximum_rating_recursive(self, costs: List[int], ratings: List[int], budget: int) -> int:
        """
        Pseudo Code (Step 3):

        Analyze Complexity (Step 5):
        
        """
        pass

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