from django.contrib import admin
from .models import News, ContentTypesNews, ActivityTypesClubs, Events, Clubs, Contacts,\
    Legals, Employees, Partners


admin.site.register(ContentTypesNews)
# admin.site.register(ActivityTypesClubs)
admin.site.register(Employees)
admin.site.register(Partners)


class NewsAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'visitors_type')
    fields = ('title', 'description', ('visitors_type', 'content_types'))


admin.site.register(News, NewsAdmin)


class EventsAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_placing')
    fields = ('name', 'date_placing')


admin.site.register(Events, EventsAdmin)


# class ClubsAdmin(admin.ModelAdmin):
#
#     list_display = ('name', 'season_set', 'members_age', 'activity_type')
#     fields = ('name', 'description', 'season_set', 'members_age', 'activity_type')
#
#
# admin.site.register(Clubs, ClubsAdmin)


class ContactsAdmin(admin.ModelAdmin):

    list_display = ('label', 'content')
    fields = ('label', 'content')


admin.site.register(Contacts, ContactsAdmin)


class LegalsAdmin(admin.ModelAdmin):

    list_display = ('name', 'detail')
    fields = ('name', 'detail')


admin.site.register(Legals, LegalsAdmin)
