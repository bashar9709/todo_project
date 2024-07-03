from django.db import models

# Create your models here.

class TodoModel(models.Model):
    CATEGORY = (
        ('family','Family'),
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('Others','Others')
        )
    #id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=CATEGORY, default='unknown')
    first_date = models.DateField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='Incompleted')
    finished_date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    
