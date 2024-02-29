from django.db import models

class ModelAlex(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    prof = models.CharField(max_length=10)


class ModelAlexImg(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to='imgs')

class ModelReg(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=10)



class Img(models.Model):
    Image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=30)
#пример модели