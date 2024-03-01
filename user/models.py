from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, tc, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, tc, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            tc=tc,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(max_length=255, verbose_name='Last Name')
    phone = models.CharField(max_length=255, verbose_name='Phone')
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)  
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'tc']

    def __str__(self):
        return self.email
    
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
class Add_Appointment(models.Model):
    Title = models.CharField(max_length=100, default='Default Title')
    Add_Address = models.TextField()
    Date = models.DateField()  
    Time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.Title}" or f'Appointment - {self.pk}'
    
    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
    


class Add_Event(models.Model):
    Title = models.CharField(max_length=100, default='Default Title')
    Add_Address = models.TextField()
    type = models.CharField(max_length=100, default='appointment')
    Date = models.DateField()  
    Time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.Title}" or f'Event - {self.pk}'
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    

class Quick_Plan(models.Model):
    Title = models.CharField(max_length=100, default='Default Title')
    Add_Address = models.TextField()
    Date = models.DateField()  
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.Title}" or f'Quick Plan - {self.pk}'
    
    class Meta:
        verbose_name = 'Quick Plan'
        verbose_name_plural = 'Quick Plans'