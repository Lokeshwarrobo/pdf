from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=70)
    Author = models.CharField(max_length=50, blank=True, null=True)
    Add_Book = models.FileField(upload_to='pdf/')
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    user = models.CharField(max_length=20,blank=True,null=True)
    cover_page = models.ImageField(upload_to='imaages/')



    def __str__(self):
        return self.Title

