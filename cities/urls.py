from django.urls import path

from . import views

app_name = 'cities'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.CityListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='city-detail'),
    path('create/', views.CityCreateView.as_view(), name='city-create'),
    path('update/<int:pk>/', views.CityUpdateView.as_view(), name='city-update'),
    path('delete/<int:pk>/', views.CityDeleteView.as_view(), name='city-delete'),
]
