from django.contrib import admin
from .models import Post,Caliculator,User,Entry

admin.site.register(Post)
admin.site.register(Caliculator)





@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass
