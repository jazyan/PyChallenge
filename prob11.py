from PIL import Image

im = Image.open('cave.jpg')
pix = im.load()
print(im.size)

for i in range(320):
	for j in range(240):
		p = pix[2*i, 2*j]
		pix[2*i + 1, 2*j] = p
		pix[2*i, 2*j + 1] = p
		pix[2*i + 1, 2*j + 1] = p
		pix[2*i, 2*j] = p

im.save('ans.jpg')