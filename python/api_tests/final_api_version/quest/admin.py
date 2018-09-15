from django.contrib import admin
from .models import Question

"""Imports and registers the Student model in the database
"""

admin.site.register(Question)
