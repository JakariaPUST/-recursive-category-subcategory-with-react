from django.contrib import admin
from .models import *
# Register your models here.




class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 5



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_editable = ('parent',)
    fieldsets =(
        (
            None, {
                'fields': ('name',)
            }
        ),
    )
    inlines = (SubCategoryInline,
    )


class SubSubCategoryInline(admin.TabularInline):
    model = SubSubCategory
    extra = 3

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'subsubcategory_count')

    fieldsets =(
        (
            None, {
                'fields': ('name',)
            }
        ),
    )
    inlines = (SubSubCategoryInline,
    )

    def subsubcategory_count(self, obj):
        return obj.subsubcategory_set.count()

    def get_ordering(self, request):
        return ('parent', 'name')

    


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

admin.site.register(SubSubCategory)