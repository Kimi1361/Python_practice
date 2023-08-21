def fl(x):
    """文字列をfloat型に変換
    :parm x: string
    :return: string converted to int
    """
    try:
        return float(x)
    except ValueError:
        print("小数点に変換できません")

c = fl("3.14")
print(c)
        

