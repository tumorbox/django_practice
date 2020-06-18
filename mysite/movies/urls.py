from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movies, name="movies"),
    path('new/', views.form, name="form"),
    path('<int:movie_pk>/', views.detail, name="detail"),
    path('<int:movie_pk>/update/', views.update, name="update"),
    path('<int:movie_pk>/delete/', views.delete, name="delete"),

]