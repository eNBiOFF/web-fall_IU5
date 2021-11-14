def print_result(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__)
        if type(res) is dict:
            for key in res:
                print('{} = {}'.format(key, res[key]))
        if type(res) is list:
            [print(i) for i in res]
        if (type(res) is not list) & (type(res) is not dict):
            print(res)
        return res
    return wrapper





