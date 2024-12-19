# from django.db import models

# # Create your models here.

# class UserRegistration(models.Model):

#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Prefer not to say'),
#     ]
#     id = models.AutoField(primary_key=True)
#     fullname = models.CharField(max_length=100,blank=False)
#     studentid = models.BigIntegerField(blank=False, unique=True)
#     email = models.EmailField(max_length=50,blank=False,unique=True)
#     phone = models.BigIntegerField(blank=False, unique=True)
#     password = models.CharField(max_length=50, blank=False)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     registrationtime = models.DateTimeField(blank=False,auto_now_add=True)

#     def __str__(self):
#         return str(self.studentid)

#     class Meta:
#         db_table = "UserRegistrationTable"


from django.db import models

# Create your models here.

class UserRegistration(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Prefer not to say'),
    ]
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100,blank=False)
    # Changed: studentid field type from BigIntegerField to CharField to allow alphanumeric validation
    studentid = models.CharField(max_length=10,blank=False, unique=True)
    email = models.EmailField(max_length=50,blank=False,unique=True)
    phone = models.BigIntegerField(blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    registrationtime = models.DateTimeField(blank=False,auto_now_add=True)

    def __str__(self):
        return str(self.studentid)

    class Meta:
        db_table = "UserRegistrationTable"