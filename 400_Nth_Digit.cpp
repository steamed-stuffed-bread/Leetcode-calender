class Solution {
public:
    int findNthDigit(int n) {
        long start = 1, cnt = 9, sum = 0, len = 1;
        while (len * cnt < n) {
            n -= len*cnt;
            cnt *= 10;
            start *= 10;
            len += 1;
        }
        start = start + (n-1)/len;
        string t = to_string(start);
        return t[(n-1)%len] - '0';
    }
};
