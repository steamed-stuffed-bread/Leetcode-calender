class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int diff = 0;
        vector<int> g(3,0);
        vector<int> l(3,0);
        for (int i = 1; i < prices.size(); ++i){
            diff = prices[i] - prices[i-1];
            for (int j = 2; j >= 1; --j) {
                // 1 case: add one transaction, 2 case sell today instead
                l[j] = max(g[j-1] + max(diff,0), l[j] + diff);
                g[j] = max(l[j], g[j]); // there is why from 2 to 1
            }
        }
        return g[2];
    }
};
