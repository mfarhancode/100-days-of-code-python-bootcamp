
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(10,2,3,4))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

# calculate(7, add=4, multiply=2)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')

my_car = Car(make='Nissan', seats=4)
print(my_car.make)
print(my_car.model)
print(my_car.seats)