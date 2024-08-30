from .views import TodoListView, TodoDetailView
from django.urls import path

urlpatterns = [
    path('todos', TodoListView.as_view()), # get tenant profile by id
    path('todos/<int:id>', TodoDetailView.as_view()), # get tenant profile by id
    
    # path('todos/<int:id>', TodoAPIView.update), # update tenant profile by id
    # path('todos/<int:id>', TodoAPIView.delete),  # archive tenant profile by id
]