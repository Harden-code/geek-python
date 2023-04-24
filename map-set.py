# 字典
# 创建方式
d1 = {'name': 'harden', 'number': '13'}
d2 = dict({'name': 'harden', 'number': '13'})
d3 = dict([('name', 'harden'), ('number', '13')])
d4 = dict(name='harden', number=2)
# 访问方式
# d1['locate'] error 代替方式使用get
d1.get('locate', 'default')

# 根据字典值升序
d5={'b': 1, 'a': 2, 'c': 10}
# 根据字典键升序
print(sorted(d5.items(), key=lambda x: x[0]))
# 根据字典值升序
print(sorted(d5.items(),key=lambda x: x[1]))

d5.setdefault('f',3)

# 集合
# 创建方式
s1 = {1, 2, 3}
s2 = set([1, 2, 3])

# 注意set的实现也是hash 所以不能使用下标引用
# 判断集合是否存在元素使用 ele in set
print(3 in s1)
# 集合的 pop() 操作是删除集合中最后一个元素，可是集合本身是无序的，你无法知道会删除哪个元素，因此这个操作得谨慎使用。

# add remove 添加删除操作
