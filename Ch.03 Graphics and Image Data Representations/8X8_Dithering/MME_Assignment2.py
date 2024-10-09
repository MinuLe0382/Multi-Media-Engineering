from PIL import Image

# Dither Matrix
d1 = ((0, 2),
      (3, 1))

d2 = ((0, 8, 2, 10),
    (12, 4, 14, 6),
    (3, 11, 1, 9),
    (15, 7, 13, 5))
d3 = ((0, 32, 8, 40, 2, 34, 10, 42),
      (48, 16, 56, 24, 50, 18, 58, 26),
      (12, 44, 4, 36, 14, 46, 6, 38),
      (60, 28, 52, 20, 62, 30, 54, 22),
      (3, 35, 11, 43, 1, 33, 9, 41),
      (51, 19, 59, 27, 49, 17, 57, 25),
      (15, 47, 7, 39, 13, 45, 5, 37),
      (63, 31, 55, 23, 61, 29, 53, 21),)

file = open('lena512.raw', 'rb')
data = file.read()
file.close()

Dithered_img_2X2 = Image.new(mode='1', size=(512, 512))
Dithered_img_4X4 = Image.new(mode='1', size=(512, 512))

Dithered_2X2_pix = Dithered_img_2X2.load()
Dithered_4X4_pix = Dithered_img_4X4.load()

for y in range(Dithered_img_2X2.height):
    for x in range(Dithered_img_2X2.width):
        i = x % 4
        j = y % 4
        if data[y * Dithered_img_2X2.width + x] > (256 // 16) * d2[j][i]:
            Dithered_2X2_pix[x, y] = 1
        else:
            Dithered_2X2_pix[x, y] = 0

for y in range(Dithered_img_4X4.height):
    for x in range(Dithered_img_4X4.width):
        i = x % 8
        j = y % 8
        if data[y * Dithered_img_4X4.width + x] > (256 // 64) * d3[j][i]:
            Dithered_4X4_pix[x, y] = 1
        else:
            Dithered_4X4_pix[x, y] = 0

Dithered_img_2X2.show()
Dithered_img_4X4.show()
for i in range(10000000):
    continue
