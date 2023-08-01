#https://www.acmicpc.net/problem/13975
# 문제를 해결하고 최소비용을 출력해주는 함수
import sys
import heapq

def solve(file) :
    sum = 0
    temp = 0
    while True :
        #print("file" , file)
        temp = 0
        f = heapq.heappop(file)
        s = heapq.heappop(file)
        sum += (f+s)
        #print("sum : ",sum)
        # file.pop(0)
        # file.pop(0)
        heapq.heappush(file,(f+s))
        if len(file) == 2 :
            return sum + file[0] + file[1]

result = []
testcase = int(sys.stdin.readline())

for i in range(testcase) :
    num_file = int(sys.stdin.readline())
    file_size = list(map(int,sys.stdin.readline().split()))
    heapq.heapify(file_size)
    sum = solve(file_size)
    result.append(sum)

for item in result :
    print(item)



