from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url,include
from .models import Location, Category, Image

'''End Of Import'''
#---------------------------------------------------------------------#


# VIEW FUNCTIONS HERE!



#################################################################################################################################################################################
#INDEX PAGE VIEW FUNCTION
#################################################################################################################################################################################

#INDEX Page View Function!
def index(request):
    all_images = Image.objects.all()
    context = {'all_images': all_images}
    return render(request,'base.html',{'all_images':all_images})

#################################################################################################################################################################################
#LOCATION PAGE VIEW FUNCTION
#################################################################################################################################################################################

#LOCATION Page View Function!
def location(request):

    return render(request,'location.html',)

#################################################################################################################################################################################
#CATEGORY PAGE VIEW FUNCTION
#################################################################################################################################################################################

#CATEGORY Page View Function!

def category(request):
    return render(request,'category.html',)

#################################################################################################################################################################################
#SEARCH CAPABILITY PAGE VIEW FUNCTION
#################################################################################################################################################################################

#SEARCH CAPABILITY Page View Function!

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categorys": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

#################################################################################################################################################################################