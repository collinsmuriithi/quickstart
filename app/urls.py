
from django.urls import path


from .import views
app_name = 'app'

urlpatterns=[
    path('', views.home ,name='home'),
    path('services/', views.services,name='services'),
    path('starter/', views.starter,name='starter'),

]