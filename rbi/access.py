from brgy.models import UserBarangay
from django.contrib import messages
from django.http import request
from django.shortcuts import redirect
from functools import wraps
from rbi.models import Barangay


def barangay_access(message="Not Authorized", redirect_url="/home"):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            b=userbrgy(request.user)
            lst = UserBarangay.objects.filter(user=request.user).values_list('user__username', flat=True)
            if b:
                # if request.user.username in list(lst):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, message)
                return redirect(redirect_url)
        return _wrapped_view
    return decorator


def userbrgy(usr):
    ub=UserBarangay.objects.filter(user=usr).values_list('brgy__id',flat=True)
    if ub:
        return ub
    else:
        return [0,0]




# def restrict_mpoc(message="Not Authorized", redirect_url="/home"):
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):
#             lst = ViewAccess.objects.filter(page=1).values_list('user__username', flat=True)
#             if request.user.username in list(lst):
#                 return view_func(request, *args, **kwargs)
#             else:
#                 messages.error(request, message)
#                 return redirect(redirect_url)
#         return _wrapped_view
#     return decorator

