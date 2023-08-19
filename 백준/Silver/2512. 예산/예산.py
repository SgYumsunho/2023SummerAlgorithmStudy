N = int(input())
budget = list(map(int, input().split()))
limit = int(input())

start, end = 0, max(budget)
total_budget = 0

if sum(budget) <= limit:
    print(max(budget))
else:
    while start <= end:
        mid = (start+end) // 2
        total_budget = 0
        for i in budget:
            total_budget += min(mid, i)

        if total_budget <= limit :
            start = mid + 1
        else :
            end = mid -1
    print(end)