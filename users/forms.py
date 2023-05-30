from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import LoginForm 
from django import forms                                                                                                                                   
from .models import CustomUser                                                                                                                                          
from django.utils.translation import gettext_lazy as _                                                                                                                  


class AccountLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        return super(AccountLoginForm, self).login(*args, **kwargs)


class AccountSignUpForm(UserCreationForm):                                                                                                                                     
    email = forms.EmailField()                                                                                                                                          
    first_name = forms.CharField(max_length=50)                                                                                                                         
    last_name = forms.CharField(max_length=50)                                                                                                                          
    username = forms.CharField(max_length=50)                                                                                                                           
                                                                                                                                                                            
    class Meta:                                                                                                                                                         
        model = CustomUser                                                                                                                                              
        fields = ('first_name', 'last_name', 'username', 'email',)                                                                          
                                                                                                                                                                        
                                                                                                                                                                        
class CustomUserCreationForm(UserCreationForm):                                                                                                                         
                                                                                                                                                                        
    class Meta:                                                                                                                                                         
        model = CustomUser                                                                                                                                              
        fields = ('email',)                                                                                                                                             
                                                                                                                                                                        
                                                                                                                                                                        
class CustomUserChangeForm(UserChangeForm):                                                                                                                             
                                                                                                                                                                        
    class Meta:                                                                                                                                                         
        model = CustomUser                                                                                                                                              
        fields = ('email',)                                                                                                                                             
                                  

class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username',
        'phone','avatar',)

