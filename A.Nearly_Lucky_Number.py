num=str(input())
lucky=0

for i in num:
    if i in "47":
        lucky+=1
if str(lucky) in "47" :
    print("YES")
else:
    print("NO")
