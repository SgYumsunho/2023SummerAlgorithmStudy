#https://www.acmicpc.net/problem/2503

n = int(input())
nums = []
for i in range(100,1000) :
    nums.append(i)

#input 받는부분
for i in range(n) :
    res,ts,tb = map(int,input().split())
    for j in range(len(nums)) :
        ns,nb = 0,0
        tmp = str(nums[j])
        if(tmp == '0') :
            continue
        if ('0' in tmp) or ((tmp[0] == tmp[1] or tmp[0] == tmp[2] or tmp[1] == tmp[2])) :
            nums[j] = 0
        else :
            res = str(res)
            for k in range(3) :
                for l in range(3) :
                    if (tmp[k] == res[l] and k == l) :
                        ns += 1
                    elif(tmp[k] == res[l] and k != l) :
                        nb += 1
            if (ns != ts or nb != tb) :
                nums[j] = 0

print(900 - nums.count(0))

