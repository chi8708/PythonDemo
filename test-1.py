
def add(a, b):
    return int(a) + int(b)


num = 1
while num <= 10:
    print(num)
    num += 1


for i in range(1, 11):
    print("for测试:%s" % i)

# 字典
dic1 = {"key1": "value1", 2: "value2"}
for k, v in dic1.items():
    print("%s→%s" % (k, v))

# 列表
list=[1, 2, 3]
for i in list:
    print(i)


# 类
class Person():
    '人'

    # 公共变量
    first_name = "TK"

    def __init__(self, name, age, gender=1):
        self.Name = name
        self.Age = age
        self._privateGender = gender

    def Gender(self):
        return self._privateGender

    def SayHello(self):
        print('hello,My name is %s,%s' % (self.Name, self.Age))

    @property
    def Name(self):
        # 如果返回大写Name 报错maximum recursion depth exceeded
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    # 私有方法 下划线
    def _getAge(self):
        return self.Age


class Teacher(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    @property
    def Level(self):
        return self._level

    @Level.setter
    def Level(self, level):
        self._level = level


p = Person('jack', 12, 1)
print(p)
p.Name = "rose"
p._name = 'sss'
print(p._name)
Person.first_name = 'df'
p.first_name = 'idf'
print(Person.first_name)
p._privateGender = 0
print(p.Gender())
print(p._getAge())
p.SayHello()

t = Teacher('t1', 18)
t.Level = '教授'
print(t.Level)
t.SayHello()


i = input("输入数字1 ")
j = input("输入数字2 ")
print(add(i, j))
