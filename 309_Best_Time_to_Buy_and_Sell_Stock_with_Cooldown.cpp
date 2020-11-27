class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int pre_buy = 0, buy = INT_MIN;
        int pre_sell = 0, sell = 0;
        for (auto p:prices){
            pre_buy = buy;
            buy = max(pre_sell - p, pre_buy);
            pre_sell = sell;
            sell = max(pre_sell, pre_buy + p);
        }
        return sell;
    }
};
