#https://www.acmicpc.net/problem/10448
def find(n,triangle) :
    for i in range(len(triangle)) :
        for j in range(i,len(triangle)) :
            for k in range(j,len(triangle)) :
                if triangle[i] + triangle[j] + triangle[k] == n :
                    return 1
    return 0

triangle = []
for i in range(1,100) :
    triangle.append(int((i*(i+1)/2)))

n = int(input())
data = []
for i in range(n) :
    data.append(int(input()))

for k in range(len(data)) :
    print(find(data[k],triangle))