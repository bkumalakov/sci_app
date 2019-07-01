from django.contrib import admin
from .models import *


class AuthorsModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "scopus_author_id", "staff_member"]
    list_filter = ["staff_member"]
    search_fields = ["l_name", "f_name", "m_name"]

    class Meta:
        model = Author


class AuthoredModelAdmin(admin.ModelAdmin):
    list_display = ["pub_title", "author"]

    def pub_title(self, obj):
        return obj.p_title.title

    pub_title.admin_order_field = 'pub_title'

    def author(self, obj):
        return obj.author.__def__

    author.admin_order_field = 'author'

    class Meta:
        model = Authored


class SourceModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "year_published"]

    class Meta:
        model = Source


admin.site.register(Author, AuthorsModelAdmin)
admin.site.register(Authored, AuthoredModelAdmin)
admin.site.register(Paper)
admin.site.register(PType)
admin.site.register(Source, SourceModelAdmin)
