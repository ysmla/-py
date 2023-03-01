import os
import time
import tkinter as tk
timenow2 = time.ctime(1469101837.655935)
timenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
number = 0
number2 = 1
def tishi():
    root = tk.Tk()
    root.title("数学积分管理系统")
    theLabel = tk.Label(root, text="积分统计文件夹已经保存至桌面，路径为：" + desk, font=("华文楷体", 30, "bold italic underline"))
    theLabel.pack()
    root.mainloop()
def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")
desk = get_desk_p()
try:
    os.makedirs(desk + "\\"+timenow+'数学积分统计')
    os.system('导出分数.py')
    for i in range(46):
        number += 1
        os.makedirs(desk + "\\"+timenow+'数学积分统计\详细\\' + str(number) + "号")
        f = open(desk + "\\"+timenow+"数学积分统计\详细\\" + str(number) + "号\\个人统计.doc", "x")
        f.close()

        f = open("C:\\maths\\people\\" + str(number) + "\\a.txt", "r+")
        g = f.readlines()[-1]
        f.close()



        f = open(desk +"\\"+timenow+ "数学积分统计\详细\\" + str(number) + "号\\个人统计.doc", "a+")
        f.write(str(number) + "号的总分为：" + g)
        f.close()

        f = open("C:\\maths\\people\\" + str(number) + "\\b.txt", "r+")
        g = f.read()
        f.close()
        f = open(desk +"\\"+timenow+ "数学积分统计\详细\\" + str(number) + "号\\个人统计.doc", "a+")
        f.write("\n" + "\n" + "历史记录：" + "\n" + g)
        f.close()
    f = open("C:\\maths\\record\\a.txt","r+")
    text = f.read()
    f.close()
    f = open(desk +"\\"+timenow+ "数学积分统计\\积分变动记录.docx","x")
    f.write(text)
    f.close()
    tishi()
except FileExistsError:
    tishi()
