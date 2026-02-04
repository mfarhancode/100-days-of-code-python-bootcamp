import art
# print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def new_calculation():
    print(art.logo)
    n1 = float(input("What's the first number?: "))
    oper = input("""+
    -
    *
    /
    Pick an operation: """)
    n2 = float(input("What's the next number?: "))
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    result = operations[oper](n1, n2)
    print(f'{n1} {oper} {n2} = {result}')
    return result

def again_calculate(oper, result, n2):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    new_result = operations[oper](result, n2)
    print(f'{result} {oper} {n2} = {new_result}')
    return new_result
def calculator():
    run = True
    while run:
        result = new_calculation()
        ask = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if ask == 'y':
            continue_calc = True
            while continue_calc:
                oper = input("""+
                -
                *
                /
                Pick an operation: """)
                n2 = float(input("What's the next number?: "))
                operations = {
                    '+': add,
                    '-': subtract,
                    '*': multiply,
                    '/': divide
                }
                new_result = again_calculate(oper,result, n2)
                result = new_result
                ask = input(f"Type 'y' to continue calculating with {new_result}, or type 'n' to start a new calculation: ").lower()
                if ask == 'n':
                    continue_calc = False

calculator()
def function():
    n = int(input('What is n? '))
    repeat = True
    while repeat:
        result = n + 1
        print(result)
        ask = input(f' n is {result}. Want new value for n or want to add 1 again in it?(y for again add 1, n for new value)').lower()
        if ask == 'n':
            function()
        else:
            n = result
# function()
