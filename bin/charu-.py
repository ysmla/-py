number = 0
number2 = 1
while 1:
    time = input("输入要插入的日期，年月日用空格空开")
    ex = time.split()
    year = ex[0]
    month = ex[1]
    day = ex[2]
    if int(day) < 10 and len(day) == 1:
        newday = "0" + day
    else:
        newday = day
    if int(month) < 10 and len(month) == 1:
        nmonth = "0" + month
    else:
        nmonth = month
    timenow = year + "-" + nmonth + "-" + newday


    print("输入阿拉伯数字以选择")
    print("输入1非全班性扣分")
    print("输入2全班批量扣分")
    print("输入3批量扣分")
    b = input("在此处输入数字>")
    if b != "1" and b!= "2" and b!="3":
        print("该操作不存在，请重新输入")
    if b == "1":
        reason = input("输入扣分原因敲回车>")
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "扣分原因："+reason)
        f.close()
        while True:
            print("在输入学号的位置输入a结束")
            while 1:
                try:
                    d = input("输入学号敲回车>")
                    if d == "a":
                        print("结束")
                        exit()
                    else:
                        if int(d) > 46 or int(d) <= 0:
                            print("该学号不存在，最大学号为46，请重新输入")
                        else:
                            try:

                                e = input("输入分值敲回车>")
                                f = open("C:\\maths\\people\\" + d + "\\b.txt", "a+")
                                f.write("\n" + timenow + "\n" + "减分原因：" + reason + "\n扣" + e + "分")
                                f.close()
                                f = open('C:\\maths\\people\\' + d + '\\a.txt', "r+")
                                g = f.readlines()[-1]
                                h = int(g) - int(e)
                                f.write("\n" + str(h))
                                f.close()
                                break
                            except ValueError:
                                print("学号不正确，请重新输入")
                        print("\n" + "\n")
                        break
                except ValueError:
                    print("学号错误，请重新输入")
    if b == "2":
        reason = input("输入扣分原因敲回车>")
        print("按照学号的顺序扣分")
        print("每个人要扣的分数相同吗")
        print("相同输入阿拉伯数字1")
        print("不相同输入阿拉伯数字2")
        i = input("输入阿拉伯数字>")
        if i == "1":
            j = input("输入每个人扣多少分>")
            f = open('C:\\maths\\record\\a.txt', "a+")
            f.write("\n" + timenow + '\n' +"扣分原因："+ reason)
            f.close()
            for i in range(46):
                if number>46:
                    break
                number+=1
                f = open("C:\\maths\\people\\"+str(number)+"\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "扣分原因：" + reason + "\n扣" + j + "分")
                f.close()

            while True:
                number += 1
                if number > 46:
                    print("成功")
                    input("")
                    break
                else:
                    f = open('C:\\maths\\people\\' + str(number2) + '\\a.txt', "r+")
                    g = f.readlines()[-1]
                    h = int(g) - int(j)
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
                    k = input("输入" + str(number2) + "号要扣的分>")
                    f = open("C:\\maths\\people\\" + str(number2) + "\\b.txt", "a+")
                    f.write("\n" + timenow + "\n" + "扣分原因：" + reason + "\n扣" + j + "分")
                    f.close()
                    f = open('C:\\maths\\people\\' + str(number2) + '\\a.txt', "r+")
                    g = f.readlines()[-1]
                    h = int(g) - int(k)
                    f.write("\n" + str(h))
                    f.close()
                    number2 += 1
            print("\n" + "\n")
            break
    if b == "3":
        fen = input("输入要扣的分数>")
        reason = input("输入扣分原因>")
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "扣分原因：" + reason)
        f.close()
        number3 = int(input("有多少人要扣分>"))
        if int(number3)>46 or int(number3)<=0:
            print("学生总数不正确，一共46人，请重新输入")
        for i in range(number3):
            number4 = input("输入扣分人的学号:>")
            if int(number4)>46 or int(number4)<0:
                print("该学号不存在，最大学号为46，请重新输入")
            else:
                f = open("C:\\maths\\people\\" + str(number4) + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "扣分原因：" + reason + "\n扣" + fen + "分")
                f.close()
                f = open('C:\\maths\\people\\' + str(number4) + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) - int(fen)
                f.write("\n" + str(h))
                f.close()
            print("成功")
        break
