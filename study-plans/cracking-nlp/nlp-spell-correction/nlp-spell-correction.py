def spell_correction(misspelled: list, dictionary: list, frequencies: dict) -> list:
    """
    Returns one corrected dictionary word per input word.
    """
    def levenshtein_distance(str1, str2):
        m, n = len(str1), len(str2)
        dp = [list(range(n + 1))] + [[i] + [0] * n for i in range(1, m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]
    
    distances = {}
    correct_words = []
    for miss_word in misspelled:
        distances[miss_word] = []
        for word in dictionary:
            distance = levenshtein_distance(word,miss_word)
            freq = frequencies.get(word,0)
            distances[miss_word].append((distance,-1*freq,word))
        correct_words.append(min(distances[miss_word])[-1])
    return correct_words