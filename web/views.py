"""`Web` views
"""


from django.shortcuts import render
from api.models import Crops, Zone, Districts
import uuid

def index(request):
    """ `Index` view for the `web` module
    """    
    crop_count = Crops.objects.count()
    return render(request, "home.html", {"crop_count": crop_count}) #CHANGE

def about(request):
    """Displays the landing page"""
    return render(request, "about.html")

def gen_uuid(request):
    """ Generate UUID for static files """
    u_id = uuid.uuid4()
    return render(request, "index.html",{"u_id": u_id})
    

def get_crops(request):
    """ Get all crops and return on a single page """
    if request.method == "POST":
        search = request.POST["query"]
        if search == "All":
            crops = Crops.objects.all()
        else:   
            crops = Crops.objects.filter(name__contains=search)
    else:
        search = None
        crops = None
    return render(request, "crops.html",{"search": search, "crops": crops})

def get_crop_by_id(request, id):
    """ Display a single crop's info """
    single = Crops.objects.get(id=id)
    consumers = single.consumed_in.all()
    return render(request, "crop.html", {'single': single, 'consumers': consumers})
    
def get_zone_by_id(request, id):
    """ Display a single Zone info """
    zone = Zone.objects.get(name=id)
    dists = zone.districts.all()
    return render(request, "zone.html", {'zone': zone, 'dists': dists})