
def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    Q = deque([(beginWord, 1)])
    word_set = set(wordList)
    while Q:
        word, length = Q.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                check_word = word[:i]+char+word[i+1:]
                if check_word in word_set:
                    word_set.remove(check_word)
                    Q.append((check_word, length+1))
    return 0