from django.db import models
from django.contrib.auth.models import User

Rating_Choices = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)

class Type(models.Model):
    name=models.CharField(max_length=200,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Food(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    avg_rating=models.FloatField(null=True,blank=True)
    type=models.ForeignKey(Type,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    name_food=models.ForeignKey(Food,on_delete=models.CASCADE)
    description=models.TextField(max_length=1000)
    rating=models.IntegerField(choices=Rating_Choices,default='3')
    user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.description[0:100]
    
class Meal(models.Model):
    choices=(
        ('BreakFast','BreakFast'),
        ('Lunch','Lunch'),
        ('Snacks','Snacks'),
        ('Dinner','Dinner'),
    )
    date=models.DateField()
    Type=models.CharField(max_length=10,null=True,choices=choices)
    item=models.ManyToManyField(Food)

    def __str__(self):
        return f'{self.date} {self.Type}'
