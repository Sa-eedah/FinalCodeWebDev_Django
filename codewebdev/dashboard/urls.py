from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_index, name='index'),
    path('<int:item_id>/', views.dashboard_detail, name='detail'),
]
