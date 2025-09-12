# have parameter have return
'''
def func_name(a, b, ....):
    คำสั่ง
    คำสั่ง
    ....
    return ค่าที่ต้องการส่งกลับ
'''

def sum_num(a, b):
    total = a + b
    return total

def welcome(name):
    message = "Welcome " + name
    return message , 'DTI-SAU'

print(sum_num(10, 20))
print(welcome("John")) #ไม่ควรใช้ print ซ้อนกัน
print(sum_num(10,20))

data1, data2  = welcome("Modern Python")
print(data1)
print(data2)