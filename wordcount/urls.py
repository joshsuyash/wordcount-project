
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('COUNT/',views.COUNT , name='COUNT'),
    path('Newcount/',views.Newcount , name='NEWCOUNT'),
]
