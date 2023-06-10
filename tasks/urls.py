from django.urls import path


from . import views

app_name = "tasks"

urlpatterns = [
    path("new_task/", views.new_task, name="new_task"),
    path("", views.index, name="index"),
    #path("<int:pk>/delete/", views.delete_task, name="delete"),
    path("delete/<int:pk>", views.delete_task, name="delete"),
    path("edit/<int:pk>/", views.edit_task, name="edit"),
    path("tags/", views.edit_tags, name="edit_tags"),
]
