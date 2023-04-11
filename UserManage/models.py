from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import jwt
import datetime
from website import settings

# Create your models here.
class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __str__(self):
        return '%s(%s)' % (self.name, self.url)


class RoleList(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList, blank=True)

    def __str__(self):
        return self.name
        # return '%s(%s)' %(self.name,self.permission)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), username=username, )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username=username, password=password, )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64, null=True)
    sex = models.CharField(max_length=2, null=True)
    role = models.ForeignKey(RoleList, null=True, blank=True, default=1, on_delete=models.PROTECT)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            'exp': datetime.datetime.now() + datetime.timedelta(days=1),
            'iat': datetime.datetime.now(),
            'data': {
                'name': self.username
            }
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.encode("utf-8").decode('utf-8')
