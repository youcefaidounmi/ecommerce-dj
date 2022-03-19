from django.urls import path
from . import views

 # included to main.urls
urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/',views.store, name='store_by_category')
]
