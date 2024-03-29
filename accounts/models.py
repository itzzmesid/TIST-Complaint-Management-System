from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

#create a new (super)user
class MyAccountManager(BaseUserManager):

    def create_user(self, email, username , password=None):
        if not email:
            raise ValueError("Users must have an E-mail address!")
        if not username:
            raise ValueError("Users must have an Username!")
        
        user = self.model(
            email       = self.normalize_email(email),
            username    = username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    DEPT = (
        ('CSE', 'Computer Science & Engineering (CSE)'),
        ('IT', 'Information Technology (IT)'),
        ('SF', 'Fire & Safety (SE)'),
        ('ME', 'Mechanical Engineering (ME)'),
        ('ECE', 'Electronics & Communication (ECE)'),
        ('EEE', 'Electrical & Electronics (EEE'),
    )

    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    # user            = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    username        = models.CharField(max_length=40)
    employeeId      = models.CharField(max_length=20, unique=True)
    phone_regex     = RegexValidator(regex=r'^\d{10,10}$', message="Phone number must contain only numbers:Up to 10 digits allowed.")
    phone           = models.CharField(validators=[phone_regex], max_length=10)
    department      = models.CharField(max_length=4, choices=DEPT,default='Computer Science & Engineering (CSE)')

#Below fields are already present in AbstractBaseUser.So we need to override them
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    objects = MyAccountManager()


    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

