import os
tool2 = 0
print('''
输入阿拉伯数字以选择
输入1查总体历史
输入2查个人历史
''')
while 1:

    choose = input("在此处输入阿拉伯数字\n>")
    if choose!="1"and choose!= "2":
        print("输入错误，请重新输入")
    else:
        break
if choose=="1":
    f = open("C:\\maths\\record\\a.txt","r+",encoding="ANSI")
    str = f.read()
    f.close()
    all = str.splitlines()
    while 1:
        try:
            newc = input("\n输入日期年月日，中间用空格空开，示例：2021 2 2(退出请输入a)\n>")
            if newc=="a":
                break
            else:
                ex = newc.split()
                year = ex[0]
                month = ex[1]
                day = ex[2]
                if int(day)<10 and len(day)==1:
                    newday = "0"+day
                else:
                    newday = day
                if int(month) < 10 and len(month) == 1:
                    nmonth = "0" + month
                else:
                    nmonth=month
                key = year+"-"+nmonth+"-"+newday
                mm = all.count(key)
                tool = int(all.index(key))
                for i in range(mm):
                    wh = all.index(key,tool,-1)
                    print("===============================================\n"+all[wh]+"-----------"+all[int(wh)+1]+"\n===============================================\n")
                    tool+=2
                    tool2+=1
                if tool2 == 0:
                    print("没有找到相关记录或日期不是正确的格式，请尝试重新输入")
                else:
                    print("检索结束,一共有%s条记录\n"%(tool2))
                    tool2 *=0
                    tool*=0
        except:
            print("格式错误或日期不存在，重新输入")
else:
    number = input("输入要查询的学生学号")
    str(number)
    f = open("C:\\maths\\people\\%s\\b.txt"%(number), "r+", encoding="ANSI")
    str = f.read()
    f.close()
    all = str.splitlines()
    while 1:
        try:
            newc = input("\n输入日期年月日，中间用空格空开，示例：2021 2 2(退出请输入a)\n>")
            if newc == "a":
                break
            else:
                ex = newc.split()
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
                key = year + "-" + nmonth + "-" + newday
                mm = all.count(key)
                tool = int(all.index(key))
                for i in range(mm):
                    wh = all.index(key, tool, -1)
                    weizhi = wh
                    print(all[wh] + "-----------" + all[int(wh) + 1]+"----------"+ all[int(wh) + 2]+ "\n=====================================================\n")
                    tool += 3
                    tool2 += 1
                if tool2 == 0:
                    print("没有找到相关记录或日期不是正确的格式，请尝试重新输入\n")
                else:
                    print("检索结束,一共有%s条记录\n" % (tool2))
                    tool2 *= 0
                    tool *= 0
        except:
            print("格式错误或日期不存在，重新输入")