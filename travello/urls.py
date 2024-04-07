from django.urls import path

from. import views

urlpatterns=[
    path('',views.index, name='index'),
    path('index.html', views.index),

    path('', views.contact, name='contact'),
    path('contact.html', views.contact),

    path('', views.searchBar, name='searchBar'),
    path('searchBar.html', views.searchBar)

    

]
