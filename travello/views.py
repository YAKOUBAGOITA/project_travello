from django.shortcuts import render
from .models import Destination
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
     
  dests=Destination.objects.all()
   
  return render(request, "index.html", {'dests': dests})

def contact(request):
    return render(request, 'contact.html')

def searchBar(request):
   if request.method=="GET":
      query=request.GET.get('query')
      if query:
         dests=Destination.objects.filter(name__icontains=query)
         dests=Destination.objects.filter(price_icontains=query)
         return render(request, 'searchBar.html',{'dests':dests})
      else:
         print("no information to show")
         return request(request, 'searchBar.html', {})