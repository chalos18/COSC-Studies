def longestConsecutive(nums: list[int]) -> int:
    non_dup = sorted(set(nums))
    longest = 1
    length = 1
    prev = None

    if len(nums) == 0:
        return 0
    
    for i in range(len(non_dup)):
        if prev == None:
            prev = non_dup[i]
        else:
            next_n = prev + 1
            if non_dup[i] == next_n:
                length+=1
            else:
                length = 1
            if length > longest:
                longest = length
            prev = non_dup[i]
                    
    return longest

nums = [2,20,4,10,3,4,5]
nums = [0,3,2,5,4,6,1,1]
nums=[0]
nums=[100,4,200,1,3,2]
nums=[9,1,4,7,3,-1,0,5,8,-1,6]

print(longestConsecutive(nums))