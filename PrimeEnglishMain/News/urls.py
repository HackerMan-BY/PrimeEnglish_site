from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name="news_home"),
    # path("<int:pk>/", views.news_full.as_view(), name='news_full'),
    path("<int:pk>/", views.news_full, name='news_full'),
    path("/create", views.create, name='create'),
    path("<int:pk>/update", views.news_update.as_view(), name='update'),
    path("<int:pk>/delete", views.news_delete.as_view(), name='delete')
]