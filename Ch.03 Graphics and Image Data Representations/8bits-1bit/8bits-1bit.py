from PIL import Image

img = Image.new('RGB', (512, 512))
pix = img.load()

in_file = open('lena512.raw', 'rb')
out_file = open('lena512_1bit.raw', 'wb')

b = bytearray(1) # buffer for write

# Read 8 bits, write 1 byte per loop
for i in range(img.height * img.width // 8):
    data = in_file.read(8) # read 8 bytes
    b[0] = 0b00000000 # little endian
    for j in range(8):
        b[0] |= 0b00000001 << j if data[j] > 127 else 0b00000000
        # or operation for to not overwrite
    out_file.write(b)

in_file.close()
out_file.close()