# 用递归的方法实现数组之和
def sum(arr):
    if(len(arr) == 0):
        return 0
    else:
        q = arr.pop()
        return q + sum(arr)
    
print(sum([1,2,3,4]))
