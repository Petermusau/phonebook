from  django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='app'
urlpatterns=[
    path('',views.MemberListView.as_view(),name='index'),
    path('<int:pk>/delete',views.MemberDeleteView.as_view(),name='delete-member'),
    path('add-contact', views.MemberCreateView.as_view(), name='add-contact'),
    path('<int:pk>/update',views.MemberUpdateView.as_view(),name='update-member'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('register',views.regist, name='register'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
]