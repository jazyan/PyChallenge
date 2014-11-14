import Image

im = Image.open("oxygen.png")
pix = im.load()
print im.size

ans = []
for i in range(629):
    ans.append(pix[i, 47][0])

ans = [chr(f) for f in ans]
new = []

for i in range(2, len(ans)-1):
    if ans[i-1] != ans[i] and ans[i-1] != ans[i + 1]:
        new.append(ans[i-1])

print ''.join(new)

print chr(105) + chr(110) + chr(116) + chr(101) + chr(103) + chr(114) + chr(105) + chr(116) + chr(121)
