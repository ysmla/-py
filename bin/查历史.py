import os
import time
timenow2 = time.ctime(1469101837.655935)


timenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
number = 0
number2 = 1
def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")
desk = get_desk_p()
while 1:
    print("输入阿拉伯数字以选择")
    print("输入1查询总体历史")
    print("输入2查询个人历史")
    b = input("在此处输入数字>")
    if b != "1" and b!= "2":
        print("该操作不存在，请重新输入")
    if b == "1":
        f = open("C:\\maths\\record\\a.txt", "r+")
        c = f.read()
        print("\n" + c + "\n")
        f.close()
        break
    if b == "2":
        while True:
            print("输入要查分的人的学号，退出请输入a")
            c = input("请在此处输入>")
            if c == "a":
                print("已退出" + "\n")
                exit()
            else:
                if c.isnumeric() != True:
                    print("非法字符，请重新输入")
                else:
                    if int(c) >46 or int(c)<0:
                        print("该学号不存在，最大学号为46，请重新输入")

                    else:

                        f = open("C:\\maths\\people\\" + c + "\\b.txt")
                        d = f.read()
                        print("\n" + d + "\n")
                        f.close()