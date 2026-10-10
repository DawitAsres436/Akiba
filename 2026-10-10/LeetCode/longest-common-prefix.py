class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prefix = ""
        first_word = strs[0]
        last_word = strs[len(strs)-1]
        size = len(min(first_word, last_word))
        
        for i in range (size):
            if first_word[i] == last_word[i]:
                prefix+=first_word[i]
            else:
                return prefix
        return prefix
        