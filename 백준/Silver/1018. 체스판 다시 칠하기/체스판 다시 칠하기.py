#https://www.acmicpc.net/problem/1018

N,M = map(int,input().split())
chess = []
for i in range(N) :
    chess.append(input())

num = []
result = []

for i in range(N-7) :
    for j in range(M-7) :
        draw_black = 0
        draw_white = 0
        for k in range(i,i+8) :
            for m in range(j,j+8) :
                if (k+m) % 2 == 0 :
                    if chess[k][m] != 'B' :
                        draw_black += 1
                    if chess[k][m] != 'W' :
                        draw_white += 1
                else :
                    if chess[k][m] != 'W' :
                        draw_black += 1
                    if chess[k][m] != 'B' :
                        draw_white += 1
        result.append(draw_black)
        result.append(draw_white)

print(min(result))

