# คำสั่ง branch และ continue *** ที่อยู่ใน loop
# break ใช้สำหรับออกจาก loop ทันที
# continue ใช้สำหรับข้ามการทำงานใน loop ครั้งนั้นๆ แล้วไปเริ่มต้น loop ใหม่

for i in range(5):
    if i == 3:
        break   # ออกจาก loop ทันที
    print(i,'Yay...')

print('-------------------')

for i in range(5):
    if i == 3:
        continue   # ข้ามการทำงานใน loop ครั้งนั้นๆ แล้วไปเริ่มต้น loop ใหม่
    print(i, 'Hello...')