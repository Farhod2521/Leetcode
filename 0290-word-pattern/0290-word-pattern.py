class Solution(object):
    def wordPattern(self, pattern, s):
        word =  s.split()
        if len(pattern) != len(word):
            return False
        pattern_to_word =  {}
        word_to_pattern =  {}
        
        for p, w in zip(pattern, word):
            if p in pattern_to_word:
                if pattern_to_word[p] != w:
                    return False
            
            else:
                if w in word_to_pattern:
                    return False
                
            pattern_to_word[p] = w
            word_to_pattern[w] = w
            
        return True

