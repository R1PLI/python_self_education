class MyClass(object):

    @classmethod
    def divide_by(cls, divider):
        try:
            return 42 / divider
        except ZeroDivisionError:
            print('Error by division by zero')

inst = MyClass.divide_by()

print(inst(21))
print(inst(0))