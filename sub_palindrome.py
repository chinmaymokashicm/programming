def sub_palindrome(a):
    strings = set([])
    for i in range(0, len(a)):
        for j in range(i+1, len(a) + 1):
            # print(a[i:j] + '  ' + str(i) + '  ' + str(j))
            if(palindrome(a[i:j])):
                strings.add(a[i:j])

    print(strings)
    return(len(strings))

def palindrome(a):
    def reverse(a):
        output = ''
        for i in reversed(range(len(a))):
            output = output + a[i]
        return(output)
    
    # Check if a string is palindrome
    if(len(a) % 2 == 0):
        str = a[0:int(len(a)/2)]
        reverse_str = a[int(len(a)/2):]
        if(str == reverse(reverse_str)):
            return(True)
        else:
            return(False)
    else:
        str = a[0:int((len(a) - 1)/2)]
        reverse_str = a[- int((len(a) - 1)/2): ]
        if(str == reverse(reverse_str)):
            return(True)
        else:
            return(False)


# print(palindrome('ababa')) 
print(sub_palindrome('cababac'))
# print(palindrome('cabbac'))
print(sub_palindrome('abaab'))
print(sub_palindrome('abbaeae'))
