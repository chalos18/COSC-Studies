from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        # Sorted in descending order
        count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
        # Option 2: Leave it sorted in ascending order
        # count_sorted = sorted(count.items(), key=lambda x: x[1])

        # Slice the first k numbers of the list
        top_k = [x[0] for x in count_sorted[:k]]
        # Option 2: using -k: slices the last k numbers of the list
        # top_k = [x[0] for x in count_sorted[-k:]]
        
        return top_k
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append()
                if len(res) == k:
                    return res