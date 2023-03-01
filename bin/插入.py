import os
while 1:
    print('''
    输入阿拉伯数字以选择
    输入1加分
    输入2扣分
    ''')
    c = input("在此处输入>")
    if c!="1"and c!="2":
        print("不存在这个选择，重新输入")
    else:
        if c =="1":
            os.system("charu+.py")
        else:
            os.system("charu-.py")