
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    # slug left path converter, right received paramits nly name
    path('<slug:slug>', views.post_page, name='page')
]