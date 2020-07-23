class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int red = 0, blue = n-1;
        for (int i = 0; i <= blue; i++) {
            if(nums[i] == 0) {
                swap(nums[red++], nums[i]);
            } else if (nums[i] == 2) {
                swap(nums[i--], nums[blue--]); // rescan the number at i
            }
        }
    }
};
