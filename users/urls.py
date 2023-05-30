from django.urls import path
from .views import user_account, account_update

urlpatterns = [
    path('user_accouunt/', user_account, name='user_account'), 
    path('account_update/<int:pk>/',  account_update, name='account_update'),
]
