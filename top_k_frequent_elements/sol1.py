class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        sorted_hashmap = dict(sorted(hashmap.items(),key=lambda x:x[1],reverse=True))

        res = list(sorted_hashmap.keys())[:k]

        return res