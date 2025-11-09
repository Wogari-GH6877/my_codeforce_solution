user_input = int(input()) +1

while True:
    year=list(str(user_input))
    result=list(set(year))
    if len(year)==len(result):
        print(user_input)
        break
    else:
        user_input+=1

