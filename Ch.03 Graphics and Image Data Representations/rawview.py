from PIL import Image

# 512 X 512 Canvas, return Image Object
img = Image.new(mode='RGB', size=(512, 512))
# Check the Document
# put same value at R, G, B and it will be GrayScale

# r for read mode and require binary read : rb
# dont stop reading when encounter EOF
file = open('lena512.raw', 'rb')
data = file.read() # return str when 'r', return bytes when 'rb'
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
        pix[x, y] = (val, val, val)

img.show()
checker = input()