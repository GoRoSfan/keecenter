""" URLs module

"""

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^news/$', views.AllNewsView.as_view(), name='all-news'),
    url(r'^legal/$', views.LegalsView.as_view(), name='legal'),
    url(r'^contact/$', views.ContactsView.as_view(), name='contact'),
    url(r'^events/$', views.AllEventsView.as_view(), name='all-events'),
    url(r'^employees/$', views.EmployeesView.as_view(), name='employees'),
    url(r'^partners/$', views.PartnersView.as_view(), name='partners')
]
