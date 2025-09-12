#โปรแกรมตรวจสอบรถว่าผ่านเกณฑ์ของการตรวจสอบค่าคาร์บอนไดซ์ออกไซน์หรือ 
#โดยหากค่าคาร์บอนไดซ์ออกไซน์มีค่าเกินกว่า 678.55 ให้แสดงข้อความว่า “ไม่ผ่าน”  หากน้อยกว่า 678.55 ให้แสดงข้อความ “ผ่าน” 
#โดยให้รับชื่อเจ้าของ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้ ทางแป้นพิมพี่

def show_menu():
    print('-------------------------------')
    print(' Program check CO2')
    print('-------------------------------')

def input_data():
    y_name = input('ป้อนชื่อเจ้าของรถ ==>> ')
    y_regis = input('ป้อนทะเบียนรถ ==>> ') 
    y_co2 = float(input('ป้อนค่าคาร์บอนไดซ์ออกไซน์ที่วัดได้ ==>> '))
    return y_name, y_regis, y_co2

def show_result(y_name, y_regis, y_co2):
    print('-------------------------------')
    print('คุณ {} เจ้าของรถทะเบียน {} มีค่าคาร์บอนไดซ์ออกไซน์ {} '.format(y_name,y_regis,y_co2))

def check_co2(y_name, y_regis, y_co2):
    print('-------------------------------')
    if y_co2 > 678.55 : 
        print('คุณ {} เจ้าของรถทะเบียน {} มีค่าคาร์บอนไดซ์ออกไซน์ {} ไม่ผ่านเกณฑ์'.format(y_name,y_regis,y_co2))
        print('โปรดนำรถไปตรวจซ่อม...'.format(y_name,y_regis,y_co2))
    else : 
        print('คุณ {} เจ้าของรถทะเบียน {} มีค่าคาร์บอนไดซ์ออกไซน์ {} ผ่านเกณฑ์'.format(y_name,y_regis,y_co2))
        print('ขับขี่อย่างปลอดภัย...'.format(y_name,y_regis,y_co2))

show_menu()
car_name, car_regis, car_co2 = input_data()
show_result(car_name, car_regis, car_co2)
check_co2(car_name, car_regis, car_co2)
