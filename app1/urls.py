from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.upload_pic,name='homepage'),
    path('final/',views.final,name='final_image'),
    path('aiml/',views.upload1,name='upload'),
]