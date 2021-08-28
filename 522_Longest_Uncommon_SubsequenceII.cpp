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

class Solution {
public:
    bool isSubseq(string s1, string s2) {
        int i = 0, j = 0, len = 0;
        for (i = 0; i < s2.size() && j < s1.size(); ++i) {
            if (s1[j] == s2[i]) ++j;
        }
        return j == s1.size();
    }
    
    int findLUSlength(vector<string>& strs) {
        sort(strs.begin(), strs.end(), [](string s1, string s2){return s2.size() < s1.size();});
        for (auto s:strs) {
            cout << s << endl;
        }
        int res = -1;
        int i = 0, j = 0;
        for (i = 0; i < strs.size(); ++i)  {
            bool flag = true;
            for (j = 0; j < strs.size(); ++j) {
                if (i == j) continue;
                if (isSubseq(strs[i], strs[j])) {
                    flag = false;
                    break;
                }
            }
            //if (j == strs.size()) res = max(res, (int)strs[i].size());
            if (flag) return strs[i].size();
        }
        return res;
    }
};
