# no parameter no return

# parameter คือ ตัวแปรที่ใช้รับค่าจากภายนอกฟังก์ชัน และใช้ภายในฟังก์ชัน 
# return คือ ไม่มีการส่งค่าใดๆ กลับไปยังจจุดเรียกใช้ฟังก์ชัน 

'''
def func_name():
    คำสั่ง
    คำสั่ง
    ....

'''
def func_a():
    print("Hello...")
    print("Hi...")

    def func_b():
        print("Good morning...")
        print("Good afternoon...")

print("yoo...")
func_a() # เรียกใช้ฟังก์ชัน func_a