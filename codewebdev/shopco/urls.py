from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('faq/', views.faq, name='faq'),
    # path('filterpage/', views.filterpage, name='filterpage'),
]