# users/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:

    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path starts with '/admin' (use 'startswith' to match all subpages)
        if request.path.startswith('/admin'):
            # Skip the check if the user is authenticated, if not, redirect them to login page
            if not request.user.is_authenticated:
                return redirect('login')  # Redirect to the login page

        response = self.get_response(request)
        return response
