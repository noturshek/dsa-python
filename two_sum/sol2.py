class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexi, indexj = 0,0
        hashmap = {}
        for i in range(len(nums)):
            left = target - nums[i]
            indexj = hashmap.get(left,-1)
            hashmap[nums[i]] = i
            if indexj != -1:
                indexi = i
                break
        return indexi, indexj

# for i, n in enumerate(nums):is a convenient way to loop through a list while getting both the index and the value.