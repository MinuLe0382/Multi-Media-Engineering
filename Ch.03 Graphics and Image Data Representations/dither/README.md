![image](https://github.com/user-attachments/assets/008cb545-1798-4af4-bbde-4d09e1e6b7a5)

![image](https://github.com/user-attachments/assets/0870a519-10df-4142-8004-9ccedbf75e07)

1비트로 이미지를 표현하면 명암표현이 불가능하다. 따라서 일종의 패턴이 있는 필터를 이용하려 이미지에 명암이 있는것 처럼 보이게 한다.

### **4 X 4 Dithering Matrix 적용**

![image](https://github.com/user-attachments/assets/8b1a9534-6f20-4d7f-8c95-92915017d356)

### **2 X 2 Dithering Matrix 적용**

![image](https://github.com/user-attachments/assets/8a3760bb-cc42-4d34-b072-9338fdd96b94) (256 / 4 인 64를 d[j][i]에 곱할 경우)

![image](https://github.com/user-attachments/assets/42414dc9-3649-410b-973e-761db14f54c9) (32를 d[j][i]에 곱할 경우)

![image](https://github.com/user-attachments/assets/1ca8b772-d900-46bc-9120-4ed5259f83c4) (16를 d[j][i]에 곱할 경우)
