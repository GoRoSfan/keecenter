from django.conf.urls import url

from . import views
from django.views.generic import RedirectView


urlpatterns = [

    url(r'^news/$', views.AllNewsView.as_view(), name='all-news'),
    # url(r'^news/(?P<pk>\d+)/$', views.DetailNewsView.as_view(), name='new-detail'),

    url(r'^legal/$', views.LegalsView.as_view(), name='legal'),

    url(r'^contact/$', views.ContactsView.as_view(), name='contact'),

    # url(r'^clubs/$', views.AllClubsView.as_view(), name='all-clubs'),
    # url(r'^clubs/(?P<pk>\d+)/$', views.DetailClubsView.as_view(), name='club-detail'),
    # url(r'^training_course/(?P<pk>\d+)/$', views.DetailTrainingCoursesView.as_view(), name='training-course-detail'),

    url(r'^events/$', views.AllEventsView.as_view(), name='all-events'),
    # url(r'^events/(?P<pk>\d+)/$', views.DetailEventsView.as_view(), name='event-detail'),

    url(r'^employees/$', views.EmployeesView.as_view(), name='employees'),

    url(r'^partners/$', views.PartnersView.as_view(), name='partners')

]
