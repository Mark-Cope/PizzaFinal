from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#A MODEL tells Django how to work with the data that is stroed in the app
#In reality a MODEL is just a class but is very important to have Django runs
class Pizza(models.Model):
    name = models.CharField(max_length = 200)

    date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.name
#The ForeignKey accesses another database record and brings it over
#The on delete model tells Django to delete the entry the CASCADE part of it
#tells Django to delte ALL of the parts
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    name = models.CharField(max_length = 200)

    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    name = models.CharField(max_length = 200)
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


#If a model was to have a META CLASS it is just another way to manage the model
#typically done if there is more data