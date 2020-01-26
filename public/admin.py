from django.contrib import admin
from .models import News, ContentTypesNews, ActivityTypesClubs, ContentTypesLegals, Events, \
    Clubs, TrainingCourses, Contacts, Legals, Employees, Partners


admin.site.register(ContentTypesNews)
admin.site.register(ActivityTypesClubs)
admin.site.register(ContentTypesLegals)
admin.site.register(Employees)
admin.site.register(Partners)


class NewsAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'visitors_type', 'display_content_types')
    fields = ('title', 'description', ('visitors_type', 'content_types'), 'image', 'detail')


admin.site.register(News, NewsAdmin)


class EventsAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_placing')
    fields = ('name', 'date_placing', 'detail')


admin.site.register(Events, EventsAdmin)


class ClubsAdmin(admin.ModelAdmin):

    list_display = ('name', 'season_set', 'members_age', 'activity_type')
    fields = ('name', 'description', 'season_set', 'members_age', 'activity_type', 'image', 'detail')


admin.site.register(Clubs, ClubsAdmin)


class TrainingCoursesAdmin(admin.ModelAdmin):

    list_display = ('name', )
    fields = ('name', 'description', 'image', 'detail')


admin.site.register(TrainingCourses, TrainingCoursesAdmin)


class ContactsAdmin(admin.ModelAdmin):

    list_display = ('label', 'content')
    fields = ('label', 'content')


admin.site.register(Contacts, ContactsAdmin)


class LegalsAdmin(admin.ModelAdmin):

    list_display = ('name', 'content_type')
    fields = ('name', 'detail', 'content_type')


admin.site.register(Legals, LegalsAdmin)
