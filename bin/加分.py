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

    print("输入阿拉伯数字以选择\n")
    print("输入1非全班性加分\n")
    print("输入2全班批量加分\n")
    print("输入3批量加分\n")
    print("输入4退出\n")
    b = input("在此处输入数字>")

    if int(b)!=1 and int(b)!=2 and int(b)!=3 and int(b)!=4:
        print("\n该操作不存在，请重新选择\n")
    if b == "1":
        reason = input("输入加分原因敲回车>")
        print("\n")
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        print("\n")
        f.close()
        while True:
            print("在输入学号的位置输入a结束")
            print("\n")
            while 1:
                try:
                    d = input("输入学号敲回车>")
                    print("\n")
                    if d == "a":
                        print("结束")
                        exit()
                    else:
                        if int(d)>46 or int(d)<=0:
                            print("\n该学号不存在，最大学号为46，请重新输入\n")
                        else:
                            try:

                                e = input("输入分值敲回车>")
                                print("\n")
                                f = open("C:\\maths\\people\\" + d + "\\b.txt", "a+")
                                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + e + "分")
                                f.close()
                                f = open('C:\\maths\\people\\' + d + '\\a.txt', "r+")
                                g = f.readlines()[-1]
                                h = int(g) + int(e)
                                f.write("\n" + str(h))
                                f.close()
                                break
                            except ValueError:
                                print("\n学号不正确，请重新输入\n")
                        print("\n" + "\n")
                        break
                except ValueError:
                    print("学号错误，请重新输入")

    if b == "2":
        reason = input("输入加分原因敲回车>")
        print("按照学号的顺序加分\n")
        print("每个人要加的分数相同吗\n")
        print("相同输入阿拉伯数字1\n")
        print("不相同输入阿拉伯数字2\n")
        i = input("输入阿拉伯数字>")
        if int(i) != 1 and int(i) != 2:
            print("\n该操作不存在，请重新选择\n")
        if i == "1":
            j = input("输入每个人加多少分>")
            print("\n")

            f = open('C:\\maths\\record\\a.txt', "a+")
            f.write("\n" + timenow + '\n' + "加分原因：" + reason)
            print("\n")
            f.close()
            for i in range(46):
                if number > 46:
                    break
                number += 1
                f = open("C:\\maths\\people\\" + str(number) + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + j + "分")
                f.close()

            while True:
                number += 1
                if number > 46:
                    print("成功")
                    print("\n")
                    input("")
                    exit()
                else:
                    f = open('C:\\maths\\people\\' + str(number2) + '\\a.txt', "r+")
                    g = f.readlines()[-1]
                    h = int(g) + int(j)
                    f.write("\n" + str(h))
                    f.close()
                    number2 += 1
                print("\n" + "\n")
                break
        if i == "2":
            while True:
                number += 1
                if number > 46:
                    print("成功")
                    input("")
                    break
                else:
                    while 1:

                        try:

                            k = input("输入" + str(number2) + "号要加的分>")
                            print("\n")
                            f = open("C:\\maths\\people\\" + str(number2) + "\\b.txt", "a+")
                            f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + k + "分")
                            f.close()
                            f = open('C:\\maths\\people\\' + str(number2) + '\\a.txt', "r+")
                            g = f.readlines()[-1]
                            h = int(g) + int(k)
                            f.write("\n" + str(h))
                            f.close()
                            number2 += 1
                            break
                        except  ValueError:
                            print("学号不正确，请重新输入")
                            print("\n")
            print("\n" + "\n")
            break
    if b == "3":
        print("\n")
        fen = input("输入要加的分数>")
        print("\n")
        reason = input("输入加分原因>")
        print("\n")
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            number3 = int(input("有多少人要加分>"))
            if int(number3)>46 or int(number3)<=0:
                print("\n该学号不存在，最大学号为46，请重新输入\n")
            else:
                for i in range(number3):
                    while 1:
                        number4 = input("输入加分人的学号:>")
                        if int(number4)>46 or int(number4)<=0:
                            print("\n该学号不存在，最大学号为46，请重新输入\n")
                        else:
                            break
                    f = open("C:\\maths\\people\\" + str(number4) + "\\b.txt", "a+")
                    f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + fen + "分")
                    f.close()
                    f = open('C:\\maths\\people\\' + str(number4) + '\\a.txt', "r+")
                    g = f.readlines()[-1]
                    h = int(g) + int(fen)
                    f.write("\n" + str(h))
                    f.close()
                print("成功")
                exit()
    if b == '4':
        exit()
