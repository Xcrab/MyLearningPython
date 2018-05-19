# 简单的数据库

# 使用人名作为键的字典。每个人用另一个字典来表示，其键‘phone’和‘addr’分别表示他们的电话号码和地址

people = {
    "Alice": {
        "phone": "2341",
        "addr": "Foo drive 23"
    },
    "Beth": {
        "phone": "9102",
        "addr": "Bar street 42"
    },
    "Cecil": {
        "phone": "3158",
        "addr": "Baz avenue 90"
    }
}

# 针对电话号码和地址使用的描述性标签，会在打印输出的时候用到
labels = {"phone": "phone number", "addr": "address"}

name = raw_input("Name: ")

# 查找电话号码还是地址？使用正确的键：
request = raw_input("Phone Number (p) or address (a)? ")

# 使用正确的键:
key = request       # 如果请求既不是'p'也不是'a'
if request == "p":
    key = "phone"
if request == "a":
    key = "addr"

# 使用get()提供默认值
# get("键","默认值")
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, "not available")

print("%s's %s is %s." % (name, label, result))
