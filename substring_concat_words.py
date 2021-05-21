"""
You are given a string s and an array of strings words of the same length. 
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, 
in any order, and without any intervening characters.

You can return the answer in any order.

Example 1
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""

class Solution:
    def get_indices(self, string, list_words, int_start_index):
        def remove_first_occurrence(list_words, string):
            list_words_new = list_words.copy()
            list_words_new.remove(string)
            return(list_words_new)
        if(list_words == []):
            return(int_start_index)
        if(len(string) < len("".join(list_words))):
            return
        int_word_length = len(list_words[0])
        if(string[:int_word_length] in list_words):
            return(
                self.get_indices(
                    string[int_word_length:],
                    remove_first_occurrence(list_words, string[:int_word_length]),
                    int_start_index
                )
            )
        else:
            return

    def findSubstring_recursion(self, string, list_words):
        list_indices = [
                self.get_indices(
                    string[index:],
                    list_words,
                    index
                )
                for index in range(len(string) - len(list_words) * len(list_words[0]) + 1)
            ]
        
        return([index for index in list_indices if index is not None])
    
    def findSubstring(self, string, list_words):
        i = 0
        list_words_copy = list_words.copy()
        list_indices = []
        append = list_indices.append
        remove_index = list_indices.remove
        remove_word = list_words_copy.remove
        while(i < len(string) - len(list_words[0]) * len(list_words) + 1):
            j = i
            list_words_copy = list_words.copy()
            while(len(list_words_copy) != 0):
                word = string[j: j + len(list_words_copy[0])]
                if(word in list_words_copy):
                    list_words_copy.remove(word)
                    if(list_words_copy == []):
                        append(i)
                    # if(i not in list_indices):
                    #     append(i)
                else:
                    # if(i in list_indices):
                    #     remove_index(i)
                    #     pass
                    break
                j += len(list_words[0])
            i += 1
        return(list_indices)
                
    

if __name__ == "__main__":
    string = "barfoofoobarthefoobarman" 
    list_words = ["bar","foo","the"]
    print(Solution().findSubstring(string, list_words))
    print(Solution().findSubstring_recursion(string, list_words))
    string = "wordgoodgoodgoodbestword"
    list_words = ["word","good","best","good"]
    print(Solution().findSubstring(string, list_words))
    print(Solution().findSubstring_recursion(string, list_words))
