class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        if (prices.empty()) return 0;
        int sold = 0, hold = -prices[0];
        for (auto p:prices) {
            int tmp = sold;
            sold = max(sold, hold+p-fee);
            hold = max(hold, tmp-p);
        }
        return sold;
    }
};
