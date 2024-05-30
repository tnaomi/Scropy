"""`Web` views
"""


from django.shortcuts import render
from api.models import Crops
from django.db.models import Q

def index(request):
    """ `Index` view for the `web` module
    """
    crops = Crops.objects.all()
    crop_count = 0
    for crop in crops:
        crop_count += 1
    return render(request, "index.html", {"crop_count": crop_count}) #CHANGE

def get_crops(request):
    """ Get crops and return a single page """
    crops = Crops.objects.all()
    return render(request, "crops.html",{"crops": crops})
    