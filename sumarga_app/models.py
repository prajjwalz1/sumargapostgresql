from django.db import models

# Create your models here.
class post(models.Model):
    name=models.CharField(max_length=200)
    Subject=models.CharField(max_length=200)
    text=models.CharField(max_length=50000)
    image = models.ImageField(upload_to='pic')
    thumbnail=models.ImageField(upload_to='pic')
    writter=models.TextField(null=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class images(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pic')
    about_us_img=models.ImageField(upload_to='pic')
    profileimage=models.ImageField(upload_to='pic')


    def __str__(self):
        return self.name

class booksimages(models.Model):
    name = models.CharField(max_length=50)
    image=models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name


class Feature(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True)
    book_image=models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name

class picks(models.Model):
    image=models.ImageField(upload_to='pic')
    book_name=models.CharField(null=True,max_length=50)
    writer=models.CharField(null=True,max_length=50)
    def __str__(self):
        return self.book_name
class logo(models.Model):
    logo=models.ImageField(upload_to='pic')

class news(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pic')
    category=models.CharField(max_length=50)
    article=models.TextField(null=True)
    def __str__(self):
        return self.title

class contacts(models.Model):
    name=models.CharField(max_length=100)
    adress=models.TextField(null=True)
    contact=models.TextField(null=True)
    email=models.TextField(null=True)
    image=models.ImageField(upload_to='pic')
    fb=models.TextField(max_length=50)
    twitter = models.TextField(max_length=50)
    linkedin=models.TextField(max_length=50)

    def __str__(self):
        return self.name
class newrelease(models.Model):
    book_name=models.CharField(max_length=100)
    writter = models.CharField(null=True, max_length=50)
    image = models.ImageField(upload_to='pic')
    category=models.CharField(max_length=100)
    paragraph=models.TextField(null=True)
    def __str__(self):
        return self.book_name

class status(models.Model):
    writter=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pic')
    bg_img=models.ImageField(upload_to='pic')

    def __str__(self):
        return self.status
