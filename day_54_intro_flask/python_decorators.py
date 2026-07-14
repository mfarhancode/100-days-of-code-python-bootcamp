import time

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calcluate(calculate_func, n1, n2):
    return calculate_func(n1, n2)

# result = calcluate(multiply, 12, 4)
# print(result)

# functions can be returned from another functions
def outer_func():
    print("I'm outer...")

    def inner_func():
        print("I'm inner...")
    
    return inner_func

# inner_function = outer_func()
# inner_function()


def delay_decorator(function: function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        print("-->Before...")
        print(function.__name__)
        function()
        print("-->After...")

    return wrapper_function

@delay_decorator
def say_hello():
    print('Hello...')

@delay_decorator
def say_bye():
    print('Byee...')

def say_greeting():
    print('How are you??')

# say_hello()

# ----------------------- speed_calc_decorator ------------------------

current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        # print(start_time)
        function()
        end_time = time.time()
        # print(end_time)
        run_speed = end_time - start_time
        print(f'{function.__name__} run speed:')
        print(run_speed)
    return wrapper_function
        
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()

slow_function()