routes_get = {}
routes_post = {}

def route_get(path):
    def decorator(func):
        routes_get[path] = func
        return func
    return decorator

def route_post(path):
    def decorator(func):
        routes_post[path] = func
        return func
    return decorator
