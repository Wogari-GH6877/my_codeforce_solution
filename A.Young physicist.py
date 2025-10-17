#A.Young physicist
num_rows=int(input())
num=[]

for i in range(num_rows):
    nums=list(map(int,input().split()))
    num+=nums
print("YES" if sum(num)==0 else "NO")