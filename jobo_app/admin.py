from django.contrib import admin
from .models import CategoriesModel, JobModel
# Register your models here.

admin.site.register(CategoriesModel)
admin.site.register(JobModel)