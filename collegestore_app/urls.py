from django.urls import path
from . import views
app_name='collegestore_app'

urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('newpage', views.newpage, name='newpage'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),

]