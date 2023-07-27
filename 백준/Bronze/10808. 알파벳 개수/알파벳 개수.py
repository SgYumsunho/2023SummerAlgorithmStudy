string = input()
alphabet = [0]*26

for i in range(len(string)) :
    t = ord(string[i]) - 97
    alphabet[t] += 1

for i in alphabet :
    print(i, end= " ")