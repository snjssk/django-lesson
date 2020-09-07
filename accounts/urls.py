from django.urls import path
from . import views

## name=detail, resultsなど名前被らないよう名前空間をつける
app_name = 'accounts'

urlpatterns = [

    # ex: /accounts/signup/
    path('signup/', views.SignUpView.as_view(), name='signup'),

]