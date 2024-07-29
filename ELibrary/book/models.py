from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
import uuid

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    published_at = models.DateField()
    isbn = models.CharField(max_length=100)
    available_copies = models.IntegerField()
    cover = models.ImageField(upload_to='./covers', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Books)
def delete_book_cover(sender, instance, **kwargs):
    if instance.cover and os.path.isfile(instance.cover.path):
        os.remove(instance.cover.path)