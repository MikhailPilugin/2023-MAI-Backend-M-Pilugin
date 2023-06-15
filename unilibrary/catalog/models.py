from django.db import models
from django.urls import reverse
import uuid

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
    

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name
    

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)