from django.db import models
from account.models import CustomUser


class CategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class JobModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE, default=1)
    contact_number = models.CharField(max_length=20, default='no')
    contact_email = models.EmailField()

    def __str__(self):
        return self.title