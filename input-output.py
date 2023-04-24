# 阻塞当前，等待stdin的输入
def input_demo():
    name = input("name:")
    gender = input("y or n")
    print(name)

    welcome_str = 'Welcome to the matrix {prefix} {name}.'
    welcome_dic = {'prefix': 'Mr.' if gender == 'y' else 'Mrs', 'name': name}
    # When a final formal parameter of the form **name is present, it receives a dictionary
    print(welcome_str.format(**welcome_dic))


file_path = 'C:\\Users\\Administrator\\Desktop\\temp\\temp.txt'
path = 'C:\\Users\\Administrator\\Desktop\\temp'


def read_demo():
    # readline => 读取某行  read => 读取所有,可以加个limit限制读取大小
    with open(file_path, 'r') as file:
        # for line in file:
        #     print(line)
        print(file.read(11))


import json
def write_to_str():
    params = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
    # dic => str
    json_str = json.dumps(params)

    with open(path + '\\json', 'w') as wfile:
        wfile.write(json_str)


def read_file():
    with open(path + '\\json', 'r') as rfile:
        str = rfile.read()
        # 解析json
        dic = json.loads(str)
        print(type(dic))
        # 遍历map 使用items
        ele = dic.items()
        for key, val in ele:
            print(key, val)


# write_to_str()
read_file()


