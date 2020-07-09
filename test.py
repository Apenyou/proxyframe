
def log(func):
    def wrapper(*args, **kw):
        # print('call %s():' % func.__name__)
        print(args[0])
        return func(*args, **kw)
    return wrapper

@log
def testdel(a):
    print(123123123)

testdel(6666)