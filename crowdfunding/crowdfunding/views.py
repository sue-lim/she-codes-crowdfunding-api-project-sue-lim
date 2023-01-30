from django.shortcuts import render
from django.http import JsonResponse

def custom404(request, exception=None):
    return JsonResponse({
        'Status_code': 404,
        'Error': 'Sorry the page you are looking for does not exist. Please contact admin to log issue admin@admin '
    })
    
# def custom500(request, exception=None):
#     return JsonResponse({
#         'Status_code': 500,
#         'Error': 'Sorry the page you are looking for does not exist. Please contact admin to log issue admin@admin '
#     })