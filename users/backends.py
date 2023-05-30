from django.contrib.auth.hashers import check_password                                                                                                                  
from users.models import CustomUser
from django.db.models import Q                                                                                                                                          
                                                                                                                                                                       
                                                                                                                                                                        
class EmailPhoneUsernameAuthenticationBackend(object):                                                                                                                  
    def authenticate(self, request, username=None, password=None):                                                                                                      
        try:                                                                                                                                                            
            user = CustomUser.objects.get(Q(username=username)\
                    | Q(phone=username) | Q(email=username))                                                                       
        except CustomUser.DoesNotExist:                                                                                                                                       
            return None                                                                                                                                                 
        if user and check_password(password, user.password):                                                                                                            
            return user                                                                                                                                                 
        return None                                                                                                                                                     
    def get_user(self, user_id):                                                                                                                                        
        try:                                                                                                                                                            
            return CustomUser.objects.get(pk=user_id)                                                                                                                         
        except CustomUser.DoesNotExist:                                                                                                                                       
            return None                                                                                                                                                 
                                                                                                                                                                      
                                                                                                                                                                       
                                                                                                                                                                       
                                                                                                                                                                       
                                                                                                                                                                       
                           
