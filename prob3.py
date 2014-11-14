import string, re
f = open('prob3.in')
message = f.read()
f.close()

message = message.replace("\n", "")

r = re.compile("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")
extract = r.findall(message)

print ''.join(extract)
