from django.contrib import admin
from .models import Question

# Register Question model to admin page.
admin.site.register(Question)