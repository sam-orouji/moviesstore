from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='dashboard.index'),
    path('top-purchaser/', views.top_purchaser, name='dashboard.top_purchaser'),
    path('top-commenter/', views.top_commenter, name='dashboard.top_commenter'),
]