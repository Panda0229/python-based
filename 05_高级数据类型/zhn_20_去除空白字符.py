poem = ["\t\n登鹳雀楼",
        "王之涣",
    "白日依山尽\t\n",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"]

for poem_str in poem:
    # 先是用strip方法去除空白字符，在使用center居中文本
    print("|%s|" % poem_str.strip().center(10, " "))