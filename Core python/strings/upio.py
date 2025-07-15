print("enter the string")
str = input()
i = 0
newstr = ""
while(i <= len(str)-1):
    data = str[i]
    ascii = ord(data)
    if(ascii >= 97 and ascii <= 122):
        newascii = ascii - 32
        convchar = chr(newascii)
        newstr = newstr + convchar
    else:
        newstr = newstr + data
    i = i+1
print(newstr)


        