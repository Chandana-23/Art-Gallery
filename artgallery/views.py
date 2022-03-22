from django.shortcuts import render

from .models import Colour, Cross, Doodle, Graphite

# Create your views here.
def home(request):
    colour = Colour.objects.all()
    cross = Cross.objects.all()
    graphite = Graphite.objects.all()
    doodle = Doodle.objects.all()
    return render(request,'index.html',{'colour':colour,'cross':cross,'graphite':graphite,'doodle':doodle})

