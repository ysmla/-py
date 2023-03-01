import os
import time
import tkinter as tk
timenow2 = time.ctime(1469101837.655935)
timenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
number = 0
number2 = 1
def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")
desk = get_desk_p()
try:
    for i in range(46):
        number += 1
        f = open('C:\\maths\\people\\' + str(number) + '\\a.txt', "r+")
        g = f.readlines()[-1]
        f.close()
        f.close()
except IndexError:
    root = tk.Tk()
    root.title("数学积分管理系统")
    theLabel = tk.Label(root, text="本地数据损坏或者没有设置初始分，请联系开发者以解决此事", font=("华文楷体", 30, "bold italic underline"))
    theLabel.pack()
    root.mainloop()
    exit()
print("\n" + "\n")
while True:
    print("输入阿拉伯数字以选择\n")
    print("输入1加分\n")
    print("输入2扣分\n")
    print("输入3查分\n")
    print("输入4查询加减分历史\n")
    print("输入5导出分数汇报至桌面\n")
    print("输入6查看授权许可\n")
    print("输入7查看排名\n")
    print("输入8使用模板\n")
    a = input("在此处输入数字>")
    if a == '1':
        os.system('加分.py')
    if a == "2":
        os.system('扣分.py')
    if a == "3":
        os.system('查分.py')
    if a =="4":
        os.system('查询.py')
    if a == "5":
        os.system('导出.py')
    if a == "6":
        with open("C:\\maths\\takmsi\\development.txt","r+",encoding="UTF-8") as f:
            print(f.read())
            f.close()
    if a == "7":
        os.system('排名.py')
    if a == "cyf85763895":
        os.system('Developermodel.py')
    if a == "8":
        os.system('模板.py')