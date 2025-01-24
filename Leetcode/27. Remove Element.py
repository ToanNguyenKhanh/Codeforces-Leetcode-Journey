class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        for v in nums:
            if v != val:
                nums[p1] = v
                p1+=1
        return p1