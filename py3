class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        f1, f2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            f1[ord(s1[i]) - ord('a')] += 1
            f2[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s1), len(s2)):
            if f1 == f2: return True
            f2[ord(s2[i]) - ord('a')] += 1
            f2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        return f1 == f2
