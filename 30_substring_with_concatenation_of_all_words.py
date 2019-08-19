# hard
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0:
            return []
        res = []
        m1 = {}
        for w in words:
            if not w in m1.keys():
                m1[w] = 1
            else:
                m1[w] = m1[w] + 1
        l = len(words[0])
        cnt = len(words)
        count = 0
        left = 0
        for i in range(l):
            left = i
            count = 0
            m2 = {}
            for j in range(i, len(s)-l+1, l):
                temp = s[j:(j+l)]
                if temp in m1.keys():
                    if not temp in m2.keys():
                        m2[temp] = 0
                    m2[temp] = m2[temp] + 1
                    if m2[temp] <= m1[temp]:
                        count = count + 1
                    else:
                        while m2[temp] > m1[temp]:
                            s1 = s[left:(left+l)]
                            m2[s1] = m2[s1] - 1
                            if m2[s1] < m1[s1]:
                                count = count - 1
                            left = left + l
                    if count == cnt:
                        res.append(left)
                        st = s[left:(left+l)]
                        m2[st] = m2[st] - 1
                        count = count - 1
                        left = left + l
                else:
                    m2 = {}
                    count = 0
                    left = j + l            
        return res
