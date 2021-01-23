/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int res = 0, tmp = 0, i = 0;
        for (i = 0; i <= n/4; ++i) {
            tmp = read4(buf+res);
            if (tmp == 0) break;
            res += tmp;
        }
        
        return min(res, n);
    }
};
