class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return not (len(unique) == len(nums))