from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    publication_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def to_json(self):
        return {
            "id": str(self.id),
            "title": str(self.title),
            "author": self.author.to_json(),
            "publication_date": str(self.publication_date)
        }
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "date_of_birth": str(self.date_of_birth),
            "date_of_death": str(self.date_of_death)
        }