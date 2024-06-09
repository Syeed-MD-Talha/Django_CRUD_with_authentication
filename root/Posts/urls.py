from django.urls import path 
from .import views
urlpatterns = [
    path('create/',views.PostCreate,name='create_post'),
    path('edit/<int:id>/',views.edit_post,name='edit_post'),
    path('delete/<int:id>/',views.delete_post,name='delete_post'),
    path('',views.PostView,name='view_post')
]
