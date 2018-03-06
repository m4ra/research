from django.utils.html import format_html
from django.urls import reverse

from django.contrib import admin
from phd.models import *


class MaterialAdmin(admin.ModelAdmin):
	#fields = _all_
	list_display = ('title', 'kind', 'year')
	pass


class FieldAdmin(admin.ModelAdmin):
	#fields = _all_
	list_display = ('name', 'related_materials',)
	pass

class ConceptAdmin(admin.ModelAdmin):
	#fields = _all_
	pass

class NoteAdmin(admin.ModelAdmin):
	#fields = _all_
	pass

class ChapterAdmin(admin.ModelAdmin):
	#fields = _all_
	pass

admin.site.register(Material, MaterialAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Concept, ConceptAdmin)
