n = int(input())

list = []
for i in range(n) :
    x,y = map(int,input().split())
    list.append([x,y])

list.sort(key = lambda x : (x[1], x[0]))

for d in list :
    print(d[0], d[1])
