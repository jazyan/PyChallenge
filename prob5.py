# channel

import pickle

f = open('prob5.in', 'rb')
message = f.read()
ans = pickle.loads(message)

for item in ans:
    print "".join(i[0] * i[1] for i in item)
