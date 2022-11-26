from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    facs_number = models.CharField(max_length=13)
    email = models.EmailField()
    website = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    logo = models.ImageField(upload_to='images/', blank=True)
    top = models.BooleanField(default=False)
    number_table = models.IntegerField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.name


class Jurnal(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    date = models.DateField()
    downloadview = models.IntegerField(default=0)
    file = models.FileField(upload_to='media')
    keyword = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    facs_number = models.CharField(max_length=13)
    email = models.EmailField()
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Statya(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    jurnal = models.ForeignKey(Jurnal, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Conference(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    adress = models.CharField(max_length=500)
    phon_number = models.CharField(max_length=13)
    date = models.DateField()
    sponsor = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Seminar(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = RichTextField()
    link = models.URLField()
    phon_number = models.CharField(max_length=13)
    date = models.DateField()
    sponsor = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class Video_Gallery(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    videourl = models.URLField()
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phon_number = models.CharField(max_length=20)
    email = models.EmailField()
    taklif = models.TextField()