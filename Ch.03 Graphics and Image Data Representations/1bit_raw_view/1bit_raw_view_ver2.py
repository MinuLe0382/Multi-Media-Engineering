from PIL import Image

img = Image.new(mode='L', size=(512, 512))
pix = img.load()
file = open('lena512_1bit_mono.raw', 'rb')

# 읽을때도 little endian으로 저장이 되어있으니 바이트단위로 읽어야 하지 않을까?
b = bytearray(1)
for i in range(img.height * img.width // 8):
    y = i // (img.width // 8) # 64번 돌면 하나 증가한다.
    data = file.read(1) # 아무것도 안넣으면 파일 전체를 읽는다
    b[0] = 0b00000001
    for j in range(8):
        mask = b[0] << j
        val = (mask & data[0]) >> j
        val = 255 if val == 0b00000001 else 0
        # 일단 j 만큼 움직이는데 몇번 8번만큼 읽었는가? 그리고 i가 512넘으면 초기화
        # 8bit - 1bit 할때의 j는 읽은 8개의 바이트를 넘기는데, 
        # 여기서는 1바이트의 1비트 각각을 보기위해
        x = (8 * i % img.width) + j 
        pix[x, y] = (val)

img.show()
file.close()
