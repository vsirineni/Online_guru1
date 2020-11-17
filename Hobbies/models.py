from django.db import models
from django.utils import timezone
# Create your models here. Created on march 28

class Inclass(models.Model):
    class_name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to="User/images", null=True)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.class_name)