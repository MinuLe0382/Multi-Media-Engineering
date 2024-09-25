from PIL import Image

img = Image.new('RGB', (512, 512))
pix = img.load()

file = open('lena512_1bit.raw', 'rb')
data = file.read()
file.close()

x = -1 
y = 0

for i in range(len(data)): # Loop 32768 times
    y = i // (img.height // 8) # Change Location of Target to Write

    for j in range(8): # Loop for BitMask Control

        Mask = 0b00000001 << j # Mask for Extract Target bit value
        val = (Mask & data[i]) >> j # '&' Operation for Masking, and '>>' Operation for change it to single bit
        val = 255 if val == 1 else 0 # val == 1 mean white, val == 0 mean black

        x += 1  # Change Location of Target to Write
        x %= img.width

        pix[x, y] = (val, val, val) # Write
    
img.show()

# debug = input()
# 현재 제 VSCODE 설정으로는 img.show()만 하면 이미지가 출력되기도 전에 프로그램이 종료되어 추가한 코드입니다.