class Solution {
public:
    string minNumber(vector<int>& nums) {
        vector<string> res;
        for (auto n:nums) res.push_back(to_string(n));
        helper(res, 0, res.size()-1);
        string r = "";
        for (auto s:res) r += s;
        return r;
    }

    void helper(vector<string>& nums, int l, int r) {
        if (l >= r) return;
        int i = l, j = r;
        string pivot = nums[l];
        while (i < j) {
            while (i < j && pivot + nums[j] <= nums[j] + pivot) --j;
            nums[i] = nums[j];
            while (i < j && nums[i] + pivot <= pivot + nums[i]) ++i;
            nums[j] = nums[i];
        }
        nums[i] = pivot;
        helper(nums, l, i-1);
        helper(nums, i+1, r);
    }
};
