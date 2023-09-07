a,b,c = map(int,input().split())
start = []
end = []

for i in range(3) :
    n1,n2 = map(int,input().split())
    start.append(n1)
    end.append(n2)

cnt = [0 for _ in range(max(end))]

for i in range(3) :
    for j in range(start[i],end[i]) :
        cnt[j] += 1


sum = 0
for i in range(len(cnt)) :
    if cnt[i] == 1 :
        sum += a
    elif cnt[i] == 2 :
        sum += b*2
    elif cnt[i] == 3 :
        sum += c*3

print(sum)