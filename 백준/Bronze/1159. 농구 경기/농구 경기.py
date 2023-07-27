n = int(input())
alphabet = [0]*26
flag = False

for i in range(n) :
    name = input()
    alphabet[ord(name[0])-97] += 1

for i in range(len(alphabet)):
    if alphabet[i] >= 5 :
        print(chr(i+97),end="")
        flag = True

if flag == False :
    print("PREDAJA")
