'''
01 类定义
'''
class Player():
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    def print_role(self):
        print('%s: %s' %(self.__name, self.__hp))

    def update_name(self, new_name):
        self.__name = new_name

user_a = Player('tom', 100)
user_b = Player('jerry', 90)

user_a.print_role()
user_b.print_role()

user_a.print_role()
user_a.update_name('dddd')
user_a.print_role()

'''
02 类继承
'''
class Monster():
    def __init__(self, hp):
        self.hp = hp
    def run(self):
        print('移动到某个位置')

class Animals(Monster):
    def __init__(self, hp):
        super().__init__(hp)

class Boss(Monster):
    pass

a1 = Monster(200)
a1.run()

a2 = Animals(10)
a2.run()

print(isinstance(a2, Animals))