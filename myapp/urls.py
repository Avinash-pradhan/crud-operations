from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('form/', views.form_view, name='form'),
    path('articles/', views.articles_view, name='articles'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    

]
