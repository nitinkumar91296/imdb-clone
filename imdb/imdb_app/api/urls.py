from django import views
from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from imdb_app.api.views import movie_list, movie_details # for function views
from imdb_app.api.views import ReviewCreate, ReviewDetails, ReviewList, StreamPlatformDetailAV, StreamPlatformVS, WatchDetailAV, WatchListAV, SteamPlatformListAV, StreamPlatform

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('', include(router.urls)),
    
    # path('stream/', SteamPlatformListAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
        
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetails.as_view(), name='review-detail')
    
]
