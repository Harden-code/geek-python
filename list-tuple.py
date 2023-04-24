# 列表是动态的
# 元祖是静态的，长度大小固定，无法删除或改变
tup = (1, 2, 3)
arr = [1, 2, 3]

# 添加操作
new_tup = tup + (4,)  # 返回一个新的元组
arr.append(4)

# 负数 代表从后像前返回
val = tup[-1]
print(val)

# 切片操作
re = tup[0:1]
# (1,) 如果没有,会有歧义
print(re)

# 两个的相互转换
print(list(tup))
print(tuple(arr))

# 内置函数
# count 统计出现次数
# index 返回第一次出现的索引
# reverse和sort 原地倒转和排序

# different
# 列表 使用一种over allocating来保证高效性
print("start", arr.__sizeof__())
for i in range(10):
    arr.append(i)
    print("append->", arr.__sizeof__())

print(tup.__sizeof__())
if __name__ == "__main__":
    pass
    # print(new_tup)
