# Neetcode
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
