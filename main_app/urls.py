from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("explore/", views.explore, name="explore"),
    path("povs/", views.pov_index, name="pov-index"),
    path("povs/<int:pov_id>/", views.pov_detail, name="pov-detail"),
    path("povs/create/", views.CreatePost.as_view(), name="create-post"),
    path("povs/<int:pk>/update/", views.UpdatePost.as_view(), name="update-post"),
    path("povs/<int:pk>/delete/", views.DeletePost.as_view(), name="delete-post"),
    path("accounts/signup/", views.signup, name="signup"),
]
