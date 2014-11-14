# map -> ocr

f = open('prob1.in', 'r')
message = f.read()

ans = []
for i in message:
    if ord(i) == 121:
        x = 'a'
    elif ord(i) == 122:
        x = 'b'
    elif ord(i) == 32:
        x = " "
    else:
        x = chr(ord(i) + 2)
    ans.append(x)

print ans

