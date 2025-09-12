# have parameter no return
'''
def func_name(พารามิเตอร์1, พารามิเตอร์2, ...):
    คำสั่ง
    คำสั่ง
    ....
'''

def func_c( xx ):
    print(f'hello {xx}')

def func_d( num1, num2 , xx):
    sum = num1 + num2 + xx 
    print(f' Sum of 3 number = {sum} ')

func_c('Aom') # ข้อมูลที่ส่งไป parameter เรียกว่า อาร์กิวเมนต์ (argument)
func_c('iT')
print('--------------')
func_d(10,20,30)