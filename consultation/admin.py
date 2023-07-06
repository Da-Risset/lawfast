from django.contrib import admin
from .models import Consultation, Lawyer, Review, Variation


admin.site.register(Consultation)
admin.site.register(Lawyer)
admin.site.register(Review)
admin.site.register(Variation)
