n = int(input())
nums = list(map(int,input().split()))
nums.sort()

result = 0
for i in range(n) :
    left = 0
    right = n-1
    while left < right :
        if left == i :
            left += 1
            continue
        elif right == i :
            right -= 1
            continue
        if nums[left] + nums[right] == nums[i] :
            result += 1
            break
        elif nums[left] + nums[right] > nums[i] :
            right -= 1
        else :
            left += 1


print(result)
