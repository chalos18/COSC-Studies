def lcs(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    
    # Create a 2D array to store lengths of longest common subsequence.
    cache = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]
    
    # Fill the cache using the bottom-up approach
    for i in range(1, s1_length + 1):
        for j in range(1, s2_length + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    
    # Reconstruct the LCS from the cache
    i, j = s1_length, s2_length
    lcs_str = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif cache[i - 1][j] > cache[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_str))

# A simple test that should run without caching
s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))

s1 = 1500 * 'x'
s2 = 1500 * 'y'
print(lcs(s1, s2))