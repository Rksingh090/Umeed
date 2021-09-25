from django.db import models

# Create your models here.
class ModalForm(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=254,null=True)
    mobile_no = models.IntegerField(null=True)
    message = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True,null=True)

class EnquiryForm(models.Model):
    name = models.CharField(max_length=100,null=True)
    mobile_no = models.IntegerField(null=True)
    property_type = models.CharField(max_length=100,null=True)
    budget = models.CharField(null=True,max_length=50)
    created = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=254,null=True)
    mobile_no = models.IntegerField(null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name


class BiharPropertyContactForm(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=254,null=True)
    mobile_no = models.IntegerField(null=True)
    message = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

class PatnaPropertyContactForm(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    mobile_no = models.IntegerField(null=True)
    message = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name


class CareerForm(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    mobile_no = models.IntegerField(null=True)
    filename = models.FileField(upload_to='careerfile/')
    message = models.TextField(null=True)

    def __str__(self):
        return self.name
    