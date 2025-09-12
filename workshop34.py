# return คือ ที่ใช้ส่งข้อมูล กลับไปยังจุดที่เรียกใช้ฟังก์ชัน
# no parameter have returns
'''
def func_name():
    คำสั่ง
    คำสั่ง
    ....
    return ค่าที่ส่งกลับ
'''

def func_f():
    print("Hello...")
    return ' Hi... ' 
    
def func_g():
    return 'Wow...' , 'Great...' , 909090

print( func_f() )

xx = func_f() 
print(xx)

a , b , c = func_g()
print(a)
print(b)
print(c)
