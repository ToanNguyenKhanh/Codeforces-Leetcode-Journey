class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        fre_count = [0] * (max_val + 1)  
        for v in nums:  
            fre_count[v] += 1
        ans = 0
        for idx, val in enumerate(fre_count):  
            if val != 1:
                continue
            ans += idx
        return ans
