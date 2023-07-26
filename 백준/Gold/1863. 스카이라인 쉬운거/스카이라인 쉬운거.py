#https://www.acmicpc.net/problem/1863

n = int(input())
building = [0]
answer = 0
for _ in range(n) :
    x, cur_h = map(int,input().split())

    if cur_h > building[-1] :
        answer += 1
        building.append(cur_h)
    else:
        while building[-1] > cur_h :
            building.pop()

        if building[-1] < cur_h :
            answer += 1
            building.append(cur_h)

print(answer)
