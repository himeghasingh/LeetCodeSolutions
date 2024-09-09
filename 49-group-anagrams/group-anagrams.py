class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for word in strs:
            anaMap[''.join(sorted(word))].append(word)
        result = []
        # for val in anaMap.values():
        #     result.append(val)
        return anaMap.values()
        