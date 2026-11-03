from django.db import models
from django.contrib.auth.hashers import (
    check_password as django_check_password,
    identify_hasher,
    make_password,
)
from django.utils.crypto import constant_time_compare

# Create your models here.
class Student(models.Model):
    rollno = models.CharField(max_length=20, primary_key=True)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    program=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    regdate=models.CharField(max_length=30)

class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=128)
    usertype=models.CharField(max_length=50)
    status=models.CharField(max_length=5)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        if django_check_password(raw_password, self.password):
            return True

        # Upgrade accounts created before passwords were hashed. The data
        # migration handles existing rows, while this keeps imported or
        # otherwise unmigrated legacy rows usable without storing plaintext.
        try:
            identify_hasher(self.password)
        except ValueError:
            if constant_time_compare(str(raw_password), str(self.password)):
                self.set_password(raw_password)
                self.save(update_fields=['password'])
                return True
        return False

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.CharField(max_length=30)
    enquirydate=models.CharField(max_length=30)
