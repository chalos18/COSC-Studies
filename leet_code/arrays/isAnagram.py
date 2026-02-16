# 1
def isAnagram(s: str, t: str) -> bool:
    # return Counter(s) == Counter(t) -> This is the same as below
    hash_count_s, hash_count_t = {}, {}

    for char in s:
        if char not in hash_count_s:
            hash_count_s[char] = 1
        else:
            hash_count_s[char] += 1

    for char in t:
        if char not in hash_count_t:
            hash_count_t[char] = 1
        else:
            hash_count_t[char] += 1

    return hash_count_s == hash_count_t

#2
def isAnagram(s: str, t: str) -> bool:
    s_split = list(s)
    s_split.sort()
    
    t_split = list(t)
    t_split.sort()

    return s_split == t_split

# Neetcode solution
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Neetcode solution
def isAnagram(s: str, t: str) -> bool:
    dic_s, dic_t = {}, {}
    
    for i in range(len(s)):
        dic_s[s[i]] = 1 + dic_s.get(s[i], 0)

    for i in range(len(t)):
        dic_t[t[i]] = 1 + dic_t.get(t[i], 0)

    return dic_s == dic_t