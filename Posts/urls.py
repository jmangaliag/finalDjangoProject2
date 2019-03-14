from django.urls import path, include
from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:post_id>', views.update, name='update'),
    path('post/<int:post_id>/delete', views.delete, name='delete'),
    path('signup', views.signup, name='signup')
]
