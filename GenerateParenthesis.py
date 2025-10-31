from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses for n pairs.

        Args:
        n (int): Number of pairs of parentheses.

        Returns:
        List[str]: List containing all valid combinations of parentheses.
        """

        # List to store all valid parentheses combinations
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            """
            Helper function to build parentheses combinations using backtracking.

            Args:
            current (str): The current combination being built.
            open_count (int): Number of '(' used so far.
            close_count (int): Number of ')' used so far.
            """

            # Base case: if we have used all n open and n close parentheses
            if open_count == n and close_count == n:
                result.append(current)  # Add valid combination to result
                return

            # If we can still add an open parenthesis, do so
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            # If we can add a close parenthesis without exceeding the number of opens
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        # Start the recursion with an empty string and zero counts
        backtrack("", 0, 0)

        return result
