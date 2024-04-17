from django.db import models

class Orders(models.Model):
    name = models.CharField(max_length=50)
    tel_num = models.CharField(max_length=20, default='+996.........')
    description = models.TextField()
    address = models.CharField(max_length=100, default='ул.Фрунзе...')
    time = models.CharField(max_length=20, default='к 12:30 (15мин)')
    class Meta:
        verbose_name = "orders"
        verbose_name_plural = "orders"
        
    def __str__(self):
        return self.name

class Menu(models.Model):
    category = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=10, default='100сом')
    image_url = models.URLField()
    
    def __str__(self):
        return self.title
    
class Contacts(models.Model):
    category = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    
    def __str__(self):
        return self.title
    
class Vacancies(models.Model):
    category = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title