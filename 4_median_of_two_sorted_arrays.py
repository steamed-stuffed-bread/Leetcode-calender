# medium
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1 = nums1
        self.nums2 = nums2
        m = len(nums1)
        n = len(nums2)
        left = (m+n+1)/2
        right = (m+n+2)/2
        mid = (self.findkth(0,0,left)+self.findkth(0,0,right))/2.0
        return mid
    
    def findkth(self,i,j,k):
        if i >= len(self.nums1):
            return self.nums2[j+k-1]
        if j >= len(self.nums2):
            return self.nums1[i+k-1]
        if k == 1:
            return min(self.nums1[i], self.nums2[j])
        mid1 = self.nums1[i+k/2-1] if i+k/2-1 < len(self.nums1) else sys.maxint
        mid2 = self.nums2[j+k/2-1] if j+k/2-1 < len(self.nums2) else sys.maxint
        if mid1 < mid2:
            return self.findkth(i+k/2, j, k-k/2)
        else:
            return self.findkth(i, j+k/2, k-k/2)
