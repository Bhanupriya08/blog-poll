from django.contrib import admin
from .models import Post,Question,Choice

# Register your models here.
admin.site.site_header = "Blog Database"

class PostAdmin(admin.ModelAdmin):
	list_display = ("created_date","author","title",)
	list_filter = ("created_date",)


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	( None, {'fields' : ['question_text']} ),
	("Date Information" ,{'fields':['pub_date'], "classes" : ['collapse']})]
	inlines = [ChoiceInline]
	list_display = ("question_text","pub_date")
	list_filter = ['pub_date']
	search_fields = ['question_text']





	

admin.site.register(Post,PostAdmin)
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice,ChoiceAdmin)