class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = list(nums1 & nums2)
        print(result)
        return result

if __name__ == '__main__':
    So = Solution()
    So.intersect([1,2,2,1], [2,2])
