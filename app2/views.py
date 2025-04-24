from django.shortcuts import render

# Create your views here.
def app2homepage(request):
    return render(request=request, template_name='app2homepage.html')

def app2temp(request):
    return render(request=request, template_name='app2temp.html')
