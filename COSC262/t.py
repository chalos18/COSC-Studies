def find_max_length_sequence(S, L, K):
    n = len(S)
    dp = [1] * n  # Initialize all lengths to 1
    
    for i in range(1, n):
        for j in range(i):
            if S[i] > S[j] and L[i] == L[j] + 1 and K[i] >= K[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Reconstruct the sequence
    sequence = []
    for i in range(max_index, -1, -1):
        if dp[i] == max_length and (len(sequence) == 0 or S[i] < sequence[-1]):
            sequence.append(S[i])
            max_length -= 1

    sequence.reverse()
    return sequence

# Given arrays
S = [3, 8, 3, 7, 10, 8, 11, 10, 9]
L = [1, 2, 1, 2, 3, 3, 4, 4, 4]
K = [-1, 1, -1, 1, 2, 4, 5, 6, 6]

# Find and print the maximum length sequence
print("Maximum length sequence:", find_max_length_sequence(S, L, K))
