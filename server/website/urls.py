from django.urls import path, include
from . import views


# Basic structure for now, will revisit for better organization later
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('oauth/', include('allauth.urls')),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('delete_ticket/<int:pk>', views.delete_ticket, name='delete_ticket'),
    path('my_tickets/<int:pk>', views.my_tickets, name='my_tickets'),
    path('update_ticket/<int:pk>', views.update_ticket, name='update_ticket'),
    path('buy_ticket/<str:f>', views.buy_ticket, name='buy_ticket'),
    path('facility/', views.facility, name='facility'),
]

