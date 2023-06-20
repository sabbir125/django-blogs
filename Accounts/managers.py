from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
   

    def create_superuser(self,email,username,password,**othersField):

        othersField.setdefault("is_superuser",True)
        othersField.setdefault("is_staff",True)
        othersField.setdefault("is_active",True)
        if othersField.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        if othersField.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email,username,password, **othersField)


    def create_user(self,username,email,password,**othersField):
        if not email :
            raise ValueError(_("you must provide an email"))

        email = self.normalize_email(email)
        print(email)
        #create a model on BaseUserManager's User 
        #[ref https://stackoverflow.com/questions/51163088/self-model-in-django-custom-usermanager]
        user = self.model(email=email, username=username,**othersField)
        
        user.set_password(password)
        user.save()
        return user

 




        

