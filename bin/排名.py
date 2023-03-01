number2 = 0
number = 0
number3 = 46
T = True
F = False
name = []
print('''
输入阿拉伯数字以选择\n
输入1按照降序排名\n
输入2按照升序排名\n''')
ser = input("在此处输入阿拉伯数字")
end = T if int(ser)==1 else F
for i in range(46):
    number+=1
    name2 = []
    f = open("C:\\maths\\people\\"+str(number)+"\\c.txt","r+",encoding="UTF-8")
    name2.append(f.read())
    f.close()
    f = open("C:\\maths\\people\\" + str(number) + "\\a.txt", "r+", encoding="UTF-8")
    g = f.readlines()[-1]
    name2.append(int(g))
    f.close()
    name.append(name2)
    del name2
def takeSecond(elem):
    return elem[1]
name.sort(key=takeSecond,reverse=end)
number-=46
for i in range(46):
    if end == True:

        number+=1
        newname = str(name[number2][0])
        newpoint = str(name[number2][1])
        print("第" + str(number) +"名"+"          "+newname+"           "+newpoint+"分"+"\n===================================")
        number2+=1
    else:
        newname = str(name[number2][0])
        newpoint = str(name[number2][1])
        print("第" + str(
            number3) + "名" + "          " + newname + "           " + newpoint + "分" + "\n===================================")
        number2 += 1
        number3-=1