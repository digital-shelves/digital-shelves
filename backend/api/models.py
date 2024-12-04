from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    checkout_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=500, default='')
    amount_available = models.IntegerField(default=0)
    img_url = models.URLField(default='127.0.0.1:8080/static/img')

    def __str__(self):
        return f"{self.name} ({self.amount_available} available)"

    class Meta:
        ordering = ['name']