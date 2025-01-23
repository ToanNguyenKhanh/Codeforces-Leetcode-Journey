class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        fre_count = [0] * (max_val + 1)  # M
        for v in nums:  # N
            fre_count[v] += 1
        ans = 0
        for idx, val in enumerate(fre_count):  # M
            if val != 1:
                continue
            ans += idx
        return ans
