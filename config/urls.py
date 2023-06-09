from users.views import account_signup_view, account_login_view
from django.contrib import admin                                                
from django.contrib.auth import views as auth_views                             
from django.urls import path, include                                           
from django.conf.urls.static import static                                      
from django.conf import settings                                                


urlpatterns = [                                             
    path('admin/', admin.site.urls),                 
    path('accounts/login/', view=account_login_view),
    path("accounts/signup/", view=account_signup_view),                                                                                                                 
    path('accounts/', include('allauth.urls')),                 
    path('users/', include('users.urls')), 
    path('', include('home.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),                                                                     
         name='password_reset'),                                                
    path('password-reset/done/',                                                
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),                                           
    path('password-reset-confirm/<uidb64>/<token>/',                            
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),                                                                     
         name='password_reset_confirm'),                                        
    path('password-reset-complete/',                                            
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),                                                                     
         name='password_reset_complete'),                                       
]                                                                               
                                                                                
if settings.DEBUG:                                                              
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

