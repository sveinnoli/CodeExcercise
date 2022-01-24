import functools
users = {"Pete":"123", "Kyle" : "456"}

def is_authenticated(func):
    functools.wraps(func)
    def wrapper_is_authenticated(*args, **kwargs):
        if [user for user in args if user in users]:
            return func(*args, **kwargs)
        return "Not Authorized"
    return wrapper_is_authenticated

def access_denied():
    return "Access Denied"

@is_authenticated
def access_site(user):
    return "Site"

print(access_site("Pete"))

print(access_site("james"))
