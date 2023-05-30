from django.contrib import admin                                                                                                                                        
from django.contrib.auth.admin import UserAdmin                                                                                                                         
from .forms import CustomUserCreationForm, CustomUserChangeForm                                                                                                         
from .models import CustomUser                                                                                                                                          
                                                                                                                                                                        
                                                                                                                                                                        
class CustomUserAdmin(UserAdmin):                                                                                                                                       
    add_form = CustomUserCreationForm                                                                                                                                   
    form = CustomUserChangeForm                                                                                                                                         
    model = CustomUser                                                                                                                                                  
    list_display = list_display = ('username', 'email', 'phone',
                                   'is_staff', 'first_name', 'last_name',)                                                                
    list_filter = ('email', 'is_staff', 'is_active', 'last_name',)                                                                                                      
    fieldsets = (                                                                                                                                                       
        (None, {'fields': ('username', 'email', 'password', 'phone',)}),                                                                                                
        ('Personal Info', {'fields': ('first_name', 'last_name',)}),                                                                                      
        ('Profile Pic',  {'fields': ('avatar',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),      
    )                                                                                                                                                                   
    add_fieldsets = (                                                                                                                                                   
        (                                                                                                                                                               
            None,                                                                                                                                                       
            {                                                                                                                                                           
                'classes': ('wide',),                                                                                                                                   
                'fields': (                                                                                                                                             
                    'username', 'email', 'first_name',
                    'last_name', 'password1', 'password2',                                                                           
                )                                                                                                                                                       
            }                                                                                                                                                           
        ),                                                                                                                                                              
    )                                                                                                                                                                   
    search_fields = ('email', 'username', 'last_name', 'first_name', 'phone',)                                                                                          
    ordering = ('username', 'email', 'last_name', 'first_name',)                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
admin.site.register(CustomUser, CustomUserAdmin)
