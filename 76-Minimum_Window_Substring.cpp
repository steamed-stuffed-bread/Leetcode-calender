class Solution {
public:
    string minWindow(string s, string t) {
        string res = "";
        unordered_map<char, int> m;
        for (int i = 0; i < t.size(); ++i) ++m[t[i]];
        int cnt = 0, left = 0, minlen = INT_MAX;
        for (int i = 0; i < s.size(); ++i) {
            if (--m[s[i]] >= 0) ++cnt;
            while (cnt == t.size()) {
                if (minlen > i - left + 1) {
                    minlen = i-left+1;
                    res = s.substr(left, minlen);
                }
                if (++m[s[left]] > 0) --cnt;
                ++left;
            }
        }
        return res;
    }
};
