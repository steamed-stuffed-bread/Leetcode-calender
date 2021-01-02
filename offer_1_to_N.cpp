class Solution {
public:
    vector<int> printNumbers(int n) {
        if (n <= 0) return {};
        vector<int> res;
        int tmp = 0;
        vector<char> num(n+1, '0');
        while (!incre(num)) {
            tmp = to_num(num);
            res.push_back(tmp);
        }
        return res;
    }

    bool incre(vector<char>& num) {
        int cnt = 0;
        for (int i = num.size()-1; i >= 0; --i) {
            int tmp = num[i] + cnt - '0';
            if (i == num.size()-1) tmp++;

            cnt = tmp/10;
            tmp %= 10;
            num[i] = (char)(tmp + '0');
        }
        return num[0] == '1';
    }

    int to_num(vector<char>& num) {
        int n = num.size();
        int res = 0;
        int i = 0;
        while (num[i] == '0') ++i;
        int cnt = 0;
        for (;i < num.size(); ++i) {
            res = res*10 + (num[i]-'0');
        }
        return res;
    }
};
