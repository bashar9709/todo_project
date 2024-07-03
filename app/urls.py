from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('add/',views.Task_add,name='add'),
   path('delete_task/<int:id>/',views.task_delete,name='delete'),
   path('details_task/<int:id>/',views.Task_Details.as_view(),name='details'),
   path('edit/<int:id>/',views.complete_editTask,name ='edit_task'),
   path('complete/<int:id>/',views.CompletedTask,name ='complete'),
   path('see_completed_task',views.Completed_Task_show,name ='see_completed_task'),
]
