# test 2018.07.21
# test 2018.07.21.00000
names = ["name", "beth", "george", "damon"]
ages = [12, 45, 32, 102]

print("循环索引:")
for i in range(len(names)):
    print(str(names[i]) + " is " + str(ages[i]) + " years old")

print("zip函数:")
for name, age in zip(names, ages):
    print(str(name) + " is " + str(age) + " year old")

# zip特殊用法，可以应付不等长的序列，当短的序列”用完“的时候就会停止
print(zip(range(5), xrange(100000)))
