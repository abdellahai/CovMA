from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager (BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Email is mandatory')
        if not username:
            raise ValueError('Username is mandatory')
        user = self.model(email = self.normalize_email(email), username = username)
        user.set_password(password)
        user.save(using =self._db)
        return user
    def create_superuser(self,email,username,password):
        user = self.create_user(email = self.normalize_email(email), username = username, password=password)
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using =self._db)
        return user

class User (AbstractBaseUser):
    email = models.EmailField(verbose_name = 'email', max_length=60, unique = True)
    username = models.CharField(max_length=30, unique = True)
    date_join = models.DateTimeField(verbose_name = 'Joining date', auto_now_add=True)
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField (default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email
    def has_perm (self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_Label):
        return True
class Chercheur(models.Model):
    firs_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField( max_length=50)
    add_date = models.DateTimeField(auto_now_add=True)
    affiliation = models.TextField()

    

    # class Meta:
    #     verbose_name = _("Chercheur")
    #     verbose_name_plural = _("Chercheurs")

    def __str__(self):
        return self.firs_name

    # def get_absolute_url(self):
    #     return reverse("Chercheur_detail", kwargs={"pk": self.pk})

