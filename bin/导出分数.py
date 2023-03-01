import xlwt
import os
import time
number = 0
number2 = 0
number3 = 0
timenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")
desk = get_desk_p()
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(1,1, label = '学号')
worksheet.write(1,2, label = '名字')
worksheet.write(1,3, label = '积分')
for i in  range(46):
    number+=1
    worksheet.write(number+1, 1, label= str(number)+"号")
    f = open("C:\\maths\\people\\"+str(number)+"\\c.txt","r+",encoding="utf-8")
    a = f.read()
    f.close()
    worksheet.write(number + 1, 2, label = a)
    f = open("C:\\maths\\people\\" + str(number) + "\\a.txt", "r+", encoding="utf-8")
    g = f.readlines()[-1]
    f.close()
    worksheet.write(number + 1, 3, label=int(g))



# 保存
workbook.save(desk + "\\"+timenow+'数学积分统计\\'+timenow+'积分统计.excel')

