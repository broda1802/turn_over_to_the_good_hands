from django.contrib.auth.views import LogoutView
from django.urls import path


from .views import SignUpView, UserUpdateView, UserPasswordChangeView, UserPasswordResetView, Login

urlpatterns = [

    path('change_password/', UserPasswordChangeView.as_view(), name='change_password'),
    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
]