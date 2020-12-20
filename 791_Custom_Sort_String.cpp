class Solution {
public:
    string customSortString(string S, string T) {
        unordered_map <char, int> m;
        string res = "";
        for (auto c:T) ++m[c];
        
        for (auto c:S) {
            res += string(m[c], c);
            m[c] = 0;
        }
        
        for (auto a:m) {
            res += string(a.second, a.first);
        }
        return res;
    }
};
