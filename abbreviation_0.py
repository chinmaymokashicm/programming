def abbreviation(a, b):
    status = False
    if(len(a) >= len(b)):
        if(len(b) == 1 ):
            # print("THE END   " + a + "  "+ b)
            if(a[0] == b or a[0].upper() == b):
                for char in a[1:]:
                    if(char.isupper()):
                        return("NO")
                return("YES")
            else:
                return(False)
        elif(a[0].isupper()):
            if(a[0] != b[0]):
                # print("Caps but unequal first char   " + a + "  "+ b)
                return(False)
            else:
                # print("Caps and equal first char   " + a + "  "+ b)
                status = status or abbreviation(a[1:], b[1:])
        elif(a[0].islower()):
            # print("HERE", end=" ")
            # print(a, end="  ")
            # print(b)
            status = status or abbreviation(a[1:], b) or abbreviation(a.capitalize(), b)
            # print(status)
        
    else:
        # print("Something went wrong   " + a + "  "+ b)
        return(False)
    # return(status)
    if(status):
        return("YES")
    else:
        return("NO")


print(abbreviation('aBc','ABC')) # Yes
print(abbreviation('AbcDE','ADE')) # Yes 
print(abbreviation('VLKHNlpsrlrvfxftslslrrh','VLKHN')) # Yes
print(abbreviation('KXzQ','K')) # No
print(abbreviation('AfPZN','APZNC')) # No
print(abbreviation('sYOCa','YOCN')) # No
print(abbreviation('QYCH','QYCH')) # Yes
print(abbreviation('LDJAN','LJJM')) # No
print(abbreviation('UMKFW','UMKFW')) # Yes

# print(type(abbreviation('LDJAN','LJJM')))
print(abbreviation('Pi','P'))
