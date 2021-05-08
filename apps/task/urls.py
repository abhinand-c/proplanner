from django.urls import path
from . import views

urlpatterns = [

    path('', views.TaskView.as_view(), name='task'),
    path('manager/', views.ManagerDash.as_view(), name='manager-dash'),
    path('manager/<int:pk>', views.ManagerProjectDetail.as_view(), name='manager-dash'),

]
