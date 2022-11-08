from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_app),
    path('<int:id>/', views.num_page_view),
    path('<str:topic>/', views.news_view, name="topic-page"),
    path('<int:num1>/<int:num2>/', views.add_view)
]
