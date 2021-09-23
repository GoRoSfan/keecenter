from django.contrib import admin

from .models import News, Legals, Profile, ClubType, Club


class NewsAdmin(admin.ModelAdmin):

    list_display = ('title', 'post_date')
    fields = ('title', 'description', 'content_types')


class LegalsAdmin(admin.ModelAdmin):

    list_display = ('name', 'detail')
    fields = ('name', 'detail')


class ClubAdmin(admin.ModelAdmin):

    list_display = ('name', 'club_type')
    fields = ('name', 'club_type', 'description')


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'is_teacher')
    fields = ('photo', 'user', 'is_teacher')


admin.site.register(ClubType)

admin.site.register(News, NewsAdmin)
admin.site.register(Legals, LegalsAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Profile, ProfileAdmin)
