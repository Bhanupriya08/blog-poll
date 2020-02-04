from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('poll/',views.poll,name='poll'),
	path('new/', views.post_new, name='post_new'),
	path('poll/<int:question_id>/vote/', views.vote, name='vote'),
	path('poll/<int:question_id>/results/',views.poll_result,name='poll_result'),
	path('<int:pk>/detail/', views.post_detail, name='post_detail'),
	path('<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('poll/<int:question_id>/',views.poll_detail,name='poll_detail'),
	


]