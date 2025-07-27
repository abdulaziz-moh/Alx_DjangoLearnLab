from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    search_fields = ('title','author')
    list_filter = ('publication_year',)

admin.site.register(Book,BookAdmin)

# Custom admin for CustomUser (for auto-check compliance)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo')

admin.site.register(CustomUser, CustomUserAdmin)