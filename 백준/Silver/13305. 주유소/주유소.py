#https://www.acmicpc.net/problem/13305

def isMinimumNode(nodes,selectedNode) :
    if min(nodes) == selectedNode :
        return True
    else :
        return False

N = int(input())
distances = list(map(int,input().split()))
nodes = list(map(int,input().split()))
nodes = nodes[0:len(nodes)-2]

result = 0
cnt = 0
for i in range(len(nodes)) :
    if isMinimumNode(nodes,nodes[i]) == True and cnt == 0 :
        for j in range(i,len(distances)) :
            result += nodes[i] * distances[j]
        cnt+=1
        break
    else :
        #("else" ,result)
        result += nodes[i] * distances[i]

print(result)