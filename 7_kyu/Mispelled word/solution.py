def mispelled(word1, word2):
    if word1 == word2:
        return True
    if not word1 and word2 or word1 and not word2:
        return False
    count = 0
    if len(word1) != len(word2):
        if max(len(word1), len(word2)) - min(len(word1), len(word2)) == 1:
            if (
                word1.startswith(word2)
                or word1.endswith(word2)
                or word2.startswith(word1)
                or word2.endswith(word1)
            ):
                return True
        else:
            return False
    for i in range(len(word1)):
        if count > 1:
            return False
        if word1[i] != word2[i]:
            count += 1
    return False if count > 1 else True
