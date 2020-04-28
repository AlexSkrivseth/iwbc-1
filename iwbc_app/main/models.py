from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField('Group Name', max_length=50)

class Boy(models.Model):

    firstname = models.CharField('First Name', max_length=50)
    lastname = models.CharField('Last Name', max_length=50)
    address = models.CharField('Address', max_length=150)
    state = models.CharField('State', max_length=20)
    dob = models.DateField('Date of Birth')
    email = models.EmailField('Email')
    phone = models.IntegerField('Phone Number', max_length=9)
    guardian_email = models.EmailField('Guardian Email')
    guardian_phone = models.IntegerField('Guardian Phone Number', max_length=9)
    allergies = models.BooleanField('Allergies?',False)
    swims = models.BooleanField(True)
    fitness_level = models.IntegerField(max_length=2)
    firt_year = models.BooleanField(True)
    hieght = models.IntegerField(max_length=2)
    wieght = models.IntegerField(max_length=3)
    other_health_issues = models.CharField(max_length=300)

    group = models.OneToOneField(Group, on_delete=False)
    accepted = models.BooleanField(False)
    paid = models.BooleanField(False)
    lodging = models.CharField(max_length=300)
    chief_notes = models.CharField(max_length=300)
