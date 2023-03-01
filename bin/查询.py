import  os
print('''
输入阿拉伯数字以选择

输入1为概览查询

如果需要按照日期查询请输入2

输入3退出
''')
while 1:

    choose = input("在此处输入阿拉伯数字")
    if choose!="1" and choose!="2" and choose!="3":
        print("不是正确的选项，请重新输入")
    else:
        break
if choose == "1":
    os.system("查历史.py")
if choose == "3":
        exit()
        print("\n"+"\n")
if choose == "2":
    os.system("查准确历史.py")
