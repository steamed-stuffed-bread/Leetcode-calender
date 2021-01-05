class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        int n = nums.size(), i = 0;
        for (i = 0; i < n; ++i) {
            int k = nums[i];
            if (k < 0) k += n;
            if (nums[k] < 0) return k;
            nums[k] -= n;
        }

        return 0;
    }
};
