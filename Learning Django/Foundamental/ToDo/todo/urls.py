from django.urls import path

from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.Mark_As_Done, name='mark_as_done'),
    path('edit_task/<int:pk>/', views.Edit_Task, name='edit_task'),
    path('delete_task/<int:pk>/', views.Delete_Task, name='delete_task'),
    path('undo_task/<int:pk>/', views.Undo_Task, name='undo_task'),
]
