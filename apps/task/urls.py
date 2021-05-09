from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [

    path('', views.TaskView.as_view(), name='task'),
    path('complete/<int:pk>', views.completed, name='complete'),
    path('manager/', views.ManagerDash.as_view(), name='manager-dash'),
    path('manager/<int:pk>', views.ManagerProjectDetail.as_view(), name='manager-task'),

]
