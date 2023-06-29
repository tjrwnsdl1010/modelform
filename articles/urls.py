from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name= 'create'),
    path('create2/', views.create2, name='create2'),
    path('<int:id>/', views.detail, name='detail'),

    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    
]
