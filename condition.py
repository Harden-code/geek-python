# 条件省略
# if
def abs(x):
    if x < 0:
        return -x
    else:
        return x
# python中不支持switch语句,只能使用if elif
# 省略判断条件的常见方法
# String => 空字符串解析为false，其余true
# int => 0为false，其余为true
# Bool =>
# list/tuple/dict/set => iterable空为flase，其余为true
# Object => None解析为false，其余true

# 循环语句
# 只要是可迭代的，比如列表，集合等
# for item in iterable


# 字典的for循环
# 缺省遍历的key
# items遍历k,V
# values遍历v
dic=dict(name='junsen',phone=13)

for k in dic:
    print(k)

for v in dic.values():
    print(v)

for k,v in dic.items():
    print(k,v)

# 下标遍历，使用range()函数，第三个参数步长
l=[1,2,3,4,5]

for index in range(0,len(l)):
    print(l[index])

# 使用索引和元素 使用enumerate函数来遍历
for index,item in enumerate(l):
    print(index,item)

# 条件循环复用



attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# dics=[dict(zip(attributes,item)) for item in values]
# print(dics)

result=[]
for item in values:
    dic1 = {}
    for i,key in enumerate(attributes):
        dic1.setdefault(key, item[i])
    result.append(dic1)

# 使用zip
result=[]
for item in values:
    dic1 = {}
    for key,value in zip(attributes,item):
        dic1.setdefault(key, value)
    result.append(dic1)


# expected output:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

result=[]
result=[dict(zip(attributes, value)) for value in values]
print(result)

# level
# expression1 if condition else expression2 for item in iterable
# => for item in iterable:
#     if condition:
#         expression1
#     else:
#         expression2
# y=x+3

x=3
f=[value+3 if value>0 else -value+3 for value in range(-3,3) ]
print(f)
# 没有else
# expression for item in iterable if condition


# 双for
# expression for item in iterable if condition
# [(xx, yy) for xx in x for yy in y if xx != yy]
# =>
# l = []
# for xx in x:
#     for yy in y:
#         if xx != yy:
#             l.append((xx, yy))