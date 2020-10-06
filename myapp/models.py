from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500,blank=True,null=True)
    created = models.DateTimeField(auto_now=True,blank=True,null=True)


    def __str__(self):
        return self.search
    
    