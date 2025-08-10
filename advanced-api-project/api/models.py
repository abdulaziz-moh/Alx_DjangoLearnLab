from django.db import models

# Create your models here.

class Author(models.Model):
    # One author can have many books (1:N relationship).
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author,related_name= 'books',on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title