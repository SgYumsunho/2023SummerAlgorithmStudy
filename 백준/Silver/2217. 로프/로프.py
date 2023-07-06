num = int(input())
ropes = []
for i in range(num) :
    ropes.append(int(input()))

ropes.sort(reverse = True)

result = []
for i in range(num) :
    result.append(ropes[i]*(i+1))

print(max(result))

