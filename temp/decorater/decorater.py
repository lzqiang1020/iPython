def logger(fn):
    def wrapper(*args, **kwargs):
        """Function: wrapper """

        print("start")
        ret = fn(*args, **kwargs)
        print("end")
        return ret
    return wrapper

@logger
def add(x, y):
    """
    Function: add
    return int
    :x int
    :y int
    """

    return x + y