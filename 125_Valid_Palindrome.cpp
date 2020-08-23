class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() == 0) return true;
        int left = 0, right = s.size()-1;
        while(left < right) {
            if(!isvalid(s[left])) ++left;
            else if (!isvalid(s[right])) --right;
            else if ((s[left] + 32 - 'a') % 32 != (s[right] + 32 - 'a') % 32)
                return false;
            else {
                ++left; --right;
            }
        }
        return true;
    }
    
    bool isvalid(char& c){
        if (c >= 'a' && c <= 'z') return true;
        if (c >= 'A' && c <= 'Z') return true;
        if (c >= '0' && c <= '9') return true;
        return false;
    }
};
