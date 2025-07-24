
def convertCase(str):
    resStr=""
    arr = str.split(" ")
    print(arr)
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
       print(x[1:2])
    return resStr


print(convertCase('abdc'))