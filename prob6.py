import zipfile
import re

num = 90052
i = 0
zf = zipfile.ZipFile('channel.zip', 'r')

ans = ""
while True:
    info = zf.getinfo(str(num)+'.txt')
    data = zf.read(str(num)+'.txt')
    nothings = re.findall(r'\d+', data)
    num = str(nothings[0])
    z = info.comment
    ans += z
    print ans
