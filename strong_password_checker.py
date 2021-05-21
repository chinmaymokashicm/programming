"""
A password is considered strong if the below conditions are all met:

> It has at least 6 characters and at most 20 characters.
> It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
> It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

> Insert one character to password,
> Delete one character from password, or
> Replace one character of password with another character.

Example 1
Input: password = "a"
Output: 5

Example 2
Input: password = "aA1"
Output: 3

Example 3
Input: password = "1337C0d3"
Output: 0

https://leetcode.com/problems/strong-password-checker/

iterator = chain(range(97, 123), range(65, 91), range(48, 58))
lists = [list(range(97, 123)), list(range(65, 91)), list(range(48, 58))]

"""
class Solution:
    def __init__(self):
        self.char_index = 0
        self.list_chars = self.generate_char_list()
        # [list(range(97, 123)), list(range(65, 91)), list(range(48, 58))]
        self.list_chars_lower = self.generate_char_list([list(range(97, 123))])
        self.list_chars_upper = self.generate_char_list([list(range(65, 91))])
        self.list_chars_digit = self.generate_char_list([list(range(48, 58))])


    def is_password_strong(self, str_password):
        if(
            len(str_password) in range(6, 21) and 
            any(char.isdigit() for char in str_password) and 
            any(char.isupper() for char in str_password) and
            any(char.islower() for char in str_password)
        ):
            if(any(str_password[i - 1] == str_password[i] == str_password[i + 1] for i in range(1, len(str_password) - 1))):
                return(False)
            return(True)
        return(False)

    def evaluate_password(self, str_password):
        list_indices_triple_repeat =[]
        if(len(str_password) > 2):
            for i in range(1, len(str_password) - 1):
                if(str_password[i - 1] == str_password[i] == str_password[i + 1]):
                    list_indices_triple_repeat.append(i)
        dict_info = {
            "digit": [char for char in str_password if char.isdigit()],
            "upper": [char for char in str_password if char.isupper()],
            "triple_repeat": list_indices_triple_repeat,
            "lower": [char for char in str_password if char.islower()]
        }
        return(dict_info)

    def generate_char_list(self, lists=None):
        if(lists is None):
            lists = [list(range(97, 123)), list(range(65, 91)), list(range(48, 58))]
        list_chars = []
        while(any(len(list_) > 0 for list_ in lists)):
            for list_ in lists:
                try:
                    int_ascii = list_.pop()
                    list_chars.append(chr(int_ascii))
                except Exception:
                    pass
        return(list_chars)

    def get_char_alternatingly(self):
        list_chars = self.list_chars
        if(self.char_index >= len(list_chars)):
            self.char_index = 0
        char_current = list_chars[self.char_index]
        self.char_index += 1
        return(char_current)

    def replace_char(self, string, int_index, char=None):
        if(char is None):
            try:
                char = [char for char in self.list_chars if char not in [string[int_index-1], string[int_index+1]]][0]
            except Exception:
                char = [char for char in self.list_chars if char != string[int_index-1]][0]
        return(string[:int_index] + char + string[int_index + 1:])
    
    def delete_char(self, string, int_index):
        return(string[:int_index] + string[int_index + 1:])
    
    def add_char(self, string, int_index, char=None):
        if(char is None):
            dict_string_info = self.evaluate_password(string)
            if(dict_string_info["digit"] == []):
                char = "0"
            elif(dict_string_info["lower"] == []):
                char = "a"
            else:
                char = "A"
            if(char is None):
                char = [char for char in self.list_chars if char not in [string[i-1], string[i+1]]][0]
        return(string[:int_index] + char + string[int_index:])

    def strongPasswordChecker_0(self, str_password, int_current_index=0):
        if(len(str_password) < 6):
            if(not any(char.isdigit() for char in str_password)):
                # No number found, so add a number
                return(self.strongPasswordChecker_0(str_password + "0") + 1)
            elif(not any(char.isupper() for char in str_password)):
                # No upper found, so add an upper
                return(self.strongPasswordChecker_0(str_password + "A") + 1)
            elif(not any(char.islower() for char in str_password)):
                # No lower found, so add a lower
                return(self.strongPasswordChecker_0(str_password + "a") + 1)
            if(self.is_password_strong(str_password)):
                return(0)
            else:
                return(self.strongPasswordChecker_0(str_password + self.get_char_alternatingly()) + 1)
        elif(len(str_password) in range(6, 20)):
            # Check if we get strong password
            if(self.is_password_strong(str_password)):
                return(0)

            # If not, check if we get it by removing any character
            if(any(self.is_password_strong(str_password[:i] + str_password[i+1:]) for i in range(len(str_password)))):
                return(1)

            # (IGNORE) Check if triple repeat is found. If yes, remove one by one and keep checking for strong password

            # If not, add char of type missing
            if(not any(char.isdigit() for char in str_password)):
                # Replace all characters with integer one by one and see if the password becomes strong
                if(any(self.is_password_strong(str_password[:i] + "0" + str_password[i+1:]) for i in range(len(str_password)))):
                    return(1)
                try:
                    return(
                        min(
                            [
                                self.strongPasswordChecker_0(str_password[:i] + "0" + str_password[i+1:], int_current_index + 1) + 1 for
                                i in range(int_current_index, len(str_password))
                            ] +
                            [
                                self.strongPasswordChecker_0(str_password[:i] + "0" + str_password[i:], int_current_index + 1) + 1 for
                                i in range(int_current_index, len(str_password))
                            ]
                        )
                    )
                except Exception:
                    return(99999)
            elif(not any(char.isupper() for char in str_password)):
                # Replace all characters with upper one by one and see if the password becomes strong
                if(any(self.is_password_strong(str_password[:i] + "A" + str_password[i+1:]) for i in range(len(str_password)))):
                    return(1)
                try:
                    return(
                        min(
                            [
                                self.strongPasswordChecker_0(str_password[:i] + "A" + str_password[i+1:], int_current_index + 1) + 1 for
                                i in range(int_current_index, len(str_password))
                            ] +
                            [
                                self.strongPasswordChecker_0(str_password[:i] + "A" + str_password[i:], int_current_index + 1) + 1 for
                                i in range(int_current_index, len(str_password))
                            ]
                        )
                    )
                except Exception:
                    return(99999)
            elif(not any(char.islower() for char in str_password)):
                # Replace all characters with lower one by one and see if the password becomes strong
                if(any(self.is_password_strong(str_password[:i] + "a" + str_password[i+1:]) for i in range(len(str_password)))):
                    return(1)
                try:
                    return(
                        min(
                            [
                                self.strongPasswordChecker_0(str_password[:i] + "a" + str_password[i+1:], int_current_index + 1) + 1 for
                                i in range(int_current_index, len(str_password))
                            ] +
                            [
                                self.strongPasswordChecker_0(str_password[:i] + "a" + str_password[i:], int_current_index + 1) + 1 for
                                i in range(int_current_index, len(str_password))
                            ]
                        )
                    )
                except Exception:
                    return(99999)
            if(self.is_password_strong(str_password)):
                return(0)

            # If not, add char alternatingly
            else:
                return(self.strongPasswordChecker_0(str_password + self.get_char_alternatingly()) + 1)
        else:
            return(99999)
            # Remove char having type of highest frequency
            dict_string_info = self.evaluate_password(str_password)
            [list_index_digit, list_index_upper, list_index_lower] = [dict_string_info["digit"], dict_string_info["upper"], dict_string_info["lower"]]
            int_max_frequency = max([len(list_) for list_ in [list_index_digit, list_index_upper, list_index_lower]])
            # Remove one at a time and check
            if(int_max_frequency == len(list_index_digit)):
                if(any(self.is_password_strong(str_password[:i] + str_password[i+1:]) for i in list_index_digit)):
                    return(1)
            elif(int_max_frequency == len(list_index_upper)):
                if(any(self.is_password_strong(str_password[:i] + str_password[i+1:]) for i in list_index_upper)):
                    return(1)
            elif(int_max_frequency == len(list_index_lower)):
                if(any(self.is_password_strong(str_password[:i] + str_password[i+1:]) for i in list_index_lower)):
                    return(1)
            else:
                return(
                    min(
                        [
                            self.strongPasswordChecker_0(str_password[:i] + str_password[i+1:]) + 1 for
                            i in range(len(str_password))
                        ]
                    )
                )  

    def strongPasswordChecker(self, str_password):
        if(len(str_password) == 0):
            return(99999)
        if(self.is_password_strong(str_password)):
            return(0)
        if(len(self.evaluate_password(str_password)["triple_repeat"]) > 0):
            if(len(str_password) < 6):
                int_index_first = self.evaluate_password(str_password)["triple_repeat"]
                if(any(self.is_password_strong(self.replace_char(str_password, i)) for i in [int_index_first - 1, int_index_first, int_index_first + 1])):
                    return(1)
                elif(any(self.is_password_strong(self.add_char(str_password, i)) for i in [int_index_first - 1, int_index_first, int_index_first + 1])):
                    return(1)
                # Add and Replace
                return(
                    min(
                        [
                            self.strongPasswordChecker(self.replace_char(str_password, i)) for i in [int_index_first - 1, int_index_first, int_index_first + 1]
                        ] + 
                        [
                            self.strongPasswordChecker(self.add_char(str_password, i)) for i in [int_index_first - 1, int_index_first, int_index_first + 1]
                        ]
                    )
                )
            elif(len(str_password) in range(6, 21)):
                if(len(str_password) != 6):
                    
                    if(any(self.is_password_strong(self.replace_char(str_password, i)) for i in range(len(str_password)))):
                        return(1)
                    elif(any(self.is_password_strong(self.add_char(str_password, i)) for i in range(len(str_password)))):
                        return(1)
                    elif(any(self.is_password_strong(self.delete_char(str_password, i)) for i in range(len(str_password)))):
                        return(1)
                    return(
                        min(
                            [
                                self.strongPasswordChecker(self.replace_char(str_password, i)) for i in range(len(str_password))
                            ] + 
                            [
                                self.strongPasswordChecker(self.add_char(str_password, i)) for i in range(len(str_password))
                            ] +
                            [
                                self.strongPasswordChecker(self.delete_char(str_password, i)) for i in range(len(str_password))
                            ]
                        )
                    )
                else:
                    if(any(self.is_password_strong(self.replace_char(str_password, i)) for i in range(len(str_password)))):
                        return(1)
                    elif(any(self.is_password_strong(self.add_char(str_password, i)) for i in range(len(str_password)))):
                        return(1)
                    # Add and Replace
                    return(
                        min(
                            [
                                self.strongPasswordChecker(self.replace_char(str_password, i)) for i in range(len(str_password))
                            ] + 
                            [
                                self.strongPasswordChecker(self.add_char(str_password, i)) for i in range(len(str_password))
                            ]
                        )
                    )
            else:
                return(99999)

if __name__ == "__main__":
    str_password = "AAbbbz12345"
    str_password = "a"
    str_password = "aA1"
    str_password = "1337C0d3"
    str_password = "aaa123"
    str_password = "aaa111"
    str_password = "1111111111"
    password_obj = Solution()
    # print(password_obj.is_password_strong(password))
    # print(password_obj.evaluate_password(password))
    print(password_obj.strongPasswordChecker(str_password))
    # print(password_obj.list_chars)
