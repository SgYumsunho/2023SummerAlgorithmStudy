n = int(input())
d1 = list(map(int,input().split()))
d1.sort()
m = int(input())
d2 = list(map(int,input().split()))

def bs(target, data) :
    left, right = 0,n-1
    while left <= right :
        mid = (left + right) // 2
        if data[mid] == target :
            return True
        elif data[mid] < target :
            left = mid + 1
        else :
            right = mid -1

    return False

for i in range(len(d2)) :
    a = bs(d2[i],d1)
    if a == True :
        print(1)
    else :
        print(0)