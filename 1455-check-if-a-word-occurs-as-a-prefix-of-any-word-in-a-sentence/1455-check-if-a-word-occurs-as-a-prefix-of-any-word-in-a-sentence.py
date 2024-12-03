class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        m = len(searchWord)
        list_ = sentence.split()
        for index, word in enumerate(list_):
            if len(word) >= m and searchWord == word[:m]:
                return index + 1  

        return -1 
        