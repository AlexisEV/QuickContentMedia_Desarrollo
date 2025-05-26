
ROUTES = {}

def route(path, method="GET"):
    method = method.upper()
    def decorator(func):
        ROUTES[(method, path)] = func
        return func
    return decorator

def get_handler(method, path):
    return ROUTES.get((method.upper(), path))

def redirect(location, cookies=None):
    return {
        "redirect": True,
        "location": location,
        "cookies": cookies or {}
    }