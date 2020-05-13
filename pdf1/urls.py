from django.urls import path
from . import views

urlpatterns = [

    path('',views.BookListView.as_view(),name='home'),
    path('add/',views.AddBookView.as_view(),name='add')

]