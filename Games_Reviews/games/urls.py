from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name="main"),
    path('profile/', views.profile_view, name="profile"),
    path('register/', views.register_view, name="register"),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('game/<int:game_id>/add_review/', views.add_review, name='add_review'),
    path('rating/', views.rating_view, name='rating'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)