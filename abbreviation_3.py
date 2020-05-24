import sys
sys.setrecursionlimit(2000)


def update_memo(a, b, memo):
    memo.update([(a, b)])
    return

def eval(a, b, memo):
    if((a, b) in memo):
        status = False
    elif(len(b) == 0):
        if(a.islower() or len(a) == 0):
            status = True
        else:
            status = False
            update_memo(a, b, memo)
    elif(len(a) < len(b)):
        status = False
        update_memo(a, b, memo)
    elif(a[0].isupper()):
        # print(memo)
        if(a[0] == b[0]):
            return(eval(a[1:], b[1:], memo))
        else:
            status = False
            update_memo(a, b, memo)
    else:
        status = eval(a[0].capitalize() + a[1:],
                              b, memo) or eval(a[1:], b, memo)
        # print(memo)
    print(len(memo))
    return(status)


def abbreviation(a, b, memo):
    if(eval(a, b, memo)):
        return("YES")
    else:
        return("NO")

# print("YESSSSSSSSSSSSSS")
# print(abbreviation('aBc','ABC', set([]))) # Yes
# print(abbreviation('AbcDE','ADE', set([]))) # Yes
# print(abbreviation('VLKHNlpsrlrvfxftslslrrh', 'VLKHN', set([])))  # Yes
# print(abbreviation('QYCH','QYCH', set([]))) # Yes
# print(abbreviation('UMKFW','UMKFW', set([]))) # Yes
# print(abbreviation('Pi','P', set([]))) # Yes
# print(abbreviation('beFgH','EFH', set([]))) # Yes

# print("NOOOOOOOOOOO")
# print(abbreviation('KXzQ','K', set([]))) # No
# print(abbreviation('AfPZN','APZNC', set([]))) # No
# print(abbreviation('sYOCa','YOCN', set([]))) # No
# print(abbreviation('LDJAN','LJJM', set([]))) # No
# print(abbreviation('beFgH','EFG', set([]))) # No




print(abbreviation('hHhAhhcahhacaccacccahhchhcHcahaahhchhhchaachcaCchhchcaccccchhhcaahhhhcaacchccCaahhaahachhacaahhaachhhaaaCalhhchaccaAahHcchcazhachhhaaahaahhaacchAahccacahahhcHhccahaachAchahacaahcahacaahcahacaHhccccaahaahacaachcchhahhacchahhhaahcacacachhahchcaAhhcaahchHhhaacHcacahaccccaaahacCHhChchhhahhchcahaaCccccahhcaachhhacaaahcaaaccccaacaaHachaahcchaahhchhhcahahahhcaachhchacahhahahahAahaAcchahaahcaaaaahhChacahcacachacahcchHcaahchhcahaachnachhhhcachchahhhacHhCcaHhhhcaCccccaaahcahacahchahcaachcchaachahhhhhhhhcahhacacCcchahccaaaaaHhhccaAaaaCchahhccaahhacaccchhcahhcahaahhgacahcahhchcaaAccchahhhaahhccaaHcchaccacahHahChachhcaaacAhacacaacacchhchchacchchcacchachacaahachccchhhaccahcacchaccaahaaaccccccaaaaaaaHhcahcchmcHchcchaaahaccchaaachchHahcaccaaccahcacacahAhaacaacaccaccaaacahhhcacAhaCchcaacCcccachhchchcchhchahchchahchchhchcacaachahhccacachaAhaaachchhchchchhaachahaahahachhaaaccacahhcacchhhaaachaaacAahhcachchachhhcacchacaaChCahhhccahChaachhcahacchanaaacchhhccacacchcahccchAcahacaaachhacchachccaaHacaacAhahcCh', 'HAHHCHAACCCAHCHHAHHAHCACCHCCHHCAAHHCACCCAHHHACAAHHHHCHHCAHHAHHAAAHAACAAHAHHCAHAHACHACHCHACACHAAHHAAAHCAHHACACAACHHHCHAHCAHCHHHAHAHACCAAAHCHHCHHCCAACCCCAACHACAACAAHACHCHAHHACCHCAHHHAAACHACAACHCACACAHHCCHAHACCCACCAACHCHHHCCCCCHCCAHHCAAHHAHHHHHHHAACCCCAHCCAAAAAHHHAAAACCAHHCAHACACCHHCHAHAHHCHAACHHHHHCCHCCAHAHCHCAAACCACCCCHACCACHHACHHACACHACCAACCCCAAAAHHAHCHHHCCAHCCHACHHAHCCACACCHAHAAACACCCCAHCCAHACCCCCCHCCHHCHHHHCHCHCAHHHACHAHAACCCAAAACHAACAAAHHAAHAAAHACHHCACHCCHCHAACHACACHHCCCCCAHCACHAAAHCHCAHACAAC', set([])))
