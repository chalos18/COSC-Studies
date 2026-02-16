class Solution:
    # 1
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for i in nums:
            if seen.get(i) == 1:
                return True
            seen[i] = 1
        return False
    
    # Neetcode
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set() # hash set
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
    
    # Neetcode
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))