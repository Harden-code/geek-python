# 序列分解成单独变量
p = (1, 1)
x, y = p
print(x, y)

mp = (1, 2, 4, 'S', (1, 2, 3))

num1, num2, num3, s4, d = mp

print(num1, num2, num3, s4, d)
# 通过简单赋值,分解
num1, num2, num3, s4, (d1, d2, d3) = mp
print(num1, num2, num3, s4, d1, d2, d3)

# *解压可迭代变量赋值
l=[1,2,3,4,5,6]
*head,tail=l
print(head)

# 使用deque保留最后几位
from collections  import deque
d=deque(maxlen= 2)

d.append(1)
d.append(2)
d.append(3)
d.append(4)
for ele in d:
    print(ele)

# 找最大值和最小值
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 求最大
print(heapq.nlargest(3,nums))
# 求最小
print(heapq.nsmallest(3,nums))
#  优先级队列
print(heapq.heapify(nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# heapq实现优先级队列
# heapq.heappush() push
# heapq.heappop()  pop
# 元组的比较

# 字典中映射多个键
from collections import defaultdict
# 效果dic={'a':[],'b':[]}
# 参数是list对象
d=defaultdict(list)
d['A'].append('1')

# 字典排序


### 命名切片
record = '....................100 .......513.25 ..........'
# slice 创建一个切片
shares=slice(20,23)
price=slice(31,37)

# print(type(record[shares]))
const=int(record[shares])*float(record[price])
print(const)

a=slice(5,50,2)
s = 'HelloWorld'
# 将它映射到一个已知大小的序列上,返回一个三元组 (start, stop, step)
a.indices(len(s))

print(*a.indices(len(s)))
#  * 分解元组
for i in range(*a.indices(len(s))):
    print(i,s[i])
