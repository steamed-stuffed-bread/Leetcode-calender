# easy
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        if B in (A+A):
            return True
        else:
            return False
        #for i in range(len(A)):
        #    if A[i:]+A[0:i] == B:
        #        return True
        #return False
