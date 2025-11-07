num=str(input())
count=0
for i in range(len(num)-1):
    if num[i]==num[i+1]:
        count+=1
        if count>=6:
            break
    else:
        count=0

if count>=6:
    print("YES")
else:
    print("NO")
