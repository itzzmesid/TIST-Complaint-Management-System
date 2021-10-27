from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('menu')
            else:
                return view_func(request, *args, **kwargs)

    return wrapper_func

#This decorator is for only allowing admin to view the complaint dashboard
# def allowed_users(allowed_roles = []):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             print("Working")
#             return view_func(request, *args, **kwargs)
#         return wrapper_func
#     return decorator
