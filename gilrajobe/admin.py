from django.contrib import admin

# Register your models here.

from .models import Question

### question search add
class QuestionAdmin(admin.ModelAdmin):
	search_fields =['subject']

### question list registe
admin.site.register(Question,QuestionAdmin)



