
# def back_track(empty,nonEmpty):
#     if empty>=3:
#         nonEmpty+=empty//3
#         empty=empty%3
#
result = []
empty = int(input())
while empty!=0:
    nonEmpty=0
    count=0
    while empty>=3:
        nonEmpty+=empty//3
        count+=nonEmpty
        empty=empty%3+nonEmpty
        nonEmpty=0
    if empty==2:
        count+=1
    result.append(count)
    empty = int(input())
for r in result:
    print(r)

