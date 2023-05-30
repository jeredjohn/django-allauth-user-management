from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin                                                                                                                                                       
from django.db import models                                                                                                                                                                                                    
from django.conf import settings 
from django.dispatch import receiver
from django.utils import timezone                                                                                                                                                                                               
from django.utils.translation import gettext_lazy as _                                                                                                                                                                          
from .managers import CustomUserManager
from django.urls import reverse
from django.core.validators import RegexValidator                                                                                                                                                                               
                                                                                                                                                                                                                                
phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")                                                                    
                                                                                                                                                                                                                                
class CustomUser(AbstractBaseUser, PermissionsMixin):                                                                                                                                                                           
    email = models.EmailField(_('email address'), null=True, blank=True, unique=True)                                                                                                                                           
    is_staff = models.BooleanField(default=False)                                                                                                                                                                               
    is_active = models.BooleanField(default=True)                                                                                                                                                                               
    date_joined = models.DateTimeField(default=timezone.now)                                                                                                                                                                    
    first_name = models.CharField( max_length=50, null=True)                                                                                                                                                                    
    last_name = models.CharField( max_length=50, null=True)                                                                                                                                                                     
    username = models.CharField(max_length=50, unique=True)                                                                                                                                                                     
    phone = models.CharField(max_length=20, validators=[phone_validator], null=True, blank=True, unique=True)                                                                                                                   
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.jpg')                                                                                                                                              
                                                                                                                                                                                                                                
    USERNAME_FIELD = 'username'                                                                                                                                                                                                 
    REQUIRED_FIELDS = ['email',]                                                                                                                                                                                        
                                                                                                                                                                                                                                
    objects = CustomUserManager()                                                                                                                                                                                               
                                                                                                                                                                                                                                
    def __str__(self):                                                                                                                                                                                                          
        return f"{self.username}"      
    
    def get_absolute_url(self):                                                                                                       
        return reverse('account_detail', kwargs={'pk': self.pk}) 

    def format_phone(self, phone=None):
        phone = str(self.phone)
        format_ph = phone[0:3] + "-" + phone[3:6] + "-" + phone[6:10]
        return format_ph
        
