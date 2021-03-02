#Add 'ing' to the end of the given string.if it already ends with 'ing',then add 'ly',
def add_ing(str):
    length=len(str)
    if length>3:
        if str[-3:]=='ing':
            str+='ly'
        else:
            str+='ing'
    return str            
print(add_ing('calling'))
