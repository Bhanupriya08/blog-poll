from django.contrib import admin
from django.urls import path,include
from . import views


app_name = "myblog"

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('new/', views.post_new, name='post_new'),
	path('<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('<int:pk>/', views.post_detail, name='post_detail'),
	path('<int:pk>/vote/', views.vote, name='vote'),
	
]