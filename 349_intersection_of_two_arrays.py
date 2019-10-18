# easy
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            s = set(nums1)
            os = nums2
        else:
            s = set(nums2)
            os = nums1
        res = []
        for e in s:
            if e in os:
                res.append(e)
        return res
