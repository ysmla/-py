import time
import os
timenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
def xp():
    reaso = "作业全对"
    add = "5"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        n = input("输入课时数字")
        reason = reaso + n
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def gongzi():
    number = 0
    reason = "工资"
    add = "10"
    man = ["33号 陈语凡","37号 徐敬天","30号 李方瑞","24号 卞思源","4号 王馨妤","13号 胡馨元","12号 郑好"]
    rman = ["33","37","30","24","4","13","12"]
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%(str(man),reason,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r =="1":
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        for i in range(7):
            f = open("C:\\maths\\people\\" + rman[number] + "\\b.txt", "a+")
            f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
            f.close()
            f = open('C:\\maths\\people\\' + rman[number] + '\\a.txt', "r+")
            g = f.readlines()[-1]
            h = int(g) + int(add)
            f.write("\n" + str(h))
            f.close()
            number+=1
        print("成功")
def ks100():
    reaso = "考试满分"
    add = "10"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def ks95():
    reaso = "考试95分以上"
    add = "5"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def ks90():
    reaso = "考试90分以上"
    add = "3"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def ks9510():
    reaso = "考试95分以上"
    add = "10"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def ks905():
    reaso = "考试90分以上"
    add = "5"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def ks853():
    reaso = "考试85分以上"
    add = "3"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def xiaozumax():
    reaso = "小组分最高"
    add = "5"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
def xiaozumin():
    reaso = "小组分最低"
    add = "5"
    print('''
    模板内容：
    对象：%s
    原因：%s
    扣分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "扣分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入扣分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "扣分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) - int(add)
                f.write("\n" + str(h))
                f.close()
def xiaozumina():
    reaso = "小组均分最低"
    add = "5"
    print('''
    模板内容：
    对象：%s
    原因：%s
    扣分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "扣分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入扣分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "扣分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) - int(add)
                f.write("\n" + str(h))
                f.close()
def meiyuxi():
    reaso = "没预习"
    add = "5"
    print('''
    模板内容：
    对象：%s
    原因：%s
    扣分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "扣分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入扣分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "扣分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) - int(add)
                f.write("\n" + str(h))
                f.close()

def xiaozumaxa():
    reaso = "小组均分最高"
    add = "3"
    print('''
    模板内容：
    对象：%s
    原因：%s
    加分：%s
    '''%("自定义",reaso,add))
    print("确认输入阿拉伯数字1，键入任意键返回")
    r = input("在此处输入阿拉伯数字>")
    if r == "1":
        reason = reaso
        f = open('C:\\maths\\record\\a.txt', "a+")
        f.write("\n" + timenow + '\n' + "加分原因：" + reason)
        f.close()
        while 1:
            man  = input("输入加分人的学号，输入a退出>")
            if man == "a":
                break
            else:
                f = open("C:\\maths\\people\\" + man + "\\b.txt", "a+")
                f.write("\n" + timenow + "\n" + "加分原因：" + reason + "\n加" + add + "分")
                f.close()
                f = open('C:\\maths\\people\\' + man + '\\a.txt', "r+")
                g = f.readlines()[-1]
                h = int(g) + int(add)
                f.write("\n" + str(h))
                f.close()
print("输入阿拉伯数字以选择需要使用的模板类型\n")
print("1.工资\n")
print("2.作业全对加分\n")
print("3.考试100分（10）\n")
print("4.考试95分以上（5）\n")
print("5.考试90分以上（3）\n")
print("6.考试95分以上（10）\n")
print("7.考试90分以上（5）\n")
print("8.考试85分以上（3）\n")
print("9.退出\n")
print("10.小组分最高\n")
print("11.小组分最低\n")
print("12.小组均分最高\n")
print("13.小组均分最低\n")
print("14.没预习\n")
while 1:
    choes = input("在此处输入阿拉伯数字")
    if choes!="1"and choes!="2" and choes!="3" and choes!="4"and choes!="14"and choes!="13"  and choes!="12" and choes!="5"and choes!="6" and choes!="11"and choes!="7"and choes!="8"and choes!="9"and choes!="10":
        print("输入的选项无效，请重新输入")
    else:
        break
if choes=="1":
    gongzi()
if choes == "2":
    xp()
if choes == "3":
    ks100()
if choes == "4":
    ks95()
if choes == "5":
    ks90()
if choes == "6":
    ks9510()
if choes == "7":
    ks905()
if choes == "8":
    ks853()
if choes == "9":
    exit()
if choes == "10":
    xiaozumax()
if choes == "11":
    xiaozumin()
if choes == "12":
    xiaozumaxa()
if choes == "13":
    xiaozumina()
if choes == "14":
    meiyuxi()