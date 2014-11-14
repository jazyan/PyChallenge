# equality

f = open('prob2.in', 'r')
message = f.read()
unique_char = set(message)
curr_min = len(message) + 100
D = {i:message.count(str(i)) for i in unique_char}

ans = ''
for i in unique_char:
    if D[i] == 1:
        ans += i

print ans

