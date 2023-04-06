from django.shortcuts import get_object_or_404
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (WatchListAV, WatchListDetailAV, StreamPlatformAV,
                    StreamPlatformDetailAV, ReviewList, ReviewDetail,
                    ReviewCreate, StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('watchlist/', WatchListAV.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', WatchListDetailAV.as_view(),
         name='watchlist-detail'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),
    #     name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail")

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail")

]
