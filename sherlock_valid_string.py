"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. 
Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

For example, if s = abc, it is a valid string because frequencies are {a:1, b:1, c:1}. 
So is s = abcc because we can remove one c and have 1 of each character in the remaining string. 
If  however, the string s = abccc is not valid as we can only remove 1 occurrence of c. 
That would leave character frequencies of {a:1, b:1, c:2}.
"""
"""
Complete the 'isValid' function. Return either 'YES' or 'NO'
"""

def isValid(string):
    unique_chars = list(set(string))
    dict_frequencies = {}
    for char in unique_chars:
        dict_frequencies[char] = string.count(char)
    min_frequency = min(dict_frequencies.values())
    dict_new_frequencies = { key: value - min_frequency for key, value in dict_frequencies.items() }
    unique_values = list(set([value for value in dict_new_frequencies.values()]))
    unique_values.sort()
    if(
        (
            len(unique_values) == 2
            and
            unique_values[0] == 0
            and
            (
                [value for value in dict_new_frequencies.values()].count(unique_values[0]) == 1
                or
                (
                    [value for value in dict_new_frequencies.values()].count(unique_values[1]) == 1
                    and
                    unique_values[1] == 1
                )
            )
        )
        or
        (
            len(unique_values) == 1
        )
        ):
        return('YES')
    else:
        return('NO')
        

print(isValid('aasscca'))
print(isValid('abc'))
print(isValid('abcc'))
print(isValid('abccc'))
print(isValid('aabbcd'))
print(isValid('aabbc'))
print(isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))
print(isValid('aaaabbcc'))