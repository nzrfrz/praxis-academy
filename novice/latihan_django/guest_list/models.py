from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Registration(models.Model):
    CHOICES_VALUE = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
        ("5", "Five")
    )

    MULTIPLE_CHOICES_VALUE = (
        ('Take', 'Take'),
        ('a break', 'a break'),
        ('Make', 'Make'),
        ('a coffe', 'a coffe'),
        ('Napping', 'Napping')
    )

    # MULTIPLE_CHOICES_VALUE = (
    #     ('1', 'Take'),
    #     ('2', 'a break'),
    #     ('3', 'Make'),
    #     ('4', 'a coffe'),
    #     ('5', 'Napping')
    # )

    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    guest_photo = models.ImageField(upload_to="images/", blank = True, default = '')
    choices_input = models.CharField(max_length = 255, choices = CHOICES_VALUE, blank = True)
    multiple_choices_input = MultiSelectField(choices = MULTIPLE_CHOICES_VALUE, max_choices=2, max_length=5, default='1')
    # multiple_choices_input = models.CharField(max_length = 255, choices = MULTIPLE_CHOICES_VALUE, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name