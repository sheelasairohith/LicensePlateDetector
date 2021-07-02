from django.shortcuts import render
from .forms import *
# Create your views here.
from django.conf import settings
import os
#from ./yolov4-custom-functions import detect
def hello_world(request):
    return render(request, 'upload_pic.html', {})
    
def upload_pic(request):
    context={}
    django_form= CustomerForm()
    if request.method =='POST':
        django_form= CustomerForm(request.POST,request.FILES)
        if django_form.is_valid(): 
            django_form.save()
            img=django_form.cleaned_data.get('profile_pic')
            print(img.name)
            a=img.name
            print('python detect.py --images '+'./static/images/'+a)
            print(type(img.name))
            # os.system('python detect.py --images '+'./static/images/'+str(img))
            try:
                os.system('python detect.py --images '+'./static/images/'+a)
            except:
                pass
            #return render(request,'final.html',{})
            return final(request)
          
    else:
        django_form=CustomerForm()
    return render(request,'upload_pic.html',{'form':django_form})
    
    
def final(request):
    return render(request, 'output.html', {})
    
def upload1(request):
    django_form= CustomerForm()
    if request.method =='POST':
        django_form= CustomerForm(request.POST,request.FILES)
        if django_form.is_valid(): 
            django_form.save()
            img=django_form.cleaned_data.get('profile_pic')
            print(img.name)
            a=img.name
            print('python detect.py --images '+'./static/images/'+a)
            print(type(img.name))
            try:
                os.system('python detect.py --images '+'./static/images/'+a)
            except:
                pass
            return final(request)
          
    else:
        django_form=CustomerForm()
    return render(request,'upload.html',{'form':django_form})

