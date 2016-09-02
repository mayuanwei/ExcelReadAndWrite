
def log(arg):
    if hasattr(arg,'__call__') is False:
        def decorator(func):
            def wrapper():
                print('begin call',arg)
                func()
                print('end call',arg)
                #return func()
            #print('begin call')
            return wrapper
        return decorator

    else:
        def wrapper():
            print('begin call', 'function')
            arg()
            print('end call', 'funcion')
        return wrapper


@log('123')
def xxx():
    print('mayuanwei')

@log
def yyy():
    print('yujie')

#log(xxx)()
xxx()
yyy()
