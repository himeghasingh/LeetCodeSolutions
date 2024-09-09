class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        len1 = len(v1)
        len2 = len(v2)
        diff = abs(len1 - len2)
        if len1 > len2:
            v2.extend(['0']*diff)
        elif len2 > len1:
            v1.extend(['0']*diff)
        n = len(v1)
        for i in range(0, n):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                continue
        return 0
        