correct = [14,25,54,87,91]
number = []
y = len(correct)

for i in range(1,101):
    number.append(i)


while True:
    x = input("1~100の内当たりは5個、辞める時はq")
    if x == "q":
        break
    try:
        x = int(x)
    except ValueError:
        print("数字を入力してください。")
        continue
    if x not in number:
        print("1~100の数字を入力するか、qで終了します。")
    elif x in correct:
        y -= 1
        del correct[correct.index(x)]
        if y == 0:
            print("全問正解！")
            break
        else:
            print("正解！あと{}つ！".format(y))
            continue
    else:
        print("不正解")
