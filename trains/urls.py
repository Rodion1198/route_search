from django.urls import path

from . import views

app_name = 'trains'

urlpatterns = [
    path('', views.TrainListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.TrainDetailView.as_view(), name='train-detail'),
    path('create/', views.TrainCreateView.as_view(), name='train-create'),
    path('update/<int:pk>/', views.TrainUpdateView.as_view(), name='train-update'),
    path('delete/<int:pk>/', views.TrainDeleteView.as_view(), name='train-delete'),
]
