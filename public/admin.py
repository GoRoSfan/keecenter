""" Admin module

"""

from django.contrib import admin

from .bot import send_image
from .models import News, NewContentTypes, Events, Contacts, Legals, \
    Employees, Partners
from keecenter.settings import ALLOWED_HOSTS


class NewsAdmin(admin.ModelAdmin):
    """ News Admin

    """

    list_display = ('title', 'post_date', 'visitors_type')
    fields = ('title', 'description', ('visitors_type', 'content_types'),
              'image')

    def save_model(self, request, obj: News, form, change):
        if '127.0.0.1' in ALLOWED_HOSTS:
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)
            image_link = request.META['HTTP_ORIGIN'] + obj.image.url
            obj.image_hash = send_image(
                image_link, obj._meta.verbose_name_plural)
            super().save_model(request, obj, form, change)


class EventsAdmin(admin.ModelAdmin):
    """ Events Admin

    """

    list_display = ('name', 'date_placing')
    fields = ('name', 'date_placing')


class ContactsAdmin(admin.ModelAdmin):
    """ Contacts Admin

    """

    list_display = ('label', 'content')
    fields = ('label', 'content')


class LegalsAdmin(admin.ModelAdmin):
    """ Legals Admin

    """

    list_display = ('name', 'detail')
    fields = ('name', 'detail')


admin.site.register(NewContentTypes)
admin.site.register(Employees)
admin.site.register(Partners)

admin.site.register(News, NewsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Legals, LegalsAdmin)
