from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def django(request):
    return render(request, 'django.html')

def python(request):
    return render(request, 'python.html')   

def mvt(request):
    return render(request, 'mvt.html')

