import wrapt


def login_exempt(view_func):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        return wrapped(*args, **kwargs)

    wrapper.login_exempt = True
    return wrapper
