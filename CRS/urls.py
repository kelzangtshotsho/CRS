from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),

	path('photo/<str:pk>', views.viewPhoto, name='photo'),

	path('add/', views.addPhoto, name='add'),

	path('rent/', views.rentcar, name='rent'),

	path('comfirm/', views.comfirm, name='comfirm'),


	
]