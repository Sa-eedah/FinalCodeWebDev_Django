from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter_page, name='filter'),
    # path('faq/', views.faq, name='faq'),
    
]