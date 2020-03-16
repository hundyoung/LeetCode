n,m = input().split()
n=int(n)
m=int(m)

column = []
for i in range(m):
    column.append({})
for row in range(n):
    s = input()
    for c in range(m):
        char = s[c]
        column_dict = column[c]
        column_dict[char]=char
p=1
for i in range(m):
    column_dict = column[i]
    p*=len(column_dict)
print(p%1000000007)
