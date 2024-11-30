from flask import redirect, url_for
from functools import wraps
from flask_dance.contrib.github import github

def login_required(func):
    """
    Custom decorator for checking login
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        if not github.authorized:
            return redirect(url_for('public.home'))
        return func(*args, **kwargs)
    return decorated
