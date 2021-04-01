from django.contrib import admin
from .models import Contents, Comment
# Register your models here.

class ContentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contents, ContentsAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)

