from django.urls import path,include
from. import views

urlpatterns = [
    
    path('home',views.home,name='home'),
    path('service',views.service,name='service'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('<str:slug>',views.blogpost,name='blogpost')
]