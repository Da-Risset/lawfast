from django.contrib import admin
from .models import Document, TypeDocument


admin.site.register(TypeDocument)
admin.site.register(Document)