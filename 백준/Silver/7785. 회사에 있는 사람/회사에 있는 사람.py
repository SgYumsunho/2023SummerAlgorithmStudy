n = int(input())
enter_list = {}
result = []

for i in range(n) :
    name, status = input().split()
    if status == 'enter' :
        enter_list[name] = 1
    elif status == 'leave' :
        enter_list[name] = 0

for name in enter_list :
    if enter_list[name] == 1 :
        result.append(name)

result.sort(reverse = True)

for i in range(len(result)) :
    print(result[i])