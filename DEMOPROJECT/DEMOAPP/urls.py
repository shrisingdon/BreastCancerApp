from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='home-page'),
    path('demo', views.demo, name='demo'),
    path('result/', views.result, name='result'),
    path('malignant', views.malignant, name='malignant'),
    path('benign', views.benign, name='benign'),
]


