import uuid

from django.db import models

# Create your models here.

class TestSet(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    nomenclature = models.TextField(null=True, blank=True, max_length=100)
    nsn = models.TextField(null=True, blank=True, max_length=20)
    model = models.TextField(null=True, blank=True, max_length=20)
    serial_number = models.TextField(null=True, blank=True, max_length=30)
    tm_number = models.TextField(null=True, blank=True, max_length=50)
    tm_date = models.TextField(null=True, blank=True, max_length=20)

    def __str__(self):
        return f"{self.nomenclature} {self.serial_number}"