m,n = map(int, input().split())

dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
        '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

result = []

for i in range(m, n+1) :
    1
    string = ' '.join([dict[j] for j in str(i)]) # dict[str(i)[0]], dict[[str(i)[1]]
    result.append([i, string])
    #print(string)
    #2
    # string = ""
    # for j in str(i) :
    #     string += dict[j]
    #     string += ' '
    # print(string)

result.sort(key=lambda x:x[1])

for i in range(len(result)) :
    if i%10 == 0 and i!= 0 :
        print()
    print(result[i][0], end = " ")