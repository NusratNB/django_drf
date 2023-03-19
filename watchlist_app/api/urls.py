from django.urls import path
from .views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList

urlpatterns = [
    path('watchlist/', WatchListAV.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', WatchListDetailAV.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('review/', ReviewList.as_view(), name='review-list')

]