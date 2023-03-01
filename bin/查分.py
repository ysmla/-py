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
    print("输入1非全班性查分\n")
    print("输入2查全班的分\n")
    print("输入3退出\n")
    l = input("在此处输入数字>")
    if l!="1" and l !="2" and l !="3":
        print("该操作不存在，请重新输入")
    if l == "1":
        while True:
            x1 = input("输入要查的人的学号,输入a结束>")
            if x1 == "a":
                exit()
            else:
                if x1.isnumeric() != True:
                    print("非法字符，请重新输入")
                else:
                    if int(x1)>46 or int(x1)<0:
                        print("该学号不存在，最大学号为46，请重新输入")
                    else:

                        f = open('C:\\maths\\people\\'+str(x1)+'\\a.txt',"r+")
                        g = f.readlines()[-1]
                        print(x1+"号的分数为"+g)
                        number += 1
                        print("\n" + "\n")

    if l == "2":
        for i in range(46):
            try:

                number += 1
                f = open("C:\\maths\\people\\"+str(number)+"\\c.txt","r+",encoding="UTF-8")
                name = f.read()

                f = open('C:\\maths\\people\\' + str(number) + '\\a.txt', "r+")
                g = f.readlines()[-1]
                print(str(number) +"号"+ "    +    "+name+ "    +    "+ str(g)+"分"+" +"+"\n================================")
                f.close()
                f.close()
            except FileNotFoundError:
                break
    if l == "3":
        exit()
        print("\n"+"\n")
        break
