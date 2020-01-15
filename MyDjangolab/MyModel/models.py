from django.db import models

# Create your models here.


class MyDjangoLab(models.Model):
    name = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=2)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    addtime = models.DateField(max_length=14)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
