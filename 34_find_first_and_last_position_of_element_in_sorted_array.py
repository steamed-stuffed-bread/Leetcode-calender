# medium
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        res = [-1,-1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                start = mid
                while start >= 0 and nums[start] == target:
                    start = start - 1
                while mid <= len(nums)-1 and nums[mid] == target:
                    mid = mid + 1
                start = start + 1
                mid = mid - 1
                res = [start, mid]
                return res
        return res

    
    
    class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        res = [-1,-1]
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if right == len(nums)-1 or nums[right+1] != target:
            return res
        res[0] = right+1
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1
        res[1] = right
        return res
    
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2,-1);
        int left = 0, right = nums.size();
        int mid = 0;
        while(left < right) {
            mid = left + (right-left)/2;
            if (nums[mid] < target)   /* find first one equal or larger */
                left = mid + 1;
            else
                right = mid;
        }
        if (right == nums.size() || nums[right] != target) return res;
        res[0] = right;
        right = nums.size();
        while(left < right) {
            mid = left + (right-left)/2;
            if (nums[mid] <= target)  /* find first one larger */
                left = mid + 1;
            else
                right = mid;
        }
        res[1] = right-1;
        return res;
    }
};
