from django.urls import path
from myapp import views

urlpatterns = [
    path('' , views.login_view , name="login"),
    path('register/' , views.register , name="register"),
    path('otp/<uid>/' , views.otp , name="otp"),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('logout/',views.user_logout, name='logout'),

    path('dl-form/',views.driving_licence, name='dl-form'),
    path('new/',views.new, name='new'),

    # #path('login-otp', login_otp , name="login_otp") 
]
