from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []

        for s in strs:
            key = frozenset(Counter(s).items())

            is_present = hashmap.get(key, -1)

            if is_present == -1:
                hashmap[key] = len(ans)
                ans.append([])

            ans[hashmap[key]].append(s)

        return ans