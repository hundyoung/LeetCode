digits = "23"
digitMap = {}
# print(ord("A"))
index = ord("a")
end = ord("z")
for i in range(2,10):
    letters = []
    end = 3
    if i==7 or i== 9:
        end=4
    for j in range(0,end):
        letters.append(chr(index+j))
    index+=end
    digitMap[i]=letters
print(digitMap)
result = []
preResult = []
if len(digits)<1:
    # return []
    print([])
firstDigit = digits[0]
firstStrs = digitMap[int(firstDigit)]
# BFS！！！！！
for digitChar in firstStrs:
    result.append(digitChar)
for i in range(1,len(digits)):
    chars = digitMap[int(digits[i])]
    preResult = list(result)
    result=[]
    while len(preResult)>0:
        topResult = preResult.pop(0)
        for digitChar in chars:
            copiedTopResult = topResult
            copiedTopResult+=digitChar
            result.append(copiedTopResult)
print(result)