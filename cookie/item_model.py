arr=[1,2,3]
# 使用no for 模式遍历，当遍历到没有元素时会抛出 StopIteration
it=iter(arr)
# print(next(it))
# print(next(it))
# print(next(it))

# 迭代器 send 用法,调用后会发送数据到yield前面的值
def item_send():
    for _ in range(3):
        j=yield _
        print(j,_)

n=item_send()
next(n)
n.send(4)
next(n)


