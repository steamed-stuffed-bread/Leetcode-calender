class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int res = 1, tmp = 9;
        for (int i = 1; i <= n; ++i) {
            res += tmp;
            tmp *= (9-i+1);
        }
        return res;
    }
};
