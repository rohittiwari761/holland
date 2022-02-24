from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('dealer/',views.dealer_auth,name='dealer_auth'),
path('crops/',views.crops,name='crops'),
path('about/',views.about,name='about')
]
