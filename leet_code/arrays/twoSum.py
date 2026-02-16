class Solution:
    # 1
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        output.append(i)
                        output.append(j)
                        return output
        return []
    
    # Neetcode - minor improvement of the above
    def twoSum(nums: list[int], target: int) -> list[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    