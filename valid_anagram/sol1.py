class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temps = ''.join(sorted(s))
        tempt = ''.join(sorted(t))
        return temps == tempt