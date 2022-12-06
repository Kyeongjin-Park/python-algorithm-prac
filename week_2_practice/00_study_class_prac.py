class Person:
    def __init__(self, param_name):
        print("hello", self)
        self.name = param_name

    def talk(self):
        print('안녕하세요, 저는', self.name, "입니다.")

person_1 = Person("solrasido")  # hello <__main__.Person object at 0x7fe600190760>
print(person_1.name)            # solrasido
person_1.talk()                 # 안녕하세요, 저는 solrasido 입니다.