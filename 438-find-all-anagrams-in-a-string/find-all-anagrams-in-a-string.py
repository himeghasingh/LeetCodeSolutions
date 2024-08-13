class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)
        if np > ns:
            return []
        pCounter = Counter(p)
        sCounter = Counter()
        res = []

        for i in range(0, ns):
            sCounter[s[i]] += 1
            if i >= np:
                sCounter[s[i-np]] -= 1
                if sCounter[s[i-np]] == 0:
                    del sCounter[s[i-np]]
            if sCounter == pCounter:
                res.append(i - np + 1)

        return res











        # Beats only 7%, not efficient
        # sorted_p = sorted(p)
        # n_p = len(p)
        # n = len(s)
        # res = []
        # for i in range(0, n - n_p + 1):
        #     if sorted(s[i:i+n_p]) == sorted_p:
        #         res.append(i)
        # return res

        