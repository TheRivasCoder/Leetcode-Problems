from collections import deque 
start = "qa"
end = "sq"
test_list = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
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

print(ladderLength(start, end, test_list))