from django.contrib import admin
from .models import Exam
from .models import Choice
from .models import Quiz

# Register your models here.

admin.site.register(Exam)
admin.site.register(Choice)
admin.site.register(Quiz)

