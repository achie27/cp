class Solution:
    def solve(self, A, B, C):
        start_a, ln_a = 0, len(A)
        end_b, ln_b = len(B) - 1, len(B)
        
        min_diff, min_diff_index = float('inf'), [-1, -1]
        while start_a < ln_a and end_b >= 0:
            cur_sum = A[start_a] + B[end_b]

            if min_diff > abs(cur_sum - C):
                min_diff = abs(cur_sum - C)
                min_diff_index = [start_a, end_b]
            elif min_diff == abs(cur_sum - C) and min_diff_index[0] == start_a:
                min_diff_index = [start_a, end_b]

            if cur_sum > C:
                end_b -= 1
            elif cur_sum < C:
                start_a += 1
            else:
                break

        return [A[min_diff_index[0]], B[min_diff_index[1]]]