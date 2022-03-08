from django.contrib import admin
from .models import Editor, Tag, Article, NewsletterRecipients, MoringaMerch



# Register your models here.

class ArticleAdmin(admin.ModelAdmin) :
  filter_horizontal = ('Tag',)

admin.site.register(Editor)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(NewsletterRecipients)
admin.site.register(MoringaMerch)
