# 导入队列模块
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []                                    # 这个数组用来记录检查过的人
    while (search_queue):
        person = search_queue.popleft()
        if (person not in searched):                 # 仅当这个人没检查过时才检查
            if (person_is_seller(person)):
                print(person + " is a mango seller")
                return True
            else:
                print(person + " is not a mango seller")
                search_queue += graph[person]
                searched.append(person)              # 将这个人标记为检查过
    return False


def person_is_seller(name):
    return name[-1] == 'm'


search("you")
