from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name