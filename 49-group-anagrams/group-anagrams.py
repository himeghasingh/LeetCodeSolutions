class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # wordSet = set()
        anaMap = defaultdict(list)
        # for word in strs:
        #     wordSet.add(''.join(sorted(word)))
        # print(wordSet)
        for word in strs:
            anaMap[''.join(sorted(word))].append(word)
        result = []
        print(anaMap)
        for val in anaMap.values():
            result.append(val)
        print(result)
        return result
        