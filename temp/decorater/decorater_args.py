import logging


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is runninig." % func.__name__)
            return func()
        return wrapper
    return decorator

@use_logging("warn")
def fo():
    print("I am fo.")

fo()