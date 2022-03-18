from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('rev/<int:id>', views.rev, name="rev"),
    path('success', views.success, name="success"),
]
