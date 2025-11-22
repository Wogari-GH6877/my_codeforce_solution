user_input=input()
the_root="hello"
j=0
for i in range(len(user_input)):
    if user_input[i]==the_root[j]:
        j+=1
        if len(the_root)==j:
            break
if len(the_root)==j:
    print("YES")
else:
    print("NO")



