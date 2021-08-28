class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        unordered_map<string, int> m;
        int i = 0, j = 0;
        for (auto s:strs) {
            int len = s.size();
            for (i = 0; i < (1 << len); ++i) {
                string t = "";
                for (j = 0; j < s.size(); ++j) {
                    if ((i >> j)&1) t += s[j];

                    if (m.count(t)) m[t] = m[t] + 1;
                    else m[t] = 1;
                }
            }
        }
        
        int res = -1;
        unordered_map<string, int>::iterator it;
        for (it = m.begin(); it != m.end(); ++it) {
            if (it->second == 1) {
                res = max(res, (int)it->first.size());
            }
        }
        return res;
    }
};
