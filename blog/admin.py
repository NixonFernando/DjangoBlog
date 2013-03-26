from django.contrib import admin
from django.db.models import TextField
from blog.models import Post
from file_picker.wymeditor.widgets import WYMeditorWidget


class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('title', 'created')
    formfield_overrides = {TextField: {'widget': WYMeditorWidget({})}}

    class Media:
        js = ('http://cdn.jquerytools.org/1.2.5/full/jquery.tools.min.js',)


admin.site.register(Post, BlogAdmin)
