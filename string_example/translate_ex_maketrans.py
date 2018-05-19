from string import maketrans
table = maketrans("cs", "kz")      # 将ASCII字符表中的c替換成k，s替換成z
print("转换后的字母表： " + table[97:123])                 # 提取转换后的字母表
print("转换前的字母表： " + maketrans("", "")[97:123])     # 提起转换前的字母表
str = "this is an incredible test".translate(table)     # 用转换表对字符串进行替换
print(str)
