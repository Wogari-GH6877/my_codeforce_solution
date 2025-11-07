maxs=0
current=0
num=int(input())

for i in range(num):
    inp=list(map(int,input().split()))
    current-=inp[0]
    current+=inp[1]
    if maxs < current:
        maxs=current
print(maxs)