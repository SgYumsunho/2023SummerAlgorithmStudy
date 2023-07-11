n = float(input())
k = list(map(int, input().split())) #에너지 드링크 양을 k 리스트에 저장

k.sort(reverse = True) #에너지 드링크 양 내림차순으로 정렬

result = 0
count = 1
for i in k:
    if count == 1: #첫번째 에너지 드링크는 그대로 result 값에 넣어준다
        count += 1
        result += i
        continue
    else:
        result += (i/2) #두번째 에너지드링크부터 쭉 각 원소를 절반으로 나누어 result에 추가해준다. 
print(result)