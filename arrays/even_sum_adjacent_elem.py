class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        odd_numbers = sum([x%2 for x in A])
        return min(len(A) - odd_numbers, odd_numbers)