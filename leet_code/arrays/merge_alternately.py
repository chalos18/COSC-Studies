def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    i, j = 0, 0
    merged_list = []

    while i < len(word1) and j < len(word2):
        merged_list.append(word1[i])
        merged_list.append(word2[j])
        i += 1
        j += 1
    merged_list.append(word1[i:])
    merged_list.append(word2[j:])
    # print(merged_list)
    return "".join(merged_list)


# word1 = "abc"
# word2 = "pqr"

word1 = "ab"
word2 = "pqrs"

# word1 = "abcd"
# word2 = "pq"

# result = mergeAlternately(word1, word2)
# print(result)

# assert result == "apbqcr"
# assert result == "apbqrs"
# assert result == "apbqcd"
