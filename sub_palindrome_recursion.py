def palindrome(a):
    i = 0
    j = len(a) - 1
    if(len(a) < 2):
        return(False)
    else:
        while(i < j):
            # print(str(i) + '  ' + str(j))
            if(a[i] != a[j]):
                return(False)
            else:
                i += 1
                j -= 1
        return(True)


def sub_palindrome(a, memo):
    if(a in memo):
        # print(str(memo) + '    ' + a)
        count = 0
        # return(count)
    elif(len(a) < 4):
        if(palindrome(a)):
            # print(a)
            count = 1
            memo.add(a)
        else:
            count = 0
        # return(count)
    else:
        if(palindrome(a)):
            x = 1
            memo.add(a)
        else:
            x = 0

        # print(str(memo) + '    ' + a)
        # part_1 = sub_palindrome(a[0:-1], memo)
        # print('part_1 | sub_palindrome(' + a[0:-1] + ', memo) = ' + str(part_1))
        # part_2 = sub_palindrome(a[1:], memo)
        # print('part_2 | sub_palindrome(' + a[1:] + ', memo) = ' + str(part_2))
        # part_3 = -sub_palindrome(a[1:-1], memo)
        # print('part_3 | -sub_palindrome(' + a[1:-1] + ', memo) = ' + str(part_3))
        # part_4 = x
        # print('x = ' + str(part_4))
        # print('\n')
        # count = part_1 + part_2 + part_3 + part_4
        # print(count)
        # print('\n\n\n')

        count = sub_palindrome(
            a[0:-1], memo) + sub_palindrome(a[1:], memo) + sub_palindrome(a[1:-1], memo) + x
        # print(memo)
    # print(memo)
    # print(count)
    return(count)
    # return(len(memo))


print(sub_palindrome('cababac', set([])))
print(sub_palindrome('abaab', set([])))
print(sub_palindrome('abbaeae', set([])))
print(sub_palindrome('abbabba', set([])))
print(sub_palindrome('acccabbbabcabcaa', set([])))

# def x():
#     a = 'hhhajka'
#     print(a[1:-1])

# x()
