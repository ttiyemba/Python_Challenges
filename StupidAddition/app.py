


def stupid_addition(a,b):

    if(type(a) == int and type(b) == int):
        astr =str(a)
        bstr = str(b)
        return astr+bstr
    elif(type(a) == str and type(b)==str):
        aint = int(a)
        bint=int (b)
        return aint + bint

    else:
        return None;

        
        



   
print(stupid_addition(1,2))

