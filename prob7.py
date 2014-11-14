import Image

im = Image.open("oxygen.png")
pix = im.load()
print im.size

ans = []
for i in range(629):
    ans.append(pix[i, 47][0])

ans = [chr(f) for f in ans]

ans = [ans[i] for i in range(len(ans)) if i % 7 == 0]
print chr(105) + chr(110) + chr(116) + chr(101) + chr(103) + chr(114) + chr(105) + chr(116) + chr(121)
