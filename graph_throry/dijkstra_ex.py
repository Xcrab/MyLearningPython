# 测试git
# 建图，使用散列表
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}  # 终点没有任何邻居

# 创建开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 创建存储父节点的表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 用数组标记处理过的结点
processed = []


# 寻找开销最小的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if (cost < lowest_cost and node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 真正算法的实现
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
