
class Human(object):
    def __init__(self, *args, **kwargs):
        for arg in args:
            print(arg)
        for arg_name, arg_value in kwargs.items():
            print(arg_name + ': ' + arg_value)


class Man(Human):
    def __init__(self, name):
        self.name = name
        print(name + ' M')
        super(Man, self).__init__(name)

class Woman(Human):
    def __init__(self, name):
        self.name = name
        print(name + ' W')
        super(Woman, self).__init__(name)

class Programmer(object):
    def __init__(self, name, lang):
        man = Man(name)
        lang = lang

    def get_name(self):
        return self.man.get_name()

human = Human(
    *['First', 'second', 3 , 5],
    **{'prog': 'Vasya'}
)
