class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        if (nums.empty()) return {{}};
        vector<vector<int>> res;
        vector<int> out;
        sort(nums.begin(), nums.end());
        helper(nums, res, out, 0);
        return res;
    }
    void helper(vector<int>& nums, vector<vector<int>>& res, vector<int>& out, int start) {
        res.push_back(out);
        for (int i = start; i < nums.size(); ++i){
            out.push_back(nums[i]);
            helper(nums,res,out,i+1);
            out.pop_back();
            while(i+1 < nums.size() && nums[i]== nums[i+1]) i++;  // need to keep the first duplicated number, because other position allow duplicate.
        }
    }
};
