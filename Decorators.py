# To Make Own Function
def Hello():
    print("Hello World");

# greet = Hello()
greet = Hello            #It's Gives Function location (<function Hello at 0x000001F21123A2A0>)
#print(greet)
del Hello
print(greet())



def Hello(func):
    func()

def greet():
    print("Still Here!!!")

a = Hello(greet)
print(a)


#Higher Order Functions HOC

def greet(func):
    func()

filter()
def greet2():
    def func():
        return 5
    return func



#Decorator
# def Hello():
#     print('Hello')

def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func

@my_decorator
def Hello():
    print('Hello')

@my_decorator
def bye():
    print('See You Later')
# bye()
# Hello()



def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func

def Hello():
    print('Hello')

def bye():
    print('See You Later')

# Hello2 = my_decorator(Hello)
# Hello2()
my_decorator(Hello)()


#Decorator Pattern

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func

@my_decorator
def Hello(Greeting, emoji =':('):
    print(Greeting, emoji)

# Hello('Hey,Hello')

Hello('Hiii') 


#Why do we need Decorator
"""
@classmethod
@staticmethod
"""


from time import time 
def performance(fn):
   def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time() 
        print(f"took {t2 - t1} s")
        return result
   return wrapper


@performance 
def long_time():
    for i in range(100000000 ):
        i * 5

long_time()
