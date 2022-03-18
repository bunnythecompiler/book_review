from django.db import models
from django.utils import timezone 


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=3000)
    author = models.CharField(max_length=60)
    upload_date = models.DateTimeField(default=timezone.now)
    book_cover = models.ImageField(upload_to='')

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.CharField(max_length=50)
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=400)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return self.book.title 



    
    
