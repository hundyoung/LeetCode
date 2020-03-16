t = int(input())
result = []
for i in range(t):
    n = int(input())
    nums = list(map(lambda x:int(x),input().split()))
    if n<=3:
        result.append(False)
    if n>3:
        if min(nums)==1:
            result.append(True)
        else:
            pass
for r in result:
    if r:
        print('Yes')
    else:
        print('No')