from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Add in this class to customize the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
# Update the registration to include this customised interface    
admin.site.register(Category, CategoryAdmin)
#admin.site.register(Page, PageAdmin)
admin.site.register(Page)
# NH - Add UserProfile to the admin controls
admin.site.register(UserProfile)