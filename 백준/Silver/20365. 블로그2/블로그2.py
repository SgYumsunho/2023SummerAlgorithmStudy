#https://www.acmicpc.net/problem/20365

n = int(input())
data = input()

color = data[0]
cnt = 1

#연속적으로 처음과 다른색이 나오는 예외상황을 처리해야함
data = data.split(color)
result = []
for x in data :
    if x != '' :
        result.append(x)

cnt += len(result)

print(cnt)