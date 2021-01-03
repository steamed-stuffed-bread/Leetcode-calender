class Solution {
public:
    bool isStraight(vector<int>& nums) {
        int n = nums.size(), i = 0;
        set<int> s;
        int mx = -1, mn = 14;
        for (i = 0; i < n; ++i) {
            if (nums[i] == 0) continue;
            if (s.count(nums[i])) return false;
            mx = max(mx, nums[i]);
            mn = min(mn, nums[i]);
            s.insert(nums[i]);
        }

        return mx - mn < 5;
    }
};

class Solution {
public:
    bool isStraight(vector<int>& nums) {
        int n = nums.size(), i = 0;
        int zeros = 0;
        sort(nums.begin(), nums.end());
        for (i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                zeros++;
                continue;
            }
            if (i > 0 && nums[i] == nums[i-1]) return false;
        }

        return nums[n-1] - nums[zeros] < 5;
    }
};
