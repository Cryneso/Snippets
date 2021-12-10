from django.contrib import admin
from MainApp.models import Snippet
from MainApp.models import Comment

admin.site.register(Snippet)
admin.site.register(Comment)
