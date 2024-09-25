from PIL import Image

# 512 X 512 Canvas, return Image Object
img = Image.new(mode='RGB', size=(512, 512))
# Check the Document
# put same value at R, G, B and it will be GrayScale

# r for read mode and require binary read : rb
# dont stop reading when encounter EOF
file = open('lena512.raw', 'rb')
data = file.read()
# read all when given no parameter
# read 256bytes when read(256)
file.close()

pix = img.load() # enable direct access to img 
'''
print(px[4, 4])
(0, 0, 0) returned

px[0, 0] = (0, 0, 0) >> black
'''
'''
print(data[262143])
98 << value returned

'''
for y in range(img.height):
    for x in range(img.width):
        val = data[y * img.width + x]
        temp = 255 if val > 127 else 0
        # Quantization to 1 or 0
        pix[x, y] = (temp, temp, temp)

img.show()
checker = input()

'''
question : data[y * img.width + x] is integer like 200, it is byte?
and raw file is grayscale?
'''