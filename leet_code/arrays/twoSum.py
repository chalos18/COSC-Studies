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
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # Neetcode - two pointer solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        
        while i < j:
            current = A[i][0] + A[j][0]
            if current == target:
                return [min(A[i][1], A[j][1]), 
                        max(A[i][1], A[j][1])]
            elif current < target:
                i+=1 
            else:
                j-=1

        return []

    # Neetcode - Hash Map (Two Pass)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                j = prevMap[diff]
                return [min(i, j), max(i, j)]
            prevMap[num] = i
        
        return []
            
