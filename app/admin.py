from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


class MemberAdmin(admin.ModelAdmin):
    exclude = ('User_Id',)

    def save_model(self, request, obj, form, change):
        if not change:  # If the object is being created
            user = User.objects.create(username=f'{obj.First_Name}{obj.Second_Name}')
            user.password = "hhhhhh"
            obj.User_Id = user.id
        super().save_model(request, obj, form, change)


class Application_Admin(admin.ModelAdmin):
    #exclude = ('Status',)
    pass


class NewsEventImageInline(admin.TabularInline):
    model = NewsEventImage
    extra = 1  # Number of empty forms to display

class NewsEventParagraphInline(admin.TabularInline):
    model = NewsEventParagraph
    extra = 1  # Number of empty forms to display


@admin.register(NewsEvent)
class ProductAdmin(admin.ModelAdmin):
    inlines = [NewsEventImageInline, NewsEventParagraphInline]


admin.site.register(Thrust)
admin.site.register(Member, MemberAdmin)
admin.site.register(Application, Application_Admin)
admin.site.register(Publication_Elearning)
admin.site.register(Seminars_Webinars_Podcast)
admin.site.register(Pooling_Equipment)