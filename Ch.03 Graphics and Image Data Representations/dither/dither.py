from PIL import Image
img = Image.new(mode = 'RGB', size = (512, 512))
img2 = Image.new(mode = 'RGB', size = (512, 512))
file = open('lena512.raw', 'rb')
data = file.read()
file.close()

pix = img.load()
pix2 = img2.load()

# Dither Matrix
d = ((0, 8, 2, 10),
    (12, 4, 14, 6),
    (3, 11, 1, 9),
    (15, 7, 13, 5))
d2 = ((0, 2),
      (3, 1))

for y in range(512):
    for x in range(512):
        i = x % 4
        j = y % 4
        value = 255 if data[y * 512 + x] > (d[j][i] * 16) else 0
        pix[x, y] = (value, value, value)

for y in range(512):
    for x in range(512):
        i = x % 2
        j = y % 2
        value = 255 if data[y * 512 + x] > (d[j][i] * 16) else 0
        pix2[x, y] = (value, value, value)

img.show()
img2.show()

for i in range(10000000):
    continue

