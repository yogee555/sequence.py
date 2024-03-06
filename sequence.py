ch='A'
for i in range(1,6):
    for j in range(1,i+1):
        ch = chr(ord(ch) + 1)
        print(ch,end='')
    print("")
