#!/usr/bin/env python
# A function decorator to require auth on Flask pages
# See here: http://flask.pocoo.org/snippets/8/
# http://thecodeship.com/patterns/guide-to-python-function-decorators/
from functools import wraps
from flask import Response, request

def notAuthorized():
    #Sends a 401 response that enables basic auth
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(username, password):
    def auth_decorator(func):
        @wraps(func)
        def func_wrapper(*flask_args, **flask_kwargs):
            auth = request.authorization
            if not auth or (auth.username != username) or (auth.password != password):
                return notAuthorized()
            return func(*flask_args, **flask_kwargs)
        return func_wrapper
    return auth_decorator
