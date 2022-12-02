from django.urls import path
from . import views
from .views import accountDeleteView

urlpatterns = [
    path('all/', views.ProfileListView.as_view(), name='profile-list-view'),
    path('follow/', views.follow_unfollow_profile, name='follow-unfollow-view'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
    path('public-profile/<str:username>/', views.public_profile, name='public-profile'),
    path('delete/<int:pk>', accountDeleteView.as_view(), name='account-delete'),
   
]