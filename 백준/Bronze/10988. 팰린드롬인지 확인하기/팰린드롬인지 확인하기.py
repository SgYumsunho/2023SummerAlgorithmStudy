string = input()

if len(string) %2 == 0 :
    for i in range(len(string)//2) :
        if string[i] != string[len(string)-i-1] :
            print(0)
            break
    else :
        print(1)
else :
    for i in range(len(string)//2) :
        if string[i] != string[len(string)-i-1] :
            print(0)
            break
    else :
        print(1)



