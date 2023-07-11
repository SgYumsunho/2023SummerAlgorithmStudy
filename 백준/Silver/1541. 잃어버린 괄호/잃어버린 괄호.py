#https://www.acmicpc.net/problem/1541

data = input()

result = 0
if data[0].isnumeric() :
    data = data.split('-')
    k = list(map(int,data[0].split('+')))
    result = sum(k)
    for x in data[1:] :
        result -= sum(list(map(int,x.split('+'))))
if data[0] == '-' :
    data = data[1:].split('-')
    k = list(map(int,data[0].split('+')))
    result = sum(k)
    result *= -1
    for x in data[1:] :
        result -= sum(list(map(int,x.split('+'))))

print(result)
