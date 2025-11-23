# num=int(input())
# room=0
#
# for i in range(num):
#     a,b=map(int,input().split())
#
#     if (a==0 and b>=2) or (b-a>=2):
#         room=i+1
#
#
# if room==0:
#     print(0)
# else:
#     print(room)

n = int(input())
count = 0

for _ in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        count += 1

print(count)
