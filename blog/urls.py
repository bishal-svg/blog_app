from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('blog/view/<int:id>',views.view_blog,name='view_blog'),
    path('blog/new',views.create_blog,name='create_blog'),
    path('blog/edit/<int:id>',views.edit_blog,name='edit_blog'),
    path('blog/delete/<int:id>',views.delete_blog,name='delete_blog')

]

