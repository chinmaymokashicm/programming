def abbreviation(a, b):
    # status = False
    def eval(a,b,memo):
        # print(memo)
        if((a,b) in memo):
            status = False
            print((a,b))
            return(status)
        elif(len(b) == 0):
            # Check if all remaining characters in a are lowercase
            if(a.islower() or len(a) == 0):
                status = True
            else:
                status = False
                memo.add((a,b))
            return(status)
        elif(len(a) < len(b)):
            status = False
            memo.add((a,b))
            return(status)
        elif(a[0].isupper()):
            if(a[0] == b[0]):
                # print("Yayyy  " + a + '   ' + b)
                return(eval(a[1:], b[1:], memo))
            else:
                status = False
                memo.add((a,b))
                return(status)
        else:
            # print(a + '    ' + b + '    ' + a[0].capitalize() + a[1:])
            status = eval(a[1:], b, memo) or eval(a[0].capitalize() + a[1:], b, memo)
            # return(eval(a[1:], b))
        print(memo)
        return(status)
    
    memo = set([])
    result = eval(a,b,memo)
    if(result):
        return("YES")
    else:
        return("NO")

print("YESSSSSSSSSSSSSS")

# print(abbreviation('aBc','ABC')) # Yes
# print(abbreviation('AbcDE','ADE')) # Yes 
print(abbreviation('VLKHNlpsrlrvfxftslslrrh','VLKHN')) # Yes
# print(abbreviation('QYCH','QYCH')) # Yes
# print(abbreviation('UMKFW','UMKFW')) # Yes
# print(abbreviation('Pi','P')) # Yes
# print(abbreviation('beFgH','EFH')) # Yes

# print("NOOOOOOOOOOO")
# print(abbreviation('KXzQ','K')) # No
# print(abbreviation('AfPZN','APZNC')) # No
# print(abbreviation('sYOCa','YOCN')) # No
# print(abbreviation('LDJAN','LJJM')) # No
# print(abbreviation('beFgH','EFG')) # No 