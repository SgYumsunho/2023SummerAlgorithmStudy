#https://www.acmicpc.net/problem/14889

from itertools import combinations, permutations

n = int(input())
nums = []
for i in range(1,n+1) :
    nums.append(i)
combi = list(combinations(nums,n//2))
data = []
for i in range(n) :
    data.append(list(map(int,input().split())))

stat_x = []
stat_y = []

for i in range(len(combi) // 2) :
    combi_x = list(combinations(combi[i],2))
    #print(combi_x)
    result_x = 0
    for j in range(len(combi_x)) :
        result_x += data[combi_x[j][0]-1][combi_x[j][1]-1]
        result_x += data[combi_x[j][1]-1][combi_x[j][0]-1]
    stat_x.append(result_x)

for i in range(len(combi)-1,len(combi)//2-1,-1) :
    combi_y = list(combinations(combi[i],2))
    #(combi_y)
    result_y = 0
    for j in range(len(combi_y)) :
        result_y += data[combi_y[j][0]-1][combi_y[j][1]-1]
        result_y += data[combi_y[j][1]-1][combi_y[j][0]-1]
    stat_y.append(result_y)

result = []
for i in range(len(stat_x)):
    result.append(abs(stat_x[i] - stat_y[i]))

# print(stat_x)
# print(stat_y)

print(min(result))
#print(combi_x)
#print(stat_x)
#combi i번째와 len(combi)-(i+1)번째가 세트이다.
