# Example of *args (Arbitrary Positional Arguments)

def concatenate(*strings,sep=''):
    '''This function returns the string by concatenating all the given strings as arguments.'''
    string = ''
    for index, s in enumerate(strings):
        string += str(s)
        if index != len(strings)-1:
            string += sep
    return string

# print(concatenate('a','b','c','d',sep='-'))


# Example of **kwargs (Arbitrary Keyword Arguments)
class Student:
    def __init__(self, **data):
        self.name = data.get('name')
        self.age = data.setdefault('age', 00)
        self.country = data.get('country')

# s = Student(name='farhan')
# print(s.name)
# print(s.age)
