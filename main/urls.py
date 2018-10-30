from django.urls import path

from .views import (
    TodoCreateView, TodoUpdateView, IndexView, TodoDetailView, TodoJsonView, TodoDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/update', TodoUpdateView.as_view(), name='todo_update'),
    path('todo/json/', TodoJsonView.as_view(), name='todo_json'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name='todo_delete'),
]
