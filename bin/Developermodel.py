import os
from io import UnsupportedOperation
number = 0
print('''
============================================
此为开发者模式，所有操作都将记录
非开发者请勿进入，任何操作都是不可逆的
请谨慎
输入yes进入开发者选项
输入其他任意字符退出''')
key = input("PLEASE INPUT\n>")
if key =="yes":
    while 1:
        print('''
        输入阿拉伯数字以选择
        输入1清空所有人的分数
        输入2清空总记录
        输入3清空个人记录
        输入4检查系统
        输入5退出
        输入6定义初始分
        输入7清空本地所有数据
        输入8定义名字
        输入9恢复出厂设置
        ''')
        choose = input("PLEASE INPUT\n>")
        if choose == "1":
            while 1 :
                number+=1
                if number>46:
                    break
                else:
                    f= open("C:\\maths\\people\\%d\\a.txt"%(number),"w",encoding="UTF-8")
                    try:
                        f.read()
                        print("\nERROR:NUMBER=%s\n" % (str(number)))
                    except UnsupportedOperation:
                        print("\n成功清空%s号的分数\n" % (str(number)))
                    f.close()
            number*=0
        if choose == "3":
            while 1 :
                number+=1
                if number>46:
                    break
                else:
                    f= open("C:\\maths\\people\\%d\\b.txt"%(number),"w",encoding="UTF-8")
                    try:
                        f.read()
                        print("\nERROR:NUMBER=%s\n" % (str(number)))
                    except UnsupportedOperation:
                        print("\n成功清空%s号的个人记录\n" % (str(number)))
                    f.close()
            number*=0
        if choose == "2":
            f = open("C:\\maths\\record\\a.txt","w",encoding="ANSI")
            try:
                f.read()
                print("\nERROR:FAIL")
            except UnsupportedOperation:
                print("\n成功清空总记录")
            f.close()
        if choose == "5":
            exit()
        if choose == "6":
            print("设置初始分会清空所有分数")
            point = input("请输入每个人的初始分")
            for i in range(46):
                number+=1
                str(number)
                f = open("C:\\maths\\people\\%s\\a.txt"%(number),"w",encoding="UTF-8")
                f.write(point)
                f.close()
                f = open("C:\\maths\\people\\46\\a.txt", "w", encoding="UTF-8")
                f.write(point)
                f.close()
                int(number)
        if choose == "7":
            while 1 :
                number+=1
                if number>46:
                    break
                else:
                    f= open("C:\\maths\\people\\%d\\a.txt"%(number),"w",encoding="UTF-8")
                    try:
                        f.read()
                        print("\nERROR:NUMBER=%s\n" % (str(number)))
                    except UnsupportedOperation:
                        print("\n成功清空%s号的分数\n" % (str(number)))
                    f.close()
            number*=0

            while 1 :
                number+=1
                if number>46:
                    break
                else:
                    f= open("C:\\maths\\people\\%d\\b.txt"%(number),"w",encoding="UTF-8")
                    try:
                        f.read()
                        print("\nERROR:NUMBER=%s\n" % (str(number)))
                    except UnsupportedOperation:
                        print("\n成功清空%s号的个人记录\n" % (str(number)))
                    f.close()
            number*=0

            f = open("C:\\maths\\record\\a.txt", "w", encoding="ANSI")
            try:
                f.read()
                print("\nERROR:FAIL")
            except UnsupportedOperation:
                print("\n成功清空总记录")
            f.close()
        if choose=="8":
            for i in range(1,47):
                name = input("输入"+str(i)+"号的名字")
                f = open("C:\\maths\\people\\%d\\c.txt"%(i),"w",encoding="UTF-8")
                f.write(name)
                f.close()
        if choose == "9":
            while 1 :
                number+=1
                if number>46:
                    break
                else:
                    f= open("C:\\maths\\people\\%d\\a.txt"%(number),"w",encoding="UTF-8")
                    try:
                        f.read()
                        print("\nERROR:NUMBER=%s\n" % (str(number)))
                    except UnsupportedOperation:
                        print("\n成功清空%s号的分数\n" % (str(number)))
                    f.close()
            number*=0

            while 1 :
                number+=1
                if number>46:
                    break
                else:
                    f= open("C:\\maths\\people\\%d\\b.txt"%(number),"w",encoding="UTF-8")
                    try:
                        f.read()
                        print("\nERROR:NUMBER=%s\n" % (str(number)))
                    except UnsupportedOperation:
                        print("\n成功清空%s号的个人记录\n" % (str(number)))
                    f.close()
            number*=0

            f = open("C:\\maths\\record\\a.txt", "w", encoding="ANSI")
            while 1 :
                number+=1
                if number>46:
                    break
                else:
                    f= open("C:\\maths\\people\\%d\\c.txt"%(number),"w",encoding="UTF-8")
                    try:
                        f.read()
                        print("\nERROR:NUMBER=%s\n" % (str(number)))
                    except UnsupportedOperation:
                        print("\n成功清空%s号的名字\n" % (str(number)))
                    f.close()
            number*=0
            try:
                f.read()
                print("\nERROR:FAIL")
            except :
                print("\n成功清空总记录")
            f.close()

else:
    exit()