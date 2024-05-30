from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view as AV

@AV()
def index(request):
    return HttpResponse("Hello there, Welcome to scropy")
    
@AV(http_method_names= ['GET', 'POST'])
def get_crops(request):
    """Display a list of all crops using GET methods
    """
    return("Hello world")