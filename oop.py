class my_obj:
    def __init__(self):
        self.id=1
        self.name='f'


obj = my_obj()
print(obj.name)


def my_iter():
    for i in range(10):
        # yield send发送到yield前面的值
        j = yield i*2
        if(j==8):
            print('BIBI')


my = my_iter()
print(next(my))
print(next(my))

print(my.send(8))
# print(next(my))
