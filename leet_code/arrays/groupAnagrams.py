from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        intermediate = []
        filtered = []

        for i in range(len(strs)):
            sub_list = [strs[i]]
            for j in range(len(strs)):
                if i != j:
                    filt_i, filt_j = sorted(strs[i]), sorted(strs[j])
                    if filt_i == filt_j:
                        sub_list.append(strs[j])
            sub_list.sort()
            intermediate.append(sub_list)
        
        for sublist in intermediate:
            if sublist not in filtered:
                filtered.append(sublist)

        return filtered
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        A = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            A[sorted_word].append(word)

        return list(A.values())

                
