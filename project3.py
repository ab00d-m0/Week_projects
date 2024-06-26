class Solution:
    @staticmethod
    def solve(A, B):
        n = len(A)
        left = 0
        max_length = 0
        zero_count = 0
        for right in range(n):
            if A[right] == 0:
                zero_count += 1
            while zero_count > B:
                if A[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

A1 = [1, 0, 0, 1, 1, 0, 1]
B1 = 1
print(Solution.solve(A1, B1))

A2 = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
B2 = 2
print(Solution.solve(A2, B2))
