from django.db import models




class Qoute(models.Model):
    title=models.CharField(max_length=200,null=False)
    author=models.CharField(max_length=200)
    text=models.TextField(blank=True, null=True)
    picture=models.ImageField(blank=True,null=True,upload_to='images')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)
     
       
    
