def lcs(s1, s2, cache=None):
    s1_length = len(s1)
    s2_length = len(s2)
    if cache is None:
        cache = [[-1] * (s2_length + 1) for _  in range(s1_length + 1)]
    
    if cache[s1_length][s2_length] != -1:
        return cache[s1_length][s2_length]
    
    if s1 == '' or s2 == '':
        return ''
    elif s1[-1] == s2[-1]: # Last chars match
        result = lcs(s1[:-1], s2[:-1], cache) + s1[-1]
    else:
        soln1 = lcs(s1[:-1], s2, cache)
        soln2 = lcs(s1, s2[:-1], cache)
        if len(soln1) > len(soln2):
            result = soln1
        else:
            result = soln2
    
    cache[s1_length][s2_length] = result
    return result

# A simple test that should run without caching
s1 = "abcde"
s2 = "qbxxd"
lcs_string = lcs(s1, s2)
print(lcs_string)

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))

s1 = "Solidandkeen\nSolidandkeen\nSolidandkeen\n"
s2 = "Whoisn'tsick\nWhoisn'tsick\nWhoisn'tsick"
lcs_string = lcs(s1, s2)
print(lcs_string)
print(repr(lcs_string))